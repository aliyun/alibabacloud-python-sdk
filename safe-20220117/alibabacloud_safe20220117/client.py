# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_safe20220117 import models as safe_20220117_models
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
        self._endpoint = self.get_endpoint('safe', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_block_with_options(
        self,
        request: safe_20220117_models.CancelBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.CancelBlockResponse:
        """
        @summary 取消封网接口
        
        @param request: CancelBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelBlockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.block_id):
            body['BlockId'] = request.block_id
        if not UtilClient.is_unset(request.cancel_block_desc):
            body['CancelBLockDesc'] = request.cancel_block_desc
        if not UtilClient.is_unset(request.create_emp_id):
            body['CreateEmpId'] = request.create_emp_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelBlock',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.CancelBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_block_with_options_async(
        self,
        request: safe_20220117_models.CancelBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.CancelBlockResponse:
        """
        @summary 取消封网接口
        
        @param request: CancelBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelBlockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.block_id):
            body['BlockId'] = request.block_id
        if not UtilClient.is_unset(request.cancel_block_desc):
            body['CancelBLockDesc'] = request.cancel_block_desc
        if not UtilClient.is_unset(request.create_emp_id):
            body['CreateEmpId'] = request.create_emp_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelBlock',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.CancelBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_block(
        self,
        request: safe_20220117_models.CancelBlockRequest,
    ) -> safe_20220117_models.CancelBlockResponse:
        """
        @summary 取消封网接口
        
        @param request: CancelBlockRequest
        @return: CancelBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_block_with_options(request, runtime)

    async def cancel_block_async(
        self,
        request: safe_20220117_models.CancelBlockRequest,
    ) -> safe_20220117_models.CancelBlockResponse:
        """
        @summary 取消封网接口
        
        @param request: CancelBlockRequest
        @return: CancelBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_block_with_options_async(request, runtime)

    def change_cancel_with_options(
        self,
        request: safe_20220117_models.ChangeCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.ChangeCancelResponse:
        """
        @summary 变更取消
        
        @param request: ChangeCancelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeCancelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeCancel',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.ChangeCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_cancel_with_options_async(
        self,
        request: safe_20220117_models.ChangeCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.ChangeCancelResponse:
        """
        @summary 变更取消
        
        @param request: ChangeCancelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeCancelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeCancel',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.ChangeCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_cancel(
        self,
        request: safe_20220117_models.ChangeCancelRequest,
    ) -> safe_20220117_models.ChangeCancelResponse:
        """
        @summary 变更取消
        
        @param request: ChangeCancelRequest
        @return: ChangeCancelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_cancel_with_options(request, runtime)

    async def change_cancel_async(
        self,
        request: safe_20220117_models.ChangeCancelRequest,
    ) -> safe_20220117_models.ChangeCancelResponse:
        """
        @summary 变更取消
        
        @param request: ChangeCancelRequest
        @return: ChangeCancelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_cancel_with_options_async(request, runtime)

    def change_check_with_options(
        self,
        tmp_req: safe_20220117_models.ChangeCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.ChangeCheckResponse:
        """
        @summary 安全变更check
        
        @param tmp_req: ChangeCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeCheckResponse
        """
        UtilClient.validate_model(tmp_req)
        request = safe_20220117_models.ChangeCheckShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.damaged_change_notices):
            request.damaged_change_notices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.damaged_change_notices, 'DamagedChangeNotices', 'json')
        body = {}
        if not UtilClient.is_unset(request.affect_customer):
            body['AffectCustomer'] = request.affect_customer
        body_flat = {}
        if not UtilClient.is_unset(request.approve_flow_param):
            body_flat['ApproveFlowParam'] = request.approve_flow_param
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.bg_custom_template_extra_dto):
            body_flat['BgCustomTemplateExtraDTO'] = request.bg_custom_template_extra_dto
        if not UtilClient.is_unset(request.bg_vid):
            body['BgVid'] = request.bg_vid
        if not UtilClient.is_unset(request.block_infos):
            body['BlockInfos'] = request.block_infos
        if not UtilClient.is_unset(request.call_back_info):
            body_flat['CallBackInfo'] = request.call_back_info
        if not UtilClient.is_unset(request.change_data_type):
            body['ChangeDataType'] = request.change_data_type
        if not UtilClient.is_unset(request.change_desc):
            body['ChangeDesc'] = request.change_desc
        if not UtilClient.is_unset(request.change_end_time):
            body['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_env):
            body['ChangeEnv'] = request.change_env
        if not UtilClient.is_unset(request.change_items):
            body['ChangeItems'] = request.change_items
        if not UtilClient.is_unset(request.change_object):
            body['ChangeObject'] = request.change_object
        if not UtilClient.is_unset(request.change_opt_sub_type):
            body['ChangeOptSubType'] = request.change_opt_sub_type
        if not UtilClient.is_unset(request.change_opt_type):
            body['ChangeOptType'] = request.change_opt_type
        if not UtilClient.is_unset(request.change_reason):
            body['ChangeReason'] = request.change_reason
        if not UtilClient.is_unset(request.change_rmarks):
            body['ChangeRmarks'] = request.change_rmarks
        if not UtilClient.is_unset(request.change_schemes):
            body['ChangeSchemes'] = request.change_schemes
        if not UtilClient.is_unset(request.change_start_time):
            body['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.change_sub_type_desc):
            body['ChangeSubTypeDesc'] = request.change_sub_type_desc
        if not UtilClient.is_unset(request.change_system):
            body['ChangeSystem'] = request.change_system
        if not UtilClient.is_unset(request.change_times):
            body['ChangeTimes'] = request.change_times
        if not UtilClient.is_unset(request.change_title):
            body['ChangeTitle'] = request.change_title
        if not UtilClient.is_unset(request.change_validation):
            body['ChangeValidation'] = request.change_validation
        if not UtilClient.is_unset(request.creator_emp_id):
            body['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.damaged_change_notices_shrink):
            body['DamagedChangeNotices'] = request.damaged_change_notices_shrink
        if not UtilClient.is_unset(request.executor_emp_id):
            body['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.follower):
            body['Follower'] = request.follower
        if not UtilClient.is_unset(request.gray_status):
            body['GrayStatus'] = request.gray_status
        if not UtilClient.is_unset(request.harm_change_notice_enum):
            body['HarmChangeNoticeEnum'] = request.harm_change_notice_enum
        if not UtilClient.is_unset(request.incidence):
            body['Incidence'] = request.incidence
        if not UtilClient.is_unset(request.influence_info):
            body_flat['InfluenceInfo'] = request.influence_info
        if not UtilClient.is_unset(request.instance):
            body_flat['Instance'] = request.instance
        if not UtilClient.is_unset(request.need_modify_doc):
            body['NeedModifyDoc'] = request.need_modify_doc
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.release_package_infos):
            body['ReleasePackageInfos'] = request.release_package_infos
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.reuse_source_order_id):
            body['ReuseSourceOrderId'] = request.reuse_source_order_id
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.rollback):
            body['Rollback'] = request.rollback
        if not UtilClient.is_unset(request.source_name):
            body['SourceName'] = request.source_name
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.white_type):
            body['WhiteType'] = request.white_type
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeCheck',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.ChangeCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_check_with_options_async(
        self,
        tmp_req: safe_20220117_models.ChangeCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.ChangeCheckResponse:
        """
        @summary 安全变更check
        
        @param tmp_req: ChangeCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeCheckResponse
        """
        UtilClient.validate_model(tmp_req)
        request = safe_20220117_models.ChangeCheckShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.damaged_change_notices):
            request.damaged_change_notices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.damaged_change_notices, 'DamagedChangeNotices', 'json')
        body = {}
        if not UtilClient.is_unset(request.affect_customer):
            body['AffectCustomer'] = request.affect_customer
        body_flat = {}
        if not UtilClient.is_unset(request.approve_flow_param):
            body_flat['ApproveFlowParam'] = request.approve_flow_param
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.bg_custom_template_extra_dto):
            body_flat['BgCustomTemplateExtraDTO'] = request.bg_custom_template_extra_dto
        if not UtilClient.is_unset(request.bg_vid):
            body['BgVid'] = request.bg_vid
        if not UtilClient.is_unset(request.block_infos):
            body['BlockInfos'] = request.block_infos
        if not UtilClient.is_unset(request.call_back_info):
            body_flat['CallBackInfo'] = request.call_back_info
        if not UtilClient.is_unset(request.change_data_type):
            body['ChangeDataType'] = request.change_data_type
        if not UtilClient.is_unset(request.change_desc):
            body['ChangeDesc'] = request.change_desc
        if not UtilClient.is_unset(request.change_end_time):
            body['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_env):
            body['ChangeEnv'] = request.change_env
        if not UtilClient.is_unset(request.change_items):
            body['ChangeItems'] = request.change_items
        if not UtilClient.is_unset(request.change_object):
            body['ChangeObject'] = request.change_object
        if not UtilClient.is_unset(request.change_opt_sub_type):
            body['ChangeOptSubType'] = request.change_opt_sub_type
        if not UtilClient.is_unset(request.change_opt_type):
            body['ChangeOptType'] = request.change_opt_type
        if not UtilClient.is_unset(request.change_reason):
            body['ChangeReason'] = request.change_reason
        if not UtilClient.is_unset(request.change_rmarks):
            body['ChangeRmarks'] = request.change_rmarks
        if not UtilClient.is_unset(request.change_schemes):
            body['ChangeSchemes'] = request.change_schemes
        if not UtilClient.is_unset(request.change_start_time):
            body['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.change_sub_type_desc):
            body['ChangeSubTypeDesc'] = request.change_sub_type_desc
        if not UtilClient.is_unset(request.change_system):
            body['ChangeSystem'] = request.change_system
        if not UtilClient.is_unset(request.change_times):
            body['ChangeTimes'] = request.change_times
        if not UtilClient.is_unset(request.change_title):
            body['ChangeTitle'] = request.change_title
        if not UtilClient.is_unset(request.change_validation):
            body['ChangeValidation'] = request.change_validation
        if not UtilClient.is_unset(request.creator_emp_id):
            body['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.damaged_change_notices_shrink):
            body['DamagedChangeNotices'] = request.damaged_change_notices_shrink
        if not UtilClient.is_unset(request.executor_emp_id):
            body['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.follower):
            body['Follower'] = request.follower
        if not UtilClient.is_unset(request.gray_status):
            body['GrayStatus'] = request.gray_status
        if not UtilClient.is_unset(request.harm_change_notice_enum):
            body['HarmChangeNoticeEnum'] = request.harm_change_notice_enum
        if not UtilClient.is_unset(request.incidence):
            body['Incidence'] = request.incidence
        if not UtilClient.is_unset(request.influence_info):
            body_flat['InfluenceInfo'] = request.influence_info
        if not UtilClient.is_unset(request.instance):
            body_flat['Instance'] = request.instance
        if not UtilClient.is_unset(request.need_modify_doc):
            body['NeedModifyDoc'] = request.need_modify_doc
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.release_package_infos):
            body['ReleasePackageInfos'] = request.release_package_infos
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.reuse_source_order_id):
            body['ReuseSourceOrderId'] = request.reuse_source_order_id
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.rollback):
            body['Rollback'] = request.rollback
        if not UtilClient.is_unset(request.source_name):
            body['SourceName'] = request.source_name
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.white_type):
            body['WhiteType'] = request.white_type
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeCheck',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.ChangeCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_check(
        self,
        request: safe_20220117_models.ChangeCheckRequest,
    ) -> safe_20220117_models.ChangeCheckResponse:
        """
        @summary 安全变更check
        
        @param request: ChangeCheckRequest
        @return: ChangeCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_check_with_options(request, runtime)

    async def change_check_async(
        self,
        request: safe_20220117_models.ChangeCheckRequest,
    ) -> safe_20220117_models.ChangeCheckResponse:
        """
        @summary 安全变更check
        
        @param request: ChangeCheckRequest
        @return: ChangeCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_check_with_options_async(request, runtime)

    def change_end_with_options(
        self,
        request: safe_20220117_models.ChangeEndRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.ChangeEndResponse:
        """
        @summary 变更执行end
        
        @param request: ChangeEndRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeEndResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.change_end_time):
            query['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_result):
            query['ChangeResult'] = request.change_result
        if not UtilClient.is_unset(request.cur_batch_no):
            query['CurBatchNo'] = request.cur_batch_no
        if not UtilClient.is_unset(request.executor_emp_id):
            query['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.total_batch_no):
            query['TotalBatchNo'] = request.total_batch_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeEnd',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.ChangeEndResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_end_with_options_async(
        self,
        request: safe_20220117_models.ChangeEndRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.ChangeEndResponse:
        """
        @summary 变更执行end
        
        @param request: ChangeEndRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeEndResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.change_end_time):
            query['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_result):
            query['ChangeResult'] = request.change_result
        if not UtilClient.is_unset(request.cur_batch_no):
            query['CurBatchNo'] = request.cur_batch_no
        if not UtilClient.is_unset(request.executor_emp_id):
            query['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.total_batch_no):
            query['TotalBatchNo'] = request.total_batch_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeEnd',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.ChangeEndResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_end(
        self,
        request: safe_20220117_models.ChangeEndRequest,
    ) -> safe_20220117_models.ChangeEndResponse:
        """
        @summary 变更执行end
        
        @param request: ChangeEndRequest
        @return: ChangeEndResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_end_with_options(request, runtime)

    async def change_end_async(
        self,
        request: safe_20220117_models.ChangeEndRequest,
    ) -> safe_20220117_models.ChangeEndResponse:
        """
        @summary 变更执行end
        
        @param request: ChangeEndRequest
        @return: ChangeEndResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_end_with_options_async(request, runtime)

    def change_start_with_options(
        self,
        request: safe_20220117_models.ChangeStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.ChangeStartResponse:
        """
        @summary 变更执行start
        
        @param request: ChangeStartRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeStartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.change_end_time):
            query['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_object):
            query['ChangeObject'] = request.change_object
        if not UtilClient.is_unset(request.change_opt_type):
            query['ChangeOptType'] = request.change_opt_type
        if not UtilClient.is_unset(request.change_start_time):
            query['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.change_title):
            query['ChangeTitle'] = request.change_title
        if not UtilClient.is_unset(request.creator_emp_id):
            query['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.cur_batch_no):
            query['CurBatchNo'] = request.cur_batch_no
        if not UtilClient.is_unset(request.executor_emp_id):
            query['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.total_batch_no):
            query['TotalBatchNo'] = request.total_batch_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeStart',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.ChangeStartResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_start_with_options_async(
        self,
        request: safe_20220117_models.ChangeStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.ChangeStartResponse:
        """
        @summary 变更执行start
        
        @param request: ChangeStartRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeStartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.change_end_time):
            query['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_object):
            query['ChangeObject'] = request.change_object
        if not UtilClient.is_unset(request.change_opt_type):
            query['ChangeOptType'] = request.change_opt_type
        if not UtilClient.is_unset(request.change_start_time):
            query['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.change_title):
            query['ChangeTitle'] = request.change_title
        if not UtilClient.is_unset(request.creator_emp_id):
            query['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.cur_batch_no):
            query['CurBatchNo'] = request.cur_batch_no
        if not UtilClient.is_unset(request.executor_emp_id):
            query['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.total_batch_no):
            query['TotalBatchNo'] = request.total_batch_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeStart',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.ChangeStartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_start(
        self,
        request: safe_20220117_models.ChangeStartRequest,
    ) -> safe_20220117_models.ChangeStartResponse:
        """
        @summary 变更执行start
        
        @param request: ChangeStartRequest
        @return: ChangeStartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_start_with_options(request, runtime)

    async def change_start_async(
        self,
        request: safe_20220117_models.ChangeStartRequest,
    ) -> safe_20220117_models.ChangeStartResponse:
        """
        @summary 变更执行start
        
        @param request: ChangeStartRequest
        @return: ChangeStartResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_start_with_options_async(request, runtime)

    def create_block_with_options(
        self,
        request: safe_20220117_models.CreateBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.CreateBlockResponse:
        """
        @summary 三方创建封网接口
        
        @param request: CreateBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBlockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.approve_strategy_nodes):
            body_flat['ApproveStrategyNodes'] = request.approve_strategy_nodes
        if not UtilClient.is_unset(request.block_id):
            body['BlockId'] = request.block_id
        if not UtilClient.is_unset(request.director):
            body['Director'] = request.director
        if not UtilClient.is_unset(request.is_need_approve):
            body['IsNeedApprove'] = request.is_need_approve
        if not UtilClient.is_unset(request.is_recall):
            body['IsRecall'] = request.is_recall
        if not UtilClient.is_unset(request.is_template):
            body['IsTemplate'] = request.is_template
        if not UtilClient.is_unset(request.label_name):
            body['LabelName'] = request.label_name
        if not UtilClient.is_unset(request.notice_desc):
            body['NoticeDesc'] = request.notice_desc
        if not UtilClient.is_unset(request.notice_enclosure_infos):
            body_flat['NoticeEnclosureInfos'] = request.notice_enclosure_infos
        if not UtilClient.is_unset(request.notice_request_link):
            body['NoticeRequestLink'] = request.notice_request_link
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.scopes):
            body_flat['Scopes'] = request.scopes
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        if not UtilClient.is_unset(request.creator_emp_id):
            body['creatorEmpId'] = request.creator_emp_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBlock',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.CreateBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_block_with_options_async(
        self,
        request: safe_20220117_models.CreateBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.CreateBlockResponse:
        """
        @summary 三方创建封网接口
        
        @param request: CreateBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBlockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.approve_strategy_nodes):
            body_flat['ApproveStrategyNodes'] = request.approve_strategy_nodes
        if not UtilClient.is_unset(request.block_id):
            body['BlockId'] = request.block_id
        if not UtilClient.is_unset(request.director):
            body['Director'] = request.director
        if not UtilClient.is_unset(request.is_need_approve):
            body['IsNeedApprove'] = request.is_need_approve
        if not UtilClient.is_unset(request.is_recall):
            body['IsRecall'] = request.is_recall
        if not UtilClient.is_unset(request.is_template):
            body['IsTemplate'] = request.is_template
        if not UtilClient.is_unset(request.label_name):
            body['LabelName'] = request.label_name
        if not UtilClient.is_unset(request.notice_desc):
            body['NoticeDesc'] = request.notice_desc
        if not UtilClient.is_unset(request.notice_enclosure_infos):
            body_flat['NoticeEnclosureInfos'] = request.notice_enclosure_infos
        if not UtilClient.is_unset(request.notice_request_link):
            body['NoticeRequestLink'] = request.notice_request_link
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.scopes):
            body_flat['Scopes'] = request.scopes
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        if not UtilClient.is_unset(request.creator_emp_id):
            body['creatorEmpId'] = request.creator_emp_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBlock',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.CreateBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_block(
        self,
        request: safe_20220117_models.CreateBlockRequest,
    ) -> safe_20220117_models.CreateBlockResponse:
        """
        @summary 三方创建封网接口
        
        @param request: CreateBlockRequest
        @return: CreateBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_block_with_options(request, runtime)

    async def create_block_async(
        self,
        request: safe_20220117_models.CreateBlockRequest,
    ) -> safe_20220117_models.CreateBlockResponse:
        """
        @summary 三方创建封网接口
        
        @param request: CreateBlockRequest
        @return: CreateBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_block_with_options_async(request, runtime)

    def create_ma_yi_block_with_options(
        self,
        tmp_req: safe_20220117_models.CreateMaYiBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.CreateMaYiBlockResponse:
        """
        @summary 创建蚂蚁封网接口
        
        @param tmp_req: CreateMaYiBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMaYiBlockResponse
        """
        UtilClient.validate_model(tmp_req)
        request = safe_20220117_models.CreateMaYiBlockShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scope):
            request.scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scope, 'Scope', 'json')
        body = {}
        if not UtilClient.is_unset(request.block_id):
            body['BlockId'] = request.block_id
        if not UtilClient.is_unset(request.block_times):
            body['BlockTimes'] = request.block_times
        if not UtilClient.is_unset(request.block_type):
            body['BlockType'] = request.block_type
        if not UtilClient.is_unset(request.creator_emp_id):
            body['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.director):
            body['Director'] = request.director
        if not UtilClient.is_unset(request.fault_version):
            body['FaultVersion'] = request.fault_version
        if not UtilClient.is_unset(request.information):
            body['Information'] = request.information
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.scope_shrink):
            body['Scope'] = request.scope_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMaYiBlock',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.CreateMaYiBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ma_yi_block_with_options_async(
        self,
        tmp_req: safe_20220117_models.CreateMaYiBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.CreateMaYiBlockResponse:
        """
        @summary 创建蚂蚁封网接口
        
        @param tmp_req: CreateMaYiBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMaYiBlockResponse
        """
        UtilClient.validate_model(tmp_req)
        request = safe_20220117_models.CreateMaYiBlockShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scope):
            request.scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scope, 'Scope', 'json')
        body = {}
        if not UtilClient.is_unset(request.block_id):
            body['BlockId'] = request.block_id
        if not UtilClient.is_unset(request.block_times):
            body['BlockTimes'] = request.block_times
        if not UtilClient.is_unset(request.block_type):
            body['BlockType'] = request.block_type
        if not UtilClient.is_unset(request.creator_emp_id):
            body['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.director):
            body['Director'] = request.director
        if not UtilClient.is_unset(request.fault_version):
            body['FaultVersion'] = request.fault_version
        if not UtilClient.is_unset(request.information):
            body['Information'] = request.information
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.scope_shrink):
            body['Scope'] = request.scope_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMaYiBlock',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.CreateMaYiBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ma_yi_block(
        self,
        request: safe_20220117_models.CreateMaYiBlockRequest,
    ) -> safe_20220117_models.CreateMaYiBlockResponse:
        """
        @summary 创建蚂蚁封网接口
        
        @param request: CreateMaYiBlockRequest
        @return: CreateMaYiBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ma_yi_block_with_options(request, runtime)

    async def create_ma_yi_block_async(
        self,
        request: safe_20220117_models.CreateMaYiBlockRequest,
    ) -> safe_20220117_models.CreateMaYiBlockResponse:
        """
        @summary 创建蚂蚁封网接口
        
        @param request: CreateMaYiBlockRequest
        @return: CreateMaYiBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ma_yi_block_with_options_async(request, runtime)

    def create_operator_with_options(
        self,
        request: safe_20220117_models.CreateOperatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.CreateOperatorResponse:
        """
        @summary 创建操作类型
        
        @param request: CreateOperatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOperatorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.bg_object):
            body['BgObject'] = request.bg_object
        if not UtilClient.is_unset(request.bg_system):
            body['BgSystem'] = request.bg_system
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.cur_emp_id):
            body['CurEmpId'] = request.cur_emp_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.no_check):
            body['NoCheck'] = request.no_check
        if not UtilClient.is_unset(request.no_risk):
            body['NoRisk'] = request.no_risk
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOperator',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.CreateOperatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_operator_with_options_async(
        self,
        request: safe_20220117_models.CreateOperatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.CreateOperatorResponse:
        """
        @summary 创建操作类型
        
        @param request: CreateOperatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOperatorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.bg_object):
            body['BgObject'] = request.bg_object
        if not UtilClient.is_unset(request.bg_system):
            body['BgSystem'] = request.bg_system
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.cur_emp_id):
            body['CurEmpId'] = request.cur_emp_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.no_check):
            body['NoCheck'] = request.no_check
        if not UtilClient.is_unset(request.no_risk):
            body['NoRisk'] = request.no_risk
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOperator',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.CreateOperatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_operator(
        self,
        request: safe_20220117_models.CreateOperatorRequest,
    ) -> safe_20220117_models.CreateOperatorResponse:
        """
        @summary 创建操作类型
        
        @param request: CreateOperatorRequest
        @return: CreateOperatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_operator_with_options(request, runtime)

    async def create_operator_async(
        self,
        request: safe_20220117_models.CreateOperatorRequest,
    ) -> safe_20220117_models.CreateOperatorResponse:
        """
        @summary 创建操作类型
        
        @param request: CreateOperatorRequest
        @return: CreateOperatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_operator_with_options_async(request, runtime)

    def query_with_options(
        self,
        request: safe_20220117_models.QueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryResponse:
        """
        @summary 变更状态查询
        
        @param request: QueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.need_validate):
            query['NeedValidate'] = request.need_validate
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Query',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_with_options_async(
        self,
        request: safe_20220117_models.QueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryResponse:
        """
        @summary 变更状态查询
        
        @param request: QueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.need_validate):
            query['NeedValidate'] = request.need_validate
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Query',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query(
        self,
        request: safe_20220117_models.QueryRequest,
    ) -> safe_20220117_models.QueryResponse:
        """
        @summary 变更状态查询
        
        @param request: QueryRequest
        @return: QueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_with_options(request, runtime)

    async def query_async(
        self,
        request: safe_20220117_models.QueryRequest,
    ) -> safe_20220117_models.QueryResponse:
        """
        @summary 变更状态查询
        
        @param request: QueryRequest
        @return: QueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_with_options_async(request, runtime)

    def query_approve_flow_with_options(
        self,
        request: safe_20220117_models.QueryApproveFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryApproveFlowResponse:
        """
        @summary 查询审批实例信息
        
        @param request: QueryApproveFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryApproveFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.stage):
            query['Stage'] = request.stage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryApproveFlow',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryApproveFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_approve_flow_with_options_async(
        self,
        request: safe_20220117_models.QueryApproveFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryApproveFlowResponse:
        """
        @summary 查询审批实例信息
        
        @param request: QueryApproveFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryApproveFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.stage):
            query['Stage'] = request.stage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryApproveFlow',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryApproveFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_approve_flow(
        self,
        request: safe_20220117_models.QueryApproveFlowRequest,
    ) -> safe_20220117_models.QueryApproveFlowResponse:
        """
        @summary 查询审批实例信息
        
        @param request: QueryApproveFlowRequest
        @return: QueryApproveFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_approve_flow_with_options(request, runtime)

    async def query_approve_flow_async(
        self,
        request: safe_20220117_models.QueryApproveFlowRequest,
    ) -> safe_20220117_models.QueryApproveFlowResponse:
        """
        @summary 查询审批实例信息
        
        @param request: QueryApproveFlowRequest
        @return: QueryApproveFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_approve_flow_with_options_async(request, runtime)

    def query_block_event_with_options(
        self,
        request: safe_20220117_models.QueryBlockEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryBlockEventResponse:
        """
        @summary 查封网事件
        
        @param request: QueryBlockEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryBlockEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.bg_system_name):
            body['BgSystemName'] = request.bg_system_name
        if not UtilClient.is_unset(request.block_harm):
            body['BlockHarm'] = request.block_harm
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.dept_no):
            body['DeptNo'] = request.dept_no
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_rule):
            body['NeedRule'] = request.need_rule
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.product_codes):
            body['ProductCodes'] = request.product_codes
        if not UtilClient.is_unset(request.region_reqs):
            body['RegionReqs'] = request.region_reqs
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryBlockEvent',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryBlockEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_block_event_with_options_async(
        self,
        request: safe_20220117_models.QueryBlockEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryBlockEventResponse:
        """
        @summary 查封网事件
        
        @param request: QueryBlockEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryBlockEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.bg_system_name):
            body['BgSystemName'] = request.bg_system_name
        if not UtilClient.is_unset(request.block_harm):
            body['BlockHarm'] = request.block_harm
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.dept_no):
            body['DeptNo'] = request.dept_no
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_rule):
            body['NeedRule'] = request.need_rule
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.product_codes):
            body['ProductCodes'] = request.product_codes
        if not UtilClient.is_unset(request.region_reqs):
            body['RegionReqs'] = request.region_reqs
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryBlockEvent',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryBlockEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_block_event(
        self,
        request: safe_20220117_models.QueryBlockEventRequest,
    ) -> safe_20220117_models.QueryBlockEventResponse:
        """
        @summary 查封网事件
        
        @param request: QueryBlockEventRequest
        @return: QueryBlockEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_block_event_with_options(request, runtime)

    async def query_block_event_async(
        self,
        request: safe_20220117_models.QueryBlockEventRequest,
    ) -> safe_20220117_models.QueryBlockEventResponse:
        """
        @summary 查封网事件
        
        @param request: QueryBlockEventRequest
        @return: QueryBlockEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_block_event_with_options_async(request, runtime)

    def query_change_info_with_options(
        self,
        request: safe_20220117_models.QueryChangeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryChangeInfoResponse:
        """
        @summary 变更单详情
        
        @param request: QueryChangeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChangeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.az):
            body['Az'] = request.az
        if not UtilClient.is_unset(request.bg_vid):
            body['BgVid'] = request.bg_vid
        if not UtilClient.is_unset(request.bu_id):
            body['BuId'] = request.bu_id
        if not UtilClient.is_unset(request.change_system):
            body['ChangeSystem'] = request.change_system
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        body_flat = {}
        if not UtilClient.is_unset(request.level_tree):
            body_flat['LevelTree'] = request.level_tree
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryChangeInfo',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryChangeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_change_info_with_options_async(
        self,
        request: safe_20220117_models.QueryChangeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryChangeInfoResponse:
        """
        @summary 变更单详情
        
        @param request: QueryChangeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChangeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.az):
            body['Az'] = request.az
        if not UtilClient.is_unset(request.bg_vid):
            body['BgVid'] = request.bg_vid
        if not UtilClient.is_unset(request.bu_id):
            body['BuId'] = request.bu_id
        if not UtilClient.is_unset(request.change_system):
            body['ChangeSystem'] = request.change_system
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        body_flat = {}
        if not UtilClient.is_unset(request.level_tree):
            body_flat['LevelTree'] = request.level_tree
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryChangeInfo',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryChangeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_change_info(
        self,
        request: safe_20220117_models.QueryChangeInfoRequest,
    ) -> safe_20220117_models.QueryChangeInfoResponse:
        """
        @summary 变更单详情
        
        @param request: QueryChangeInfoRequest
        @return: QueryChangeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_change_info_with_options(request, runtime)

    async def query_change_info_async(
        self,
        request: safe_20220117_models.QueryChangeInfoRequest,
    ) -> safe_20220117_models.QueryChangeInfoResponse:
        """
        @summary 变更单详情
        
        @param request: QueryChangeInfoRequest
        @return: QueryChangeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_change_info_with_options_async(request, runtime)

    def query_check_info_with_options(
        self,
        request: safe_20220117_models.QueryCheckInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryCheckInfoResponse:
        """
        @summary 查询检测详情接口
        
        @param request: QueryCheckInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCheckInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCheckInfo',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryCheckInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_check_info_with_options_async(
        self,
        request: safe_20220117_models.QueryCheckInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryCheckInfoResponse:
        """
        @summary 查询检测详情接口
        
        @param request: QueryCheckInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCheckInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCheckInfo',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryCheckInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_check_info(
        self,
        request: safe_20220117_models.QueryCheckInfoRequest,
    ) -> safe_20220117_models.QueryCheckInfoResponse:
        """
        @summary 查询检测详情接口
        
        @param request: QueryCheckInfoRequest
        @return: QueryCheckInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_check_info_with_options(request, runtime)

    async def query_check_info_async(
        self,
        request: safe_20220117_models.QueryCheckInfoRequest,
    ) -> safe_20220117_models.QueryCheckInfoResponse:
        """
        @summary 查询检测详情接口
        
        @param request: QueryCheckInfoRequest
        @return: QueryCheckInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_check_info_with_options_async(request, runtime)

    def query_customer_with_options(
        self,
        request: safe_20220117_models.QueryCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryCustomerResponse:
        """
        @summary 查询敏感客户
        
        @param request: QueryCustomerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCustomerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCustomer',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_customer_with_options_async(
        self,
        request: safe_20220117_models.QueryCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryCustomerResponse:
        """
        @summary 查询敏感客户
        
        @param request: QueryCustomerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCustomerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCustomer',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryCustomerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_customer(
        self,
        request: safe_20220117_models.QueryCustomerRequest,
    ) -> safe_20220117_models.QueryCustomerResponse:
        """
        @summary 查询敏感客户
        
        @param request: QueryCustomerRequest
        @return: QueryCustomerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_customer_with_options(request, runtime)

    async def query_customer_async(
        self,
        request: safe_20220117_models.QueryCustomerRequest,
    ) -> safe_20220117_models.QueryCustomerResponse:
        """
        @summary 查询敏感客户
        
        @param request: QueryCustomerRequest
        @return: QueryCustomerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_customer_with_options_async(request, runtime)

    def query_execute_info_with_options(
        self,
        request: safe_20220117_models.QueryExecuteInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryExecuteInfoResponse:
        """
        @summary 执行单详情
        
        @param request: QueryExecuteInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryExecuteInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.az):
            body['Az'] = request.az
        if not UtilClient.is_unset(request.bg_vid):
            body['BgVid'] = request.bg_vid
        if not UtilClient.is_unset(request.bu_id):
            body['BuId'] = request.bu_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ex_vid):
            body['ExVid'] = request.ex_vid
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        body_flat = {}
        if not UtilClient.is_unset(request.level_tree):
            body_flat['LevelTree'] = request.level_tree
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryExecuteInfo',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryExecuteInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_execute_info_with_options_async(
        self,
        request: safe_20220117_models.QueryExecuteInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryExecuteInfoResponse:
        """
        @summary 执行单详情
        
        @param request: QueryExecuteInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryExecuteInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.az):
            body['Az'] = request.az
        if not UtilClient.is_unset(request.bg_vid):
            body['BgVid'] = request.bg_vid
        if not UtilClient.is_unset(request.bu_id):
            body['BuId'] = request.bu_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ex_vid):
            body['ExVid'] = request.ex_vid
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        body_flat = {}
        if not UtilClient.is_unset(request.level_tree):
            body_flat['LevelTree'] = request.level_tree
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryExecuteInfo',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryExecuteInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_execute_info(
        self,
        request: safe_20220117_models.QueryExecuteInfoRequest,
    ) -> safe_20220117_models.QueryExecuteInfoResponse:
        """
        @summary 执行单详情
        
        @param request: QueryExecuteInfoRequest
        @return: QueryExecuteInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_execute_info_with_options(request, runtime)

    async def query_execute_info_async(
        self,
        request: safe_20220117_models.QueryExecuteInfoRequest,
    ) -> safe_20220117_models.QueryExecuteInfoResponse:
        """
        @summary 执行单详情
        
        @param request: QueryExecuteInfoRequest
        @return: QueryExecuteInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_execute_info_with_options_async(request, runtime)

    def query_inner_product_info_with_options(
        self,
        request: safe_20220117_models.QueryInnerProductInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryInnerProductInfoResponse:
        """
        @summary 查询内部产品接口
        
        @param request: QueryInnerProductInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInnerProductInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInnerProductInfo',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryInnerProductInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_inner_product_info_with_options_async(
        self,
        request: safe_20220117_models.QueryInnerProductInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryInnerProductInfoResponse:
        """
        @summary 查询内部产品接口
        
        @param request: QueryInnerProductInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInnerProductInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInnerProductInfo',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryInnerProductInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_inner_product_info(
        self,
        request: safe_20220117_models.QueryInnerProductInfoRequest,
    ) -> safe_20220117_models.QueryInnerProductInfoResponse:
        """
        @summary 查询内部产品接口
        
        @param request: QueryInnerProductInfoRequest
        @return: QueryInnerProductInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_inner_product_info_with_options(request, runtime)

    async def query_inner_product_info_async(
        self,
        request: safe_20220117_models.QueryInnerProductInfoRequest,
    ) -> safe_20220117_models.QueryInnerProductInfoResponse:
        """
        @summary 查询内部产品接口
        
        @param request: QueryInnerProductInfoRequest
        @return: QueryInnerProductInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_inner_product_info_with_options_async(request, runtime)

    def query_region_az_with_options(
        self,
        request: safe_20220117_models.QueryRegionAzRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryRegionAzResponse:
        """
        @param request: QueryRegionAzRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRegionAzResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRegionAz',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryRegionAzResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_region_az_with_options_async(
        self,
        request: safe_20220117_models.QueryRegionAzRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.QueryRegionAzResponse:
        """
        @param request: QueryRegionAzRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRegionAzResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRegionAz',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.QueryRegionAzResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_region_az(
        self,
        request: safe_20220117_models.QueryRegionAzRequest,
    ) -> safe_20220117_models.QueryRegionAzResponse:
        """
        @param request: QueryRegionAzRequest
        @return: QueryRegionAzResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_region_az_with_options(request, runtime)

    async def query_region_az_async(
        self,
        request: safe_20220117_models.QueryRegionAzRequest,
    ) -> safe_20220117_models.QueryRegionAzResponse:
        """
        @param request: QueryRegionAzRequest
        @return: QueryRegionAzResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_region_az_with_options_async(request, runtime)

    def safe_change_cancel_with_options(
        self,
        request: safe_20220117_models.SafeChangeCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeCancelResponse:
        """
        @summary 变更取消接口
        
        @param request: SafeChangeCancelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeCancelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.bg_vid):
            body['BgVid'] = request.bg_vid
        if not UtilClient.is_unset(request.operate_emp_no):
            body['OperateEmpNo'] = request.operate_emp_no
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeCancel',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def safe_change_cancel_with_options_async(
        self,
        request: safe_20220117_models.SafeChangeCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeCancelResponse:
        """
        @summary 变更取消接口
        
        @param request: SafeChangeCancelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeCancelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.bg_vid):
            body['BgVid'] = request.bg_vid
        if not UtilClient.is_unset(request.operate_emp_no):
            body['OperateEmpNo'] = request.operate_emp_no
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeCancel',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def safe_change_cancel(
        self,
        request: safe_20220117_models.SafeChangeCancelRequest,
    ) -> safe_20220117_models.SafeChangeCancelResponse:
        """
        @summary 变更取消接口
        
        @param request: SafeChangeCancelRequest
        @return: SafeChangeCancelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.safe_change_cancel_with_options(request, runtime)

    async def safe_change_cancel_async(
        self,
        request: safe_20220117_models.SafeChangeCancelRequest,
    ) -> safe_20220117_models.SafeChangeCancelResponse:
        """
        @summary 变更取消接口
        
        @param request: SafeChangeCancelRequest
        @return: SafeChangeCancelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.safe_change_cancel_with_options_async(request, runtime)

    def safe_change_check_with_options(
        self,
        tmp_req: safe_20220117_models.SafeChangeCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeCheckResponse:
        """
        @summary 变更check接口
        
        @param tmp_req: SafeChangeCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeCheckResponse
        """
        UtilClient.validate_model(tmp_req)
        request = safe_20220117_models.SafeChangeCheckShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.harm_notice_combine_param):
            request.harm_notice_combine_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.harm_notice_combine_param, 'HarmNoticeCombineParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.checker):
            query['Checker'] = request.checker
        if not UtilClient.is_unset(request.harm_change_notice_enum):
            query['HarmChangeNoticeEnum'] = request.harm_change_notice_enum
        body = {}
        if not UtilClient.is_unset(request.affect_customer):
            body['AffectCustomer'] = request.affect_customer
        body_flat = {}
        if not UtilClient.is_unset(request.approve_flow_param):
            body_flat['ApproveFlowParam'] = request.approve_flow_param
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.bg_custom_template_extra_dto):
            body_flat['BgCustomTemplateExtraDTO'] = request.bg_custom_template_extra_dto
        if not UtilClient.is_unset(request.block_infos):
            body['BlockInfos'] = request.block_infos
        if not UtilClient.is_unset(request.call_back_info):
            body_flat['CallBackInfo'] = request.call_back_info
        if not UtilClient.is_unset(request.change_data_type):
            body['ChangeDataType'] = request.change_data_type
        if not UtilClient.is_unset(request.change_desc):
            body['ChangeDesc'] = request.change_desc
        if not UtilClient.is_unset(request.change_end_time):
            body['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_env):
            body['ChangeEnv'] = request.change_env
        if not UtilClient.is_unset(request.change_items):
            body['ChangeItems'] = request.change_items
        if not UtilClient.is_unset(request.change_object):
            body['ChangeObject'] = request.change_object
        if not UtilClient.is_unset(request.change_opt_sub_type):
            body['ChangeOptSubType'] = request.change_opt_sub_type
        if not UtilClient.is_unset(request.change_opt_type):
            body['ChangeOptType'] = request.change_opt_type
        if not UtilClient.is_unset(request.change_reason):
            body['ChangeReason'] = request.change_reason
        if not UtilClient.is_unset(request.change_rmarks):
            body['ChangeRmarks'] = request.change_rmarks
        if not UtilClient.is_unset(request.change_schemes):
            body['ChangeSchemes'] = request.change_schemes
        if not UtilClient.is_unset(request.change_start_time):
            body['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.change_sub_type_desc):
            body['ChangeSubTypeDesc'] = request.change_sub_type_desc
        if not UtilClient.is_unset(request.change_system):
            body['ChangeSystem'] = request.change_system
        if not UtilClient.is_unset(request.change_times):
            body['ChangeTimes'] = request.change_times
        if not UtilClient.is_unset(request.change_title):
            body['ChangeTitle'] = request.change_title
        if not UtilClient.is_unset(request.change_validation):
            body['ChangeValidation'] = request.change_validation
        if not UtilClient.is_unset(request.creator_emp_id):
            body['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.damaged_change_notices):
            body_flat['DamagedChangeNotices'] = request.damaged_change_notices
        if not UtilClient.is_unset(request.executor_emp_id):
            body['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.follower):
            body['Follower'] = request.follower
        if not UtilClient.is_unset(request.gray_status):
            body['GrayStatus'] = request.gray_status
        if not UtilClient.is_unset(request.harm_notice_combine_param_shrink):
            body['HarmNoticeCombineParam'] = request.harm_notice_combine_param_shrink
        if not UtilClient.is_unset(request.incidence):
            body['Incidence'] = request.incidence
        if not UtilClient.is_unset(request.influence_info):
            body_flat['InfluenceInfo'] = request.influence_info
        if not UtilClient.is_unset(request.instance):
            body_flat['Instance'] = request.instance
        if not UtilClient.is_unset(request.need_modify_doc):
            body['NeedModifyDoc'] = request.need_modify_doc
        if not UtilClient.is_unset(request.operate_emp_no):
            body['OperateEmpNo'] = request.operate_emp_no
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.release_package_infos):
            body['ReleasePackageInfos'] = request.release_package_infos
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.reuse_source_order_id):
            body['ReuseSourceOrderId'] = request.reuse_source_order_id
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.rollback):
            body['Rollback'] = request.rollback
        if not UtilClient.is_unset(request.source_name):
            body['SourceName'] = request.source_name
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.white_type):
            body['whiteType'] = request.white_type
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeCheck',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def safe_change_check_with_options_async(
        self,
        tmp_req: safe_20220117_models.SafeChangeCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeCheckResponse:
        """
        @summary 变更check接口
        
        @param tmp_req: SafeChangeCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeCheckResponse
        """
        UtilClient.validate_model(tmp_req)
        request = safe_20220117_models.SafeChangeCheckShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.harm_notice_combine_param):
            request.harm_notice_combine_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.harm_notice_combine_param, 'HarmNoticeCombineParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.checker):
            query['Checker'] = request.checker
        if not UtilClient.is_unset(request.harm_change_notice_enum):
            query['HarmChangeNoticeEnum'] = request.harm_change_notice_enum
        body = {}
        if not UtilClient.is_unset(request.affect_customer):
            body['AffectCustomer'] = request.affect_customer
        body_flat = {}
        if not UtilClient.is_unset(request.approve_flow_param):
            body_flat['ApproveFlowParam'] = request.approve_flow_param
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.bg_custom_template_extra_dto):
            body_flat['BgCustomTemplateExtraDTO'] = request.bg_custom_template_extra_dto
        if not UtilClient.is_unset(request.block_infos):
            body['BlockInfos'] = request.block_infos
        if not UtilClient.is_unset(request.call_back_info):
            body_flat['CallBackInfo'] = request.call_back_info
        if not UtilClient.is_unset(request.change_data_type):
            body['ChangeDataType'] = request.change_data_type
        if not UtilClient.is_unset(request.change_desc):
            body['ChangeDesc'] = request.change_desc
        if not UtilClient.is_unset(request.change_end_time):
            body['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_env):
            body['ChangeEnv'] = request.change_env
        if not UtilClient.is_unset(request.change_items):
            body['ChangeItems'] = request.change_items
        if not UtilClient.is_unset(request.change_object):
            body['ChangeObject'] = request.change_object
        if not UtilClient.is_unset(request.change_opt_sub_type):
            body['ChangeOptSubType'] = request.change_opt_sub_type
        if not UtilClient.is_unset(request.change_opt_type):
            body['ChangeOptType'] = request.change_opt_type
        if not UtilClient.is_unset(request.change_reason):
            body['ChangeReason'] = request.change_reason
        if not UtilClient.is_unset(request.change_rmarks):
            body['ChangeRmarks'] = request.change_rmarks
        if not UtilClient.is_unset(request.change_schemes):
            body['ChangeSchemes'] = request.change_schemes
        if not UtilClient.is_unset(request.change_start_time):
            body['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.change_sub_type_desc):
            body['ChangeSubTypeDesc'] = request.change_sub_type_desc
        if not UtilClient.is_unset(request.change_system):
            body['ChangeSystem'] = request.change_system
        if not UtilClient.is_unset(request.change_times):
            body['ChangeTimes'] = request.change_times
        if not UtilClient.is_unset(request.change_title):
            body['ChangeTitle'] = request.change_title
        if not UtilClient.is_unset(request.change_validation):
            body['ChangeValidation'] = request.change_validation
        if not UtilClient.is_unset(request.creator_emp_id):
            body['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.damaged_change_notices):
            body_flat['DamagedChangeNotices'] = request.damaged_change_notices
        if not UtilClient.is_unset(request.executor_emp_id):
            body['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.follower):
            body['Follower'] = request.follower
        if not UtilClient.is_unset(request.gray_status):
            body['GrayStatus'] = request.gray_status
        if not UtilClient.is_unset(request.harm_notice_combine_param_shrink):
            body['HarmNoticeCombineParam'] = request.harm_notice_combine_param_shrink
        if not UtilClient.is_unset(request.incidence):
            body['Incidence'] = request.incidence
        if not UtilClient.is_unset(request.influence_info):
            body_flat['InfluenceInfo'] = request.influence_info
        if not UtilClient.is_unset(request.instance):
            body_flat['Instance'] = request.instance
        if not UtilClient.is_unset(request.need_modify_doc):
            body['NeedModifyDoc'] = request.need_modify_doc
        if not UtilClient.is_unset(request.operate_emp_no):
            body['OperateEmpNo'] = request.operate_emp_no
        if not UtilClient.is_unset(request.product):
            body['Product'] = request.product
        if not UtilClient.is_unset(request.release_package_infos):
            body['ReleasePackageInfos'] = request.release_package_infos
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.reuse_source_order_id):
            body['ReuseSourceOrderId'] = request.reuse_source_order_id
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.rollback):
            body['Rollback'] = request.rollback
        if not UtilClient.is_unset(request.source_name):
            body['SourceName'] = request.source_name
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.white_type):
            body['whiteType'] = request.white_type
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeCheck',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def safe_change_check(
        self,
        request: safe_20220117_models.SafeChangeCheckRequest,
    ) -> safe_20220117_models.SafeChangeCheckResponse:
        """
        @summary 变更check接口
        
        @param request: SafeChangeCheckRequest
        @return: SafeChangeCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.safe_change_check_with_options(request, runtime)

    async def safe_change_check_async(
        self,
        request: safe_20220117_models.SafeChangeCheckRequest,
    ) -> safe_20220117_models.SafeChangeCheckResponse:
        """
        @summary 变更check接口
        
        @param request: SafeChangeCheckRequest
        @return: SafeChangeCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.safe_change_check_with_options_async(request, runtime)

    def safe_change_end_with_options(
        self,
        request: safe_20220117_models.SafeChangeEndRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeEndResponse:
        """
        @summary 变更End接口
        
        @param request: SafeChangeEndRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeEndResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.change_end_time):
            body['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_result):
            body['ChangeResult'] = request.change_result
        if not UtilClient.is_unset(request.cur_batch_no):
            body['CurBatchNo'] = request.cur_batch_no
        if not UtilClient.is_unset(request.executor_emp_id):
            body['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.total_batch_no):
            body['TotalBatchNo'] = request.total_batch_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeEnd',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeEndResponse(),
            self.call_api(params, req, runtime)
        )

    async def safe_change_end_with_options_async(
        self,
        request: safe_20220117_models.SafeChangeEndRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeEndResponse:
        """
        @summary 变更End接口
        
        @param request: SafeChangeEndRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeEndResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.change_end_time):
            body['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_result):
            body['ChangeResult'] = request.change_result
        if not UtilClient.is_unset(request.cur_batch_no):
            body['CurBatchNo'] = request.cur_batch_no
        if not UtilClient.is_unset(request.executor_emp_id):
            body['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.total_batch_no):
            body['TotalBatchNo'] = request.total_batch_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeEnd',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeEndResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def safe_change_end(
        self,
        request: safe_20220117_models.SafeChangeEndRequest,
    ) -> safe_20220117_models.SafeChangeEndResponse:
        """
        @summary 变更End接口
        
        @param request: SafeChangeEndRequest
        @return: SafeChangeEndResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.safe_change_end_with_options(request, runtime)

    async def safe_change_end_async(
        self,
        request: safe_20220117_models.SafeChangeEndRequest,
    ) -> safe_20220117_models.SafeChangeEndResponse:
        """
        @summary 变更End接口
        
        @param request: SafeChangeEndRequest
        @return: SafeChangeEndResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.safe_change_end_with_options_async(request, runtime)

    def safe_change_query_with_options(
        self,
        request: safe_20220117_models.SafeChangeQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeQueryResponse:
        """
        @summary 变更单查询
        
        @param request: SafeChangeQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.return_type):
            query['ReturnType'] = request.return_type
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.need_validate):
            body['NeedValidate'] = request.need_validate
        if not UtilClient.is_unset(request.query_type):
            body['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeQuery',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def safe_change_query_with_options_async(
        self,
        request: safe_20220117_models.SafeChangeQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeQueryResponse:
        """
        @summary 变更单查询
        
        @param request: SafeChangeQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.return_type):
            query['ReturnType'] = request.return_type
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.need_validate):
            body['NeedValidate'] = request.need_validate
        if not UtilClient.is_unset(request.query_type):
            body['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeQuery',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def safe_change_query(
        self,
        request: safe_20220117_models.SafeChangeQueryRequest,
    ) -> safe_20220117_models.SafeChangeQueryResponse:
        """
        @summary 变更单查询
        
        @param request: SafeChangeQueryRequest
        @return: SafeChangeQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.safe_change_query_with_options(request, runtime)

    async def safe_change_query_async(
        self,
        request: safe_20220117_models.SafeChangeQueryRequest,
    ) -> safe_20220117_models.SafeChangeQueryResponse:
        """
        @summary 变更单查询
        
        @param request: SafeChangeQueryRequest
        @return: SafeChangeQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.safe_change_query_with_options_async(request, runtime)

    def safe_change_query_approve_flow_with_options(
        self,
        request: safe_20220117_models.SafeChangeQueryApproveFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeQueryApproveFlowResponse:
        """
        @summary 查询审批实例信息
        
        @param request: SafeChangeQueryApproveFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeQueryApproveFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.stage):
            body['Stage'] = request.stage
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeQueryApproveFlow',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeQueryApproveFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def safe_change_query_approve_flow_with_options_async(
        self,
        request: safe_20220117_models.SafeChangeQueryApproveFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeQueryApproveFlowResponse:
        """
        @summary 查询审批实例信息
        
        @param request: SafeChangeQueryApproveFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeQueryApproveFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.stage):
            body['Stage'] = request.stage
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeQueryApproveFlow',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeQueryApproveFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def safe_change_query_approve_flow(
        self,
        request: safe_20220117_models.SafeChangeQueryApproveFlowRequest,
    ) -> safe_20220117_models.SafeChangeQueryApproveFlowResponse:
        """
        @summary 查询审批实例信息
        
        @param request: SafeChangeQueryApproveFlowRequest
        @return: SafeChangeQueryApproveFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.safe_change_query_approve_flow_with_options(request, runtime)

    async def safe_change_query_approve_flow_async(
        self,
        request: safe_20220117_models.SafeChangeQueryApproveFlowRequest,
    ) -> safe_20220117_models.SafeChangeQueryApproveFlowResponse:
        """
        @summary 查询审批实例信息
        
        @param request: SafeChangeQueryApproveFlowRequest
        @return: SafeChangeQueryApproveFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.safe_change_query_approve_flow_with_options_async(request, runtime)

    def safe_change_start_with_options(
        self,
        request: safe_20220117_models.SafeChangeStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeStartResponse:
        """
        @summary 变更Start接口
        
        @param request: SafeChangeStartRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeStartResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.change_end_time):
            body['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_object):
            body['ChangeObject'] = request.change_object
        if not UtilClient.is_unset(request.change_opt_type):
            body['ChangeOptType'] = request.change_opt_type
        if not UtilClient.is_unset(request.change_start_time):
            body['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.change_title):
            body['ChangeTitle'] = request.change_title
        if not UtilClient.is_unset(request.creator_emp_id):
            body['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.cur_batch_no):
            body['CurBatchNo'] = request.cur_batch_no
        if not UtilClient.is_unset(request.executor_emp_id):
            body['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.total_batch_no):
            body['TotalBatchNo'] = request.total_batch_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeStart',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeStartResponse(),
            self.call_api(params, req, runtime)
        )

    async def safe_change_start_with_options_async(
        self,
        request: safe_20220117_models.SafeChangeStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeStartResponse:
        """
        @summary 变更Start接口
        
        @param request: SafeChangeStartRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeStartResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.change_end_time):
            body['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_object):
            body['ChangeObject'] = request.change_object
        if not UtilClient.is_unset(request.change_opt_type):
            body['ChangeOptType'] = request.change_opt_type
        if not UtilClient.is_unset(request.change_start_time):
            body['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.change_title):
            body['ChangeTitle'] = request.change_title
        if not UtilClient.is_unset(request.creator_emp_id):
            body['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.cur_batch_no):
            body['CurBatchNo'] = request.cur_batch_no
        if not UtilClient.is_unset(request.executor_emp_id):
            body['ExecutorEmpId'] = request.executor_emp_id
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        if not UtilClient.is_unset(request.total_batch_no):
            body['TotalBatchNo'] = request.total_batch_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeStart',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeStartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def safe_change_start(
        self,
        request: safe_20220117_models.SafeChangeStartRequest,
    ) -> safe_20220117_models.SafeChangeStartResponse:
        """
        @summary 变更Start接口
        
        @param request: SafeChangeStartRequest
        @return: SafeChangeStartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.safe_change_start_with_options(request, runtime)

    async def safe_change_start_async(
        self,
        request: safe_20220117_models.SafeChangeStartRequest,
    ) -> safe_20220117_models.SafeChangeStartResponse:
        """
        @summary 变更Start接口
        
        @param request: SafeChangeStartRequest
        @return: SafeChangeStartResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.safe_change_start_with_options_async(request, runtime)

    def safe_change_start_approve_with_options(
        self,
        request: safe_20220117_models.SafeChangeStartApproveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeStartApproveResponse:
        """
        @summary 提交审批
        
        @param request: SafeChangeStartApproveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeStartApproveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.creator_emp_id):
            body['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeStartApprove',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeStartApproveResponse(),
            self.call_api(params, req, runtime)
        )

    async def safe_change_start_approve_with_options_async(
        self,
        request: safe_20220117_models.SafeChangeStartApproveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeChangeStartApproveResponse:
        """
        @summary 提交审批
        
        @param request: SafeChangeStartApproveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeChangeStartApproveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.creator_emp_id):
            body['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            body['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeChangeStartApprove',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeChangeStartApproveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def safe_change_start_approve(
        self,
        request: safe_20220117_models.SafeChangeStartApproveRequest,
    ) -> safe_20220117_models.SafeChangeStartApproveResponse:
        """
        @summary 提交审批
        
        @param request: SafeChangeStartApproveRequest
        @return: SafeChangeStartApproveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.safe_change_start_approve_with_options(request, runtime)

    async def safe_change_start_approve_async(
        self,
        request: safe_20220117_models.SafeChangeStartApproveRequest,
    ) -> safe_20220117_models.SafeChangeStartApproveResponse:
        """
        @summary 提交审批
        
        @param request: SafeChangeStartApproveRequest
        @return: SafeChangeStartApproveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.safe_change_start_approve_with_options_async(request, runtime)

    def safe_scope_data_with_options(
        self,
        request: safe_20220117_models.SafeScopeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeScopeDataResponse:
        """
        @summary 封网范围数据查询
        
        @param request: SafeScopeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeScopeDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.code_list):
            body['CodeList'] = request.code_list
        if not UtilClient.is_unset(request.factor):
            body['Factor'] = request.factor
        if not UtilClient.is_unset(request.group_by):
            body['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.id_list):
            body['IdList'] = request.id_list
        if not UtilClient.is_unset(request.item):
            body['Item'] = request.item
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_total_count):
            body['NeedTotalCount'] = request.need_total_count
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.parent_code):
            body['ParentCode'] = request.parent_code
        if not UtilClient.is_unset(request.parent_id):
            body['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_name_en):
            body['RegionNameEn'] = request.region_name_en
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            body['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeScopeData',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeScopeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def safe_scope_data_with_options_async(
        self,
        request: safe_20220117_models.SafeScopeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SafeScopeDataResponse:
        """
        @summary 封网范围数据查询
        
        @param request: SafeScopeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SafeScopeDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.code_list):
            body['CodeList'] = request.code_list
        if not UtilClient.is_unset(request.factor):
            body['Factor'] = request.factor
        if not UtilClient.is_unset(request.group_by):
            body['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.id_list):
            body['IdList'] = request.id_list
        if not UtilClient.is_unset(request.item):
            body['Item'] = request.item
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_total_count):
            body['NeedTotalCount'] = request.need_total_count
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.parent_code):
            body['ParentCode'] = request.parent_code
        if not UtilClient.is_unset(request.parent_id):
            body['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_name_en):
            body['RegionNameEn'] = request.region_name_en
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            body['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SafeScopeData',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SafeScopeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def safe_scope_data(
        self,
        request: safe_20220117_models.SafeScopeDataRequest,
    ) -> safe_20220117_models.SafeScopeDataResponse:
        """
        @summary 封网范围数据查询
        
        @param request: SafeScopeDataRequest
        @return: SafeScopeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.safe_scope_data_with_options(request, runtime)

    async def safe_scope_data_async(
        self,
        request: safe_20220117_models.SafeScopeDataRequest,
    ) -> safe_20220117_models.SafeScopeDataResponse:
        """
        @summary 封网范围数据查询
        
        @param request: SafeScopeDataRequest
        @return: SafeScopeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.safe_scope_data_with_options_async(request, runtime)

    def start_approve_with_options(
        self,
        request: safe_20220117_models.StartApproveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.StartApproveResponse:
        """
        @summary 提交审批
        
        @param request: StartApproveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartApproveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.creator_emp_id):
            query['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartApprove',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.StartApproveResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_approve_with_options_async(
        self,
        request: safe_20220117_models.StartApproveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.StartApproveResponse:
        """
        @summary 提交审批
        
        @param request: StartApproveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartApproveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            query['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.creator_emp_id):
            query['CreatorEmpId'] = request.creator_emp_id
        if not UtilClient.is_unset(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.req_timestamp):
            query['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.source_order_id):
            query['SourceOrderId'] = request.source_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartApprove',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.StartApproveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_approve(
        self,
        request: safe_20220117_models.StartApproveRequest,
    ) -> safe_20220117_models.StartApproveResponse:
        """
        @summary 提交审批
        
        @param request: StartApproveRequest
        @return: StartApproveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_approve_with_options(request, runtime)

    async def start_approve_async(
        self,
        request: safe_20220117_models.StartApproveRequest,
    ) -> safe_20220117_models.StartApproveResponse:
        """
        @summary 提交审批
        
        @param request: StartApproveRequest
        @return: StartApproveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_approve_with_options_async(request, runtime)

    def sync_product_with_options(
        self,
        request: safe_20220117_models.SyncProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SyncProductResponse:
        """
        @summary 同步产品接口
        
        @param request: SyncProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.sync_product_list):
            body['SyncProductList'] = request.sync_product_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncProduct',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SyncProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_product_with_options_async(
        self,
        request: safe_20220117_models.SyncProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220117_models.SyncProductResponse:
        """
        @summary 同步产品接口
        
        @param request: SyncProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_key):
            body['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_sign):
            body['AuthSign'] = request.auth_sign
        if not UtilClient.is_unset(request.req_timestamp):
            body['ReqTimestamp'] = request.req_timestamp
        if not UtilClient.is_unset(request.sync_product_list):
            body['SyncProductList'] = request.sync_product_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncProduct',
            version='2022-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220117_models.SyncProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_product(
        self,
        request: safe_20220117_models.SyncProductRequest,
    ) -> safe_20220117_models.SyncProductResponse:
        """
        @summary 同步产品接口
        
        @param request: SyncProductRequest
        @return: SyncProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_product_with_options(request, runtime)

    async def sync_product_async(
        self,
        request: safe_20220117_models.SyncProductRequest,
    ) -> safe_20220117_models.SyncProductResponse:
        """
        @summary 同步产品接口
        
        @param request: SyncProductRequest
        @return: SyncProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_product_with_options_async(request, runtime)
