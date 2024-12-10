# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mssp20161228 import models as mssp_20161228_models
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
        self._endpoint = self.get_endpoint('mssp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_service_work_order_with_options(
        self,
        request: mssp_20161228_models.CreateServiceWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.CreateServiceWorkOrderResponse:
        """
        @summary Create Service Work Order
        
        @param request: CreateServiceWorkOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceWorkOrderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator):
            body['Creator'] = request.creator
        if not UtilClient.is_unset(request.customer_id):
            body['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.duration_day):
            body['DurationDay'] = request.duration_day
        if not UtilClient.is_unset(request.is_attachment):
            body['IsAttachment'] = request.is_attachment
        if not UtilClient.is_unset(request.is_work_order_notify):
            body['IsWorkOrderNotify'] = request.is_work_order_notify
        if not UtilClient.is_unset(request.notify_day):
            body['NotifyDay'] = request.notify_day
        if not UtilClient.is_unset(request.notify_id):
            body['NotifyId'] = request.notify_id
        if not UtilClient.is_unset(request.operate_remark):
            body['OperateRemark'] = request.operate_remark
        if not UtilClient.is_unset(request.operate_type):
            body['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.work_order_detail):
            body['WorkOrderDetail'] = request.work_order_detail
        if not UtilClient.is_unset(request.work_order_name):
            body['WorkOrderName'] = request.work_order_name
        if not UtilClient.is_unset(request.work_order_source):
            body['WorkOrderSource'] = request.work_order_source
        if not UtilClient.is_unset(request.work_order_status):
            body['WorkOrderStatus'] = request.work_order_status
        if not UtilClient.is_unset(request.work_order_type):
            body['WorkOrderType'] = request.work_order_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceWorkOrder',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.CreateServiceWorkOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_work_order_with_options_async(
        self,
        request: mssp_20161228_models.CreateServiceWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.CreateServiceWorkOrderResponse:
        """
        @summary Create Service Work Order
        
        @param request: CreateServiceWorkOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceWorkOrderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator):
            body['Creator'] = request.creator
        if not UtilClient.is_unset(request.customer_id):
            body['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.duration_day):
            body['DurationDay'] = request.duration_day
        if not UtilClient.is_unset(request.is_attachment):
            body['IsAttachment'] = request.is_attachment
        if not UtilClient.is_unset(request.is_work_order_notify):
            body['IsWorkOrderNotify'] = request.is_work_order_notify
        if not UtilClient.is_unset(request.notify_day):
            body['NotifyDay'] = request.notify_day
        if not UtilClient.is_unset(request.notify_id):
            body['NotifyId'] = request.notify_id
        if not UtilClient.is_unset(request.operate_remark):
            body['OperateRemark'] = request.operate_remark
        if not UtilClient.is_unset(request.operate_type):
            body['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.work_order_detail):
            body['WorkOrderDetail'] = request.work_order_detail
        if not UtilClient.is_unset(request.work_order_name):
            body['WorkOrderName'] = request.work_order_name
        if not UtilClient.is_unset(request.work_order_source):
            body['WorkOrderSource'] = request.work_order_source
        if not UtilClient.is_unset(request.work_order_status):
            body['WorkOrderStatus'] = request.work_order_status
        if not UtilClient.is_unset(request.work_order_type):
            body['WorkOrderType'] = request.work_order_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceWorkOrder',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.CreateServiceWorkOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_work_order(
        self,
        request: mssp_20161228_models.CreateServiceWorkOrderRequest,
    ) -> mssp_20161228_models.CreateServiceWorkOrderResponse:
        """
        @summary Create Service Work Order
        
        @param request: CreateServiceWorkOrderRequest
        @return: CreateServiceWorkOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_work_order_with_options(request, runtime)

    async def create_service_work_order_async(
        self,
        request: mssp_20161228_models.CreateServiceWorkOrderRequest,
    ) -> mssp_20161228_models.CreateServiceWorkOrderResponse:
        """
        @summary Create Service Work Order
        
        @param request: CreateServiceWorkOrderRequest
        @return: CreateServiceWorkOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_work_order_with_options_async(request, runtime)

    def dispose_service_work_order_with_options(
        self,
        request: mssp_20161228_models.DisposeServiceWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.DisposeServiceWorkOrderResponse:
        """
        @summary Process Service Work Order
        
        @param request: DisposeServiceWorkOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisposeServiceWorkOrderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attachment_name):
            body['AttachmentName'] = request.attachment_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.forward_owner_id):
            body['ForwardOwnerId'] = request.forward_owner_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.is_attachment):
            body['IsAttachment'] = request.is_attachment
        if not UtilClient.is_unset(request.is_work_order_notify):
            body['IsWorkOrderNotify'] = request.is_work_order_notify
        if not UtilClient.is_unset(request.notify_id):
            body['NotifyId'] = request.notify_id
        if not UtilClient.is_unset(request.operate_remark):
            body['OperateRemark'] = request.operate_remark
        if not UtilClient.is_unset(request.operate_type):
            body['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.upgrade_owner_id):
            body['UpgradeOwnerId'] = request.upgrade_owner_id
        if not UtilClient.is_unset(request.work_order_detail):
            body['WorkOrderDetail'] = request.work_order_detail
        if not UtilClient.is_unset(request.work_order_name):
            body['WorkOrderName'] = request.work_order_name
        if not UtilClient.is_unset(request.work_order_status):
            body['WorkOrderStatus'] = request.work_order_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisposeServiceWorkOrder',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.DisposeServiceWorkOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def dispose_service_work_order_with_options_async(
        self,
        request: mssp_20161228_models.DisposeServiceWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.DisposeServiceWorkOrderResponse:
        """
        @summary Process Service Work Order
        
        @param request: DisposeServiceWorkOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisposeServiceWorkOrderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attachment_name):
            body['AttachmentName'] = request.attachment_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.forward_owner_id):
            body['ForwardOwnerId'] = request.forward_owner_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.is_attachment):
            body['IsAttachment'] = request.is_attachment
        if not UtilClient.is_unset(request.is_work_order_notify):
            body['IsWorkOrderNotify'] = request.is_work_order_notify
        if not UtilClient.is_unset(request.notify_id):
            body['NotifyId'] = request.notify_id
        if not UtilClient.is_unset(request.operate_remark):
            body['OperateRemark'] = request.operate_remark
        if not UtilClient.is_unset(request.operate_type):
            body['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.upgrade_owner_id):
            body['UpgradeOwnerId'] = request.upgrade_owner_id
        if not UtilClient.is_unset(request.work_order_detail):
            body['WorkOrderDetail'] = request.work_order_detail
        if not UtilClient.is_unset(request.work_order_name):
            body['WorkOrderName'] = request.work_order_name
        if not UtilClient.is_unset(request.work_order_status):
            body['WorkOrderStatus'] = request.work_order_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisposeServiceWorkOrder',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.DisposeServiceWorkOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dispose_service_work_order(
        self,
        request: mssp_20161228_models.DisposeServiceWorkOrderRequest,
    ) -> mssp_20161228_models.DisposeServiceWorkOrderResponse:
        """
        @summary Process Service Work Order
        
        @param request: DisposeServiceWorkOrderRequest
        @return: DisposeServiceWorkOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dispose_service_work_order_with_options(request, runtime)

    async def dispose_service_work_order_async(
        self,
        request: mssp_20161228_models.DisposeServiceWorkOrderRequest,
    ) -> mssp_20161228_models.DisposeServiceWorkOrderResponse:
        """
        @summary Process Service Work Order
        
        @param request: DisposeServiceWorkOrderRequest
        @return: DisposeServiceWorkOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dispose_service_work_order_with_options_async(request, runtime)

    def dispose_work_task_with_options(
        self,
        request: mssp_20161228_models.DisposeWorkTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.DisposeWorkTaskResponse:
        """
        @summary Handle Alert Work Order
        
        @param request: DisposeWorkTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisposeWorkTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.opt_remark):
            body['OptRemark'] = request.opt_remark
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.task_ids):
            body['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisposeWorkTask',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.DisposeWorkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def dispose_work_task_with_options_async(
        self,
        request: mssp_20161228_models.DisposeWorkTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.DisposeWorkTaskResponse:
        """
        @summary Handle Alert Work Order
        
        @param request: DisposeWorkTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisposeWorkTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.opt_remark):
            body['OptRemark'] = request.opt_remark
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.task_ids):
            body['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisposeWorkTask',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.DisposeWorkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dispose_work_task(
        self,
        request: mssp_20161228_models.DisposeWorkTaskRequest,
    ) -> mssp_20161228_models.DisposeWorkTaskResponse:
        """
        @summary Handle Alert Work Order
        
        @param request: DisposeWorkTaskRequest
        @return: DisposeWorkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dispose_work_task_with_options(request, runtime)

    async def dispose_work_task_async(
        self,
        request: mssp_20161228_models.DisposeWorkTaskRequest,
    ) -> mssp_20161228_models.DisposeWorkTaskResponse:
        """
        @summary Handle Alert Work Order
        
        @param request: DisposeWorkTaskRequest
        @return: DisposeWorkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dispose_work_task_with_options_async(request, runtime)

    def get_alarm_detail_by_id_with_options(
        self,
        request: mssp_20161228_models.GetAlarmDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetAlarmDetailByIdResponse:
        """
        @summary Query Alarm Details
        
        @param request: GetAlarmDetailByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAlarmDetailByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAlarmDetailById',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetAlarmDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alarm_detail_by_id_with_options_async(
        self,
        request: mssp_20161228_models.GetAlarmDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetAlarmDetailByIdResponse:
        """
        @summary Query Alarm Details
        
        @param request: GetAlarmDetailByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAlarmDetailByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAlarmDetailById',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetAlarmDetailByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alarm_detail_by_id(
        self,
        request: mssp_20161228_models.GetAlarmDetailByIdRequest,
    ) -> mssp_20161228_models.GetAlarmDetailByIdResponse:
        """
        @summary Query Alarm Details
        
        @param request: GetAlarmDetailByIdRequest
        @return: GetAlarmDetailByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_alarm_detail_by_id_with_options(request, runtime)

    async def get_alarm_detail_by_id_async(
        self,
        request: mssp_20161228_models.GetAlarmDetailByIdRequest,
    ) -> mssp_20161228_models.GetAlarmDetailByIdResponse:
        """
        @summary Query Alarm Details
        
        @param request: GetAlarmDetailByIdRequest
        @return: GetAlarmDetailByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_alarm_detail_by_id_with_options_async(request, runtime)

    def get_attacked_asset_deal_with_options(
        self,
        request: mssp_20161228_models.GetAttackedAssetDealRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetAttackedAssetDealResponse:
        """
        @summary Trend of Attacked Asset Convergence
        
        @param request: GetAttackedAssetDealRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAttackedAssetDealResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAttackedAssetDeal',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetAttackedAssetDealResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_attacked_asset_deal_with_options_async(
        self,
        request: mssp_20161228_models.GetAttackedAssetDealRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetAttackedAssetDealResponse:
        """
        @summary Trend of Attacked Asset Convergence
        
        @param request: GetAttackedAssetDealRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAttackedAssetDealResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAttackedAssetDeal',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetAttackedAssetDealResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_attacked_asset_deal(
        self,
        request: mssp_20161228_models.GetAttackedAssetDealRequest,
    ) -> mssp_20161228_models.GetAttackedAssetDealResponse:
        """
        @summary Trend of Attacked Asset Convergence
        
        @param request: GetAttackedAssetDealRequest
        @return: GetAttackedAssetDealResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_attacked_asset_deal_with_options(request, runtime)

    async def get_attacked_asset_deal_async(
        self,
        request: mssp_20161228_models.GetAttackedAssetDealRequest,
    ) -> mssp_20161228_models.GetAttackedAssetDealResponse:
        """
        @summary Trend of Attacked Asset Convergence
        
        @param request: GetAttackedAssetDealRequest
        @return: GetAttackedAssetDealResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_attacked_asset_deal_with_options_async(request, runtime)

    def get_baseline_summary_with_options(
        self,
        request: mssp_20161228_models.GetBaselineSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetBaselineSummaryResponse:
        """
        @summary Compliance Risk Convergence Trend
        
        @param request: GetBaselineSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBaselineSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBaselineSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetBaselineSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_baseline_summary_with_options_async(
        self,
        request: mssp_20161228_models.GetBaselineSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetBaselineSummaryResponse:
        """
        @summary Compliance Risk Convergence Trend
        
        @param request: GetBaselineSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBaselineSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBaselineSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetBaselineSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_baseline_summary(
        self,
        request: mssp_20161228_models.GetBaselineSummaryRequest,
    ) -> mssp_20161228_models.GetBaselineSummaryResponse:
        """
        @summary Compliance Risk Convergence Trend
        
        @param request: GetBaselineSummaryRequest
        @return: GetBaselineSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_summary_with_options(request, runtime)

    async def get_baseline_summary_async(
        self,
        request: mssp_20161228_models.GetBaselineSummaryRequest,
    ) -> mssp_20161228_models.GetBaselineSummaryResponse:
        """
        @summary Compliance Risk Convergence Trend
        
        @param request: GetBaselineSummaryRequest
        @return: GetBaselineSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_baseline_summary_with_options_async(request, runtime)

    def get_console_score_with_options(
        self,
        request: mssp_20161228_models.GetConsoleScoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetConsoleScoreResponse:
        """
        @summary Get Console Score
        
        @param request: GetConsoleScoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsoleScoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetConsoleScore',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetConsoleScoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_console_score_with_options_async(
        self,
        request: mssp_20161228_models.GetConsoleScoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetConsoleScoreResponse:
        """
        @summary Get Console Score
        
        @param request: GetConsoleScoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConsoleScoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetConsoleScore',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetConsoleScoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_console_score(
        self,
        request: mssp_20161228_models.GetConsoleScoreRequest,
    ) -> mssp_20161228_models.GetConsoleScoreResponse:
        """
        @summary Get Console Score
        
        @param request: GetConsoleScoreRequest
        @return: GetConsoleScoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_console_score_with_options(request, runtime)

    async def get_console_score_async(
        self,
        request: mssp_20161228_models.GetConsoleScoreRequest,
    ) -> mssp_20161228_models.GetConsoleScoreResponse:
        """
        @summary Get Console Score
        
        @param request: GetConsoleScoreRequest
        @return: GetConsoleScoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_console_score_with_options_async(request, runtime)

    def get_detail_by_id_with_options(
        self,
        request: mssp_20161228_models.GetDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetDetailByIdResponse:
        """
        @summary Query Risk Details
        
        @param request: GetDetailByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDetailByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDetailById',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_detail_by_id_with_options_async(
        self,
        request: mssp_20161228_models.GetDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetDetailByIdResponse:
        """
        @summary Query Risk Details
        
        @param request: GetDetailByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDetailByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDetailById',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetDetailByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_detail_by_id(
        self,
        request: mssp_20161228_models.GetDetailByIdRequest,
    ) -> mssp_20161228_models.GetDetailByIdResponse:
        """
        @summary Query Risk Details
        
        @param request: GetDetailByIdRequest
        @return: GetDetailByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_detail_by_id_with_options(request, runtime)

    async def get_detail_by_id_async(
        self,
        request: mssp_20161228_models.GetDetailByIdRequest,
    ) -> mssp_20161228_models.GetDetailByIdResponse:
        """
        @summary Query Risk Details
        
        @param request: GetDetailByIdRequest
        @return: GetDetailByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_detail_by_id_with_options_async(request, runtime)

    def get_document_download_url_with_options(
        self,
        request: mssp_20161228_models.GetDocumentDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetDocumentDownloadUrlResponse:
        """
        @summary Single Service Report Download
        
        @param request: GetDocumentDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentDownloadUrl',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetDocumentDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_download_url_with_options_async(
        self,
        request: mssp_20161228_models.GetDocumentDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetDocumentDownloadUrlResponse:
        """
        @summary Single Service Report Download
        
        @param request: GetDocumentDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentDownloadUrl',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetDocumentDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_download_url(
        self,
        request: mssp_20161228_models.GetDocumentDownloadUrlRequest,
    ) -> mssp_20161228_models.GetDocumentDownloadUrlResponse:
        """
        @summary Single Service Report Download
        
        @param request: GetDocumentDownloadUrlRequest
        @return: GetDocumentDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_document_download_url_with_options(request, runtime)

    async def get_document_download_url_async(
        self,
        request: mssp_20161228_models.GetDocumentDownloadUrlRequest,
    ) -> mssp_20161228_models.GetDocumentDownloadUrlResponse:
        """
        @summary Single Service Report Download
        
        @param request: GetDocumentDownloadUrlRequest
        @return: GetDocumentDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_document_download_url_with_options_async(request, runtime)

    def get_document_page_with_options(
        self,
        request: mssp_20161228_models.GetDocumentPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetDocumentPageResponse:
        """
        @summary Service Report Query
        
        @param request: GetDocumentPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentPageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.delivered_by):
            body['DeliveredBy'] = request.delivered_by
        if not UtilClient.is_unset(request.document_name):
            body['DocumentName'] = request.document_name
        if not UtilClient.is_unset(request.document_type):
            body['DocumentType'] = request.document_type
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.report_type):
            body['ReportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentPage',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetDocumentPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_page_with_options_async(
        self,
        request: mssp_20161228_models.GetDocumentPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetDocumentPageResponse:
        """
        @summary Service Report Query
        
        @param request: GetDocumentPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentPageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.delivered_by):
            body['DeliveredBy'] = request.delivered_by
        if not UtilClient.is_unset(request.document_name):
            body['DocumentName'] = request.document_name
        if not UtilClient.is_unset(request.document_type):
            body['DocumentType'] = request.document_type
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.report_type):
            body['ReportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentPage',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetDocumentPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_page(
        self,
        request: mssp_20161228_models.GetDocumentPageRequest,
    ) -> mssp_20161228_models.GetDocumentPageResponse:
        """
        @summary Service Report Query
        
        @param request: GetDocumentPageRequest
        @return: GetDocumentPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_document_page_with_options(request, runtime)

    async def get_document_page_async(
        self,
        request: mssp_20161228_models.GetDocumentPageRequest,
    ) -> mssp_20161228_models.GetDocumentPageResponse:
        """
        @summary Service Report Query
        
        @param request: GetDocumentPageRequest
        @return: GetDocumentPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_document_page_with_options_async(request, runtime)

    def get_document_summary_with_options(
        self,
        request: mssp_20161228_models.GetDocumentSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetDocumentSummaryResponse:
        """
        @summary Service Report Home Page Statistics Acquisition
        
        @param request: GetDocumentSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.report_type):
            body['ReportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetDocumentSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_summary_with_options_async(
        self,
        request: mssp_20161228_models.GetDocumentSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetDocumentSummaryResponse:
        """
        @summary Service Report Home Page Statistics Acquisition
        
        @param request: GetDocumentSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.report_type):
            body['ReportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetDocumentSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_summary(
        self,
        request: mssp_20161228_models.GetDocumentSummaryRequest,
    ) -> mssp_20161228_models.GetDocumentSummaryResponse:
        """
        @summary Service Report Home Page Statistics Acquisition
        
        @param request: GetDocumentSummaryRequest
        @return: GetDocumentSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_document_summary_with_options(request, runtime)

    async def get_document_summary_async(
        self,
        request: mssp_20161228_models.GetDocumentSummaryRequest,
    ) -> mssp_20161228_models.GetDocumentSummaryResponse:
        """
        @summary Service Report Home Page Statistics Acquisition
        
        @param request: GetDocumentSummaryRequest
        @return: GetDocumentSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_document_summary_with_options_async(request, runtime)

    def get_recent_document_with_options(
        self,
        request: mssp_20161228_models.GetRecentDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetRecentDocumentResponse:
        """
        @summary Get Recently Uploaded Service Reports
        
        @param request: GetRecentDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRecentDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRecentDocument',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetRecentDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recent_document_with_options_async(
        self,
        request: mssp_20161228_models.GetRecentDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetRecentDocumentResponse:
        """
        @summary Get Recently Uploaded Service Reports
        
        @param request: GetRecentDocumentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRecentDocumentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRecentDocument',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetRecentDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recent_document(
        self,
        request: mssp_20161228_models.GetRecentDocumentRequest,
    ) -> mssp_20161228_models.GetRecentDocumentResponse:
        """
        @summary Get Recently Uploaded Service Reports
        
        @param request: GetRecentDocumentRequest
        @return: GetRecentDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_recent_document_with_options(request, runtime)

    async def get_recent_document_async(
        self,
        request: mssp_20161228_models.GetRecentDocumentRequest,
    ) -> mssp_20161228_models.GetRecentDocumentResponse:
        """
        @summary Get Recently Uploaded Service Reports
        
        @param request: GetRecentDocumentRequest
        @return: GetRecentDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_recent_document_with_options_async(request, runtime)

    def get_safety_cover_with_options(
        self,
        request: mssp_20161228_models.GetSafetyCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetSafetyCoverResponse:
        """
        @summary Get Safety Coverage
        
        @param request: GetSafetyCoverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSafetyCoverResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSafetyCover',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetSafetyCoverResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_safety_cover_with_options_async(
        self,
        request: mssp_20161228_models.GetSafetyCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetSafetyCoverResponse:
        """
        @summary Get Safety Coverage
        
        @param request: GetSafetyCoverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSafetyCoverResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSafetyCover',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetSafetyCoverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_safety_cover(
        self,
        request: mssp_20161228_models.GetSafetyCoverRequest,
    ) -> mssp_20161228_models.GetSafetyCoverResponse:
        """
        @summary Get Safety Coverage
        
        @param request: GetSafetyCoverRequest
        @return: GetSafetyCoverResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_safety_cover_with_options(request, runtime)

    async def get_safety_cover_async(
        self,
        request: mssp_20161228_models.GetSafetyCoverRequest,
    ) -> mssp_20161228_models.GetSafetyCoverResponse:
        """
        @summary Get Safety Coverage
        
        @param request: GetSafetyCoverRequest
        @return: GetSafetyCoverResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_safety_cover_with_options_async(request, runtime)

    def get_sow_list_with_options(
        self,
        request: mssp_20161228_models.GetSowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetSowListResponse:
        """
        @summary Get SOW List
        
        @param request: GetSowListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSowListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSowList',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetSowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sow_list_with_options_async(
        self,
        request: mssp_20161228_models.GetSowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetSowListResponse:
        """
        @summary Get SOW List
        
        @param request: GetSowListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSowListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSowList',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetSowListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sow_list(
        self,
        request: mssp_20161228_models.GetSowListRequest,
    ) -> mssp_20161228_models.GetSowListResponse:
        """
        @summary Get SOW List
        
        @param request: GetSowListRequest
        @return: GetSowListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sow_list_with_options(request, runtime)

    async def get_sow_list_async(
        self,
        request: mssp_20161228_models.GetSowListRequest,
    ) -> mssp_20161228_models.GetSowListResponse:
        """
        @summary Get SOW List
        
        @param request: GetSowListRequest
        @return: GetSowListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sow_list_with_options_async(request, runtime)

    def get_susp_event_page_with_options(
        self,
        request: mssp_20161228_models.GetSuspEventPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetSuspEventPageResponse:
        """
        @summary Alarm Disposal Query
        
        @param request: GetSuspEventPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSuspEventPageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_end_time):
            body['AlarmEndTime'] = request.alarm_end_time
        if not UtilClient.is_unset(request.alarm_start_time):
            body['AlarmStartTime'] = request.alarm_start_time
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSuspEventPage',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetSuspEventPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_susp_event_page_with_options_async(
        self,
        request: mssp_20161228_models.GetSuspEventPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetSuspEventPageResponse:
        """
        @summary Alarm Disposal Query
        
        @param request: GetSuspEventPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSuspEventPageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_end_time):
            body['AlarmEndTime'] = request.alarm_end_time
        if not UtilClient.is_unset(request.alarm_start_time):
            body['AlarmStartTime'] = request.alarm_start_time
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSuspEventPage',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetSuspEventPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_susp_event_page(
        self,
        request: mssp_20161228_models.GetSuspEventPageRequest,
    ) -> mssp_20161228_models.GetSuspEventPageResponse:
        """
        @summary Alarm Disposal Query
        
        @param request: GetSuspEventPageRequest
        @return: GetSuspEventPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_susp_event_page_with_options(request, runtime)

    async def get_susp_event_page_async(
        self,
        request: mssp_20161228_models.GetSuspEventPageRequest,
    ) -> mssp_20161228_models.GetSuspEventPageResponse:
        """
        @summary Alarm Disposal Query
        
        @param request: GetSuspEventPageRequest
        @return: GetSuspEventPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_susp_event_page_with_options_async(request, runtime)

    def get_susp_event_summary_with_options(
        self,
        request: mssp_20161228_models.GetSuspEventSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetSuspEventSummaryResponse:
        """
        @summary Get Alert Statistics
        
        @param request: GetSuspEventSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSuspEventSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSuspEventSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetSuspEventSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_susp_event_summary_with_options_async(
        self,
        request: mssp_20161228_models.GetSuspEventSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetSuspEventSummaryResponse:
        """
        @summary Get Alert Statistics
        
        @param request: GetSuspEventSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSuspEventSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSuspEventSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetSuspEventSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_susp_event_summary(
        self,
        request: mssp_20161228_models.GetSuspEventSummaryRequest,
    ) -> mssp_20161228_models.GetSuspEventSummaryResponse:
        """
        @summary Get Alert Statistics
        
        @param request: GetSuspEventSummaryRequest
        @return: GetSuspEventSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_susp_event_summary_with_options(request, runtime)

    async def get_susp_event_summary_async(
        self,
        request: mssp_20161228_models.GetSuspEventSummaryRequest,
    ) -> mssp_20161228_models.GetSuspEventSummaryResponse:
        """
        @summary Get Alert Statistics
        
        @param request: GetSuspEventSummaryRequest
        @return: GetSuspEventSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_susp_event_summary_with_options_async(request, runtime)

    def get_susp_page_summary_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetSuspPageSummaryResponse:
        """
        @summary Alarm Page Statistics
        
        @param request: GetSuspPageSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSuspPageSummaryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetSuspPageSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetSuspPageSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_susp_page_summary_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetSuspPageSummaryResponse:
        """
        @summary Alarm Page Statistics
        
        @param request: GetSuspPageSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSuspPageSummaryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetSuspPageSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetSuspPageSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_susp_page_summary(self) -> mssp_20161228_models.GetSuspPageSummaryResponse:
        """
        @summary Alarm Page Statistics
        
        @return: GetSuspPageSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_susp_page_summary_with_options(runtime)

    async def get_susp_page_summary_async(self) -> mssp_20161228_models.GetSuspPageSummaryResponse:
        """
        @summary Alarm Page Statistics
        
        @return: GetSuspPageSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_susp_page_summary_with_options_async(runtime)

    def get_user_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetUserStatusResponse:
        """
        @summary Query User Activation Status
        
        @param request: GetUserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetUserStatus',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetUserStatusResponse:
        """
        @summary Query User Activation Status
        
        @param request: GetUserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetUserStatus',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_status(self) -> mssp_20161228_models.GetUserStatusResponse:
        """
        @summary Query User Activation Status
        
        @return: GetUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_status_with_options(runtime)

    async def get_user_status_async(self) -> mssp_20161228_models.GetUserStatusResponse:
        """
        @summary Query User Activation Status
        
        @return: GetUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_status_with_options_async(runtime)

    def get_vul_item_page_with_options(
        self,
        request: mssp_20161228_models.GetVulItemPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetVulItemPageResponse:
        """
        @summary Risk Query
        
        @param request: GetVulItemPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVulItemPageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            body['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scan_type):
            body['ScanType'] = request.scan_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVulItemPage',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetVulItemPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vul_item_page_with_options_async(
        self,
        request: mssp_20161228_models.GetVulItemPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetVulItemPageResponse:
        """
        @summary Risk Query
        
        @param request: GetVulItemPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVulItemPageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            body['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scan_type):
            body['ScanType'] = request.scan_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVulItemPage',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetVulItemPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vul_item_page(
        self,
        request: mssp_20161228_models.GetVulItemPageRequest,
    ) -> mssp_20161228_models.GetVulItemPageResponse:
        """
        @summary Risk Query
        
        @param request: GetVulItemPageRequest
        @return: GetVulItemPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vul_item_page_with_options(request, runtime)

    async def get_vul_item_page_async(
        self,
        request: mssp_20161228_models.GetVulItemPageRequest,
    ) -> mssp_20161228_models.GetVulItemPageResponse:
        """
        @summary Risk Query
        
        @param request: GetVulItemPageRequest
        @return: GetVulItemPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vul_item_page_with_options_async(request, runtime)

    def get_vul_list_by_id_with_options(
        self,
        request: mssp_20161228_models.GetVulListByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetVulListByIdResponse:
        """
        @summary Query processed details
        
        @param request: GetVulListByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVulListByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            body['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.necessity):
            body['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.uuids):
            body['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVulListById',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetVulListByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vul_list_by_id_with_options_async(
        self,
        request: mssp_20161228_models.GetVulListByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetVulListByIdResponse:
        """
        @summary Query processed details
        
        @param request: GetVulListByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVulListByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            body['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.necessity):
            body['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.uuids):
            body['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVulListById',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetVulListByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vul_list_by_id(
        self,
        request: mssp_20161228_models.GetVulListByIdRequest,
    ) -> mssp_20161228_models.GetVulListByIdResponse:
        """
        @summary Query processed details
        
        @param request: GetVulListByIdRequest
        @return: GetVulListByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vul_list_by_id_with_options(request, runtime)

    async def get_vul_list_by_id_async(
        self,
        request: mssp_20161228_models.GetVulListByIdRequest,
    ) -> mssp_20161228_models.GetVulListByIdResponse:
        """
        @summary Query processed details
        
        @param request: GetVulListByIdRequest
        @return: GetVulListByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vul_list_by_id_with_options_async(request, runtime)

    def get_vul_page_summary_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetVulPageSummaryResponse:
        """
        @summary Risk Page Statistics
        
        @param request: GetVulPageSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVulPageSummaryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetVulPageSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetVulPageSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vul_page_summary_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetVulPageSummaryResponse:
        """
        @summary Risk Page Statistics
        
        @param request: GetVulPageSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVulPageSummaryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetVulPageSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetVulPageSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vul_page_summary(self) -> mssp_20161228_models.GetVulPageSummaryResponse:
        """
        @summary Risk Page Statistics
        
        @return: GetVulPageSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vul_page_summary_with_options(runtime)

    async def get_vul_page_summary_async(self) -> mssp_20161228_models.GetVulPageSummaryResponse:
        """
        @summary Risk Page Statistics
        
        @return: GetVulPageSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vul_page_summary_with_options_async(runtime)

    def get_vul_summary_with_options(
        self,
        request: mssp_20161228_models.GetVulSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetVulSummaryResponse:
        """
        @summary Get Risk Statistics
        
        @param request: GetVulSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVulSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVulSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetVulSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vul_summary_with_options_async(
        self,
        request: mssp_20161228_models.GetVulSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetVulSummaryResponse:
        """
        @summary Get Risk Statistics
        
        @param request: GetVulSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVulSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVulSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetVulSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vul_summary(
        self,
        request: mssp_20161228_models.GetVulSummaryRequest,
    ) -> mssp_20161228_models.GetVulSummaryResponse:
        """
        @summary Get Risk Statistics
        
        @param request: GetVulSummaryRequest
        @return: GetVulSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vul_summary_with_options(request, runtime)

    async def get_vul_summary_async(
        self,
        request: mssp_20161228_models.GetVulSummaryRequest,
    ) -> mssp_20161228_models.GetVulSummaryResponse:
        """
        @summary Get Risk Statistics
        
        @param request: GetVulSummaryRequest
        @return: GetVulSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vul_summary_with_options_async(request, runtime)

    def get_work_task_summary_with_options(
        self,
        request: mssp_20161228_models.GetWorkTaskSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetWorkTaskSummaryResponse:
        """
        @summary Get the First Line Work Order Statistics
        
        @param request: GetWorkTaskSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkTaskSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWorkTaskSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetWorkTaskSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_work_task_summary_with_options_async(
        self,
        request: mssp_20161228_models.GetWorkTaskSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.GetWorkTaskSummaryResponse:
        """
        @summary Get the First Line Work Order Statistics
        
        @param request: GetWorkTaskSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkTaskSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.date_type):
            body['DateType'] = request.date_type
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.susp_event_source):
            body['SuspEventSource'] = request.susp_event_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWorkTaskSummary',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.GetWorkTaskSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_work_task_summary(
        self,
        request: mssp_20161228_models.GetWorkTaskSummaryRequest,
    ) -> mssp_20161228_models.GetWorkTaskSummaryResponse:
        """
        @summary Get the First Line Work Order Statistics
        
        @param request: GetWorkTaskSummaryRequest
        @return: GetWorkTaskSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_work_task_summary_with_options(request, runtime)

    async def get_work_task_summary_async(
        self,
        request: mssp_20161228_models.GetWorkTaskSummaryRequest,
    ) -> mssp_20161228_models.GetWorkTaskSummaryResponse:
        """
        @summary Get the First Line Work Order Statistics
        
        @param request: GetWorkTaskSummaryRequest
        @return: GetWorkTaskSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_work_task_summary_with_options_async(request, runtime)

    def page_service_customer_with_options(
        self,
        request: mssp_20161228_models.PageServiceCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.PageServiceCustomerResponse:
        """
        @summary Service Customer Information Query
        
        @param request: PageServiceCustomerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageServiceCustomerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_status):
            body['AuthStatus'] = request.auth_status
        if not UtilClient.is_unset(request.cm_auth_status):
            body['CmAuthStatus'] = request.cm_auth_status
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.monitor_auth_status):
            body['MonitorAuthStatus'] = request.monitor_auth_status
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageServiceCustomer',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.PageServiceCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_service_customer_with_options_async(
        self,
        request: mssp_20161228_models.PageServiceCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.PageServiceCustomerResponse:
        """
        @summary Service Customer Information Query
        
        @param request: PageServiceCustomerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageServiceCustomerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_status):
            body['AuthStatus'] = request.auth_status
        if not UtilClient.is_unset(request.cm_auth_status):
            body['CmAuthStatus'] = request.cm_auth_status
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.monitor_auth_status):
            body['MonitorAuthStatus'] = request.monitor_auth_status
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageServiceCustomer',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.PageServiceCustomerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_service_customer(
        self,
        request: mssp_20161228_models.PageServiceCustomerRequest,
    ) -> mssp_20161228_models.PageServiceCustomerResponse:
        """
        @summary Service Customer Information Query
        
        @param request: PageServiceCustomerRequest
        @return: PageServiceCustomerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.page_service_customer_with_options(request, runtime)

    async def page_service_customer_async(
        self,
        request: mssp_20161228_models.PageServiceCustomerRequest,
    ) -> mssp_20161228_models.PageServiceCustomerResponse:
        """
        @summary Service Customer Information Query
        
        @param request: PageServiceCustomerRequest
        @return: PageServiceCustomerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.page_service_customer_with_options_async(request, runtime)

    def send_custom_event_with_options(
        self,
        request: mssp_20161228_models.SendCustomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.SendCustomEventResponse:
        """
        @summary Send Custom Alert Event
        
        @param request: SendCustomEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendCustomEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.customer_id):
            body['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.data_source):
            body['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.event_description):
            body['EventDescription'] = request.event_description
        if not UtilClient.is_unset(request.event_details):
            body['EventDetails'] = request.event_details
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.find_time):
            body['FindTime'] = request.find_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.is_send):
            body['IsSend'] = request.is_send
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.occurrence_time):
            body['OccurrenceTime'] = request.occurrence_time
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomEvent',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.SendCustomEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_custom_event_with_options_async(
        self,
        request: mssp_20161228_models.SendCustomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mssp_20161228_models.SendCustomEventResponse:
        """
        @summary Send Custom Alert Event
        
        @param request: SendCustomEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendCustomEventResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.customer_id):
            body['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.data_source):
            body['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.event_description):
            body['EventDescription'] = request.event_description
        if not UtilClient.is_unset(request.event_details):
            body['EventDetails'] = request.event_details
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.find_time):
            body['FindTime'] = request.find_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.is_send):
            body['IsSend'] = request.is_send
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.occurrence_time):
            body['OccurrenceTime'] = request.occurrence_time
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomEvent',
            version='2016-12-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mssp_20161228_models.SendCustomEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_custom_event(
        self,
        request: mssp_20161228_models.SendCustomEventRequest,
    ) -> mssp_20161228_models.SendCustomEventResponse:
        """
        @summary Send Custom Alert Event
        
        @param request: SendCustomEventRequest
        @return: SendCustomEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_custom_event_with_options(request, runtime)

    async def send_custom_event_async(
        self,
        request: mssp_20161228_models.SendCustomEventRequest,
    ) -> mssp_20161228_models.SendCustomEventResponse:
        """
        @summary Send Custom Alert Event
        
        @param request: SendCustomEventRequest
        @return: SendCustomEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_custom_event_with_options_async(request, runtime)
