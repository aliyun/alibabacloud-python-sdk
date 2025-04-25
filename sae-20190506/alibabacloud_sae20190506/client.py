# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sae20190506 import models as sae_20190506_models
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
        self._endpoint = self.get_endpoint('sae', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abort_and_rollback_change_order_with_options(
        self,
        request: sae_20190506_models.AbortAndRollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.AbortAndRollbackChangeOrderResponse:
        """
        @summary Terminates a change order and rolls back the corresponding application.
        
        @param request: AbortAndRollbackChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortAndRollbackChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortAndRollbackChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/AbortAndRollbackChangeOrder',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.AbortAndRollbackChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_and_rollback_change_order_with_options_async(
        self,
        request: sae_20190506_models.AbortAndRollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.AbortAndRollbackChangeOrderResponse:
        """
        @summary Terminates a change order and rolls back the corresponding application.
        
        @param request: AbortAndRollbackChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortAndRollbackChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortAndRollbackChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/AbortAndRollbackChangeOrder',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.AbortAndRollbackChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_and_rollback_change_order(
        self,
        request: sae_20190506_models.AbortAndRollbackChangeOrderRequest,
    ) -> sae_20190506_models.AbortAndRollbackChangeOrderResponse:
        """
        @summary Terminates a change order and rolls back the corresponding application.
        
        @param request: AbortAndRollbackChangeOrderRequest
        @return: AbortAndRollbackChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_and_rollback_change_order_with_options(request, headers, runtime)

    async def abort_and_rollback_change_order_async(
        self,
        request: sae_20190506_models.AbortAndRollbackChangeOrderRequest,
    ) -> sae_20190506_models.AbortAndRollbackChangeOrderResponse:
        """
        @summary Terminates a change order and rolls back the corresponding application.
        
        @param request: AbortAndRollbackChangeOrderRequest
        @return: AbortAndRollbackChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.abort_and_rollback_change_order_with_options_async(request, headers, runtime)

    def abort_change_order_with_options(
        self,
        request: sae_20190506_models.AbortChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.AbortChangeOrderResponse:
        """
        @summary Terminate a change order.
        
        @param request: AbortChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/AbortChangeOrder',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.AbortChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_change_order_with_options_async(
        self,
        request: sae_20190506_models.AbortChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.AbortChangeOrderResponse:
        """
        @summary Terminate a change order.
        
        @param request: AbortChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/AbortChangeOrder',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.AbortChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_change_order(
        self,
        request: sae_20190506_models.AbortChangeOrderRequest,
    ) -> sae_20190506_models.AbortChangeOrderResponse:
        """
        @summary Terminate a change order.
        
        @param request: AbortChangeOrderRequest
        @return: AbortChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_change_order_with_options(request, headers, runtime)

    async def abort_change_order_async(
        self,
        request: sae_20190506_models.AbortChangeOrderRequest,
    ) -> sae_20190506_models.AbortChangeOrderResponse:
        """
        @summary Terminate a change order.
        
        @param request: AbortChangeOrderRequest
        @return: AbortChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.abort_change_order_with_options_async(request, headers, runtime)

    def batch_start_applications_with_options(
        self,
        request: sae_20190506_models.BatchStartApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BatchStartApplicationsResponse:
        """
        @summary cn-shanghai
        
        @param request: BatchStartApplicationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStartApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/batchStartApplications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BatchStartApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_applications_with_options_async(
        self,
        request: sae_20190506_models.BatchStartApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BatchStartApplicationsResponse:
        """
        @summary cn-shanghai
        
        @param request: BatchStartApplicationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStartApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/batchStartApplications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BatchStartApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_applications(
        self,
        request: sae_20190506_models.BatchStartApplicationsRequest,
    ) -> sae_20190506_models.BatchStartApplicationsResponse:
        """
        @summary cn-shanghai
        
        @param request: BatchStartApplicationsRequest
        @return: BatchStartApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_start_applications_with_options(request, headers, runtime)

    async def batch_start_applications_async(
        self,
        request: sae_20190506_models.BatchStartApplicationsRequest,
    ) -> sae_20190506_models.BatchStartApplicationsResponse:
        """
        @summary cn-shanghai
        
        @param request: BatchStartApplicationsRequest
        @return: BatchStartApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_start_applications_with_options_async(request, headers, runtime)

    def batch_stop_applications_with_options(
        self,
        request: sae_20190506_models.BatchStopApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BatchStopApplicationsResponse:
        """
        @summary Stops multiple applications at a time.
        
        @param request: BatchStopApplicationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStopApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/batchStopApplications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BatchStopApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_applications_with_options_async(
        self,
        request: sae_20190506_models.BatchStopApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BatchStopApplicationsResponse:
        """
        @summary Stops multiple applications at a time.
        
        @param request: BatchStopApplicationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStopApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/batchStopApplications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BatchStopApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_applications(
        self,
        request: sae_20190506_models.BatchStopApplicationsRequest,
    ) -> sae_20190506_models.BatchStopApplicationsResponse:
        """
        @summary Stops multiple applications at a time.
        
        @param request: BatchStopApplicationsRequest
        @return: BatchStopApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_stop_applications_with_options(request, headers, runtime)

    async def batch_stop_applications_async(
        self,
        request: sae_20190506_models.BatchStopApplicationsRequest,
    ) -> sae_20190506_models.BatchStopApplicationsResponse:
        """
        @summary Stops multiple applications at a time.
        
        @param request: BatchStopApplicationsRequest
        @return: BatchStopApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_stop_applications_with_options_async(request, headers, runtime)

    def bind_slb_with_options(
        self,
        request: sae_20190506_models.BindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BindSlbResponse:
        """
        @param request: BindSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.internet):
            query['Internet'] = request.internet
        if not UtilClient.is_unset(request.internet_slb_charge_type):
            query['InternetSlbChargeType'] = request.internet_slb_charge_type
        if not UtilClient.is_unset(request.internet_slb_id):
            query['InternetSlbId'] = request.internet_slb_id
        if not UtilClient.is_unset(request.intranet):
            query['Intranet'] = request.intranet
        if not UtilClient.is_unset(request.intranet_slb_charge_type):
            query['IntranetSlbChargeType'] = request.intranet_slb_charge_type
        if not UtilClient.is_unset(request.intranet_slb_id):
            query['IntranetSlbId'] = request.intranet_slb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_slb_with_options_async(
        self,
        request: sae_20190506_models.BindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BindSlbResponse:
        """
        @param request: BindSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.internet):
            query['Internet'] = request.internet
        if not UtilClient.is_unset(request.internet_slb_charge_type):
            query['InternetSlbChargeType'] = request.internet_slb_charge_type
        if not UtilClient.is_unset(request.internet_slb_id):
            query['InternetSlbId'] = request.internet_slb_id
        if not UtilClient.is_unset(request.intranet):
            query['Intranet'] = request.intranet
        if not UtilClient.is_unset(request.intranet_slb_charge_type):
            query['IntranetSlbChargeType'] = request.intranet_slb_charge_type
        if not UtilClient.is_unset(request.intranet_slb_id):
            query['IntranetSlbId'] = request.intranet_slb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BindSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_slb(
        self,
        request: sae_20190506_models.BindSlbRequest,
    ) -> sae_20190506_models.BindSlbResponse:
        """
        @param request: BindSlbRequest
        @return: BindSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_slb_with_options(request, headers, runtime)

    async def bind_slb_async(
        self,
        request: sae_20190506_models.BindSlbRequest,
    ) -> sae_20190506_models.BindSlbResponse:
        """
        @param request: BindSlbRequest
        @return: BindSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.bind_slb_with_options_async(request, headers, runtime)

    def confirm_pipeline_batch_with_options(
        self,
        request: sae_20190506_models.ConfirmPipelineBatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ConfirmPipelineBatchResponse:
        """
        @param request: ConfirmPipelineBatchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmPipelineBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.confirm):
            query['Confirm'] = request.confirm
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmPipelineBatch',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/ConfirmPipelineBatch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ConfirmPipelineBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_pipeline_batch_with_options_async(
        self,
        request: sae_20190506_models.ConfirmPipelineBatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ConfirmPipelineBatchResponse:
        """
        @param request: ConfirmPipelineBatchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmPipelineBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.confirm):
            query['Confirm'] = request.confirm
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmPipelineBatch',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/ConfirmPipelineBatch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ConfirmPipelineBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_pipeline_batch(
        self,
        request: sae_20190506_models.ConfirmPipelineBatchRequest,
    ) -> sae_20190506_models.ConfirmPipelineBatchResponse:
        """
        @param request: ConfirmPipelineBatchRequest
        @return: ConfirmPipelineBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.confirm_pipeline_batch_with_options(request, headers, runtime)

    async def confirm_pipeline_batch_async(
        self,
        request: sae_20190506_models.ConfirmPipelineBatchRequest,
    ) -> sae_20190506_models.ConfirmPipelineBatchResponse:
        """
        @param request: ConfirmPipelineBatchRequest
        @return: ConfirmPipelineBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.confirm_pipeline_batch_with_options_async(request, headers, runtime)

    def create_application_with_options(
        self,
        tmp_req: sae_20190506_models.CreateApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateApplicationResponse:
        """
        @param tmp_req: CreateApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sae_20190506_models.CreateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.init_containers_config):
            request.init_containers_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.init_containers_config, 'InitContainersConfig', 'json')
        if not UtilClient.is_unset(tmp_req.sidecar_containers_config):
            request.sidecar_containers_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sidecar_containers_config, 'SidecarContainersConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.custom_image_network_type):
            query['CustomImageNetworkType'] = request.custom_image_network_type
        if not UtilClient.is_unset(request.deploy):
            query['Deploy'] = request.deploy
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.dotnet):
            query['Dotnet'] = request.dotnet
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.enable_cpu_burst):
            query['EnableCpuBurst'] = request.enable_cpu_burst
        if not UtilClient.is_unset(request.enable_ebpf):
            query['EnableEbpf'] = request.enable_ebpf
        if not UtilClient.is_unset(request.enable_new_arms):
            query['EnableNewArms'] = request.enable_new_arms
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not UtilClient.is_unset(request.microservice_engine_config):
            query['MicroserviceEngineConfig'] = request.microservice_engine_config
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not UtilClient.is_unset(request.oidc_role_name):
            query['OidcRoleName'] = request.oidc_role_name
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sae_version):
            query['SaeVersion'] = request.sae_version
        if not UtilClient.is_unset(request.secret_mount_desc):
            query['SecretMountDesc'] = request.secret_mount_desc
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not UtilClient.is_unset(request.base_app_id):
            body['BaseAppId'] = request.base_app_id
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_sidecar_resource_isolated):
            body['EnableSidecarResourceIsolated'] = request.enable_sidecar_resource_isolated
        if not UtilClient.is_unset(request.init_containers_config_shrink):
            body['InitContainersConfig'] = request.init_containers_config_shrink
        if not UtilClient.is_unset(request.micro_registration_config):
            body['MicroRegistrationConfig'] = request.micro_registration_config
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php):
            body['Php'] = request.php
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        if not UtilClient.is_unset(request.service_tags):
            body['ServiceTags'] = request.service_tags
        if not UtilClient.is_unset(request.sidecar_containers_config_shrink):
            body['SidecarContainersConfig'] = request.sidecar_containers_config_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/createApplication',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        tmp_req: sae_20190506_models.CreateApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateApplicationResponse:
        """
        @param tmp_req: CreateApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sae_20190506_models.CreateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.init_containers_config):
            request.init_containers_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.init_containers_config, 'InitContainersConfig', 'json')
        if not UtilClient.is_unset(tmp_req.sidecar_containers_config):
            request.sidecar_containers_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sidecar_containers_config, 'SidecarContainersConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.custom_image_network_type):
            query['CustomImageNetworkType'] = request.custom_image_network_type
        if not UtilClient.is_unset(request.deploy):
            query['Deploy'] = request.deploy
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.dotnet):
            query['Dotnet'] = request.dotnet
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.enable_cpu_burst):
            query['EnableCpuBurst'] = request.enable_cpu_burst
        if not UtilClient.is_unset(request.enable_ebpf):
            query['EnableEbpf'] = request.enable_ebpf
        if not UtilClient.is_unset(request.enable_new_arms):
            query['EnableNewArms'] = request.enable_new_arms
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not UtilClient.is_unset(request.microservice_engine_config):
            query['MicroserviceEngineConfig'] = request.microservice_engine_config
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not UtilClient.is_unset(request.oidc_role_name):
            query['OidcRoleName'] = request.oidc_role_name
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sae_version):
            query['SaeVersion'] = request.sae_version
        if not UtilClient.is_unset(request.secret_mount_desc):
            query['SecretMountDesc'] = request.secret_mount_desc
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not UtilClient.is_unset(request.base_app_id):
            body['BaseAppId'] = request.base_app_id
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_sidecar_resource_isolated):
            body['EnableSidecarResourceIsolated'] = request.enable_sidecar_resource_isolated
        if not UtilClient.is_unset(request.init_containers_config_shrink):
            body['InitContainersConfig'] = request.init_containers_config_shrink
        if not UtilClient.is_unset(request.micro_registration_config):
            body['MicroRegistrationConfig'] = request.micro_registration_config
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php):
            body['Php'] = request.php
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        if not UtilClient.is_unset(request.service_tags):
            body['ServiceTags'] = request.service_tags
        if not UtilClient.is_unset(request.sidecar_containers_config_shrink):
            body['SidecarContainersConfig'] = request.sidecar_containers_config_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/createApplication',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: sae_20190506_models.CreateApplicationRequest,
    ) -> sae_20190506_models.CreateApplicationResponse:
        """
        @param request: CreateApplicationRequest
        @return: CreateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_application_with_options(request, headers, runtime)

    async def create_application_async(
        self,
        request: sae_20190506_models.CreateApplicationRequest,
    ) -> sae_20190506_models.CreateApplicationResponse:
        """
        @param request: CreateApplicationRequest
        @return: CreateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_application_with_options_async(request, headers, runtime)

    def create_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.CreateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateApplicationScalingRuleResponse:
        """
        @summary Null
        
        @description The HTTP status code. Take note of the following rules:
        **2xx**: The call was successful.
        **3xx**: The call was redirected.
        **4xx**: The call failed.
        **5xx**: A server error occurred.
        
        @param request: CreateApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.enable_idle):
            query['EnableIdle'] = request.enable_idle
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.CreateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateApplicationScalingRuleResponse:
        """
        @summary Null
        
        @description The HTTP status code. Take note of the following rules:
        **2xx**: The call was successful.
        **3xx**: The call was redirected.
        **4xx**: The call failed.
        **5xx**: A server error occurred.
        
        @param request: CreateApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.enable_idle):
            query['EnableIdle'] = request.enable_idle
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_scaling_rule(
        self,
        request: sae_20190506_models.CreateApplicationScalingRuleRequest,
    ) -> sae_20190506_models.CreateApplicationScalingRuleResponse:
        """
        @summary Null
        
        @description The HTTP status code. Take note of the following rules:
        **2xx**: The call was successful.
        **3xx**: The call was redirected.
        **4xx**: The call failed.
        **5xx**: A server error occurred.
        
        @param request: CreateApplicationScalingRuleRequest
        @return: CreateApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_application_scaling_rule_with_options(request, headers, runtime)

    async def create_application_scaling_rule_async(
        self,
        request: sae_20190506_models.CreateApplicationScalingRuleRequest,
    ) -> sae_20190506_models.CreateApplicationScalingRuleResponse:
        """
        @summary Null
        
        @description The HTTP status code. Take note of the following rules:
        **2xx**: The call was successful.
        **3xx**: The call was redirected.
        **4xx**: The call failed.
        **5xx**: A server error occurred.
        
        @param request: CreateApplicationScalingRuleRequest
        @return: CreateApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_application_scaling_rule_with_options_async(request, headers, runtime)

    def create_config_map_with_options(
        self,
        request: sae_20190506_models.CreateConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateConfigMapResponse:
        """
        @summary Create a ConfigMap in a namespace.
        
        @param request: CreateConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigMapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_map_with_options_async(
        self,
        request: sae_20190506_models.CreateConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateConfigMapResponse:
        """
        @summary Create a ConfigMap in a namespace.
        
        @param request: CreateConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigMapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config_map(
        self,
        request: sae_20190506_models.CreateConfigMapRequest,
    ) -> sae_20190506_models.CreateConfigMapResponse:
        """
        @summary Create a ConfigMap in a namespace.
        
        @param request: CreateConfigMapRequest
        @return: CreateConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_config_map_with_options(request, headers, runtime)

    async def create_config_map_async(
        self,
        request: sae_20190506_models.CreateConfigMapRequest,
    ) -> sae_20190506_models.CreateConfigMapResponse:
        """
        @summary Create a ConfigMap in a namespace.
        
        @param request: CreateConfigMapRequest
        @return: CreateConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_config_map_with_options_async(request, headers, runtime)

    def create_grey_tag_route_with_options(
        self,
        request: sae_20190506_models.CreateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateGreyTagRouteResponse:
        """
        @summary Creates a canary release rule for a Spring Cloud or Dubbo application.
        
        @description >  You can configure only one canary release rule for each application.
        
        @param request: CreateGreyTagRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGreyTagRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_grey_tag_route_with_options_async(
        self,
        request: sae_20190506_models.CreateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateGreyTagRouteResponse:
        """
        @summary Creates a canary release rule for a Spring Cloud or Dubbo application.
        
        @description >  You can configure only one canary release rule for each application.
        
        @param request: CreateGreyTagRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGreyTagRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_grey_tag_route(
        self,
        request: sae_20190506_models.CreateGreyTagRouteRequest,
    ) -> sae_20190506_models.CreateGreyTagRouteResponse:
        """
        @summary Creates a canary release rule for a Spring Cloud or Dubbo application.
        
        @description >  You can configure only one canary release rule for each application.
        
        @param request: CreateGreyTagRouteRequest
        @return: CreateGreyTagRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_grey_tag_route_with_options(request, headers, runtime)

    async def create_grey_tag_route_async(
        self,
        request: sae_20190506_models.CreateGreyTagRouteRequest,
    ) -> sae_20190506_models.CreateGreyTagRouteResponse:
        """
        @summary Creates a canary release rule for a Spring Cloud or Dubbo application.
        
        @description >  You can configure only one canary release rule for each application.
        
        @param request: CreateGreyTagRouteRequest
        @return: CreateGreyTagRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_grey_tag_route_with_options_async(request, headers, runtime)

    def create_ingress_with_options(
        self,
        request: sae_20190506_models.CreateIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateIngressResponse:
        """
        @summary Creates a routing rule.
        
        @param request: CreateIngressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIngressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.cors_config):
            query['CorsConfig'] = request.cors_config
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_xforwarded_for):
            query['EnableXForwardedFor'] = request.enable_xforwarded_for
        if not UtilClient.is_unset(request.enable_xforwarded_for_client_src_port):
            query['EnableXForwardedForClientSrcPort'] = request.enable_xforwarded_for_client_src_port
        if not UtilClient.is_unset(request.enable_xforwarded_for_proto):
            query['EnableXForwardedForProto'] = request.enable_xforwarded_for_proto
        if not UtilClient.is_unset(request.enable_xforwarded_for_slb_id):
            query['EnableXForwardedForSlbId'] = request.enable_xforwarded_for_slb_id
        if not UtilClient.is_unset(request.enable_xforwarded_for_slb_port):
            query['EnableXForwardedForSlbPort'] = request.enable_xforwarded_for_slb_port
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        if not UtilClient.is_unset(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        body = {}
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ingress_with_options_async(
        self,
        request: sae_20190506_models.CreateIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateIngressResponse:
        """
        @summary Creates a routing rule.
        
        @param request: CreateIngressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIngressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.cors_config):
            query['CorsConfig'] = request.cors_config
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_xforwarded_for):
            query['EnableXForwardedFor'] = request.enable_xforwarded_for
        if not UtilClient.is_unset(request.enable_xforwarded_for_client_src_port):
            query['EnableXForwardedForClientSrcPort'] = request.enable_xforwarded_for_client_src_port
        if not UtilClient.is_unset(request.enable_xforwarded_for_proto):
            query['EnableXForwardedForProto'] = request.enable_xforwarded_for_proto
        if not UtilClient.is_unset(request.enable_xforwarded_for_slb_id):
            query['EnableXForwardedForSlbId'] = request.enable_xforwarded_for_slb_id
        if not UtilClient.is_unset(request.enable_xforwarded_for_slb_port):
            query['EnableXForwardedForSlbPort'] = request.enable_xforwarded_for_slb_port
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        if not UtilClient.is_unset(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        body = {}
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ingress(
        self,
        request: sae_20190506_models.CreateIngressRequest,
    ) -> sae_20190506_models.CreateIngressResponse:
        """
        @summary Creates a routing rule.
        
        @param request: CreateIngressRequest
        @return: CreateIngressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ingress_with_options(request, headers, runtime)

    async def create_ingress_async(
        self,
        request: sae_20190506_models.CreateIngressRequest,
    ) -> sae_20190506_models.CreateIngressResponse:
        """
        @summary Creates a routing rule.
        
        @param request: CreateIngressRequest
        @return: CreateIngressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ingress_with_options_async(request, headers, runtime)

    def create_job_with_options(
        self,
        request: sae_20190506_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateJobResponse:
        """
        @summary Create a job template.
        
        @param request: CreateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.slice):
            query['Slice'] = request.slice
        if not UtilClient.is_unset(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/createJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: sae_20190506_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateJobResponse:
        """
        @summary Create a job template.
        
        @param request: CreateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.slice):
            query['Slice'] = request.slice
        if not UtilClient.is_unset(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/createJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: sae_20190506_models.CreateJobRequest,
    ) -> sae_20190506_models.CreateJobResponse:
        """
        @summary Create a job template.
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(request, headers, runtime)

    async def create_job_async(
        self,
        request: sae_20190506_models.CreateJobRequest,
    ) -> sae_20190506_models.CreateJobResponse:
        """
        @summary Create a job template.
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(request, headers, runtime)

    def create_namespace_with_options(
        self,
        request: sae_20190506_models.CreateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateNamespaceResponse:
        """
        @summary Create a namespace.
        
        @param request: CreateNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_micro_registration):
            query['EnableMicroRegistration'] = request.enable_micro_registration
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: sae_20190506_models.CreateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateNamespaceResponse:
        """
        @summary Create a namespace.
        
        @param request: CreateNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_micro_registration):
            query['EnableMicroRegistration'] = request.enable_micro_registration
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: sae_20190506_models.CreateNamespaceRequest,
    ) -> sae_20190506_models.CreateNamespaceResponse:
        """
        @summary Create a namespace.
        
        @param request: CreateNamespaceRequest
        @return: CreateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_namespace_with_options(request, headers, runtime)

    async def create_namespace_async(
        self,
        request: sae_20190506_models.CreateNamespaceRequest,
    ) -> sae_20190506_models.CreateNamespaceResponse:
        """
        @summary Create a namespace.
        
        @param request: CreateNamespaceRequest
        @return: CreateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_namespace_with_options_async(request, headers, runtime)

    def create_secret_with_options(
        self,
        tmp_req: sae_20190506_models.CreateSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateSecretResponse:
        """
        @summary Null
        
        @param tmp_req: CreateSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecretResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sae_20190506_models.CreateSecretShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.secret_data):
            request.secret_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.secret_data, 'SecretData', 'json')
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_data_shrink):
            query['SecretData'] = request.secret_data_shrink
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.secret_type):
            query['SecretType'] = request.secret_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_with_options_async(
        self,
        tmp_req: sae_20190506_models.CreateSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateSecretResponse:
        """
        @summary Null
        
        @param tmp_req: CreateSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecretResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sae_20190506_models.CreateSecretShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.secret_data):
            request.secret_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.secret_data, 'SecretData', 'json')
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_data_shrink):
            query['SecretData'] = request.secret_data_shrink
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.secret_type):
            query['SecretType'] = request.secret_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret(
        self,
        request: sae_20190506_models.CreateSecretRequest,
    ) -> sae_20190506_models.CreateSecretResponse:
        """
        @summary Null
        
        @param request: CreateSecretRequest
        @return: CreateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_secret_with_options(request, headers, runtime)

    async def create_secret_async(
        self,
        request: sae_20190506_models.CreateSecretRequest,
    ) -> sae_20190506_models.CreateSecretResponse:
        """
        @summary Null
        
        @param request: CreateSecretRequest
        @return: CreateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_secret_with_options_async(request, headers, runtime)

    def create_web_application_with_options(
        self,
        request: sae_20190506_models.CreateWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateWebApplicationResponse:
        """
        @summary Create a web application
        
        @description Call the CreateWebApplication operation to create a web application.
        
        @param request: CreateWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_web_application_with_options_async(
        self,
        request: sae_20190506_models.CreateWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateWebApplicationResponse:
        """
        @summary Create a web application
        
        @description Call the CreateWebApplication operation to create a web application.
        
        @param request: CreateWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_web_application(
        self,
        request: sae_20190506_models.CreateWebApplicationRequest,
    ) -> sae_20190506_models.CreateWebApplicationResponse:
        """
        @summary Create a web application
        
        @description Call the CreateWebApplication operation to create a web application.
        
        @param request: CreateWebApplicationRequest
        @return: CreateWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_web_application_with_options(request, headers, runtime)

    async def create_web_application_async(
        self,
        request: sae_20190506_models.CreateWebApplicationRequest,
    ) -> sae_20190506_models.CreateWebApplicationResponse:
        """
        @summary Create a web application
        
        @description Call the CreateWebApplication operation to create a web application.
        
        @param request: CreateWebApplicationRequest
        @return: CreateWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_web_application_with_options_async(request, headers, runtime)

    def create_web_custom_domain_with_options(
        self,
        request: sae_20190506_models.CreateWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateWebCustomDomainResponse:
        """
        @summary Create a custom domain name for the web application.
        
        @description Create a custom domain name for the web application.
        
        @param request: CreateWebCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWebCustomDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateWebCustomDomain',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/custom-domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateWebCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_web_custom_domain_with_options_async(
        self,
        request: sae_20190506_models.CreateWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateWebCustomDomainResponse:
        """
        @summary Create a custom domain name for the web application.
        
        @description Create a custom domain name for the web application.
        
        @param request: CreateWebCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWebCustomDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateWebCustomDomain',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/custom-domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateWebCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_web_custom_domain(
        self,
        request: sae_20190506_models.CreateWebCustomDomainRequest,
    ) -> sae_20190506_models.CreateWebCustomDomainResponse:
        """
        @summary Create a custom domain name for the web application.
        
        @description Create a custom domain name for the web application.
        
        @param request: CreateWebCustomDomainRequest
        @return: CreateWebCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_web_custom_domain_with_options(request, headers, runtime)

    async def create_web_custom_domain_async(
        self,
        request: sae_20190506_models.CreateWebCustomDomainRequest,
    ) -> sae_20190506_models.CreateWebCustomDomainResponse:
        """
        @summary Create a custom domain name for the web application.
        
        @description Create a custom domain name for the web application.
        
        @param request: CreateWebCustomDomainRequest
        @return: CreateWebCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_web_custom_domain_with_options_async(request, headers, runtime)

    def delete_application_with_options(
        self,
        request: sae_20190506_models.DeleteApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/deleteApplication',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: sae_20190506_models.DeleteApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/deleteApplication',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: sae_20190506_models.DeleteApplicationRequest,
    ) -> sae_20190506_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_application_with_options(request, headers, runtime)

    async def delete_application_async(
        self,
        request: sae_20190506_models.DeleteApplicationRequest,
    ) -> sae_20190506_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_application_with_options_async(request, headers, runtime)

    def delete_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.DeleteApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteApplicationScalingRuleResponse:
        """
        @summary 7171a6ca-d1cd-4928-8642-7d5cfe69\\\\*\\*\\*\
        
        @param request: DeleteApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.DeleteApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteApplicationScalingRuleResponse:
        """
        @summary 7171a6ca-d1cd-4928-8642-7d5cfe69\\\\*\\*\\*\
        
        @param request: DeleteApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_scaling_rule(
        self,
        request: sae_20190506_models.DeleteApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DeleteApplicationScalingRuleResponse:
        """
        @summary 7171a6ca-d1cd-4928-8642-7d5cfe69\\\\*\\*\\*\
        
        @param request: DeleteApplicationScalingRuleRequest
        @return: DeleteApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_application_scaling_rule_with_options(request, headers, runtime)

    async def delete_application_scaling_rule_async(
        self,
        request: sae_20190506_models.DeleteApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DeleteApplicationScalingRuleResponse:
        """
        @summary 7171a6ca-d1cd-4928-8642-7d5cfe69\\\\*\\*\\*\
        
        @param request: DeleteApplicationScalingRuleRequest
        @return: DeleteApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_application_scaling_rule_with_options_async(request, headers, runtime)

    def delete_config_map_with_options(
        self,
        request: sae_20190506_models.DeleteConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteConfigMapResponse:
        """
        @summary Deletes a ConfigMap.
        
        @param request: DeleteConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigMapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_map_with_options_async(
        self,
        request: sae_20190506_models.DeleteConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteConfigMapResponse:
        """
        @summary Deletes a ConfigMap.
        
        @param request: DeleteConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigMapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_map(
        self,
        request: sae_20190506_models.DeleteConfigMapRequest,
    ) -> sae_20190506_models.DeleteConfigMapResponse:
        """
        @summary Deletes a ConfigMap.
        
        @param request: DeleteConfigMapRequest
        @return: DeleteConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_config_map_with_options(request, headers, runtime)

    async def delete_config_map_async(
        self,
        request: sae_20190506_models.DeleteConfigMapRequest,
    ) -> sae_20190506_models.DeleteConfigMapResponse:
        """
        @summary Deletes a ConfigMap.
        
        @param request: DeleteConfigMapRequest
        @return: DeleteConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_config_map_with_options_async(request, headers, runtime)

    def delete_grey_tag_route_with_options(
        self,
        request: sae_20190506_models.DeleteGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteGreyTagRouteResponse:
        """
        @summary Deletes a canary release rule based on the specified rule ID.
        
        @param request: DeleteGreyTagRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGreyTagRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_grey_tag_route_with_options_async(
        self,
        request: sae_20190506_models.DeleteGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteGreyTagRouteResponse:
        """
        @summary Deletes a canary release rule based on the specified rule ID.
        
        @param request: DeleteGreyTagRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGreyTagRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_grey_tag_route(
        self,
        request: sae_20190506_models.DeleteGreyTagRouteRequest,
    ) -> sae_20190506_models.DeleteGreyTagRouteResponse:
        """
        @summary Deletes a canary release rule based on the specified rule ID.
        
        @param request: DeleteGreyTagRouteRequest
        @return: DeleteGreyTagRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_grey_tag_route_with_options(request, headers, runtime)

    async def delete_grey_tag_route_async(
        self,
        request: sae_20190506_models.DeleteGreyTagRouteRequest,
    ) -> sae_20190506_models.DeleteGreyTagRouteResponse:
        """
        @summary Deletes a canary release rule based on the specified rule ID.
        
        @param request: DeleteGreyTagRouteRequest
        @return: DeleteGreyTagRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_grey_tag_route_with_options_async(request, headers, runtime)

    def delete_history_job_with_options(
        self,
        request: sae_20190506_models.DeleteHistoryJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteHistoryJobResponse:
        """
        @summary Delete a job.
        
        @param request: DeleteHistoryJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHistoryJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHistoryJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/deleteHistoryJob',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_history_job_with_options_async(
        self,
        request: sae_20190506_models.DeleteHistoryJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteHistoryJobResponse:
        """
        @summary Delete a job.
        
        @param request: DeleteHistoryJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHistoryJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHistoryJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/deleteHistoryJob',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_history_job(
        self,
        request: sae_20190506_models.DeleteHistoryJobRequest,
    ) -> sae_20190506_models.DeleteHistoryJobResponse:
        """
        @summary Delete a job.
        
        @param request: DeleteHistoryJobRequest
        @return: DeleteHistoryJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_history_job_with_options(request, headers, runtime)

    async def delete_history_job_async(
        self,
        request: sae_20190506_models.DeleteHistoryJobRequest,
    ) -> sae_20190506_models.DeleteHistoryJobResponse:
        """
        @summary Delete a job.
        
        @param request: DeleteHistoryJobRequest
        @return: DeleteHistoryJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_history_job_with_options_async(request, headers, runtime)

    def delete_ingress_with_options(
        self,
        request: sae_20190506_models.DeleteIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteIngressResponse:
        """
        @summary Deletes a routing rule.
        
        @param request: DeleteIngressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIngressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ingress_with_options_async(
        self,
        request: sae_20190506_models.DeleteIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteIngressResponse:
        """
        @summary Deletes a routing rule.
        
        @param request: DeleteIngressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIngressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ingress(
        self,
        request: sae_20190506_models.DeleteIngressRequest,
    ) -> sae_20190506_models.DeleteIngressResponse:
        """
        @summary Deletes a routing rule.
        
        @param request: DeleteIngressRequest
        @return: DeleteIngressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ingress_with_options(request, headers, runtime)

    async def delete_ingress_async(
        self,
        request: sae_20190506_models.DeleteIngressRequest,
    ) -> sae_20190506_models.DeleteIngressResponse:
        """
        @summary Deletes a routing rule.
        
        @param request: DeleteIngressRequest
        @return: DeleteIngressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ingress_with_options_async(request, headers, runtime)

    def delete_job_with_options(
        self,
        request: sae_20190506_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteJobResponse:
        """
        @summary Delete a job template.
        
        @param request: DeleteJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/deleteJob',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: sae_20190506_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteJobResponse:
        """
        @summary Delete a job template.
        
        @param request: DeleteJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/deleteJob',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        request: sae_20190506_models.DeleteJobRequest,
    ) -> sae_20190506_models.DeleteJobResponse:
        """
        @summary Delete a job template.
        
        @param request: DeleteJobRequest
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_job_with_options(request, headers, runtime)

    async def delete_job_async(
        self,
        request: sae_20190506_models.DeleteJobRequest,
    ) -> sae_20190506_models.DeleteJobResponse:
        """
        @summary Delete a job template.
        
        @param request: DeleteJobRequest
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_job_with_options_async(request, headers, runtime)

    def delete_namespace_with_options(
        self,
        request: sae_20190506_models.DeleteNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteNamespaceResponse:
        """
        @summary Deletes a namespace.
        
        @param request: DeleteNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: sae_20190506_models.DeleteNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteNamespaceResponse:
        """
        @summary Deletes a namespace.
        
        @param request: DeleteNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: sae_20190506_models.DeleteNamespaceRequest,
    ) -> sae_20190506_models.DeleteNamespaceResponse:
        """
        @summary Deletes a namespace.
        
        @param request: DeleteNamespaceRequest
        @return: DeleteNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_namespace_with_options(request, headers, runtime)

    async def delete_namespace_async(
        self,
        request: sae_20190506_models.DeleteNamespaceRequest,
    ) -> sae_20190506_models.DeleteNamespaceResponse:
        """
        @summary Deletes a namespace.
        
        @param request: DeleteNamespaceRequest
        @return: DeleteNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_namespace_with_options_async(request, headers, runtime)

    def delete_secret_with_options(
        self,
        request: sae_20190506_models.DeleteSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteSecretResponse:
        """
        @summary Deletes a Secret.
        
        @param request: DeleteSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_with_options_async(
        self,
        request: sae_20190506_models.DeleteSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteSecretResponse:
        """
        @summary Deletes a Secret.
        
        @param request: DeleteSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret(
        self,
        request: sae_20190506_models.DeleteSecretRequest,
    ) -> sae_20190506_models.DeleteSecretResponse:
        """
        @summary Deletes a Secret.
        
        @param request: DeleteSecretRequest
        @return: DeleteSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_secret_with_options(request, headers, runtime)

    async def delete_secret_async(
        self,
        request: sae_20190506_models.DeleteSecretRequest,
    ) -> sae_20190506_models.DeleteSecretResponse:
        """
        @summary Deletes a Secret.
        
        @param request: DeleteSecretRequest
        @return: DeleteSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_secret_with_options_async(request, headers, runtime)

    def delete_web_application_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.DeleteWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteWebApplicationResponse:
        """
        @summary Delete a web application.
        
        @description Call the DeleteWebApplication operation to delete a web application.
        
        @param request: DeleteWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_application_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.DeleteWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteWebApplicationResponse:
        """
        @summary Delete a web application.
        
        @description Call the DeleteWebApplication operation to delete a web application.
        
        @param request: DeleteWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_application(
        self,
        application_id: str,
        request: sae_20190506_models.DeleteWebApplicationRequest,
    ) -> sae_20190506_models.DeleteWebApplicationResponse:
        """
        @summary Delete a web application.
        
        @description Call the DeleteWebApplication operation to delete a web application.
        
        @param request: DeleteWebApplicationRequest
        @return: DeleteWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_web_application_with_options(application_id, request, headers, runtime)

    async def delete_web_application_async(
        self,
        application_id: str,
        request: sae_20190506_models.DeleteWebApplicationRequest,
    ) -> sae_20190506_models.DeleteWebApplicationResponse:
        """
        @summary Delete a web application.
        
        @description Call the DeleteWebApplication operation to delete a web application.
        
        @param request: DeleteWebApplicationRequest
        @return: DeleteWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_web_application_with_options_async(application_id, request, headers, runtime)

    def delete_web_application_revision_with_options(
        self,
        application_id: str,
        revision_id: str,
        request: sae_20190506_models.DeleteWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteWebApplicationRevisionResponse:
        """
        @summary Delete a web application version.
        
        @description Delete a web application version.
        
        @param request: DeleteWebApplicationRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebApplicationRevisionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebApplicationRevision',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-revisions/{OpenApiUtilClient.get_encode_param(application_id)}/revisions/{OpenApiUtilClient.get_encode_param(revision_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteWebApplicationRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_application_revision_with_options_async(
        self,
        application_id: str,
        revision_id: str,
        request: sae_20190506_models.DeleteWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteWebApplicationRevisionResponse:
        """
        @summary Delete a web application version.
        
        @description Delete a web application version.
        
        @param request: DeleteWebApplicationRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebApplicationRevisionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebApplicationRevision',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-revisions/{OpenApiUtilClient.get_encode_param(application_id)}/revisions/{OpenApiUtilClient.get_encode_param(revision_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteWebApplicationRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_application_revision(
        self,
        application_id: str,
        revision_id: str,
        request: sae_20190506_models.DeleteWebApplicationRevisionRequest,
    ) -> sae_20190506_models.DeleteWebApplicationRevisionResponse:
        """
        @summary Delete a web application version.
        
        @description Delete a web application version.
        
        @param request: DeleteWebApplicationRevisionRequest
        @return: DeleteWebApplicationRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_web_application_revision_with_options(application_id, revision_id, request, headers, runtime)

    async def delete_web_application_revision_async(
        self,
        application_id: str,
        revision_id: str,
        request: sae_20190506_models.DeleteWebApplicationRevisionRequest,
    ) -> sae_20190506_models.DeleteWebApplicationRevisionResponse:
        """
        @summary Delete a web application version.
        
        @description Delete a web application version.
        
        @param request: DeleteWebApplicationRevisionRequest
        @return: DeleteWebApplicationRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_web_application_revision_with_options_async(application_id, revision_id, request, headers, runtime)

    def delete_web_custom_domain_with_options(
        self,
        domain_name: str,
        request: sae_20190506_models.DeleteWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteWebCustomDomainResponse:
        """
        @summary Delete a custom domain name.
        
        @description Delete a custom domain name.
        
        @param request: DeleteWebCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebCustomDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebCustomDomain',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteWebCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_custom_domain_with_options_async(
        self,
        domain_name: str,
        request: sae_20190506_models.DeleteWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteWebCustomDomainResponse:
        """
        @summary Delete a custom domain name.
        
        @description Delete a custom domain name.
        
        @param request: DeleteWebCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWebCustomDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebCustomDomain',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteWebCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_custom_domain(
        self,
        domain_name: str,
        request: sae_20190506_models.DeleteWebCustomDomainRequest,
    ) -> sae_20190506_models.DeleteWebCustomDomainResponse:
        """
        @summary Delete a custom domain name.
        
        @description Delete a custom domain name.
        
        @param request: DeleteWebCustomDomainRequest
        @return: DeleteWebCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_web_custom_domain_with_options(domain_name, request, headers, runtime)

    async def delete_web_custom_domain_async(
        self,
        domain_name: str,
        request: sae_20190506_models.DeleteWebCustomDomainRequest,
    ) -> sae_20190506_models.DeleteWebCustomDomainResponse:
        """
        @summary Delete a custom domain name.
        
        @description Delete a custom domain name.
        
        @param request: DeleteWebCustomDomainRequest
        @return: DeleteWebCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_web_custom_domain_with_options_async(domain_name, request, headers, runtime)

    def deploy_application_with_options(
        self,
        tmp_req: sae_20190506_models.DeployApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeployApplicationResponse:
        """
        @summary Deploys an application.
        
        @param tmp_req: DeployApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployApplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sae_20190506_models.DeployApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.init_containers_config):
            request.init_containers_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.init_containers_config, 'InitContainersConfig', 'json')
        if not UtilClient.is_unset(tmp_req.sidecar_containers_config):
            request.sidecar_containers_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sidecar_containers_config, 'SidecarContainersConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.change_order_desc):
            query['ChangeOrderDesc'] = request.change_order_desc
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.custom_image_network_type):
            query['CustomImageNetworkType'] = request.custom_image_network_type
        if not UtilClient.is_unset(request.deploy):
            query['Deploy'] = request.deploy
        if not UtilClient.is_unset(request.dotnet):
            query['Dotnet'] = request.dotnet
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not UtilClient.is_unset(request.enable_cpu_burst):
            query['EnableCpuBurst'] = request.enable_cpu_burst
        if not UtilClient.is_unset(request.enable_grey_tag_route):
            query['EnableGreyTagRoute'] = request.enable_grey_tag_route
        if not UtilClient.is_unset(request.enable_new_arms):
            query['EnableNewArms'] = request.enable_new_arms
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not UtilClient.is_unset(request.microservice_engine_config):
            query['MicroserviceEngineConfig'] = request.microservice_engine_config
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not UtilClient.is_unset(request.oidc_role_name):
            query['OidcRoleName'] = request.oidc_role_name
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.secret_mount_desc):
            query['SecretMountDesc'] = request.secret_mount_desc
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_sidecar_resource_isolated):
            body['EnableSidecarResourceIsolated'] = request.enable_sidecar_resource_isolated
        if not UtilClient.is_unset(request.init_containers_config_shrink):
            body['InitContainersConfig'] = request.init_containers_config_shrink
        if not UtilClient.is_unset(request.micro_registration_config):
            body['MicroRegistrationConfig'] = request.micro_registration_config
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php):
            body['Php'] = request.php
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        if not UtilClient.is_unset(request.service_tags):
            body['ServiceTags'] = request.service_tags
        if not UtilClient.is_unset(request.sidecar_containers_config_shrink):
            body['SidecarContainersConfig'] = request.sidecar_containers_config_shrink
        if not UtilClient.is_unset(request.swimlane_pvtz_discovery_svc):
            body['SwimlanePvtzDiscoverySvc'] = request.swimlane_pvtz_discovery_svc
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/deployApplication',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeployApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_application_with_options_async(
        self,
        tmp_req: sae_20190506_models.DeployApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeployApplicationResponse:
        """
        @summary Deploys an application.
        
        @param tmp_req: DeployApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployApplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sae_20190506_models.DeployApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.init_containers_config):
            request.init_containers_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.init_containers_config, 'InitContainersConfig', 'json')
        if not UtilClient.is_unset(tmp_req.sidecar_containers_config):
            request.sidecar_containers_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sidecar_containers_config, 'SidecarContainersConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.change_order_desc):
            query['ChangeOrderDesc'] = request.change_order_desc
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.custom_image_network_type):
            query['CustomImageNetworkType'] = request.custom_image_network_type
        if not UtilClient.is_unset(request.deploy):
            query['Deploy'] = request.deploy
        if not UtilClient.is_unset(request.dotnet):
            query['Dotnet'] = request.dotnet
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not UtilClient.is_unset(request.enable_cpu_burst):
            query['EnableCpuBurst'] = request.enable_cpu_burst
        if not UtilClient.is_unset(request.enable_grey_tag_route):
            query['EnableGreyTagRoute'] = request.enable_grey_tag_route
        if not UtilClient.is_unset(request.enable_new_arms):
            query['EnableNewArms'] = request.enable_new_arms
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not UtilClient.is_unset(request.microservice_engine_config):
            query['MicroserviceEngineConfig'] = request.microservice_engine_config
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not UtilClient.is_unset(request.oidc_role_name):
            query['OidcRoleName'] = request.oidc_role_name
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.secret_mount_desc):
            query['SecretMountDesc'] = request.secret_mount_desc
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_sidecar_resource_isolated):
            body['EnableSidecarResourceIsolated'] = request.enable_sidecar_resource_isolated
        if not UtilClient.is_unset(request.init_containers_config_shrink):
            body['InitContainersConfig'] = request.init_containers_config_shrink
        if not UtilClient.is_unset(request.micro_registration_config):
            body['MicroRegistrationConfig'] = request.micro_registration_config
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php):
            body['Php'] = request.php
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        if not UtilClient.is_unset(request.service_tags):
            body['ServiceTags'] = request.service_tags
        if not UtilClient.is_unset(request.sidecar_containers_config_shrink):
            body['SidecarContainersConfig'] = request.sidecar_containers_config_shrink
        if not UtilClient.is_unset(request.swimlane_pvtz_discovery_svc):
            body['SwimlanePvtzDiscoverySvc'] = request.swimlane_pvtz_discovery_svc
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/deployApplication',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeployApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_application(
        self,
        request: sae_20190506_models.DeployApplicationRequest,
    ) -> sae_20190506_models.DeployApplicationResponse:
        """
        @summary Deploys an application.
        
        @param request: DeployApplicationRequest
        @return: DeployApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_application_with_options(request, headers, runtime)

    async def deploy_application_async(
        self,
        request: sae_20190506_models.DeployApplicationRequest,
    ) -> sae_20190506_models.DeployApplicationResponse:
        """
        @summary Deploys an application.
        
        @param request: DeployApplicationRequest
        @return: DeployApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_application_with_options_async(request, headers, runtime)

    def describe_app_service_detail_with_options(
        self,
        request: sae_20190506_models.DescribeAppServiceDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeAppServiceDetailResponse:
        """
        @summary Queries the metadata details of the service of an application.
        
        @param request: DescribeAppServiceDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppServiceDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.nacos_instance_id):
            query['NacosInstanceId'] = request.nacos_instance_id
        if not UtilClient.is_unset(request.nacos_namespace_id):
            query['NacosNamespaceId'] = request.nacos_namespace_id
        if not UtilClient.is_unset(request.service_group):
            query['ServiceGroup'] = request.service_group
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppServiceDetail',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/describeAppServiceDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeAppServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_service_detail_with_options_async(
        self,
        request: sae_20190506_models.DescribeAppServiceDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeAppServiceDetailResponse:
        """
        @summary Queries the metadata details of the service of an application.
        
        @param request: DescribeAppServiceDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppServiceDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.nacos_instance_id):
            query['NacosInstanceId'] = request.nacos_instance_id
        if not UtilClient.is_unset(request.nacos_namespace_id):
            query['NacosNamespaceId'] = request.nacos_namespace_id
        if not UtilClient.is_unset(request.service_group):
            query['ServiceGroup'] = request.service_group
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppServiceDetail',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/describeAppServiceDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeAppServiceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_service_detail(
        self,
        request: sae_20190506_models.DescribeAppServiceDetailRequest,
    ) -> sae_20190506_models.DescribeAppServiceDetailResponse:
        """
        @summary Queries the metadata details of the service of an application.
        
        @param request: DescribeAppServiceDetailRequest
        @return: DescribeAppServiceDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_service_detail_with_options(request, headers, runtime)

    async def describe_app_service_detail_async(
        self,
        request: sae_20190506_models.DescribeAppServiceDetailRequest,
    ) -> sae_20190506_models.DescribeAppServiceDetailResponse:
        """
        @summary Queries the metadata details of the service of an application.
        
        @param request: DescribeAppServiceDetailRequest
        @return: DescribeAppServiceDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_service_detail_with_options_async(request, headers, runtime)

    def describe_application_config_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationConfigResponse:
        """
        @summary Queries the configurations of an application.
        
        @param request: DescribeApplicationConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_config_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationConfigResponse:
        """
        @summary Queries the configurations of an application.
        
        @param request: DescribeApplicationConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_config(
        self,
        request: sae_20190506_models.DescribeApplicationConfigRequest,
    ) -> sae_20190506_models.DescribeApplicationConfigResponse:
        """
        @summary Queries the configurations of an application.
        
        @param request: DescribeApplicationConfigRequest
        @return: DescribeApplicationConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_config_with_options(request, headers, runtime)

    async def describe_application_config_async(
        self,
        request: sae_20190506_models.DescribeApplicationConfigRequest,
    ) -> sae_20190506_models.DescribeApplicationConfigResponse:
        """
        @summary Queries the configurations of an application.
        
        @param request: DescribeApplicationConfigRequest
        @return: DescribeApplicationConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_config_with_options_async(request, headers, runtime)

    def describe_application_groups_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationGroupsResponse:
        """
        @param request: DescribeApplicationGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationGroups',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_groups_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationGroupsResponse:
        """
        @param request: DescribeApplicationGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationGroups',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_groups(
        self,
        request: sae_20190506_models.DescribeApplicationGroupsRequest,
    ) -> sae_20190506_models.DescribeApplicationGroupsResponse:
        """
        @param request: DescribeApplicationGroupsRequest
        @return: DescribeApplicationGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_groups_with_options(request, headers, runtime)

    async def describe_application_groups_async(
        self,
        request: sae_20190506_models.DescribeApplicationGroupsRequest,
    ) -> sae_20190506_models.DescribeApplicationGroupsResponse:
        """
        @param request: DescribeApplicationGroupsRequest
        @return: DescribeApplicationGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_groups_with_options_async(request, headers, runtime)

    def describe_application_image_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationImageResponse:
        """
        @summary Queries the information about the image of an application.
        
        @param request: DescribeApplicationImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationImage',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/container/describeApplicationImage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_image_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationImageResponse:
        """
        @summary Queries the information about the image of an application.
        
        @param request: DescribeApplicationImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationImage',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/container/describeApplicationImage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_image(
        self,
        request: sae_20190506_models.DescribeApplicationImageRequest,
    ) -> sae_20190506_models.DescribeApplicationImageResponse:
        """
        @summary Queries the information about the image of an application.
        
        @param request: DescribeApplicationImageRequest
        @return: DescribeApplicationImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_image_with_options(request, headers, runtime)

    async def describe_application_image_async(
        self,
        request: sae_20190506_models.DescribeApplicationImageRequest,
    ) -> sae_20190506_models.DescribeApplicationImageResponse:
        """
        @summary Queries the information about the image of an application.
        
        @param request: DescribeApplicationImageRequest
        @return: DescribeApplicationImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_image_with_options_async(request, headers, runtime)

    def describe_application_instances_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationInstancesResponse:
        """
        @summary Queries application instances.
        
        @param request: DescribeApplicationInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_instances_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationInstancesResponse:
        """
        @summary Queries application instances.
        
        @param request: DescribeApplicationInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_instances(
        self,
        request: sae_20190506_models.DescribeApplicationInstancesRequest,
    ) -> sae_20190506_models.DescribeApplicationInstancesResponse:
        """
        @summary Queries application instances.
        
        @param request: DescribeApplicationInstancesRequest
        @return: DescribeApplicationInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_instances_with_options(request, headers, runtime)

    async def describe_application_instances_async(
        self,
        request: sae_20190506_models.DescribeApplicationInstancesRequest,
    ) -> sae_20190506_models.DescribeApplicationInstancesResponse:
        """
        @summary Queries application instances.
        
        @param request: DescribeApplicationInstancesRequest
        @return: DescribeApplicationInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_instances_with_options_async(request, headers, runtime)

    def describe_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationScalingRuleResponse:
        """
        @summary Queries a specified auto scaling policy of an application.
        
        @param request: DescribeApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationScalingRuleResponse:
        """
        @summary Queries a specified auto scaling policy of an application.
        
        @param request: DescribeApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_scaling_rule(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DescribeApplicationScalingRuleResponse:
        """
        @summary Queries a specified auto scaling policy of an application.
        
        @param request: DescribeApplicationScalingRuleRequest
        @return: DescribeApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_scaling_rule_with_options(request, headers, runtime)

    async def describe_application_scaling_rule_async(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DescribeApplicationScalingRuleResponse:
        """
        @summary Queries a specified auto scaling policy of an application.
        
        @param request: DescribeApplicationScalingRuleRequest
        @return: DescribeApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_scaling_rule_with_options_async(request, headers, runtime)

    def describe_application_scaling_rules_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationScalingRulesResponse:
        """
        @summary Queries the auto scaling policies of an application.
        
        @param request: DescribeApplicationScalingRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRules',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_scaling_rules_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationScalingRulesResponse:
        """
        @summary Queries the auto scaling policies of an application.
        
        @param request: DescribeApplicationScalingRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRules',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_scaling_rules(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRulesRequest,
    ) -> sae_20190506_models.DescribeApplicationScalingRulesResponse:
        """
        @summary Queries the auto scaling policies of an application.
        
        @param request: DescribeApplicationScalingRulesRequest
        @return: DescribeApplicationScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_scaling_rules_with_options(request, headers, runtime)

    async def describe_application_scaling_rules_async(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRulesRequest,
    ) -> sae_20190506_models.DescribeApplicationScalingRulesResponse:
        """
        @summary Queries the auto scaling policies of an application.
        
        @param request: DescribeApplicationScalingRulesRequest
        @return: DescribeApplicationScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_scaling_rules_with_options_async(request, headers, runtime)

    def describe_application_slbs_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationSlbsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationSlbsResponse:
        """
        @summary 017f39b8-dfa4-4e16-a84b-1dcee4b1\\\\*\\*\\*\
        
        @param request: DescribeApplicationSlbsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationSlbsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationSlbs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationSlbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_slbs_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationSlbsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationSlbsResponse:
        """
        @summary 017f39b8-dfa4-4e16-a84b-1dcee4b1\\\\*\\*\\*\
        
        @param request: DescribeApplicationSlbsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationSlbsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationSlbs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationSlbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_slbs(
        self,
        request: sae_20190506_models.DescribeApplicationSlbsRequest,
    ) -> sae_20190506_models.DescribeApplicationSlbsResponse:
        """
        @summary 017f39b8-dfa4-4e16-a84b-1dcee4b1\\\\*\\*\\*\
        
        @param request: DescribeApplicationSlbsRequest
        @return: DescribeApplicationSlbsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_slbs_with_options(request, headers, runtime)

    async def describe_application_slbs_async(
        self,
        request: sae_20190506_models.DescribeApplicationSlbsRequest,
    ) -> sae_20190506_models.DescribeApplicationSlbsResponse:
        """
        @summary 017f39b8-dfa4-4e16-a84b-1dcee4b1\\\\*\\*\\*\
        
        @param request: DescribeApplicationSlbsRequest
        @return: DescribeApplicationSlbsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_slbs_with_options_async(request, headers, runtime)

    def describe_application_status_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationStatusResponse:
        """
        @summary Queries the status of an application.
        
        @param request: DescribeApplicationStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationStatus',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_status_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationStatusResponse:
        """
        @summary Queries the status of an application.
        
        @param request: DescribeApplicationStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationStatus',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_status(
        self,
        request: sae_20190506_models.DescribeApplicationStatusRequest,
    ) -> sae_20190506_models.DescribeApplicationStatusResponse:
        """
        @summary Queries the status of an application.
        
        @param request: DescribeApplicationStatusRequest
        @return: DescribeApplicationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_status_with_options(request, headers, runtime)

    async def describe_application_status_async(
        self,
        request: sae_20190506_models.DescribeApplicationStatusRequest,
    ) -> sae_20190506_models.DescribeApplicationStatusResponse:
        """
        @summary Queries the status of an application.
        
        @param request: DescribeApplicationStatusRequest
        @return: DescribeApplicationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_status_with_options_async(request, headers, runtime)

    def describe_change_order_with_options(
        self,
        request: sae_20190506_models.DescribeChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeChangeOrderResponse:
        """
        @summary Queries the information of a change order.
        
        @param request: DescribeChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/DescribeChangeOrder',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_change_order_with_options_async(
        self,
        request: sae_20190506_models.DescribeChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeChangeOrderResponse:
        """
        @summary Queries the information of a change order.
        
        @param request: DescribeChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/DescribeChangeOrder',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_change_order(
        self,
        request: sae_20190506_models.DescribeChangeOrderRequest,
    ) -> sae_20190506_models.DescribeChangeOrderResponse:
        """
        @summary Queries the information of a change order.
        
        @param request: DescribeChangeOrderRequest
        @return: DescribeChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_change_order_with_options(request, headers, runtime)

    async def describe_change_order_async(
        self,
        request: sae_20190506_models.DescribeChangeOrderRequest,
    ) -> sae_20190506_models.DescribeChangeOrderResponse:
        """
        @summary Queries the information of a change order.
        
        @param request: DescribeChangeOrderRequest
        @return: DescribeChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_change_order_with_options_async(request, headers, runtime)

    def describe_components_with_options(
        self,
        request: sae_20190506_models.DescribeComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeComponentsResponse:
        """
        @summary Queries the version of the component that is required when you create and deploy an application.
        
        @param request: DescribeComponentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponents',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/resource/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_components_with_options_async(
        self,
        request: sae_20190506_models.DescribeComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeComponentsResponse:
        """
        @summary Queries the version of the component that is required when you create and deploy an application.
        
        @param request: DescribeComponentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponents',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/resource/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_components(
        self,
        request: sae_20190506_models.DescribeComponentsRequest,
    ) -> sae_20190506_models.DescribeComponentsResponse:
        """
        @summary Queries the version of the component that is required when you create and deploy an application.
        
        @param request: DescribeComponentsRequest
        @return: DescribeComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_components_with_options(request, headers, runtime)

    async def describe_components_async(
        self,
        request: sae_20190506_models.DescribeComponentsRequest,
    ) -> sae_20190506_models.DescribeComponentsResponse:
        """
        @summary Queries the version of the component that is required when you create and deploy an application.
        
        @param request: DescribeComponentsRequest
        @return: DescribeComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_components_with_options_async(request, headers, runtime)

    def describe_config_map_with_options(
        self,
        request: sae_20190506_models.DescribeConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeConfigMapResponse:
        """
        @summary Queries the details of a ConfigMap.
        
        @param request: DescribeConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConfigMapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_config_map_with_options_async(
        self,
        request: sae_20190506_models.DescribeConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeConfigMapResponse:
        """
        @summary Queries the details of a ConfigMap.
        
        @param request: DescribeConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConfigMapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_config_map(
        self,
        request: sae_20190506_models.DescribeConfigMapRequest,
    ) -> sae_20190506_models.DescribeConfigMapResponse:
        """
        @summary Queries the details of a ConfigMap.
        
        @param request: DescribeConfigMapRequest
        @return: DescribeConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_config_map_with_options(request, headers, runtime)

    async def describe_config_map_async(
        self,
        request: sae_20190506_models.DescribeConfigMapRequest,
    ) -> sae_20190506_models.DescribeConfigMapResponse:
        """
        @summary Queries the details of a ConfigMap.
        
        @param request: DescribeConfigMapRequest
        @return: DescribeConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_config_map_with_options_async(request, headers, runtime)

    def describe_configuration_price_with_options(
        self,
        request: sae_20190506_models.DescribeConfigurationPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeConfigurationPriceResponse:
        """
        @summary Query configuration price.
        
        @param request: DescribeConfigurationPriceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConfigurationPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigurationPrice',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/configurationPrice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeConfigurationPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_configuration_price_with_options_async(
        self,
        request: sae_20190506_models.DescribeConfigurationPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeConfigurationPriceResponse:
        """
        @summary Query configuration price.
        
        @param request: DescribeConfigurationPriceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConfigurationPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigurationPrice',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/configurationPrice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeConfigurationPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_configuration_price(
        self,
        request: sae_20190506_models.DescribeConfigurationPriceRequest,
    ) -> sae_20190506_models.DescribeConfigurationPriceResponse:
        """
        @summary Query configuration price.
        
        @param request: DescribeConfigurationPriceRequest
        @return: DescribeConfigurationPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_configuration_price_with_options(request, headers, runtime)

    async def describe_configuration_price_async(
        self,
        request: sae_20190506_models.DescribeConfigurationPriceRequest,
    ) -> sae_20190506_models.DescribeConfigurationPriceResponse:
        """
        @summary Query configuration price.
        
        @param request: DescribeConfigurationPriceRequest
        @return: DescribeConfigurationPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_configuration_price_with_options_async(request, headers, runtime)

    def describe_edas_containers_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeEdasContainersResponse:
        """
        @summary Queries the container components of a microservices application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdasContainersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdasContainers',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/resource/edasContainers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeEdasContainersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_edas_containers_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeEdasContainersResponse:
        """
        @summary Queries the container components of a microservices application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdasContainersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdasContainers',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/resource/edasContainers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeEdasContainersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_edas_containers(self) -> sae_20190506_models.DescribeEdasContainersResponse:
        """
        @summary Queries the container components of a microservices application.
        
        @return: DescribeEdasContainersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edas_containers_with_options(headers, runtime)

    async def describe_edas_containers_async(self) -> sae_20190506_models.DescribeEdasContainersResponse:
        """
        @summary Queries the container components of a microservices application.
        
        @return: DescribeEdasContainersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_edas_containers_with_options_async(headers, runtime)

    def describe_grey_tag_route_with_options(
        self,
        request: sae_20190506_models.DescribeGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeGreyTagRouteResponse:
        """
        @summary Queries the details of a canary release rule based on the specified rule ID.
        
        @param request: DescribeGreyTagRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGreyTagRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grey_tag_route_with_options_async(
        self,
        request: sae_20190506_models.DescribeGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeGreyTagRouteResponse:
        """
        @summary Queries the details of a canary release rule based on the specified rule ID.
        
        @param request: DescribeGreyTagRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGreyTagRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grey_tag_route(
        self,
        request: sae_20190506_models.DescribeGreyTagRouteRequest,
    ) -> sae_20190506_models.DescribeGreyTagRouteResponse:
        """
        @summary Queries the details of a canary release rule based on the specified rule ID.
        
        @param request: DescribeGreyTagRouteRequest
        @return: DescribeGreyTagRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_grey_tag_route_with_options(request, headers, runtime)

    async def describe_grey_tag_route_async(
        self,
        request: sae_20190506_models.DescribeGreyTagRouteRequest,
    ) -> sae_20190506_models.DescribeGreyTagRouteResponse:
        """
        @summary Queries the details of a canary release rule based on the specified rule ID.
        
        @param request: DescribeGreyTagRouteRequest
        @return: DescribeGreyTagRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_grey_tag_route_with_options_async(request, headers, runtime)

    def describe_ingress_with_options(
        self,
        request: sae_20190506_models.DescribeIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeIngressResponse:
        """
        @summary Call the DescribeIngress operation to query the details of an Ingress.
        
        @param request: DescribeIngressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIngressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ingress_with_options_async(
        self,
        request: sae_20190506_models.DescribeIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeIngressResponse:
        """
        @summary Call the DescribeIngress operation to query the details of an Ingress.
        
        @param request: DescribeIngressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIngressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ingress(
        self,
        request: sae_20190506_models.DescribeIngressRequest,
    ) -> sae_20190506_models.DescribeIngressResponse:
        """
        @summary Call the DescribeIngress operation to query the details of an Ingress.
        
        @param request: DescribeIngressRequest
        @return: DescribeIngressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ingress_with_options(request, headers, runtime)

    async def describe_ingress_async(
        self,
        request: sae_20190506_models.DescribeIngressRequest,
    ) -> sae_20190506_models.DescribeIngressResponse:
        """
        @summary Call the DescribeIngress operation to query the details of an Ingress.
        
        @param request: DescribeIngressRequest
        @return: DescribeIngressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_ingress_with_options_async(request, headers, runtime)

    def describe_instance_log_with_options(
        self,
        request: sae_20190506_models.DescribeInstanceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeInstanceLogResponse:
        """
        @param request: DescribeInstanceLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_id):
            query['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceLog',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/instance/describeInstanceLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_log_with_options_async(
        self,
        request: sae_20190506_models.DescribeInstanceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeInstanceLogResponse:
        """
        @param request: DescribeInstanceLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_id):
            query['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceLog',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/instance/describeInstanceLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeInstanceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_log(
        self,
        request: sae_20190506_models.DescribeInstanceLogRequest,
    ) -> sae_20190506_models.DescribeInstanceLogResponse:
        """
        @param request: DescribeInstanceLogRequest
        @return: DescribeInstanceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_log_with_options(request, headers, runtime)

    async def describe_instance_log_async(
        self,
        request: sae_20190506_models.DescribeInstanceLogRequest,
    ) -> sae_20190506_models.DescribeInstanceLogResponse:
        """
        @param request: DescribeInstanceLogRequest
        @return: DescribeInstanceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instance_log_with_options_async(request, headers, runtime)

    def describe_instance_specifications_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeInstanceSpecificationsResponse:
        """
        @summary Queries all instance types.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSpecificationsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecifications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/quota/instanceSpecifications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeInstanceSpecificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_specifications_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeInstanceSpecificationsResponse:
        """
        @summary Queries all instance types.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSpecificationsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecifications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/quota/instanceSpecifications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeInstanceSpecificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_specifications(self) -> sae_20190506_models.DescribeInstanceSpecificationsResponse:
        """
        @summary Queries all instance types.
        
        @return: DescribeInstanceSpecificationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_specifications_with_options(headers, runtime)

    async def describe_instance_specifications_async(self) -> sae_20190506_models.DescribeInstanceSpecificationsResponse:
        """
        @summary Queries all instance types.
        
        @return: DescribeInstanceSpecificationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instance_specifications_with_options_async(headers, runtime)

    def describe_job_with_options(
        self,
        request: sae_20190506_models.DescribeJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobResponse:
        """
        @summary Queries the configurations of a job template.
        
        @param request: DescribeJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_with_options_async(
        self,
        request: sae_20190506_models.DescribeJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobResponse:
        """
        @summary Queries the configurations of a job template.
        
        @param request: DescribeJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job(
        self,
        request: sae_20190506_models.DescribeJobRequest,
    ) -> sae_20190506_models.DescribeJobResponse:
        """
        @summary Queries the configurations of a job template.
        
        @param request: DescribeJobRequest
        @return: DescribeJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_job_with_options(request, headers, runtime)

    async def describe_job_async(
        self,
        request: sae_20190506_models.DescribeJobRequest,
    ) -> sae_20190506_models.DescribeJobResponse:
        """
        @summary Queries the configurations of a job template.
        
        @param request: DescribeJobRequest
        @return: DescribeJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_job_with_options_async(request, headers, runtime)

    def describe_job_history_with_options(
        self,
        request: sae_20190506_models.DescribeJobHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobHistoryResponse:
        """
        @summary Query the information about jobs.
        
        @param request: DescribeJobHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobHistory',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJobHistory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_history_with_options_async(
        self,
        request: sae_20190506_models.DescribeJobHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobHistoryResponse:
        """
        @summary Query the information about jobs.
        
        @param request: DescribeJobHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobHistory',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJobHistory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_history(
        self,
        request: sae_20190506_models.DescribeJobHistoryRequest,
    ) -> sae_20190506_models.DescribeJobHistoryResponse:
        """
        @summary Query the information about jobs.
        
        @param request: DescribeJobHistoryRequest
        @return: DescribeJobHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_job_history_with_options(request, headers, runtime)

    async def describe_job_history_async(
        self,
        request: sae_20190506_models.DescribeJobHistoryRequest,
    ) -> sae_20190506_models.DescribeJobHistoryResponse:
        """
        @summary Query the information about jobs.
        
        @param request: DescribeJobHistoryRequest
        @return: DescribeJobHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_job_history_with_options_async(request, headers, runtime)

    def describe_job_status_with_options(
        self,
        request: sae_20190506_models.DescribeJobStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobStatusResponse:
        """
        @summary Queries the status of a job.
        
        @param request: DescribeJobStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobStatus',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJobStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_status_with_options_async(
        self,
        request: sae_20190506_models.DescribeJobStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobStatusResponse:
        """
        @summary Queries the status of a job.
        
        @param request: DescribeJobStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobStatus',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJobStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_status(
        self,
        request: sae_20190506_models.DescribeJobStatusRequest,
    ) -> sae_20190506_models.DescribeJobStatusResponse:
        """
        @summary Queries the status of a job.
        
        @param request: DescribeJobStatusRequest
        @return: DescribeJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_job_status_with_options(request, headers, runtime)

    async def describe_job_status_async(
        self,
        request: sae_20190506_models.DescribeJobStatusRequest,
    ) -> sae_20190506_models.DescribeJobStatusResponse:
        """
        @summary Queries the status of a job.
        
        @param request: DescribeJobStatusRequest
        @return: DescribeJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_job_status_with_options_async(request, headers, runtime)

    def describe_namespace_with_options(
        self,
        request: sae_20190506_models.DescribeNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceResponse:
        """
        @summary Queries the details of a namespace.
        
        @param request: DescribeNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_with_options_async(
        self,
        request: sae_20190506_models.DescribeNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceResponse:
        """
        @summary Queries the details of a namespace.
        
        @param request: DescribeNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace(
        self,
        request: sae_20190506_models.DescribeNamespaceRequest,
    ) -> sae_20190506_models.DescribeNamespaceResponse:
        """
        @summary Queries the details of a namespace.
        
        @param request: DescribeNamespaceRequest
        @return: DescribeNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespace_with_options(request, headers, runtime)

    async def describe_namespace_async(
        self,
        request: sae_20190506_models.DescribeNamespaceRequest,
    ) -> sae_20190506_models.DescribeNamespaceResponse:
        """
        @summary Queries the details of a namespace.
        
        @param request: DescribeNamespaceRequest
        @return: DescribeNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespace_with_options_async(request, headers, runtime)

    def describe_namespace_list_with_options(
        self,
        request: sae_20190506_models.DescribeNamespaceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceListResponse:
        """
        @summary Queries a list of namespaces.
        
        @param request: DescribeNamespaceListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespaceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contain_custom):
            query['ContainCustom'] = request.contain_custom
        if not UtilClient.is_unset(request.hybrid_cloud_exclude):
            query['HybridCloudExclude'] = request.hybrid_cloud_exclude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceList',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/describeNamespaceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_list_with_options_async(
        self,
        request: sae_20190506_models.DescribeNamespaceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceListResponse:
        """
        @summary Queries a list of namespaces.
        
        @param request: DescribeNamespaceListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespaceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contain_custom):
            query['ContainCustom'] = request.contain_custom
        if not UtilClient.is_unset(request.hybrid_cloud_exclude):
            query['HybridCloudExclude'] = request.hybrid_cloud_exclude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceList',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/describeNamespaceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace_list(
        self,
        request: sae_20190506_models.DescribeNamespaceListRequest,
    ) -> sae_20190506_models.DescribeNamespaceListResponse:
        """
        @summary Queries a list of namespaces.
        
        @param request: DescribeNamespaceListRequest
        @return: DescribeNamespaceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespace_list_with_options(request, headers, runtime)

    async def describe_namespace_list_async(
        self,
        request: sae_20190506_models.DescribeNamespaceListRequest,
    ) -> sae_20190506_models.DescribeNamespaceListResponse:
        """
        @summary Queries a list of namespaces.
        
        @param request: DescribeNamespaceListRequest
        @return: DescribeNamespaceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespace_list_with_options_async(request, headers, runtime)

    def describe_namespace_resources_with_options(
        self,
        request: sae_20190506_models.DescribeNamespaceResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceResourcesResponse:
        """
        @param request: DescribeNamespaceResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespaceResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/describeNamespaceResources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_resources_with_options_async(
        self,
        request: sae_20190506_models.DescribeNamespaceResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceResourcesResponse:
        """
        @param request: DescribeNamespaceResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespaceResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/describeNamespaceResources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace_resources(
        self,
        request: sae_20190506_models.DescribeNamespaceResourcesRequest,
    ) -> sae_20190506_models.DescribeNamespaceResourcesResponse:
        """
        @param request: DescribeNamespaceResourcesRequest
        @return: DescribeNamespaceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespace_resources_with_options(request, headers, runtime)

    async def describe_namespace_resources_async(
        self,
        request: sae_20190506_models.DescribeNamespaceResourcesRequest,
    ) -> sae_20190506_models.DescribeNamespaceResourcesResponse:
        """
        @param request: DescribeNamespaceResourcesRequest
        @return: DescribeNamespaceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespace_resources_with_options_async(request, headers, runtime)

    def describe_namespaces_with_options(
        self,
        request: sae_20190506_models.DescribeNamespacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespacesResponse:
        """
        @summary Queries a list of namespaces.
        
        @param request: DescribeNamespacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaces',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespaces_with_options_async(
        self,
        request: sae_20190506_models.DescribeNamespacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespacesResponse:
        """
        @summary Queries a list of namespaces.
        
        @param request: DescribeNamespacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaces',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespaces(
        self,
        request: sae_20190506_models.DescribeNamespacesRequest,
    ) -> sae_20190506_models.DescribeNamespacesResponse:
        """
        @summary Queries a list of namespaces.
        
        @param request: DescribeNamespacesRequest
        @return: DescribeNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespaces_with_options(request, headers, runtime)

    async def describe_namespaces_async(
        self,
        request: sae_20190506_models.DescribeNamespacesRequest,
    ) -> sae_20190506_models.DescribeNamespacesResponse:
        """
        @summary Queries a list of namespaces.
        
        @param request: DescribeNamespacesRequest
        @return: DescribeNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespaces_with_options_async(request, headers, runtime)

    def describe_pipeline_with_options(
        self,
        request: sae_20190506_models.DescribePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribePipelineResponse:
        """
        @summary View batch information
        
        @param request: DescribePipelineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePipelineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePipeline',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/DescribePipeline',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pipeline_with_options_async(
        self,
        request: sae_20190506_models.DescribePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribePipelineResponse:
        """
        @summary View batch information
        
        @param request: DescribePipelineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePipelineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePipeline',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/DescribePipeline',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pipeline(
        self,
        request: sae_20190506_models.DescribePipelineRequest,
    ) -> sae_20190506_models.DescribePipelineResponse:
        """
        @summary View batch information
        
        @param request: DescribePipelineRequest
        @return: DescribePipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pipeline_with_options(request, headers, runtime)

    async def describe_pipeline_async(
        self,
        request: sae_20190506_models.DescribePipelineRequest,
    ) -> sae_20190506_models.DescribePipelineResponse:
        """
        @summary View batch information
        
        @param request: DescribePipelineRequest
        @return: DescribePipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_pipeline_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/regionConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/regionConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> sae_20190506_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> sae_20190506_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def describe_secret_with_options(
        self,
        request: sae_20190506_models.DescribeSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeSecretResponse:
        """
        @summary Queries the details of a Secret.
        
        @param request: DescribeSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_secret_with_options_async(
        self,
        request: sae_20190506_models.DescribeSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeSecretResponse:
        """
        @summary Queries the details of a Secret.
        
        @param request: DescribeSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_secret(
        self,
        request: sae_20190506_models.DescribeSecretRequest,
    ) -> sae_20190506_models.DescribeSecretResponse:
        """
        @summary Queries the details of a Secret.
        
        @param request: DescribeSecretRequest
        @return: DescribeSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_secret_with_options(request, headers, runtime)

    async def describe_secret_async(
        self,
        request: sae_20190506_models.DescribeSecretRequest,
    ) -> sae_20190506_models.DescribeSecretResponse:
        """
        @summary Queries the details of a Secret.
        
        @param request: DescribeSecretRequest
        @return: DescribeSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_secret_with_options_async(request, headers, runtime)

    def describe_web_application_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebApplicationResponse:
        """
        @summary Query web applications.
        
        @description Call the DescribeWebApplication operation to query web applications.
        
        @param request: DescribeWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_application_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebApplicationResponse:
        """
        @summary Query web applications.
        
        @description Call the DescribeWebApplication operation to query web applications.
        
        @param request: DescribeWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_application(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationRequest,
    ) -> sae_20190506_models.DescribeWebApplicationResponse:
        """
        @summary Query web applications.
        
        @description Call the DescribeWebApplication operation to query web applications.
        
        @param request: DescribeWebApplicationRequest
        @return: DescribeWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_web_application_with_options(application_id, request, headers, runtime)

    async def describe_web_application_async(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationRequest,
    ) -> sae_20190506_models.DescribeWebApplicationResponse:
        """
        @summary Query web applications.
        
        @description Call the DescribeWebApplication operation to query web applications.
        
        @param request: DescribeWebApplicationRequest
        @return: DescribeWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_web_application_with_options_async(application_id, request, headers, runtime)

    def describe_web_application_resource_statics_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationResourceStaticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebApplicationResourceStaticsResponse:
        """
        @summary Query the resource usage of a web application.
        
        @description Query the resource usage of a web application.
        
        @param request: DescribeWebApplicationResourceStaticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebApplicationResourceStaticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebApplicationResourceStatics',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications-observability/{OpenApiUtilClient.get_encode_param(application_id)}/resource',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebApplicationResourceStaticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_application_resource_statics_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationResourceStaticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebApplicationResourceStaticsResponse:
        """
        @summary Query the resource usage of a web application.
        
        @description Query the resource usage of a web application.
        
        @param request: DescribeWebApplicationResourceStaticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebApplicationResourceStaticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebApplicationResourceStatics',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications-observability/{OpenApiUtilClient.get_encode_param(application_id)}/resource',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebApplicationResourceStaticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_application_resource_statics(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationResourceStaticsRequest,
    ) -> sae_20190506_models.DescribeWebApplicationResourceStaticsResponse:
        """
        @summary Query the resource usage of a web application.
        
        @description Query the resource usage of a web application.
        
        @param request: DescribeWebApplicationResourceStaticsRequest
        @return: DescribeWebApplicationResourceStaticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_web_application_resource_statics_with_options(application_id, request, headers, runtime)

    async def describe_web_application_resource_statics_async(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationResourceStaticsRequest,
    ) -> sae_20190506_models.DescribeWebApplicationResourceStaticsResponse:
        """
        @summary Query the resource usage of a web application.
        
        @description Query the resource usage of a web application.
        
        @param request: DescribeWebApplicationResourceStaticsRequest
        @return: DescribeWebApplicationResourceStaticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_web_application_resource_statics_with_options_async(application_id, request, headers, runtime)

    def describe_web_application_revision_with_options(
        self,
        application_id: str,
        revision_id: str,
        request: sae_20190506_models.DescribeWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebApplicationRevisionResponse:
        """
        @summary Describe a web application version.
        
        @description Describe a web application version.
        
        @param request: DescribeWebApplicationRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebApplicationRevisionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebApplicationRevision',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-revisions/{OpenApiUtilClient.get_encode_param(application_id)}/revisions/{OpenApiUtilClient.get_encode_param(revision_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebApplicationRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_application_revision_with_options_async(
        self,
        application_id: str,
        revision_id: str,
        request: sae_20190506_models.DescribeWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebApplicationRevisionResponse:
        """
        @summary Describe a web application version.
        
        @description Describe a web application version.
        
        @param request: DescribeWebApplicationRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebApplicationRevisionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebApplicationRevision',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-revisions/{OpenApiUtilClient.get_encode_param(application_id)}/revisions/{OpenApiUtilClient.get_encode_param(revision_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebApplicationRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_application_revision(
        self,
        application_id: str,
        revision_id: str,
        request: sae_20190506_models.DescribeWebApplicationRevisionRequest,
    ) -> sae_20190506_models.DescribeWebApplicationRevisionResponse:
        """
        @summary Describe a web application version.
        
        @description Describe a web application version.
        
        @param request: DescribeWebApplicationRevisionRequest
        @return: DescribeWebApplicationRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_web_application_revision_with_options(application_id, revision_id, request, headers, runtime)

    async def describe_web_application_revision_async(
        self,
        application_id: str,
        revision_id: str,
        request: sae_20190506_models.DescribeWebApplicationRevisionRequest,
    ) -> sae_20190506_models.DescribeWebApplicationRevisionResponse:
        """
        @summary Describe a web application version.
        
        @description Describe a web application version.
        
        @param request: DescribeWebApplicationRevisionRequest
        @return: DescribeWebApplicationRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_web_application_revision_with_options_async(application_id, revision_id, request, headers, runtime)

    def describe_web_application_scaling_config_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationScalingConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebApplicationScalingConfigResponse:
        """
        @summary Describe the scaling configuration of a web application.
        
        @description Call the DescribeWebApplicationScalingConfig operation to obtain the scaling configuration of a web application.
        
        @param request: DescribeWebApplicationScalingConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebApplicationScalingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebApplicationScalingConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-scaling/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebApplicationScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_application_scaling_config_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationScalingConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebApplicationScalingConfigResponse:
        """
        @summary Describe the scaling configuration of a web application.
        
        @description Call the DescribeWebApplicationScalingConfig operation to obtain the scaling configuration of a web application.
        
        @param request: DescribeWebApplicationScalingConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebApplicationScalingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebApplicationScalingConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-scaling/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebApplicationScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_application_scaling_config(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationScalingConfigRequest,
    ) -> sae_20190506_models.DescribeWebApplicationScalingConfigResponse:
        """
        @summary Describe the scaling configuration of a web application.
        
        @description Call the DescribeWebApplicationScalingConfig operation to obtain the scaling configuration of a web application.
        
        @param request: DescribeWebApplicationScalingConfigRequest
        @return: DescribeWebApplicationScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_web_application_scaling_config_with_options(application_id, request, headers, runtime)

    async def describe_web_application_scaling_config_async(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationScalingConfigRequest,
    ) -> sae_20190506_models.DescribeWebApplicationScalingConfigResponse:
        """
        @summary Describe the scaling configuration of a web application.
        
        @description Call the DescribeWebApplicationScalingConfig operation to obtain the scaling configuration of a web application.
        
        @param request: DescribeWebApplicationScalingConfigRequest
        @return: DescribeWebApplicationScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_web_application_scaling_config_with_options_async(application_id, request, headers, runtime)

    def describe_web_application_traffic_config_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationTrafficConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebApplicationTrafficConfigResponse:
        """
        @summary Query the traffic configurations of a web application.
        
        @description Call the DescribeWebApplicationTrafficConfig operation to query the traffic configurations of a web application.
        
        @param request: DescribeWebApplicationTrafficConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebApplicationTrafficConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebApplicationTrafficConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-traffic/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebApplicationTrafficConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_application_traffic_config_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationTrafficConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebApplicationTrafficConfigResponse:
        """
        @summary Query the traffic configurations of a web application.
        
        @description Call the DescribeWebApplicationTrafficConfig operation to query the traffic configurations of a web application.
        
        @param request: DescribeWebApplicationTrafficConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebApplicationTrafficConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebApplicationTrafficConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-traffic/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebApplicationTrafficConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_application_traffic_config(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationTrafficConfigRequest,
    ) -> sae_20190506_models.DescribeWebApplicationTrafficConfigResponse:
        """
        @summary Query the traffic configurations of a web application.
        
        @description Call the DescribeWebApplicationTrafficConfig operation to query the traffic configurations of a web application.
        
        @param request: DescribeWebApplicationTrafficConfigRequest
        @return: DescribeWebApplicationTrafficConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_web_application_traffic_config_with_options(application_id, request, headers, runtime)

    async def describe_web_application_traffic_config_async(
        self,
        application_id: str,
        request: sae_20190506_models.DescribeWebApplicationTrafficConfigRequest,
    ) -> sae_20190506_models.DescribeWebApplicationTrafficConfigResponse:
        """
        @summary Query the traffic configurations of a web application.
        
        @description Call the DescribeWebApplicationTrafficConfig operation to query the traffic configurations of a web application.
        
        @param request: DescribeWebApplicationTrafficConfigRequest
        @return: DescribeWebApplicationTrafficConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_web_application_traffic_config_with_options_async(application_id, request, headers, runtime)

    def describe_web_custom_domain_with_options(
        self,
        domain_name: str,
        request: sae_20190506_models.DescribeWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebCustomDomainResponse:
        """
        @summary Query the details of a custom domain name for a web application.
        
        @description Query the details of a custom domain name for a web application.
        
        @param request: DescribeWebCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCustomDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCustomDomain',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_custom_domain_with_options_async(
        self,
        domain_name: str,
        request: sae_20190506_models.DescribeWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebCustomDomainResponse:
        """
        @summary Query the details of a custom domain name for a web application.
        
        @description Query the details of a custom domain name for a web application.
        
        @param request: DescribeWebCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebCustomDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCustomDomain',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_custom_domain(
        self,
        domain_name: str,
        request: sae_20190506_models.DescribeWebCustomDomainRequest,
    ) -> sae_20190506_models.DescribeWebCustomDomainResponse:
        """
        @summary Query the details of a custom domain name for a web application.
        
        @description Query the details of a custom domain name for a web application.
        
        @param request: DescribeWebCustomDomainRequest
        @return: DescribeWebCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_web_custom_domain_with_options(domain_name, request, headers, runtime)

    async def describe_web_custom_domain_async(
        self,
        domain_name: str,
        request: sae_20190506_models.DescribeWebCustomDomainRequest,
    ) -> sae_20190506_models.DescribeWebCustomDomainResponse:
        """
        @summary Query the details of a custom domain name for a web application.
        
        @description Query the details of a custom domain name for a web application.
        
        @param request: DescribeWebCustomDomainRequest
        @return: DescribeWebCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_web_custom_domain_with_options_async(domain_name, request, headers, runtime)

    def describe_web_instance_logs_with_options(
        self,
        application_id: str,
        instance_id: str,
        request: sae_20190506_models.DescribeWebInstanceLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebInstanceLogsResponse:
        """
        @summary Obtain the logs of web application instances.
        
        @description Obtain the logs of web application instances.
        
        @param request: DescribeWebInstanceLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebInstanceLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebInstanceLogs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications-observability/{OpenApiUtilClient.get_encode_param(application_id)}/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebInstanceLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_instance_logs_with_options_async(
        self,
        application_id: str,
        instance_id: str,
        request: sae_20190506_models.DescribeWebInstanceLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeWebInstanceLogsResponse:
        """
        @summary Obtain the logs of web application instances.
        
        @description Obtain the logs of web application instances.
        
        @param request: DescribeWebInstanceLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWebInstanceLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebInstanceLogs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications-observability/{OpenApiUtilClient.get_encode_param(application_id)}/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeWebInstanceLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_instance_logs(
        self,
        application_id: str,
        instance_id: str,
        request: sae_20190506_models.DescribeWebInstanceLogsRequest,
    ) -> sae_20190506_models.DescribeWebInstanceLogsResponse:
        """
        @summary Obtain the logs of web application instances.
        
        @description Obtain the logs of web application instances.
        
        @param request: DescribeWebInstanceLogsRequest
        @return: DescribeWebInstanceLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_web_instance_logs_with_options(application_id, instance_id, request, headers, runtime)

    async def describe_web_instance_logs_async(
        self,
        application_id: str,
        instance_id: str,
        request: sae_20190506_models.DescribeWebInstanceLogsRequest,
    ) -> sae_20190506_models.DescribeWebInstanceLogsResponse:
        """
        @summary Obtain the logs of web application instances.
        
        @description Obtain the logs of web application instances.
        
        @param request: DescribeWebInstanceLogsRequest
        @return: DescribeWebInstanceLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_web_instance_logs_with_options_async(application_id, instance_id, request, headers, runtime)

    def disable_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.DisableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DisableApplicationScalingRuleResponse:
        """
        @param request: DisableApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/disableApplicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DisableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.DisableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DisableApplicationScalingRuleResponse:
        """
        @param request: DisableApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/disableApplicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DisableApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_scaling_rule(
        self,
        request: sae_20190506_models.DisableApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DisableApplicationScalingRuleResponse:
        """
        @param request: DisableApplicationScalingRuleRequest
        @return: DisableApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_application_scaling_rule_with_options(request, headers, runtime)

    async def disable_application_scaling_rule_async(
        self,
        request: sae_20190506_models.DisableApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DisableApplicationScalingRuleResponse:
        """
        @param request: DisableApplicationScalingRuleRequest
        @return: DisableApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_application_scaling_rule_with_options_async(request, headers, runtime)

    def downgrade_application_apm_service_with_options(
        self,
        request: sae_20190506_models.DowngradeApplicationApmServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DowngradeApplicationApmServiceResponse:
        """
        @summary Disables the advanced monitoring feature of Application Real-Time Monitoring Service (ARMS).
        
        @param request: DowngradeApplicationApmServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DowngradeApplicationApmServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DowngradeApplicationApmService',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/applicationApmService',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DowngradeApplicationApmServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_application_apm_service_with_options_async(
        self,
        request: sae_20190506_models.DowngradeApplicationApmServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DowngradeApplicationApmServiceResponse:
        """
        @summary Disables the advanced monitoring feature of Application Real-Time Monitoring Service (ARMS).
        
        @param request: DowngradeApplicationApmServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DowngradeApplicationApmServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DowngradeApplicationApmService',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/applicationApmService',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DowngradeApplicationApmServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def downgrade_application_apm_service(
        self,
        request: sae_20190506_models.DowngradeApplicationApmServiceRequest,
    ) -> sae_20190506_models.DowngradeApplicationApmServiceResponse:
        """
        @summary Disables the advanced monitoring feature of Application Real-Time Monitoring Service (ARMS).
        
        @param request: DowngradeApplicationApmServiceRequest
        @return: DowngradeApplicationApmServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.downgrade_application_apm_service_with_options(request, headers, runtime)

    async def downgrade_application_apm_service_async(
        self,
        request: sae_20190506_models.DowngradeApplicationApmServiceRequest,
    ) -> sae_20190506_models.DowngradeApplicationApmServiceResponse:
        """
        @summary Disables the advanced monitoring feature of Application Real-Time Monitoring Service (ARMS).
        
        @param request: DowngradeApplicationApmServiceRequest
        @return: DowngradeApplicationApmServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.downgrade_application_apm_service_with_options_async(request, headers, runtime)

    def enable_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.EnableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.EnableApplicationScalingRuleResponse:
        """
        @summary Enables an auto scaling policy for an application.
        
        @param request: EnableApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/enableApplicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.EnableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.EnableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.EnableApplicationScalingRuleResponse:
        """
        @summary Enables an auto scaling policy for an application.
        
        @param request: EnableApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/enableApplicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.EnableApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_scaling_rule(
        self,
        request: sae_20190506_models.EnableApplicationScalingRuleRequest,
    ) -> sae_20190506_models.EnableApplicationScalingRuleResponse:
        """
        @summary Enables an auto scaling policy for an application.
        
        @param request: EnableApplicationScalingRuleRequest
        @return: EnableApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_application_scaling_rule_with_options(request, headers, runtime)

    async def enable_application_scaling_rule_async(
        self,
        request: sae_20190506_models.EnableApplicationScalingRuleRequest,
    ) -> sae_20190506_models.EnableApplicationScalingRuleResponse:
        """
        @summary Enables an auto scaling policy for an application.
        
        @param request: EnableApplicationScalingRuleRequest
        @return: EnableApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_application_scaling_rule_with_options_async(request, headers, runtime)

    def exec_job_with_options(
        self,
        request: sae_20190506_models.ExecJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ExecJobResponse:
        """
        @param request: ExecJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/execJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ExecJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_job_with_options_async(
        self,
        request: sae_20190506_models.ExecJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ExecJobResponse:
        """
        @param request: ExecJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/execJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ExecJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_job(
        self,
        request: sae_20190506_models.ExecJobRequest,
    ) -> sae_20190506_models.ExecJobResponse:
        """
        @param request: ExecJobRequest
        @return: ExecJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.exec_job_with_options(request, headers, runtime)

    async def exec_job_async(
        self,
        request: sae_20190506_models.ExecJobRequest,
    ) -> sae_20190506_models.ExecJobResponse:
        """
        @param request: ExecJobRequest
        @return: ExecJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.exec_job_with_options_async(request, headers, runtime)

    def get_application_with_options(
        self,
        request: sae_20190506_models.GetApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetApplicationResponse:
        """
        @summary Queries the basic information of an application.
        
        @param request: GetApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/getApplication',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: sae_20190506_models.GetApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetApplicationResponse:
        """
        @summary Queries the basic information of an application.
        
        @param request: GetApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/getApplication',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: sae_20190506_models.GetApplicationRequest,
    ) -> sae_20190506_models.GetApplicationResponse:
        """
        @summary Queries the basic information of an application.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_application_with_options(request, headers, runtime)

    async def get_application_async(
        self,
        request: sae_20190506_models.GetApplicationRequest,
    ) -> sae_20190506_models.GetApplicationResponse:
        """
        @summary Queries the basic information of an application.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_application_with_options_async(request, headers, runtime)

    def get_arms_top_nmetric_with_options(
        self,
        request: sae_20190506_models.GetArmsTopNMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetArmsTopNMetricResponse:
        """
        @summary The application name.
        
        @param request: GetArmsTopNMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetArmsTopNMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArmsTopNMetric',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/getArmsTopNMetric',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetArmsTopNMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_arms_top_nmetric_with_options_async(
        self,
        request: sae_20190506_models.GetArmsTopNMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetArmsTopNMetricResponse:
        """
        @summary The application name.
        
        @param request: GetArmsTopNMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetArmsTopNMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArmsTopNMetric',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/getArmsTopNMetric',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetArmsTopNMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_arms_top_nmetric(
        self,
        request: sae_20190506_models.GetArmsTopNMetricRequest,
    ) -> sae_20190506_models.GetArmsTopNMetricResponse:
        """
        @summary The application name.
        
        @param request: GetArmsTopNMetricRequest
        @return: GetArmsTopNMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_arms_top_nmetric_with_options(request, headers, runtime)

    async def get_arms_top_nmetric_async(
        self,
        request: sae_20190506_models.GetArmsTopNMetricRequest,
    ) -> sae_20190506_models.GetArmsTopNMetricResponse:
        """
        @summary The application name.
        
        @param request: GetArmsTopNMetricRequest
        @return: GetArmsTopNMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_arms_top_nmetric_with_options_async(request, headers, runtime)

    def get_availability_metric_with_options(
        self,
        request: sae_20190506_models.GetAvailabilityMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetAvailabilityMetricResponse:
        """
        @summary Queries the top N applications in which abnormal instances exist. The applications are sorted by the total number of abnormal instances.
        
        @param request: GetAvailabilityMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAvailabilityMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAvailabilityMetric',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/getAvailabilityMetric',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetAvailabilityMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_availability_metric_with_options_async(
        self,
        request: sae_20190506_models.GetAvailabilityMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetAvailabilityMetricResponse:
        """
        @summary Queries the top N applications in which abnormal instances exist. The applications are sorted by the total number of abnormal instances.
        
        @param request: GetAvailabilityMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAvailabilityMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAvailabilityMetric',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/getAvailabilityMetric',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetAvailabilityMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_availability_metric(
        self,
        request: sae_20190506_models.GetAvailabilityMetricRequest,
    ) -> sae_20190506_models.GetAvailabilityMetricResponse:
        """
        @summary Queries the top N applications in which abnormal instances exist. The applications are sorted by the total number of abnormal instances.
        
        @param request: GetAvailabilityMetricRequest
        @return: GetAvailabilityMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_availability_metric_with_options(request, headers, runtime)

    async def get_availability_metric_async(
        self,
        request: sae_20190506_models.GetAvailabilityMetricRequest,
    ) -> sae_20190506_models.GetAvailabilityMetricResponse:
        """
        @summary Queries the top N applications in which abnormal instances exist. The applications are sorted by the total number of abnormal instances.
        
        @param request: GetAvailabilityMetricRequest
        @return: GetAvailabilityMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_availability_metric_with_options_async(request, headers, runtime)

    def get_change_order_metric_with_options(
        self,
        request: sae_20190506_models.GetChangeOrderMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetChangeOrderMetricResponse:
        """
        @summary Queries top N applications in abnormal change orders.
        
        @param request: GetChangeOrderMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChangeOrderMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChangeOrderMetric',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/getChangeOrderMetric',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetChangeOrderMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_change_order_metric_with_options_async(
        self,
        request: sae_20190506_models.GetChangeOrderMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetChangeOrderMetricResponse:
        """
        @summary Queries top N applications in abnormal change orders.
        
        @param request: GetChangeOrderMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChangeOrderMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChangeOrderMetric',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/getChangeOrderMetric',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetChangeOrderMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_change_order_metric(
        self,
        request: sae_20190506_models.GetChangeOrderMetricRequest,
    ) -> sae_20190506_models.GetChangeOrderMetricResponse:
        """
        @summary Queries top N applications in abnormal change orders.
        
        @param request: GetChangeOrderMetricRequest
        @return: GetChangeOrderMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_change_order_metric_with_options(request, headers, runtime)

    async def get_change_order_metric_async(
        self,
        request: sae_20190506_models.GetChangeOrderMetricRequest,
    ) -> sae_20190506_models.GetChangeOrderMetricResponse:
        """
        @summary Queries top N applications in abnormal change orders.
        
        @param request: GetChangeOrderMetricRequest
        @return: GetChangeOrderMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_change_order_metric_with_options_async(request, headers, runtime)

    def get_scale_app_metric_with_options(
        self,
        request: sae_20190506_models.GetScaleAppMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetScaleAppMetricResponse:
        """
        @summary Queries the top N applications in which auto scaling takes effect.
        
        @param request: GetScaleAppMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScaleAppMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScaleAppMetric',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/getScaleAppMetric',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetScaleAppMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scale_app_metric_with_options_async(
        self,
        request: sae_20190506_models.GetScaleAppMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetScaleAppMetricResponse:
        """
        @summary Queries the top N applications in which auto scaling takes effect.
        
        @param request: GetScaleAppMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScaleAppMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScaleAppMetric',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/getScaleAppMetric',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetScaleAppMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scale_app_metric(
        self,
        request: sae_20190506_models.GetScaleAppMetricRequest,
    ) -> sae_20190506_models.GetScaleAppMetricResponse:
        """
        @summary Queries the top N applications in which auto scaling takes effect.
        
        @param request: GetScaleAppMetricRequest
        @return: GetScaleAppMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_scale_app_metric_with_options(request, headers, runtime)

    async def get_scale_app_metric_async(
        self,
        request: sae_20190506_models.GetScaleAppMetricRequest,
    ) -> sae_20190506_models.GetScaleAppMetricResponse:
        """
        @summary Queries the top N applications in which auto scaling takes effect.
        
        @param request: GetScaleAppMetricRequest
        @return: GetScaleAppMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_scale_app_metric_with_options_async(request, headers, runtime)

    def get_warning_event_metric_with_options(
        self,
        request: sae_20190506_models.GetWarningEventMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetWarningEventMetricResponse:
        """
        @summary The number of Warning events.
        
        @param request: GetWarningEventMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWarningEventMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWarningEventMetric',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/getWarningEventMetric',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetWarningEventMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_warning_event_metric_with_options_async(
        self,
        request: sae_20190506_models.GetWarningEventMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetWarningEventMetricResponse:
        """
        @summary The number of Warning events.
        
        @param request: GetWarningEventMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWarningEventMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWarningEventMetric',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/getWarningEventMetric',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetWarningEventMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_warning_event_metric(
        self,
        request: sae_20190506_models.GetWarningEventMetricRequest,
    ) -> sae_20190506_models.GetWarningEventMetricResponse:
        """
        @summary The number of Warning events.
        
        @param request: GetWarningEventMetricRequest
        @return: GetWarningEventMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_warning_event_metric_with_options(request, headers, runtime)

    async def get_warning_event_metric_async(
        self,
        request: sae_20190506_models.GetWarningEventMetricRequest,
    ) -> sae_20190506_models.GetWarningEventMetricResponse:
        """
        @summary The number of Warning events.
        
        @param request: GetWarningEventMetricRequest
        @return: GetWarningEventMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_warning_event_metric_with_options_async(request, headers, runtime)

    def get_webshell_token_with_options(
        self,
        request: sae_20190506_models.GetWebshellTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetWebshellTokenResponse:
        """
        @summary Obtains the token used to remotely log on to the Webshell of an instance.
        
        @param request: GetWebshellTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWebshellTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.container_name):
            query['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.pod_name):
            query['PodName'] = request.pod_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWebshellToken',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/instance/webshellToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetWebshellTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_webshell_token_with_options_async(
        self,
        request: sae_20190506_models.GetWebshellTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.GetWebshellTokenResponse:
        """
        @summary Obtains the token used to remotely log on to the Webshell of an instance.
        
        @param request: GetWebshellTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWebshellTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.container_name):
            query['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.pod_name):
            query['PodName'] = request.pod_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWebshellToken',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/instance/webshellToken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.GetWebshellTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_webshell_token(
        self,
        request: sae_20190506_models.GetWebshellTokenRequest,
    ) -> sae_20190506_models.GetWebshellTokenResponse:
        """
        @summary Obtains the token used to remotely log on to the Webshell of an instance.
        
        @param request: GetWebshellTokenRequest
        @return: GetWebshellTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_webshell_token_with_options(request, headers, runtime)

    async def get_webshell_token_async(
        self,
        request: sae_20190506_models.GetWebshellTokenRequest,
    ) -> sae_20190506_models.GetWebshellTokenResponse:
        """
        @summary Obtains the token used to remotely log on to the Webshell of an instance.
        
        @param request: GetWebshellTokenRequest
        @return: GetWebshellTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_webshell_token_with_options_async(request, headers, runtime)

    def list_app_events_with_options(
        self,
        request: sae_20190506_models.ListAppEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppEventsResponse:
        """
        @summary Queries the events that occurred in an application.
        
        @param request: ListAppEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.object_kind):
            query['ObjectKind'] = request.object_kind
        if not UtilClient.is_unset(request.object_name):
            query['ObjectName'] = request.object_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppEvents',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listAppEvents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_events_with_options_async(
        self,
        request: sae_20190506_models.ListAppEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppEventsResponse:
        """
        @summary Queries the events that occurred in an application.
        
        @param request: ListAppEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.object_kind):
            query['ObjectKind'] = request.object_kind
        if not UtilClient.is_unset(request.object_name):
            query['ObjectName'] = request.object_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppEvents',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listAppEvents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_events(
        self,
        request: sae_20190506_models.ListAppEventsRequest,
    ) -> sae_20190506_models.ListAppEventsResponse:
        """
        @summary Queries the events that occurred in an application.
        
        @param request: ListAppEventsRequest
        @return: ListAppEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_events_with_options(request, headers, runtime)

    async def list_app_events_async(
        self,
        request: sae_20190506_models.ListAppEventsRequest,
    ) -> sae_20190506_models.ListAppEventsResponse:
        """
        @summary Queries the events that occurred in an application.
        
        @param request: ListAppEventsRequest
        @return: ListAppEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_app_events_with_options_async(request, headers, runtime)

    def list_app_services_with_options(
        self,
        request: sae_20190506_models.ListAppServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppServicesResponse:
        """
        @summary Queries the list of microservices
        
        @param request: ListAppServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.nacos_instance_id):
            query['NacosInstanceId'] = request.nacos_instance_id
        if not UtilClient.is_unset(request.nacos_namespace_id):
            query['NacosNamespaceId'] = request.nacos_namespace_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.registry_type):
            query['RegistryType'] = request.registry_type
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listAppServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_services_with_options_async(
        self,
        request: sae_20190506_models.ListAppServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppServicesResponse:
        """
        @summary Queries the list of microservices
        
        @param request: ListAppServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.nacos_instance_id):
            query['NacosInstanceId'] = request.nacos_instance_id
        if not UtilClient.is_unset(request.nacos_namespace_id):
            query['NacosNamespaceId'] = request.nacos_namespace_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.registry_type):
            query['RegistryType'] = request.registry_type
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listAppServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_services(
        self,
        request: sae_20190506_models.ListAppServicesRequest,
    ) -> sae_20190506_models.ListAppServicesResponse:
        """
        @summary Queries the list of microservices
        
        @param request: ListAppServicesRequest
        @return: ListAppServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_services_with_options(request, headers, runtime)

    async def list_app_services_async(
        self,
        request: sae_20190506_models.ListAppServicesRequest,
    ) -> sae_20190506_models.ListAppServicesResponse:
        """
        @summary Queries the list of microservices
        
        @param request: ListAppServicesRequest
        @return: ListAppServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_app_services_with_options_async(request, headers, runtime)

    def list_app_services_page_with_options(
        self,
        request: sae_20190506_models.ListAppServicesPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppServicesPageResponse:
        """
        @summary Queries the services of an application.
        
        @param request: ListAppServicesPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppServicesPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppServicesPage',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listAppServicesPage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppServicesPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_services_page_with_options_async(
        self,
        request: sae_20190506_models.ListAppServicesPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppServicesPageResponse:
        """
        @summary Queries the services of an application.
        
        @param request: ListAppServicesPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppServicesPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppServicesPage',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listAppServicesPage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppServicesPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_services_page(
        self,
        request: sae_20190506_models.ListAppServicesPageRequest,
    ) -> sae_20190506_models.ListAppServicesPageResponse:
        """
        @summary Queries the services of an application.
        
        @param request: ListAppServicesPageRequest
        @return: ListAppServicesPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_services_page_with_options(request, headers, runtime)

    async def list_app_services_page_async(
        self,
        request: sae_20190506_models.ListAppServicesPageRequest,
    ) -> sae_20190506_models.ListAppServicesPageResponse:
        """
        @summary Queries the services of an application.
        
        @param request: ListAppServicesPageRequest
        @return: ListAppServicesPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_app_services_page_with_options_async(request, headers, runtime)

    def list_app_versions_with_options(
        self,
        request: sae_20190506_models.ListAppVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppVersionsResponse:
        """
        @summary Queries the deployment versions of an application.
        
        @param request: ListAppVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppVersions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listAppVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_versions_with_options_async(
        self,
        request: sae_20190506_models.ListAppVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppVersionsResponse:
        """
        @summary Queries the deployment versions of an application.
        
        @param request: ListAppVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppVersions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listAppVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_versions(
        self,
        request: sae_20190506_models.ListAppVersionsRequest,
    ) -> sae_20190506_models.ListAppVersionsResponse:
        """
        @summary Queries the deployment versions of an application.
        
        @param request: ListAppVersionsRequest
        @return: ListAppVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_versions_with_options(request, headers, runtime)

    async def list_app_versions_async(
        self,
        request: sae_20190506_models.ListAppVersionsRequest,
    ) -> sae_20190506_models.ListAppVersionsResponse:
        """
        @summary Queries the deployment versions of an application.
        
        @param request: ListAppVersionsRequest
        @return: ListAppVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_app_versions_with_options_async(request, headers, runtime)

    def list_applications_with_options(
        self,
        request: sae_20190506_models.ListApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListApplicationsResponse:
        """
        @summary Queries a list of applications.
        
        @param request: ListApplicationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_type):
            query['FieldType'] = request.field_type
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listApplications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        request: sae_20190506_models.ListApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListApplicationsResponse:
        """
        @summary Queries a list of applications.
        
        @param request: ListApplicationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_source):
            query['AppSource'] = request.app_source
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_type):
            query['FieldType'] = request.field_type
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listApplications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: sae_20190506_models.ListApplicationsRequest,
    ) -> sae_20190506_models.ListApplicationsResponse:
        """
        @summary Queries a list of applications.
        
        @param request: ListApplicationsRequest
        @return: ListApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_applications_with_options(request, headers, runtime)

    async def list_applications_async(
        self,
        request: sae_20190506_models.ListApplicationsRequest,
    ) -> sae_20190506_models.ListApplicationsResponse:
        """
        @summary Queries a list of applications.
        
        @param request: ListApplicationsRequest
        @return: ListApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_applications_with_options_async(request, headers, runtime)

    def list_change_orders_with_options(
        self,
        request: sae_20190506_models.ListChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListChangeOrdersResponse:
        """
        @summary Query a list of change orders.
        
        @param request: ListChangeOrdersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChangeOrdersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.co_status):
            query['CoStatus'] = request.co_status
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChangeOrders',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/ListChangeOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListChangeOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_change_orders_with_options_async(
        self,
        request: sae_20190506_models.ListChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListChangeOrdersResponse:
        """
        @summary Query a list of change orders.
        
        @param request: ListChangeOrdersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChangeOrdersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.co_status):
            query['CoStatus'] = request.co_status
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChangeOrders',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/ListChangeOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListChangeOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_change_orders(
        self,
        request: sae_20190506_models.ListChangeOrdersRequest,
    ) -> sae_20190506_models.ListChangeOrdersResponse:
        """
        @summary Query a list of change orders.
        
        @param request: ListChangeOrdersRequest
        @return: ListChangeOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_change_orders_with_options(request, headers, runtime)

    async def list_change_orders_async(
        self,
        request: sae_20190506_models.ListChangeOrdersRequest,
    ) -> sae_20190506_models.ListChangeOrdersResponse:
        """
        @summary Query a list of change orders.
        
        @param request: ListChangeOrdersRequest
        @return: ListChangeOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_change_orders_with_options_async(request, headers, runtime)

    def list_consumed_services_with_options(
        self,
        request: sae_20190506_models.ListConsumedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListConsumedServicesResponse:
        """
        @summary Queries a list of microservices that are subscribed.
        
        @param request: ListConsumedServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumedServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumedServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listConsumedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListConsumedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumed_services_with_options_async(
        self,
        request: sae_20190506_models.ListConsumedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListConsumedServicesResponse:
        """
        @summary Queries a list of microservices that are subscribed.
        
        @param request: ListConsumedServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumedServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumedServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listConsumedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListConsumedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumed_services(
        self,
        request: sae_20190506_models.ListConsumedServicesRequest,
    ) -> sae_20190506_models.ListConsumedServicesResponse:
        """
        @summary Queries a list of microservices that are subscribed.
        
        @param request: ListConsumedServicesRequest
        @return: ListConsumedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumed_services_with_options(request, headers, runtime)

    async def list_consumed_services_async(
        self,
        request: sae_20190506_models.ListConsumedServicesRequest,
    ) -> sae_20190506_models.ListConsumedServicesResponse:
        """
        @summary Queries a list of microservices that are subscribed.
        
        @param request: ListConsumedServicesRequest
        @return: ListConsumedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_consumed_services_with_options_async(request, headers, runtime)

    def list_grey_tag_route_with_options(
        self,
        request: sae_20190506_models.ListGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListGreyTagRouteResponse:
        """
        @summary Queries the details of a canary release rule based on an application ID.
        
        @description >  You can configure only one canary release rule for each application.
        
        @param request: ListGreyTagRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGreyTagRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRouteList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_grey_tag_route_with_options_async(
        self,
        request: sae_20190506_models.ListGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListGreyTagRouteResponse:
        """
        @summary Queries the details of a canary release rule based on an application ID.
        
        @description >  You can configure only one canary release rule for each application.
        
        @param request: ListGreyTagRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGreyTagRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRouteList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_grey_tag_route(
        self,
        request: sae_20190506_models.ListGreyTagRouteRequest,
    ) -> sae_20190506_models.ListGreyTagRouteResponse:
        """
        @summary Queries the details of a canary release rule based on an application ID.
        
        @description >  You can configure only one canary release rule for each application.
        
        @param request: ListGreyTagRouteRequest
        @return: ListGreyTagRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_grey_tag_route_with_options(request, headers, runtime)

    async def list_grey_tag_route_async(
        self,
        request: sae_20190506_models.ListGreyTagRouteRequest,
    ) -> sae_20190506_models.ListGreyTagRouteResponse:
        """
        @summary Queries the details of a canary release rule based on an application ID.
        
        @description >  You can configure only one canary release rule for each application.
        
        @param request: ListGreyTagRouteRequest
        @return: ListGreyTagRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_grey_tag_route_with_options_async(request, headers, runtime)

    def list_ingresses_with_options(
        self,
        request: sae_20190506_models.ListIngressesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListIngressesResponse:
        """
        @summary Use ListIngress API call to query Ingress list
        
        @param request: ListIngressesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIngressesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIngresses',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/IngressList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListIngressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ingresses_with_options_async(
        self,
        request: sae_20190506_models.ListIngressesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListIngressesResponse:
        """
        @summary Use ListIngress API call to query Ingress list
        
        @param request: ListIngressesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIngressesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIngresses',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/IngressList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListIngressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ingresses(
        self,
        request: sae_20190506_models.ListIngressesRequest,
    ) -> sae_20190506_models.ListIngressesResponse:
        """
        @summary Use ListIngress API call to query Ingress list
        
        @param request: ListIngressesRequest
        @return: ListIngressesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ingresses_with_options(request, headers, runtime)

    async def list_ingresses_async(
        self,
        request: sae_20190506_models.ListIngressesRequest,
    ) -> sae_20190506_models.ListIngressesResponse:
        """
        @summary Use ListIngress API call to query Ingress list
        
        @param request: ListIngressesRequest
        @return: ListIngressesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ingresses_with_options_async(request, headers, runtime)

    def list_jobs_with_options(
        self,
        request: sae_20190506_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListJobsResponse:
        """
        @summary Queries the information about job templates.
        
        @param request: ListJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_type):
            query['FieldType'] = request.field_type
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/listJobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: sae_20190506_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListJobsResponse:
        """
        @summary Queries the information about job templates.
        
        @param request: ListJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_type):
            query['FieldType'] = request.field_type
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/listJobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: sae_20190506_models.ListJobsRequest,
    ) -> sae_20190506_models.ListJobsResponse:
        """
        @summary Queries the information about job templates.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(request, headers, runtime)

    async def list_jobs_async(
        self,
        request: sae_20190506_models.ListJobsRequest,
    ) -> sae_20190506_models.ListJobsResponse:
        """
        @summary Queries the information about job templates.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(request, headers, runtime)

    def list_log_configs_with_options(
        self,
        request: sae_20190506_models.ListLogConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListLogConfigsResponse:
        """
        @summary Queries a list of application logs.
        
        @param request: ListLogConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogConfigs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/log/listLogConfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListLogConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_log_configs_with_options_async(
        self,
        request: sae_20190506_models.ListLogConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListLogConfigsResponse:
        """
        @summary Queries a list of application logs.
        
        @param request: ListLogConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogConfigs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/log/listLogConfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListLogConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_log_configs(
        self,
        request: sae_20190506_models.ListLogConfigsRequest,
    ) -> sae_20190506_models.ListLogConfigsResponse:
        """
        @summary Queries a list of application logs.
        
        @param request: ListLogConfigsRequest
        @return: ListLogConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_log_configs_with_options(request, headers, runtime)

    async def list_log_configs_async(
        self,
        request: sae_20190506_models.ListLogConfigsRequest,
    ) -> sae_20190506_models.ListLogConfigsResponse:
        """
        @summary Queries a list of application logs.
        
        @param request: ListLogConfigsRequest
        @return: ListLogConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_log_configs_with_options_async(request, headers, runtime)

    def list_namespace_change_orders_with_options(
        self,
        request: sae_20190506_models.ListNamespaceChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListNamespaceChangeOrdersResponse:
        """
        @summary Queries a list of change orders in a namespace.
        
        @param request: ListNamespaceChangeOrdersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNamespaceChangeOrdersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.co_status):
            query['CoStatus'] = request.co_status
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaceChangeOrders',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/listNamespaceChangeOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListNamespaceChangeOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespace_change_orders_with_options_async(
        self,
        request: sae_20190506_models.ListNamespaceChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListNamespaceChangeOrdersResponse:
        """
        @summary Queries a list of change orders in a namespace.
        
        @param request: ListNamespaceChangeOrdersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNamespaceChangeOrdersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.co_status):
            query['CoStatus'] = request.co_status
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaceChangeOrders',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/listNamespaceChangeOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListNamespaceChangeOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespace_change_orders(
        self,
        request: sae_20190506_models.ListNamespaceChangeOrdersRequest,
    ) -> sae_20190506_models.ListNamespaceChangeOrdersResponse:
        """
        @summary Queries a list of change orders in a namespace.
        
        @param request: ListNamespaceChangeOrdersRequest
        @return: ListNamespaceChangeOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_namespace_change_orders_with_options(request, headers, runtime)

    async def list_namespace_change_orders_async(
        self,
        request: sae_20190506_models.ListNamespaceChangeOrdersRequest,
    ) -> sae_20190506_models.ListNamespaceChangeOrdersResponse:
        """
        @summary Queries a list of change orders in a namespace.
        
        @param request: ListNamespaceChangeOrdersRequest
        @return: ListNamespaceChangeOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_namespace_change_orders_with_options_async(request, headers, runtime)

    def list_namespaced_config_maps_with_options(
        self,
        request: sae_20190506_models.ListNamespacedConfigMapsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListNamespacedConfigMapsResponse:
        """
        @summary Queries the ConfigMap instances in a namespace.
        
        @param request: ListNamespacedConfigMapsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNamespacedConfigMapsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespacedConfigMaps',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/listNamespacedConfigMaps',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListNamespacedConfigMapsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespaced_config_maps_with_options_async(
        self,
        request: sae_20190506_models.ListNamespacedConfigMapsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListNamespacedConfigMapsResponse:
        """
        @summary Queries the ConfigMap instances in a namespace.
        
        @param request: ListNamespacedConfigMapsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNamespacedConfigMapsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespacedConfigMaps',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/listNamespacedConfigMaps',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListNamespacedConfigMapsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespaced_config_maps(
        self,
        request: sae_20190506_models.ListNamespacedConfigMapsRequest,
    ) -> sae_20190506_models.ListNamespacedConfigMapsResponse:
        """
        @summary Queries the ConfigMap instances in a namespace.
        
        @param request: ListNamespacedConfigMapsRequest
        @return: ListNamespacedConfigMapsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_namespaced_config_maps_with_options(request, headers, runtime)

    async def list_namespaced_config_maps_async(
        self,
        request: sae_20190506_models.ListNamespacedConfigMapsRequest,
    ) -> sae_20190506_models.ListNamespacedConfigMapsResponse:
        """
        @summary Queries the ConfigMap instances in a namespace.
        
        @param request: ListNamespacedConfigMapsRequest
        @return: ListNamespacedConfigMapsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_namespaced_config_maps_with_options_async(request, headers, runtime)

    def list_published_services_with_options(
        self,
        request: sae_20190506_models.ListPublishedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListPublishedServicesResponse:
        """
        @summary Queries a list of microservices that are published.
        
        @param request: ListPublishedServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishedServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listPublishedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListPublishedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_published_services_with_options_async(
        self,
        request: sae_20190506_models.ListPublishedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListPublishedServicesResponse:
        """
        @summary Queries a list of microservices that are published.
        
        @param request: ListPublishedServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishedServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listPublishedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListPublishedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_published_services(
        self,
        request: sae_20190506_models.ListPublishedServicesRequest,
    ) -> sae_20190506_models.ListPublishedServicesResponse:
        """
        @summary Queries a list of microservices that are published.
        
        @param request: ListPublishedServicesRequest
        @return: ListPublishedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_published_services_with_options(request, headers, runtime)

    async def list_published_services_async(
        self,
        request: sae_20190506_models.ListPublishedServicesRequest,
    ) -> sae_20190506_models.ListPublishedServicesResponse:
        """
        @summary Queries a list of microservices that are published.
        
        @param request: ListPublishedServicesRequest
        @return: ListPublishedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_published_services_with_options_async(request, headers, runtime)

    def list_secrets_with_options(
        self,
        request: sae_20190506_models.ListSecretsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListSecretsResponse:
        """
        @summary Queries the information about Secrets in a namespace.
        
        @param request: ListSecretsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecretsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecrets',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secrets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secrets_with_options_async(
        self,
        request: sae_20190506_models.ListSecretsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListSecretsResponse:
        """
        @summary Queries the information about Secrets in a namespace.
        
        @param request: ListSecretsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecretsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecrets',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secrets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secrets(
        self,
        request: sae_20190506_models.ListSecretsRequest,
    ) -> sae_20190506_models.ListSecretsResponse:
        """
        @summary Queries the information about Secrets in a namespace.
        
        @param request: ListSecretsRequest
        @return: ListSecretsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_secrets_with_options(request, headers, runtime)

    async def list_secrets_async(
        self,
        request: sae_20190506_models.ListSecretsRequest,
    ) -> sae_20190506_models.ListSecretsResponse:
        """
        @summary Queries the information about Secrets in a namespace.
        
        @param request: ListSecretsRequest
        @return: ListSecretsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_secrets_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        request: sae_20190506_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListTagResourcesResponse:
        """
        @summary Queries the mapping relationships between applications and tags.
        
        @param request: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: sae_20190506_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListTagResourcesResponse:
        """
        @summary Queries the mapping relationships between applications and tags.
        
        @param request: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: sae_20190506_models.ListTagResourcesRequest,
    ) -> sae_20190506_models.ListTagResourcesResponse:
        """
        @summary Queries the mapping relationships between applications and tags.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: sae_20190506_models.ListTagResourcesRequest,
    ) -> sae_20190506_models.ListTagResourcesResponse:
        """
        @summary Queries the mapping relationships between applications and tags.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_web_application_instances_with_options(
        self,
        application_id: str,
        tmp_req: sae_20190506_models.ListWebApplicationInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListWebApplicationInstancesResponse:
        """
        @summary Query the list of web application instances.
        
        @description Query the list of web application instances.
        
        @param tmp_req: ListWebApplicationInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebApplicationInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sae_20190506_models.ListWebApplicationInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not UtilClient.is_unset(tmp_req.statuses):
            request.statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        if not UtilClient.is_unset(tmp_req.version_ids):
            request.version_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.version_ids, 'VersionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.statuses_shrink):
            query['Statuses'] = request.statuses_shrink
        if not UtilClient.is_unset(request.version_ids_shrink):
            query['VersionIds'] = request.version_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWebApplicationInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications-observability/{OpenApiUtilClient.get_encode_param(application_id)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListWebApplicationInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_application_instances_with_options_async(
        self,
        application_id: str,
        tmp_req: sae_20190506_models.ListWebApplicationInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListWebApplicationInstancesResponse:
        """
        @summary Query the list of web application instances.
        
        @description Query the list of web application instances.
        
        @param tmp_req: ListWebApplicationInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebApplicationInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sae_20190506_models.ListWebApplicationInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not UtilClient.is_unset(tmp_req.statuses):
            request.statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        if not UtilClient.is_unset(tmp_req.version_ids):
            request.version_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.version_ids, 'VersionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.statuses_shrink):
            query['Statuses'] = request.statuses_shrink
        if not UtilClient.is_unset(request.version_ids_shrink):
            query['VersionIds'] = request.version_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWebApplicationInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications-observability/{OpenApiUtilClient.get_encode_param(application_id)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListWebApplicationInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_application_instances(
        self,
        application_id: str,
        request: sae_20190506_models.ListWebApplicationInstancesRequest,
    ) -> sae_20190506_models.ListWebApplicationInstancesResponse:
        """
        @summary Query the list of web application instances.
        
        @description Query the list of web application instances.
        
        @param request: ListWebApplicationInstancesRequest
        @return: ListWebApplicationInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_web_application_instances_with_options(application_id, request, headers, runtime)

    async def list_web_application_instances_async(
        self,
        application_id: str,
        request: sae_20190506_models.ListWebApplicationInstancesRequest,
    ) -> sae_20190506_models.ListWebApplicationInstancesResponse:
        """
        @summary Query the list of web application instances.
        
        @description Query the list of web application instances.
        
        @param request: ListWebApplicationInstancesRequest
        @return: ListWebApplicationInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_web_application_instances_with_options_async(application_id, request, headers, runtime)

    def list_web_application_revisions_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.ListWebApplicationRevisionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListWebApplicationRevisionsResponse:
        """
        @summary Query the list of web application versions.
        
        @description Query the list of web application versions.
        
        @param request: ListWebApplicationRevisionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebApplicationRevisionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWebApplicationRevisions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-revisions/{OpenApiUtilClient.get_encode_param(application_id)}/revisions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListWebApplicationRevisionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_application_revisions_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.ListWebApplicationRevisionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListWebApplicationRevisionsResponse:
        """
        @summary Query the list of web application versions.
        
        @description Query the list of web application versions.
        
        @param request: ListWebApplicationRevisionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebApplicationRevisionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWebApplicationRevisions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-revisions/{OpenApiUtilClient.get_encode_param(application_id)}/revisions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListWebApplicationRevisionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_application_revisions(
        self,
        application_id: str,
        request: sae_20190506_models.ListWebApplicationRevisionsRequest,
    ) -> sae_20190506_models.ListWebApplicationRevisionsResponse:
        """
        @summary Query the list of web application versions.
        
        @description Query the list of web application versions.
        
        @param request: ListWebApplicationRevisionsRequest
        @return: ListWebApplicationRevisionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_web_application_revisions_with_options(application_id, request, headers, runtime)

    async def list_web_application_revisions_async(
        self,
        application_id: str,
        request: sae_20190506_models.ListWebApplicationRevisionsRequest,
    ) -> sae_20190506_models.ListWebApplicationRevisionsResponse:
        """
        @summary Query the list of web application versions.
        
        @description Query the list of web application versions.
        
        @param request: ListWebApplicationRevisionsRequest
        @return: ListWebApplicationRevisionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_web_application_revisions_with_options_async(application_id, request, headers, runtime)

    def list_web_applications_with_options(
        self,
        request: sae_20190506_models.ListWebApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListWebApplicationsResponse:
        """
        @summary Query the list of web applications.
        
        @description Call the ListWebApplications operation to query the list of web applications.
        
        @param request: ListWebApplicationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWebApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListWebApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_applications_with_options_async(
        self,
        request: sae_20190506_models.ListWebApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListWebApplicationsResponse:
        """
        @summary Query the list of web applications.
        
        @description Call the ListWebApplications operation to query the list of web applications.
        
        @param request: ListWebApplicationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWebApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListWebApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_applications(
        self,
        request: sae_20190506_models.ListWebApplicationsRequest,
    ) -> sae_20190506_models.ListWebApplicationsResponse:
        """
        @summary Query the list of web applications.
        
        @description Call the ListWebApplications operation to query the list of web applications.
        
        @param request: ListWebApplicationsRequest
        @return: ListWebApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_web_applications_with_options(request, headers, runtime)

    async def list_web_applications_async(
        self,
        request: sae_20190506_models.ListWebApplicationsRequest,
    ) -> sae_20190506_models.ListWebApplicationsResponse:
        """
        @summary Query the list of web applications.
        
        @description Call the ListWebApplications operation to query the list of web applications.
        
        @param request: ListWebApplicationsRequest
        @return: ListWebApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_web_applications_with_options_async(request, headers, runtime)

    def list_web_custom_domains_with_options(
        self,
        request: sae_20190506_models.ListWebCustomDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListWebCustomDomainsResponse:
        """
        @summary Query available custom domain names.
        
        @description Query available custom domain names.
        
        @param request: ListWebCustomDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebCustomDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWebCustomDomains',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/custom-domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListWebCustomDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_custom_domains_with_options_async(
        self,
        request: sae_20190506_models.ListWebCustomDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListWebCustomDomainsResponse:
        """
        @summary Query available custom domain names.
        
        @description Query available custom domain names.
        
        @param request: ListWebCustomDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWebCustomDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWebCustomDomains',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/custom-domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListWebCustomDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_custom_domains(
        self,
        request: sae_20190506_models.ListWebCustomDomainsRequest,
    ) -> sae_20190506_models.ListWebCustomDomainsResponse:
        """
        @summary Query available custom domain names.
        
        @description Query available custom domain names.
        
        @param request: ListWebCustomDomainsRequest
        @return: ListWebCustomDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_web_custom_domains_with_options(request, headers, runtime)

    async def list_web_custom_domains_async(
        self,
        request: sae_20190506_models.ListWebCustomDomainsRequest,
    ) -> sae_20190506_models.ListWebCustomDomainsResponse:
        """
        @summary Query available custom domain names.
        
        @description Query available custom domain names.
        
        @param request: ListWebCustomDomainsRequest
        @return: ListWebCustomDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_web_custom_domains_with_options_async(request, headers, runtime)

    def open_sae_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.OpenSaeServiceResponse:
        """
        @summary Activates the Serverless App Engine (SAE) service for free.
        
        @description > Make sure that your account balance is greater than 0. Otherwise, the SAE service cannot be activated.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenSaeServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OpenSaeService',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/service/open',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.OpenSaeServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_sae_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.OpenSaeServiceResponse:
        """
        @summary Activates the Serverless App Engine (SAE) service for free.
        
        @description > Make sure that your account balance is greater than 0. Otherwise, the SAE service cannot be activated.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenSaeServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OpenSaeService',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/service/open',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.OpenSaeServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_sae_service(self) -> sae_20190506_models.OpenSaeServiceResponse:
        """
        @summary Activates the Serverless App Engine (SAE) service for free.
        
        @description > Make sure that your account balance is greater than 0. Otherwise, the SAE service cannot be activated.
        
        @return: OpenSaeServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_sae_service_with_options(headers, runtime)

    async def open_sae_service_async(self) -> sae_20190506_models.OpenSaeServiceResponse:
        """
        @summary Activates the Serverless App Engine (SAE) service for free.
        
        @description > Make sure that your account balance is greater than 0. Otherwise, the SAE service cannot be activated.
        
        @return: OpenSaeServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.open_sae_service_with_options_async(headers, runtime)

    def publish_web_application_revision_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.PublishWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.PublishWebApplicationRevisionResponse:
        """
        @summary Publish a web application version.
        
        @description Publish a web application version. You can change the configurations of the version and create a new version.
        
        @param request: PublishWebApplicationRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishWebApplicationRevisionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PublishWebApplicationRevision',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-revisions/{OpenApiUtilClient.get_encode_param(application_id)}/revisions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.PublishWebApplicationRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_web_application_revision_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.PublishWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.PublishWebApplicationRevisionResponse:
        """
        @summary Publish a web application version.
        
        @description Publish a web application version. You can change the configurations of the version and create a new version.
        
        @param request: PublishWebApplicationRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishWebApplicationRevisionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PublishWebApplicationRevision',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-revisions/{OpenApiUtilClient.get_encode_param(application_id)}/revisions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.PublishWebApplicationRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_web_application_revision(
        self,
        application_id: str,
        request: sae_20190506_models.PublishWebApplicationRevisionRequest,
    ) -> sae_20190506_models.PublishWebApplicationRevisionResponse:
        """
        @summary Publish a web application version.
        
        @description Publish a web application version. You can change the configurations of the version and create a new version.
        
        @param request: PublishWebApplicationRevisionRequest
        @return: PublishWebApplicationRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_web_application_revision_with_options(application_id, request, headers, runtime)

    async def publish_web_application_revision_async(
        self,
        application_id: str,
        request: sae_20190506_models.PublishWebApplicationRevisionRequest,
    ) -> sae_20190506_models.PublishWebApplicationRevisionResponse:
        """
        @summary Publish a web application version.
        
        @description Publish a web application version. You can change the configurations of the version and create a new version.
        
        @param request: PublishWebApplicationRevisionRequest
        @return: PublishWebApplicationRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_web_application_revision_with_options_async(application_id, request, headers, runtime)

    def query_resource_statics_with_options(
        self,
        request: sae_20190506_models.QueryResourceStaticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.QueryResourceStaticsResponse:
        """
        @summary Queries the resource usage of an application.
        
        @param request: QueryResourceStaticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryResourceStaticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResourceStatics',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/quota/queryResourceStatics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.QueryResourceStaticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_resource_statics_with_options_async(
        self,
        request: sae_20190506_models.QueryResourceStaticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.QueryResourceStaticsResponse:
        """
        @summary Queries the resource usage of an application.
        
        @param request: QueryResourceStaticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryResourceStaticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResourceStatics',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/quota/queryResourceStatics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.QueryResourceStaticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_resource_statics(
        self,
        request: sae_20190506_models.QueryResourceStaticsRequest,
    ) -> sae_20190506_models.QueryResourceStaticsResponse:
        """
        @summary Queries the resource usage of an application.
        
        @param request: QueryResourceStaticsRequest
        @return: QueryResourceStaticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_resource_statics_with_options(request, headers, runtime)

    async def query_resource_statics_async(
        self,
        request: sae_20190506_models.QueryResourceStaticsRequest,
    ) -> sae_20190506_models.QueryResourceStaticsResponse:
        """
        @summary Queries the resource usage of an application.
        
        @param request: QueryResourceStaticsRequest
        @return: QueryResourceStaticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_resource_statics_with_options_async(request, headers, runtime)

    def reduce_application_capacity_by_instance_ids_with_options(
        self,
        request: sae_20190506_models.ReduceApplicationCapacityByInstanceIdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse:
        """
        @summary Reduces capacity by instance IDs.
        
        @param request: ReduceApplicationCapacityByInstanceIdsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReduceApplicationCapacityByInstanceIdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReduceApplicationCapacityByInstanceIds',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/ScaleInApplicationWithInstanceIds',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def reduce_application_capacity_by_instance_ids_with_options_async(
        self,
        request: sae_20190506_models.ReduceApplicationCapacityByInstanceIdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse:
        """
        @summary Reduces capacity by instance IDs.
        
        @param request: ReduceApplicationCapacityByInstanceIdsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReduceApplicationCapacityByInstanceIdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReduceApplicationCapacityByInstanceIds',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/ScaleInApplicationWithInstanceIds',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reduce_application_capacity_by_instance_ids(
        self,
        request: sae_20190506_models.ReduceApplicationCapacityByInstanceIdsRequest,
    ) -> sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse:
        """
        @summary Reduces capacity by instance IDs.
        
        @param request: ReduceApplicationCapacityByInstanceIdsRequest
        @return: ReduceApplicationCapacityByInstanceIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reduce_application_capacity_by_instance_ids_with_options(request, headers, runtime)

    async def reduce_application_capacity_by_instance_ids_async(
        self,
        request: sae_20190506_models.ReduceApplicationCapacityByInstanceIdsRequest,
    ) -> sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse:
        """
        @summary Reduces capacity by instance IDs.
        
        @param request: ReduceApplicationCapacityByInstanceIdsRequest
        @return: ReduceApplicationCapacityByInstanceIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reduce_application_capacity_by_instance_ids_with_options_async(request, headers, runtime)

    def rescale_application_with_options(
        self,
        request: sae_20190506_models.RescaleApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RescaleApplicationResponse:
        """
        @summary Scales an application.
        
        @param request: RescaleApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RescaleApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rescaleApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RescaleApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def rescale_application_with_options_async(
        self,
        request: sae_20190506_models.RescaleApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RescaleApplicationResponse:
        """
        @summary Scales an application.
        
        @param request: RescaleApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RescaleApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rescaleApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RescaleApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rescale_application(
        self,
        request: sae_20190506_models.RescaleApplicationRequest,
    ) -> sae_20190506_models.RescaleApplicationResponse:
        """
        @summary Scales an application.
        
        @param request: RescaleApplicationRequest
        @return: RescaleApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rescale_application_with_options(request, headers, runtime)

    async def rescale_application_async(
        self,
        request: sae_20190506_models.RescaleApplicationRequest,
    ) -> sae_20190506_models.RescaleApplicationResponse:
        """
        @summary Scales an application.
        
        @param request: RescaleApplicationRequest
        @return: RescaleApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rescale_application_with_options_async(request, headers, runtime)

    def rescale_application_vertically_with_options(
        self,
        request: sae_20190506_models.RescaleApplicationVerticallyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RescaleApplicationVerticallyResponse:
        """
        @summary Changes the instance specifications of an application.
        
        @param request: RescaleApplicationVerticallyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RescaleApplicationVerticallyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['autoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['minReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['minReadyInstances'] = request.min_ready_instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplicationVertically',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rescaleApplicationVertically',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RescaleApplicationVerticallyResponse(),
            self.call_api(params, req, runtime)
        )

    async def rescale_application_vertically_with_options_async(
        self,
        request: sae_20190506_models.RescaleApplicationVerticallyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RescaleApplicationVerticallyResponse:
        """
        @summary Changes the instance specifications of an application.
        
        @param request: RescaleApplicationVerticallyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RescaleApplicationVerticallyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['autoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['minReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['minReadyInstances'] = request.min_ready_instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplicationVertically',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rescaleApplicationVertically',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RescaleApplicationVerticallyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rescale_application_vertically(
        self,
        request: sae_20190506_models.RescaleApplicationVerticallyRequest,
    ) -> sae_20190506_models.RescaleApplicationVerticallyResponse:
        """
        @summary Changes the instance specifications of an application.
        
        @param request: RescaleApplicationVerticallyRequest
        @return: RescaleApplicationVerticallyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rescale_application_vertically_with_options(request, headers, runtime)

    async def rescale_application_vertically_async(
        self,
        request: sae_20190506_models.RescaleApplicationVerticallyRequest,
    ) -> sae_20190506_models.RescaleApplicationVerticallyResponse:
        """
        @summary Changes the instance specifications of an application.
        
        @param request: RescaleApplicationVerticallyRequest
        @return: RescaleApplicationVerticallyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rescale_application_vertically_with_options_async(request, headers, runtime)

    def restart_application_with_options(
        self,
        request: sae_20190506_models.RestartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RestartApplicationResponse:
        """
        @summary Restarts an application.
        
        @param request: RestartApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/restartApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RestartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_application_with_options_async(
        self,
        request: sae_20190506_models.RestartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RestartApplicationResponse:
        """
        @summary Restarts an application.
        
        @param request: RestartApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/restartApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RestartApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_application(
        self,
        request: sae_20190506_models.RestartApplicationRequest,
    ) -> sae_20190506_models.RestartApplicationResponse:
        """
        @summary Restarts an application.
        
        @param request: RestartApplicationRequest
        @return: RestartApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_application_with_options(request, headers, runtime)

    async def restart_application_async(
        self,
        request: sae_20190506_models.RestartApplicationRequest,
    ) -> sae_20190506_models.RestartApplicationResponse:
        """
        @summary Restarts an application.
        
        @param request: RestartApplicationRequest
        @return: RestartApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_application_with_options_async(request, headers, runtime)

    def restart_instances_with_options(
        self,
        request: sae_20190506_models.RestartInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RestartInstancesResponse:
        """
        @summary Restarts one or more instances in an application.
        
        @param request: RestartInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/restartInstances',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RestartInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instances_with_options_async(
        self,
        request: sae_20190506_models.RestartInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RestartInstancesResponse:
        """
        @summary Restarts one or more instances in an application.
        
        @param request: RestartInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/restartInstances',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RestartInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instances(
        self,
        request: sae_20190506_models.RestartInstancesRequest,
    ) -> sae_20190506_models.RestartInstancesResponse:
        """
        @summary Restarts one or more instances in an application.
        
        @param request: RestartInstancesRequest
        @return: RestartInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_instances_with_options(request, headers, runtime)

    async def restart_instances_async(
        self,
        request: sae_20190506_models.RestartInstancesRequest,
    ) -> sae_20190506_models.RestartInstancesResponse:
        """
        @summary Restarts one or more instances in an application.
        
        @param request: RestartInstancesRequest
        @return: RestartInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_instances_with_options_async(request, headers, runtime)

    def rollback_application_with_options(
        self,
        request: sae_20190506_models.RollbackApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RollbackApplicationResponse:
        """
        @summary Rolls back an application.
        
        @param request: RollbackApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rollbackApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RollbackApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_application_with_options_async(
        self,
        request: sae_20190506_models.RollbackApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RollbackApplicationResponse:
        """
        @summary Rolls back an application.
        
        @param request: RollbackApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rollbackApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RollbackApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_application(
        self,
        request: sae_20190506_models.RollbackApplicationRequest,
    ) -> sae_20190506_models.RollbackApplicationResponse:
        """
        @summary Rolls back an application.
        
        @param request: RollbackApplicationRequest
        @return: RollbackApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rollback_application_with_options(request, headers, runtime)

    async def rollback_application_async(
        self,
        request: sae_20190506_models.RollbackApplicationRequest,
    ) -> sae_20190506_models.RollbackApplicationResponse:
        """
        @summary Rolls back an application.
        
        @param request: RollbackApplicationRequest
        @return: RollbackApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rollback_application_with_options_async(request, headers, runtime)

    def start_application_with_options(
        self,
        request: sae_20190506_models.StartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StartApplicationResponse:
        """
        @summary Starts an application.
        
        @param request: StartApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/startApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_application_with_options_async(
        self,
        request: sae_20190506_models.StartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StartApplicationResponse:
        """
        @summary Starts an application.
        
        @param request: StartApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/startApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StartApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_application(
        self,
        request: sae_20190506_models.StartApplicationRequest,
    ) -> sae_20190506_models.StartApplicationResponse:
        """
        @summary Starts an application.
        
        @param request: StartApplicationRequest
        @return: StartApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_application_with_options(request, headers, runtime)

    async def start_application_async(
        self,
        request: sae_20190506_models.StartApplicationRequest,
    ) -> sae_20190506_models.StartApplicationResponse:
        """
        @summary Starts an application.
        
        @param request: StartApplicationRequest
        @return: StartApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_application_with_options_async(request, headers, runtime)

    def start_web_application_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.StartWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StartWebApplicationResponse:
        """
        @summary Start a web application.
        
        @description Call the StartWebApplication operation to start a web application.
        
        @param request: StartWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-ops/{OpenApiUtilClient.get_encode_param(application_id)}/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StartWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_web_application_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.StartWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StartWebApplicationResponse:
        """
        @summary Start a web application.
        
        @description Call the StartWebApplication operation to start a web application.
        
        @param request: StartWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-ops/{OpenApiUtilClient.get_encode_param(application_id)}/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StartWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_web_application(
        self,
        application_id: str,
        request: sae_20190506_models.StartWebApplicationRequest,
    ) -> sae_20190506_models.StartWebApplicationResponse:
        """
        @summary Start a web application.
        
        @description Call the StartWebApplication operation to start a web application.
        
        @param request: StartWebApplicationRequest
        @return: StartWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_web_application_with_options(application_id, request, headers, runtime)

    async def start_web_application_async(
        self,
        application_id: str,
        request: sae_20190506_models.StartWebApplicationRequest,
    ) -> sae_20190506_models.StartWebApplicationResponse:
        """
        @summary Start a web application.
        
        @description Call the StartWebApplication operation to start a web application.
        
        @param request: StartWebApplicationRequest
        @return: StartWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_web_application_with_options_async(application_id, request, headers, runtime)

    def stop_application_with_options(
        self,
        request: sae_20190506_models.StopApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StopApplicationResponse:
        """
        @summary 0099b7be-5f5b-4512-a7fc-56049ef1\\\\*\\*\\*\
        
        @param request: StopApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/stopApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StopApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_application_with_options_async(
        self,
        request: sae_20190506_models.StopApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StopApplicationResponse:
        """
        @summary 0099b7be-5f5b-4512-a7fc-56049ef1\\\\*\\*\\*\
        
        @param request: StopApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/stopApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StopApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_application(
        self,
        request: sae_20190506_models.StopApplicationRequest,
    ) -> sae_20190506_models.StopApplicationResponse:
        """
        @summary 0099b7be-5f5b-4512-a7fc-56049ef1\\\\*\\*\\*\
        
        @param request: StopApplicationRequest
        @return: StopApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_application_with_options(request, headers, runtime)

    async def stop_application_async(
        self,
        request: sae_20190506_models.StopApplicationRequest,
    ) -> sae_20190506_models.StopApplicationResponse:
        """
        @summary 0099b7be-5f5b-4512-a7fc-56049ef1\\\\*\\*\\*\
        
        @param request: StopApplicationRequest
        @return: StopApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_application_with_options_async(request, headers, runtime)

    def stop_web_application_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.StopWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StopWebApplicationResponse:
        """
        @summary Stop a web application.
        
        @description Call the StopWebApplication operation to stop a web application.
        
        @param request: StopWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-ops/{OpenApiUtilClient.get_encode_param(application_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StopWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_web_application_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.StopWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StopWebApplicationResponse:
        """
        @summary Stop a web application.
        
        @description Call the StopWebApplication operation to stop a web application.
        
        @param request: StopWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-ops/{OpenApiUtilClient.get_encode_param(application_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StopWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_web_application(
        self,
        application_id: str,
        request: sae_20190506_models.StopWebApplicationRequest,
    ) -> sae_20190506_models.StopWebApplicationResponse:
        """
        @summary Stop a web application.
        
        @description Call the StopWebApplication operation to stop a web application.
        
        @param request: StopWebApplicationRequest
        @return: StopWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_web_application_with_options(application_id, request, headers, runtime)

    async def stop_web_application_async(
        self,
        application_id: str,
        request: sae_20190506_models.StopWebApplicationRequest,
    ) -> sae_20190506_models.StopWebApplicationResponse:
        """
        @summary Stop a web application.
        
        @description Call the StopWebApplication operation to stop a web application.
        
        @param request: StopWebApplicationRequest
        @return: StopWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_web_application_with_options_async(application_id, request, headers, runtime)

    def suspend_job_with_options(
        self,
        request: sae_20190506_models.SuspendJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.SuspendJobResponse:
        """
        @summary Suspends a job.
        
        @param request: SuspendJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.suspend):
            query['Suspend'] = request.suspend
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/suspendJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.SuspendJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_job_with_options_async(
        self,
        request: sae_20190506_models.SuspendJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.SuspendJobResponse:
        """
        @summary Suspends a job.
        
        @param request: SuspendJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.suspend):
            query['Suspend'] = request.suspend
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/suspendJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.SuspendJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_job(
        self,
        request: sae_20190506_models.SuspendJobRequest,
    ) -> sae_20190506_models.SuspendJobResponse:
        """
        @summary Suspends a job.
        
        @param request: SuspendJobRequest
        @return: SuspendJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.suspend_job_with_options(request, headers, runtime)

    async def suspend_job_async(
        self,
        request: sae_20190506_models.SuspendJobRequest,
    ) -> sae_20190506_models.SuspendJobResponse:
        """
        @summary Suspends a job.
        
        @param request: SuspendJobRequest
        @return: SuspendJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.suspend_job_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: sae_20190506_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.TagResourcesResponse:
        """
        @summary cn-beijing
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: sae_20190506_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.TagResourcesResponse:
        """
        @summary cn-beijing
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: sae_20190506_models.TagResourcesRequest,
    ) -> sae_20190506_models.TagResourcesResponse:
        """
        @summary cn-beijing
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: sae_20190506_models.TagResourcesRequest,
    ) -> sae_20190506_models.TagResourcesResponse:
        """
        @summary cn-beijing
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def unbind_nlb_with_options(
        self,
        request: sae_20190506_models.UnbindNlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UnbindNlbResponse:
        """
        @summary Calls the UnbindNlb operation to delete an NLB listener bound for application access
        
        @param request: UnbindNlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindNlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.nlb_id):
            query['NlbId'] = request.nlb_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindNlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/nlb',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UnbindNlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_nlb_with_options_async(
        self,
        request: sae_20190506_models.UnbindNlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UnbindNlbResponse:
        """
        @summary Calls the UnbindNlb operation to delete an NLB listener bound for application access
        
        @param request: UnbindNlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindNlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.nlb_id):
            query['NlbId'] = request.nlb_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindNlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/nlb',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UnbindNlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_nlb(
        self,
        request: sae_20190506_models.UnbindNlbRequest,
    ) -> sae_20190506_models.UnbindNlbResponse:
        """
        @summary Calls the UnbindNlb operation to delete an NLB listener bound for application access
        
        @param request: UnbindNlbRequest
        @return: UnbindNlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_nlb_with_options(request, headers, runtime)

    async def unbind_nlb_async(
        self,
        request: sae_20190506_models.UnbindNlbRequest,
    ) -> sae_20190506_models.UnbindNlbResponse:
        """
        @summary Calls the UnbindNlb operation to delete an NLB listener bound for application access
        
        @param request: UnbindNlbRequest
        @return: UnbindNlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.unbind_nlb_with_options_async(request, headers, runtime)

    def unbind_slb_with_options(
        self,
        request: sae_20190506_models.UnbindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UnbindSlbResponse:
        """
        @summary Disassociates an internal-facing or Internet-facing SLB instance from an application.
        
        @param request: UnbindSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.internet):
            query['Internet'] = request.internet
        if not UtilClient.is_unset(request.intranet):
            query['Intranet'] = request.intranet
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UnbindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_slb_with_options_async(
        self,
        request: sae_20190506_models.UnbindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UnbindSlbResponse:
        """
        @summary Disassociates an internal-facing or Internet-facing SLB instance from an application.
        
        @param request: UnbindSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.internet):
            query['Internet'] = request.internet
        if not UtilClient.is_unset(request.intranet):
            query['Intranet'] = request.intranet
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UnbindSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_slb(
        self,
        request: sae_20190506_models.UnbindSlbRequest,
    ) -> sae_20190506_models.UnbindSlbResponse:
        """
        @summary Disassociates an internal-facing or Internet-facing SLB instance from an application.
        
        @param request: UnbindSlbRequest
        @return: UnbindSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_slb_with_options(request, headers, runtime)

    async def unbind_slb_async(
        self,
        request: sae_20190506_models.UnbindSlbRequest,
    ) -> sae_20190506_models.UnbindSlbResponse:
        """
        @summary Disassociates an internal-facing or Internet-facing SLB instance from an application.
        
        @param request: UnbindSlbRequest
        @return: UnbindSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.unbind_slb_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: sae_20190506_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: sae_20190506_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: sae_20190506_models.UntagResourcesRequest,
    ) -> sae_20190506_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: sae_20190506_models.UntagResourcesRequest,
    ) -> sae_20190506_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_app_security_group_with_options(
        self,
        request: sae_20190506_models.UpdateAppSecurityGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateAppSecurityGroupResponse:
        """
        @summary Updates the security group of an application.
        
        @param request: UpdateAppSecurityGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppSecurityGroup',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppSecurityGroup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateAppSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_security_group_with_options_async(
        self,
        request: sae_20190506_models.UpdateAppSecurityGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateAppSecurityGroupResponse:
        """
        @summary Updates the security group of an application.
        
        @param request: UpdateAppSecurityGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppSecurityGroup',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppSecurityGroup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateAppSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_security_group(
        self,
        request: sae_20190506_models.UpdateAppSecurityGroupRequest,
    ) -> sae_20190506_models.UpdateAppSecurityGroupResponse:
        """
        @summary Updates the security group of an application.
        
        @param request: UpdateAppSecurityGroupRequest
        @return: UpdateAppSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_security_group_with_options(request, headers, runtime)

    async def update_app_security_group_async(
        self,
        request: sae_20190506_models.UpdateAppSecurityGroupRequest,
    ) -> sae_20190506_models.UpdateAppSecurityGroupResponse:
        """
        @summary Updates the security group of an application.
        
        @param request: UpdateAppSecurityGroupRequest
        @return: UpdateAppSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_app_security_group_with_options_async(request, headers, runtime)

    def update_application_description_with_options(
        self,
        request: sae_20190506_models.UpdateApplicationDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationDescriptionResponse:
        """
        @summary Updates the description of an application.
        
        @param request: UpdateApplicationDescriptionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationDescription',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppDescription',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_description_with_options_async(
        self,
        request: sae_20190506_models.UpdateApplicationDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationDescriptionResponse:
        """
        @summary Updates the description of an application.
        
        @param request: UpdateApplicationDescriptionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationDescription',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppDescription',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_description(
        self,
        request: sae_20190506_models.UpdateApplicationDescriptionRequest,
    ) -> sae_20190506_models.UpdateApplicationDescriptionResponse:
        """
        @summary Updates the description of an application.
        
        @param request: UpdateApplicationDescriptionRequest
        @return: UpdateApplicationDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_description_with_options(request, headers, runtime)

    async def update_application_description_async(
        self,
        request: sae_20190506_models.UpdateApplicationDescriptionRequest,
    ) -> sae_20190506_models.UpdateApplicationDescriptionResponse:
        """
        @summary Updates the description of an application.
        
        @param request: UpdateApplicationDescriptionRequest
        @return: UpdateApplicationDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_application_description_with_options_async(request, headers, runtime)

    def update_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.UpdateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationScalingRuleResponse:
        """
        @summary Updates the auto scaling policy of an application.
        
        @description ##
        If you want to configure more than 50 instances for an application, you must submit a [ticket](https://workorder.console.aliyun.com/#/ticket/createIndex) to add your account to the whitelist.
        
        @param request: UpdateApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.enable_idle):
            query['EnableIdle'] = request.enable_idle
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.UpdateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationScalingRuleResponse:
        """
        @summary Updates the auto scaling policy of an application.
        
        @description ##
        If you want to configure more than 50 instances for an application, you must submit a [ticket](https://workorder.console.aliyun.com/#/ticket/createIndex) to add your account to the whitelist.
        
        @param request: UpdateApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.enable_idle):
            query['EnableIdle'] = request.enable_idle
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_scaling_rule(
        self,
        request: sae_20190506_models.UpdateApplicationScalingRuleRequest,
    ) -> sae_20190506_models.UpdateApplicationScalingRuleResponse:
        """
        @summary Updates the auto scaling policy of an application.
        
        @description ##
        If you want to configure more than 50 instances for an application, you must submit a [ticket](https://workorder.console.aliyun.com/#/ticket/createIndex) to add your account to the whitelist.
        
        @param request: UpdateApplicationScalingRuleRequest
        @return: UpdateApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_scaling_rule_with_options(request, headers, runtime)

    async def update_application_scaling_rule_async(
        self,
        request: sae_20190506_models.UpdateApplicationScalingRuleRequest,
    ) -> sae_20190506_models.UpdateApplicationScalingRuleResponse:
        """
        @summary Updates the auto scaling policy of an application.
        
        @description ##
        If you want to configure more than 50 instances for an application, you must submit a [ticket](https://workorder.console.aliyun.com/#/ticket/createIndex) to add your account to the whitelist.
        
        @param request: UpdateApplicationScalingRuleRequest
        @return: UpdateApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_application_scaling_rule_with_options_async(request, headers, runtime)

    def update_application_vswitches_with_options(
        self,
        request: sae_20190506_models.UpdateApplicationVswitchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationVswitchesResponse:
        """
        @summary Update the configuration of a vSwitch.
        
        @param request: UpdateApplicationVswitchesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationVswitchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationVswitches',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppVswitches',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationVswitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_vswitches_with_options_async(
        self,
        request: sae_20190506_models.UpdateApplicationVswitchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationVswitchesResponse:
        """
        @summary Update the configuration of a vSwitch.
        
        @param request: UpdateApplicationVswitchesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationVswitchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationVswitches',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppVswitches',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationVswitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_vswitches(
        self,
        request: sae_20190506_models.UpdateApplicationVswitchesRequest,
    ) -> sae_20190506_models.UpdateApplicationVswitchesResponse:
        """
        @summary Update the configuration of a vSwitch.
        
        @param request: UpdateApplicationVswitchesRequest
        @return: UpdateApplicationVswitchesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_vswitches_with_options(request, headers, runtime)

    async def update_application_vswitches_async(
        self,
        request: sae_20190506_models.UpdateApplicationVswitchesRequest,
    ) -> sae_20190506_models.UpdateApplicationVswitchesResponse:
        """
        @summary Update the configuration of a vSwitch.
        
        @param request: UpdateApplicationVswitchesRequest
        @return: UpdateApplicationVswitchesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_application_vswitches_with_options_async(request, headers, runtime)

    def update_config_map_with_options(
        self,
        request: sae_20190506_models.UpdateConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateConfigMapResponse:
        """
        @summary Update a ConfigMap.
        
        @param request: UpdateConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigMapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_map_with_options_async(
        self,
        request: sae_20190506_models.UpdateConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateConfigMapResponse:
        """
        @summary Update a ConfigMap.
        
        @param request: UpdateConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigMapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_map(
        self,
        request: sae_20190506_models.UpdateConfigMapRequest,
    ) -> sae_20190506_models.UpdateConfigMapResponse:
        """
        @summary Update a ConfigMap.
        
        @param request: UpdateConfigMapRequest
        @return: UpdateConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_config_map_with_options(request, headers, runtime)

    async def update_config_map_async(
        self,
        request: sae_20190506_models.UpdateConfigMapRequest,
    ) -> sae_20190506_models.UpdateConfigMapResponse:
        """
        @summary Update a ConfigMap.
        
        @param request: UpdateConfigMapRequest
        @return: UpdateConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_config_map_with_options_async(request, headers, runtime)

    def update_grey_tag_route_with_options(
        self,
        request: sae_20190506_models.UpdateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateGreyTagRouteResponse:
        """
        @summary Updates a canary release rule.
        
        @param request: UpdateGreyTagRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGreyTagRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        if not UtilClient.is_unset(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_grey_tag_route_with_options_async(
        self,
        request: sae_20190506_models.UpdateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateGreyTagRouteResponse:
        """
        @summary Updates a canary release rule.
        
        @param request: UpdateGreyTagRouteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGreyTagRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        if not UtilClient.is_unset(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_grey_tag_route(
        self,
        request: sae_20190506_models.UpdateGreyTagRouteRequest,
    ) -> sae_20190506_models.UpdateGreyTagRouteResponse:
        """
        @summary Updates a canary release rule.
        
        @param request: UpdateGreyTagRouteRequest
        @return: UpdateGreyTagRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_grey_tag_route_with_options(request, headers, runtime)

    async def update_grey_tag_route_async(
        self,
        request: sae_20190506_models.UpdateGreyTagRouteRequest,
    ) -> sae_20190506_models.UpdateGreyTagRouteResponse:
        """
        @summary Updates a canary release rule.
        
        @param request: UpdateGreyTagRouteRequest
        @return: UpdateGreyTagRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_grey_tag_route_with_options_async(request, headers, runtime)

    def update_ingress_with_options(
        self,
        request: sae_20190506_models.UpdateIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateIngressResponse:
        """
        @summary Update the configurations of an Ingress instance.
        
        @param request: UpdateIngressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIngressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.cors_config):
            query['CorsConfig'] = request.cors_config
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_xforwarded_for):
            query['EnableXForwardedFor'] = request.enable_xforwarded_for
        if not UtilClient.is_unset(request.enable_xforwarded_for_client_src_port):
            query['EnableXForwardedForClientSrcPort'] = request.enable_xforwarded_for_client_src_port
        if not UtilClient.is_unset(request.enable_xforwarded_for_proto):
            query['EnableXForwardedForProto'] = request.enable_xforwarded_for_proto
        if not UtilClient.is_unset(request.enable_xforwarded_for_slb_id):
            query['EnableXForwardedForSlbId'] = request.enable_xforwarded_for_slb_id
        if not UtilClient.is_unset(request.enable_xforwarded_for_slb_port):
            query['EnableXForwardedForSlbPort'] = request.enable_xforwarded_for_slb_port
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        body = {}
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ingress_with_options_async(
        self,
        request: sae_20190506_models.UpdateIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateIngressResponse:
        """
        @summary Update the configurations of an Ingress instance.
        
        @param request: UpdateIngressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIngressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.cors_config):
            query['CorsConfig'] = request.cors_config
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_xforwarded_for):
            query['EnableXForwardedFor'] = request.enable_xforwarded_for
        if not UtilClient.is_unset(request.enable_xforwarded_for_client_src_port):
            query['EnableXForwardedForClientSrcPort'] = request.enable_xforwarded_for_client_src_port
        if not UtilClient.is_unset(request.enable_xforwarded_for_proto):
            query['EnableXForwardedForProto'] = request.enable_xforwarded_for_proto
        if not UtilClient.is_unset(request.enable_xforwarded_for_slb_id):
            query['EnableXForwardedForSlbId'] = request.enable_xforwarded_for_slb_id
        if not UtilClient.is_unset(request.enable_xforwarded_for_slb_port):
            query['EnableXForwardedForSlbPort'] = request.enable_xforwarded_for_slb_port
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        body = {}
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ingress(
        self,
        request: sae_20190506_models.UpdateIngressRequest,
    ) -> sae_20190506_models.UpdateIngressResponse:
        """
        @summary Update the configurations of an Ingress instance.
        
        @param request: UpdateIngressRequest
        @return: UpdateIngressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_ingress_with_options(request, headers, runtime)

    async def update_ingress_async(
        self,
        request: sae_20190506_models.UpdateIngressRequest,
    ) -> sae_20190506_models.UpdateIngressResponse:
        """
        @summary Update the configurations of an Ingress instance.
        
        @param request: UpdateIngressRequest
        @return: UpdateIngressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_ingress_with_options_async(request, headers, runtime)

    def update_job_with_options(
        self,
        request: sae_20190506_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateJobResponse:
        """
        @summary Updates a job template.
        
        @param request: UpdateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.slice):
            query['Slice'] = request.slice
        if not UtilClient.is_unset(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php):
            body['Php'] = request.php
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/updateJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        request: sae_20190506_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateJobResponse:
        """
        @summary Updates a job template.
        
        @param request: UpdateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.slice):
            query['Slice'] = request.slice
        if not UtilClient.is_unset(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php):
            body['Php'] = request.php
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/updateJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job(
        self,
        request: sae_20190506_models.UpdateJobRequest,
    ) -> sae_20190506_models.UpdateJobResponse:
        """
        @summary Updates a job template.
        
        @param request: UpdateJobRequest
        @return: UpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_job_with_options(request, headers, runtime)

    async def update_job_async(
        self,
        request: sae_20190506_models.UpdateJobRequest,
    ) -> sae_20190506_models.UpdateJobResponse:
        """
        @summary Updates a job template.
        
        @param request: UpdateJobRequest
        @return: UpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_job_with_options_async(request, headers, runtime)

    def update_namespace_with_options(
        self,
        request: sae_20190506_models.UpdateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateNamespaceResponse:
        """
        @summary Updates the information about a namespace.
        
        @param request: UpdateNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_micro_registration):
            query['EnableMicroRegistration'] = request.enable_micro_registration
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        request: sae_20190506_models.UpdateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateNamespaceResponse:
        """
        @summary Updates the information about a namespace.
        
        @param request: UpdateNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_micro_registration):
            query['EnableMicroRegistration'] = request.enable_micro_registration
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace(
        self,
        request: sae_20190506_models.UpdateNamespaceRequest,
    ) -> sae_20190506_models.UpdateNamespaceResponse:
        """
        @summary Updates the information about a namespace.
        
        @param request: UpdateNamespaceRequest
        @return: UpdateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_namespace_with_options(request, headers, runtime)

    async def update_namespace_async(
        self,
        request: sae_20190506_models.UpdateNamespaceRequest,
    ) -> sae_20190506_models.UpdateNamespaceResponse:
        """
        @summary Updates the information about a namespace.
        
        @param request: UpdateNamespaceRequest
        @return: UpdateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_namespace_with_options_async(request, headers, runtime)

    def update_namespace_vpc_with_options(
        self,
        request: sae_20190506_models.UpdateNamespaceVpcRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateNamespaceVpcResponse:
        """
        @summary cn-beijing:test
        
        @param request: UpdateNamespaceVpcRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNamespaceVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespaceVpc',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/updateNamespaceVpc',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateNamespaceVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_vpc_with_options_async(
        self,
        request: sae_20190506_models.UpdateNamespaceVpcRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateNamespaceVpcResponse:
        """
        @summary cn-beijing:test
        
        @param request: UpdateNamespaceVpcRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNamespaceVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespaceVpc',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/updateNamespaceVpc',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateNamespaceVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace_vpc(
        self,
        request: sae_20190506_models.UpdateNamespaceVpcRequest,
    ) -> sae_20190506_models.UpdateNamespaceVpcResponse:
        """
        @summary cn-beijing:test
        
        @param request: UpdateNamespaceVpcRequest
        @return: UpdateNamespaceVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_namespace_vpc_with_options(request, headers, runtime)

    async def update_namespace_vpc_async(
        self,
        request: sae_20190506_models.UpdateNamespaceVpcRequest,
    ) -> sae_20190506_models.UpdateNamespaceVpcResponse:
        """
        @summary cn-beijing:test
        
        @param request: UpdateNamespaceVpcRequest
        @return: UpdateNamespaceVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_namespace_vpc_with_options_async(request, headers, runtime)

    def update_secret_with_options(
        self,
        tmp_req: sae_20190506_models.UpdateSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateSecretResponse:
        """
        @summary The HTTP status code. Valid values:
        **2xx**: The call was successful.
        **3xx**: The call was redirected.
        **4xx**: The call failed.
        **5xx**: A server error occurred.
        
        @param tmp_req: UpdateSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecretResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sae_20190506_models.UpdateSecretShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.secret_data):
            request.secret_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.secret_data, 'SecretData', 'json')
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_data_shrink):
            query['SecretData'] = request.secret_data_shrink
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_with_options_async(
        self,
        tmp_req: sae_20190506_models.UpdateSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateSecretResponse:
        """
        @summary The HTTP status code. Valid values:
        **2xx**: The call was successful.
        **3xx**: The call was redirected.
        **4xx**: The call failed.
        **5xx**: A server error occurred.
        
        @param tmp_req: UpdateSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecretResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sae_20190506_models.UpdateSecretShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.secret_data):
            request.secret_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.secret_data, 'SecretData', 'json')
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_data_shrink):
            query['SecretData'] = request.secret_data_shrink
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret(
        self,
        request: sae_20190506_models.UpdateSecretRequest,
    ) -> sae_20190506_models.UpdateSecretResponse:
        """
        @summary The HTTP status code. Valid values:
        **2xx**: The call was successful.
        **3xx**: The call was redirected.
        **4xx**: The call failed.
        **5xx**: A server error occurred.
        
        @param request: UpdateSecretRequest
        @return: UpdateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_secret_with_options(request, headers, runtime)

    async def update_secret_async(
        self,
        request: sae_20190506_models.UpdateSecretRequest,
    ) -> sae_20190506_models.UpdateSecretResponse:
        """
        @summary The HTTP status code. Valid values:
        **2xx**: The call was successful.
        **3xx**: The call was redirected.
        **4xx**: The call failed.
        **5xx**: A server error occurred.
        
        @param request: UpdateSecretRequest
        @return: UpdateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_secret_with_options_async(request, headers, runtime)

    def update_web_application_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateWebApplicationResponse:
        """
        @summary Updates the configuration at the web application level.
        
        @description You can call the UpdateWebApplication operation to update the configuration at the web application level.
        
        @param request: UpdateWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_web_application_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateWebApplicationResponse:
        """
        @summary Updates the configuration at the web application level.
        
        @description You can call the UpdateWebApplication operation to update the configuration at the web application level.
        
        @param request: UpdateWebApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWebApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateWebApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/applications/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_web_application(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationRequest,
    ) -> sae_20190506_models.UpdateWebApplicationResponse:
        """
        @summary Updates the configuration at the web application level.
        
        @description You can call the UpdateWebApplication operation to update the configuration at the web application level.
        
        @param request: UpdateWebApplicationRequest
        @return: UpdateWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_web_application_with_options(application_id, request, headers, runtime)

    async def update_web_application_async(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationRequest,
    ) -> sae_20190506_models.UpdateWebApplicationResponse:
        """
        @summary Updates the configuration at the web application level.
        
        @description You can call the UpdateWebApplication operation to update the configuration at the web application level.
        
        @param request: UpdateWebApplicationRequest
        @return: UpdateWebApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_web_application_with_options_async(application_id, request, headers, runtime)

    def update_web_application_scaling_config_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationScalingConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateWebApplicationScalingConfigResponse:
        """
        @summary Update the scaling configuration of a web application.
        
        @description You can call the UpdateWebApplicationScalingConfig operation to update the scaling configurations of a web application.
        
        @param request: UpdateWebApplicationScalingConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWebApplicationScalingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateWebApplicationScalingConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-scaling/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateWebApplicationScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_web_application_scaling_config_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationScalingConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateWebApplicationScalingConfigResponse:
        """
        @summary Update the scaling configuration of a web application.
        
        @description You can call the UpdateWebApplicationScalingConfig operation to update the scaling configurations of a web application.
        
        @param request: UpdateWebApplicationScalingConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWebApplicationScalingConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateWebApplicationScalingConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-scaling/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateWebApplicationScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_web_application_scaling_config(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationScalingConfigRequest,
    ) -> sae_20190506_models.UpdateWebApplicationScalingConfigResponse:
        """
        @summary Update the scaling configuration of a web application.
        
        @description You can call the UpdateWebApplicationScalingConfig operation to update the scaling configurations of a web application.
        
        @param request: UpdateWebApplicationScalingConfigRequest
        @return: UpdateWebApplicationScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_web_application_scaling_config_with_options(application_id, request, headers, runtime)

    async def update_web_application_scaling_config_async(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationScalingConfigRequest,
    ) -> sae_20190506_models.UpdateWebApplicationScalingConfigResponse:
        """
        @summary Update the scaling configuration of a web application.
        
        @description You can call the UpdateWebApplicationScalingConfig operation to update the scaling configurations of a web application.
        
        @param request: UpdateWebApplicationScalingConfigRequest
        @return: UpdateWebApplicationScalingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_web_application_scaling_config_with_options_async(application_id, request, headers, runtime)

    def update_web_application_traffic_config_with_options(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationTrafficConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateWebApplicationTrafficConfigResponse:
        """
        @summary Update the traffic configurations of a web application.
        
        @description Call the UpdateWebApplicationTrafficConfig operation to update the traffic configurations of a web application.
        
        @param request: UpdateWebApplicationTrafficConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWebApplicationTrafficConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateWebApplicationTrafficConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-traffic/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateWebApplicationTrafficConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_web_application_traffic_config_with_options_async(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationTrafficConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateWebApplicationTrafficConfigResponse:
        """
        @summary Update the traffic configurations of a web application.
        
        @description Call the UpdateWebApplicationTrafficConfig operation to update the traffic configurations of a web application.
        
        @param request: UpdateWebApplicationTrafficConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWebApplicationTrafficConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateWebApplicationTrafficConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/application-traffic/{OpenApiUtilClient.get_encode_param(application_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateWebApplicationTrafficConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_web_application_traffic_config(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationTrafficConfigRequest,
    ) -> sae_20190506_models.UpdateWebApplicationTrafficConfigResponse:
        """
        @summary Update the traffic configurations of a web application.
        
        @description Call the UpdateWebApplicationTrafficConfig operation to update the traffic configurations of a web application.
        
        @param request: UpdateWebApplicationTrafficConfigRequest
        @return: UpdateWebApplicationTrafficConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_web_application_traffic_config_with_options(application_id, request, headers, runtime)

    async def update_web_application_traffic_config_async(
        self,
        application_id: str,
        request: sae_20190506_models.UpdateWebApplicationTrafficConfigRequest,
    ) -> sae_20190506_models.UpdateWebApplicationTrafficConfigResponse:
        """
        @summary Update the traffic configurations of a web application.
        
        @description Call the UpdateWebApplicationTrafficConfig operation to update the traffic configurations of a web application.
        
        @param request: UpdateWebApplicationTrafficConfigRequest
        @return: UpdateWebApplicationTrafficConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_web_application_traffic_config_with_options_async(application_id, request, headers, runtime)

    def update_web_custom_domain_with_options(
        self,
        domain_name: str,
        request: sae_20190506_models.UpdateWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateWebCustomDomainResponse:
        """
        @summary Update a custom domain name.
        
        @description Update a custom domain name.
        
        @param request: UpdateWebCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWebCustomDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateWebCustomDomain',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateWebCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_web_custom_domain_with_options_async(
        self,
        domain_name: str,
        request: sae_20190506_models.UpdateWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateWebCustomDomainResponse:
        """
        @summary Update a custom domain name.
        
        @description Update a custom domain name.
        
        @param request: UpdateWebCustomDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWebCustomDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateWebCustomDomain',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v2/api/web/custom-domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateWebCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_web_custom_domain(
        self,
        domain_name: str,
        request: sae_20190506_models.UpdateWebCustomDomainRequest,
    ) -> sae_20190506_models.UpdateWebCustomDomainResponse:
        """
        @summary Update a custom domain name.
        
        @description Update a custom domain name.
        
        @param request: UpdateWebCustomDomainRequest
        @return: UpdateWebCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_web_custom_domain_with_options(domain_name, request, headers, runtime)

    async def update_web_custom_domain_async(
        self,
        domain_name: str,
        request: sae_20190506_models.UpdateWebCustomDomainRequest,
    ) -> sae_20190506_models.UpdateWebCustomDomainResponse:
        """
        @summary Update a custom domain name.
        
        @description Update a custom domain name.
        
        @param request: UpdateWebCustomDomainRequest
        @return: UpdateWebCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_web_custom_domain_with_options_async(domain_name, request, headers, runtime)

    def upgrade_application_apm_service_with_options(
        self,
        request: sae_20190506_models.UpgradeApplicationApmServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpgradeApplicationApmServiceResponse:
        """
        @summary Enables the advanced monitoring feature of Application Real-Time Monitoring Service (ARMS).
        
        @description You are charged when you use the ARMS advanced monitoring feature. Enable this feature based on your business requirements. For more information, see [Billing overview](https://icms.alibaba-inc.com/content/arms/arms?l=1\\&m=16992\\&n=3183148).
        
        @param request: UpgradeApplicationApmServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeApplicationApmServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeApplicationApmService',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/applicationApmService',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpgradeApplicationApmServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_application_apm_service_with_options_async(
        self,
        request: sae_20190506_models.UpgradeApplicationApmServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpgradeApplicationApmServiceResponse:
        """
        @summary Enables the advanced monitoring feature of Application Real-Time Monitoring Service (ARMS).
        
        @description You are charged when you use the ARMS advanced monitoring feature. Enable this feature based on your business requirements. For more information, see [Billing overview](https://icms.alibaba-inc.com/content/arms/arms?l=1\\&m=16992\\&n=3183148).
        
        @param request: UpgradeApplicationApmServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeApplicationApmServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeApplicationApmService',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/applicationApmService',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpgradeApplicationApmServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_application_apm_service(
        self,
        request: sae_20190506_models.UpgradeApplicationApmServiceRequest,
    ) -> sae_20190506_models.UpgradeApplicationApmServiceResponse:
        """
        @summary Enables the advanced monitoring feature of Application Real-Time Monitoring Service (ARMS).
        
        @description You are charged when you use the ARMS advanced monitoring feature. Enable this feature based on your business requirements. For more information, see [Billing overview](https://icms.alibaba-inc.com/content/arms/arms?l=1\\&m=16992\\&n=3183148).
        
        @param request: UpgradeApplicationApmServiceRequest
        @return: UpgradeApplicationApmServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_application_apm_service_with_options(request, headers, runtime)

    async def upgrade_application_apm_service_async(
        self,
        request: sae_20190506_models.UpgradeApplicationApmServiceRequest,
    ) -> sae_20190506_models.UpgradeApplicationApmServiceResponse:
        """
        @summary Enables the advanced monitoring feature of Application Real-Time Monitoring Service (ARMS).
        
        @description You are charged when you use the ARMS advanced monitoring feature. Enable this feature based on your business requirements. For more information, see [Billing overview](https://icms.alibaba-inc.com/content/arms/arms?l=1\\&m=16992\\&n=3183148).
        
        @param request: UpgradeApplicationApmServiceRequest
        @return: UpgradeApplicationApmServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_application_apm_service_with_options_async(request, headers, runtime)
