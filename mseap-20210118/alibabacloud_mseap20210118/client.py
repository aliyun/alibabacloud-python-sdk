# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mseap20210118 import models as mseap_20210118_models
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
        self._endpoint = self.get_endpoint('mseap', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_license_with_options(
        self,
        request: mseap_20210118_models.ActivateLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.ActivateLicenseResponse:
        """
        @param request: ActivateLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.license_code):
            query['LicenseCode'] = request.license_code
        if not UtilClient.is_unset(request.license_no):
            query['LicenseNo'] = request.license_no
        if not UtilClient.is_unset(request.license_publisher):
            query['LicensePublisher'] = request.license_publisher
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateLicense',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.ActivateLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_license_with_options_async(
        self,
        request: mseap_20210118_models.ActivateLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.ActivateLicenseResponse:
        """
        @param request: ActivateLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.license_code):
            query['LicenseCode'] = request.license_code
        if not UtilClient.is_unset(request.license_no):
            query['LicenseNo'] = request.license_no
        if not UtilClient.is_unset(request.license_publisher):
            query['LicensePublisher'] = request.license_publisher
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateLicense',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.ActivateLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_license(
        self,
        request: mseap_20210118_models.ActivateLicenseRequest,
    ) -> mseap_20210118_models.ActivateLicenseResponse:
        """
        @param request: ActivateLicenseRequest
        @return: ActivateLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.activate_license_with_options(request, runtime)

    async def activate_license_async(
        self,
        request: mseap_20210118_models.ActivateLicenseRequest,
    ) -> mseap_20210118_models.ActivateLicenseResponse:
        """
        @param request: ActivateLicenseRequest
        @return: ActivateLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.activate_license_with_options_async(request, runtime)

    def callback_task_with_options(
        self,
        request: mseap_20210118_models.CallbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.CallbackTaskResponse:
        """
        @summary 任务回调
        
        @param request: CallbackTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CallbackTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.out_task_id):
            query['OutTaskId'] = request.out_task_id
        if not UtilClient.is_unset(request.principal_key):
            query['PrincipalKey'] = request.principal_key
        if not UtilClient.is_unset(request.task_data):
            query['TaskData'] = request.task_data
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CallbackTask',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.CallbackTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def callback_task_with_options_async(
        self,
        request: mseap_20210118_models.CallbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.CallbackTaskResponse:
        """
        @summary 任务回调
        
        @param request: CallbackTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CallbackTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.out_task_id):
            query['OutTaskId'] = request.out_task_id
        if not UtilClient.is_unset(request.principal_key):
            query['PrincipalKey'] = request.principal_key
        if not UtilClient.is_unset(request.task_data):
            query['TaskData'] = request.task_data
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CallbackTask',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.CallbackTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def callback_task(
        self,
        request: mseap_20210118_models.CallbackTaskRequest,
    ) -> mseap_20210118_models.CallbackTaskResponse:
        """
        @summary 任务回调
        
        @param request: CallbackTaskRequest
        @return: CallbackTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.callback_task_with_options(request, runtime)

    async def callback_task_async(
        self,
        request: mseap_20210118_models.CallbackTaskRequest,
    ) -> mseap_20210118_models.CallbackTaskResponse:
        """
        @summary 任务回调
        
        @param request: CallbackTaskRequest
        @return: CallbackTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.callback_task_with_options_async(request, runtime)

    def describe_agreement_status_with_options(
        self,
        request: mseap_20210118_models.DescribeAgreementStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.DescribeAgreementStatusResponse:
        """
        @param request: DescribeAgreementStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAgreementStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement_code):
            query['AgreementCode'] = request.agreement_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAgreementStatus',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.DescribeAgreementStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_agreement_status_with_options_async(
        self,
        request: mseap_20210118_models.DescribeAgreementStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.DescribeAgreementStatusResponse:
        """
        @param request: DescribeAgreementStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAgreementStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement_code):
            query['AgreementCode'] = request.agreement_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAgreementStatus',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.DescribeAgreementStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_agreement_status(
        self,
        request: mseap_20210118_models.DescribeAgreementStatusRequest,
    ) -> mseap_20210118_models.DescribeAgreementStatusResponse:
        """
        @param request: DescribeAgreementStatusRequest
        @return: DescribeAgreementStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_agreement_status_with_options(request, runtime)

    async def describe_agreement_status_async(
        self,
        request: mseap_20210118_models.DescribeAgreementStatusRequest,
    ) -> mseap_20210118_models.DescribeAgreementStatusResponse:
        """
        @param request: DescribeAgreementStatusRequest
        @return: DescribeAgreementStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_agreement_status_with_options_async(request, runtime)

    def generate_upload_file_policy_for_partner_with_options(
        self,
        request: mseap_20210118_models.GenerateUploadFilePolicyForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GenerateUploadFilePolicyForPartnerResponse:
        """
        @summary 合作伙伴生成上传文件策略
        
        @param request: GenerateUploadFilePolicyForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUploadFilePolicyForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUploadFilePolicyForPartner',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GenerateUploadFilePolicyForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_upload_file_policy_for_partner_with_options_async(
        self,
        request: mseap_20210118_models.GenerateUploadFilePolicyForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GenerateUploadFilePolicyForPartnerResponse:
        """
        @summary 合作伙伴生成上传文件策略
        
        @param request: GenerateUploadFilePolicyForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUploadFilePolicyForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUploadFilePolicyForPartner',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GenerateUploadFilePolicyForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_upload_file_policy_for_partner(
        self,
        request: mseap_20210118_models.GenerateUploadFilePolicyForPartnerRequest,
    ) -> mseap_20210118_models.GenerateUploadFilePolicyForPartnerResponse:
        """
        @summary 合作伙伴生成上传文件策略
        
        @param request: GenerateUploadFilePolicyForPartnerRequest
        @return: GenerateUploadFilePolicyForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_file_policy_for_partner_with_options(request, runtime)

    async def generate_upload_file_policy_for_partner_async(
        self,
        request: mseap_20210118_models.GenerateUploadFilePolicyForPartnerRequest,
    ) -> mseap_20210118_models.GenerateUploadFilePolicyForPartnerResponse:
        """
        @summary 合作伙伴生成上传文件策略
        
        @param request: GenerateUploadFilePolicyForPartnerRequest
        @return: GenerateUploadFilePolicyForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_upload_file_policy_for_partner_with_options_async(request, runtime)

    def get_node_by_flow_id_with_options(
        self,
        request: mseap_20210118_models.GetNodeByFlowIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GetNodeByFlowIdResponse:
        """
        @summary 获取node节点通过流程id
        
        @param request: GetNodeByFlowIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeByFlowIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeByFlowId',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GetNodeByFlowIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_by_flow_id_with_options_async(
        self,
        request: mseap_20210118_models.GetNodeByFlowIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GetNodeByFlowIdResponse:
        """
        @summary 获取node节点通过流程id
        
        @param request: GetNodeByFlowIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeByFlowIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeByFlowId',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GetNodeByFlowIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_by_flow_id(
        self,
        request: mseap_20210118_models.GetNodeByFlowIdRequest,
    ) -> mseap_20210118_models.GetNodeByFlowIdResponse:
        """
        @summary 获取node节点通过流程id
        
        @param request: GetNodeByFlowIdRequest
        @return: GetNodeByFlowIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_by_flow_id_with_options(request, runtime)

    async def get_node_by_flow_id_async(
        self,
        request: mseap_20210118_models.GetNodeByFlowIdRequest,
    ) -> mseap_20210118_models.GetNodeByFlowIdResponse:
        """
        @summary 获取node节点通过流程id
        
        @param request: GetNodeByFlowIdRequest
        @return: GetNodeByFlowIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_node_by_flow_id_with_options_async(request, runtime)

    def get_node_by_template_id_with_options(
        self,
        request: mseap_20210118_models.GetNodeByTemplateIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GetNodeByTemplateIdResponse:
        """
        @summary 获取node节点通过模版id
        
        @param request: GetNodeByTemplateIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeByTemplateIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeByTemplateId',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GetNodeByTemplateIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_by_template_id_with_options_async(
        self,
        request: mseap_20210118_models.GetNodeByTemplateIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GetNodeByTemplateIdResponse:
        """
        @summary 获取node节点通过模版id
        
        @param request: GetNodeByTemplateIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeByTemplateIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeByTemplateId',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GetNodeByTemplateIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_by_template_id(
        self,
        request: mseap_20210118_models.GetNodeByTemplateIdRequest,
    ) -> mseap_20210118_models.GetNodeByTemplateIdResponse:
        """
        @summary 获取node节点通过模版id
        
        @param request: GetNodeByTemplateIdRequest
        @return: GetNodeByTemplateIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_by_template_id_with_options(request, runtime)

    async def get_node_by_template_id_async(
        self,
        request: mseap_20210118_models.GetNodeByTemplateIdRequest,
    ) -> mseap_20210118_models.GetNodeByTemplateIdResponse:
        """
        @summary 获取node节点通过模版id
        
        @param request: GetNodeByTemplateIdRequest
        @return: GetNodeByTemplateIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_node_by_template_id_with_options_async(request, runtime)

    def get_proxy_by_type_with_options(
        self,
        request: mseap_20210118_models.GetProxyByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GetProxyByTypeResponse:
        """
        @summary 获取代理
        
        @param request: GetProxyByTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProxyByTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProxyByType',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GetProxyByTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_proxy_by_type_with_options_async(
        self,
        request: mseap_20210118_models.GetProxyByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GetProxyByTypeResponse:
        """
        @summary 获取代理
        
        @param request: GetProxyByTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProxyByTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProxyByType',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GetProxyByTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_proxy_by_type(
        self,
        request: mseap_20210118_models.GetProxyByTypeRequest,
    ) -> mseap_20210118_models.GetProxyByTypeResponse:
        """
        @summary 获取代理
        
        @param request: GetProxyByTypeRequest
        @return: GetProxyByTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_proxy_by_type_with_options(request, runtime)

    async def get_proxy_by_type_async(
        self,
        request: mseap_20210118_models.GetProxyByTypeRequest,
    ) -> mseap_20210118_models.GetProxyByTypeResponse:
        """
        @summary 获取代理
        
        @param request: GetProxyByTypeRequest
        @return: GetProxyByTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_proxy_by_type_with_options_async(request, runtime)

    def get_redis_value_with_options(
        self,
        request: mseap_20210118_models.GetRedisValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GetRedisValueResponse:
        """
        @summary 获取redis值
        
        @param request: GetRedisValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRedisValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRedisValue',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GetRedisValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_redis_value_with_options_async(
        self,
        request: mseap_20210118_models.GetRedisValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GetRedisValueResponse:
        """
        @summary 获取redis值
        
        @param request: GetRedisValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRedisValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRedisValue',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GetRedisValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_redis_value(
        self,
        request: mseap_20210118_models.GetRedisValueRequest,
    ) -> mseap_20210118_models.GetRedisValueResponse:
        """
        @summary 获取redis值
        
        @param request: GetRedisValueRequest
        @return: GetRedisValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_redis_value_with_options(request, runtime)

    async def get_redis_value_async(
        self,
        request: mseap_20210118_models.GetRedisValueRequest,
    ) -> mseap_20210118_models.GetRedisValueResponse:
        """
        @summary 获取redis值
        
        @param request: GetRedisValueRequest
        @return: GetRedisValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_redis_value_with_options_async(request, runtime)

    def get_variable_with_options(
        self,
        request: mseap_20210118_models.GetVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GetVariableResponse:
        """
        @summary 获取变量
        
        @param request: GetVariableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVariable',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GetVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_variable_with_options_async(
        self,
        request: mseap_20210118_models.GetVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.GetVariableResponse:
        """
        @summary 获取变量
        
        @param request: GetVariableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVariable',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.GetVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_variable(
        self,
        request: mseap_20210118_models.GetVariableRequest,
    ) -> mseap_20210118_models.GetVariableResponse:
        """
        @summary 获取变量
        
        @param request: GetVariableRequest
        @return: GetVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_variable_with_options(request, runtime)

    async def get_variable_async(
        self,
        request: mseap_20210118_models.GetVariableRequest,
    ) -> mseap_20210118_models.GetVariableResponse:
        """
        @summary 获取变量
        
        @param request: GetVariableRequest
        @return: GetVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_variable_with_options_async(request, runtime)

    def identify_code_with_options(
        self,
        request: mseap_20210118_models.IdentifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.IdentifyCodeResponse:
        """
        @summary 识别验证码
        
        @param request: IdentifyCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IdentifyCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IdentifyCode',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.IdentifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def identify_code_with_options_async(
        self,
        request: mseap_20210118_models.IdentifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.IdentifyCodeResponse:
        """
        @summary 识别验证码
        
        @param request: IdentifyCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IdentifyCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IdentifyCode',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.IdentifyCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def identify_code(
        self,
        request: mseap_20210118_models.IdentifyCodeRequest,
    ) -> mseap_20210118_models.IdentifyCodeResponse:
        """
        @summary 识别验证码
        
        @param request: IdentifyCodeRequest
        @return: IdentifyCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.identify_code_with_options(request, runtime)

    async def identify_code_async(
        self,
        request: mseap_20210118_models.IdentifyCodeRequest,
    ) -> mseap_20210118_models.IdentifyCodeResponse:
        """
        @summary 识别验证码
        
        @param request: IdentifyCodeRequest
        @return: IdentifyCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.identify_code_with_options_async(request, runtime)

    def pull_rpa_model_with_options(
        self,
        request: mseap_20210118_models.PullRpaModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.PullRpaModelResponse:
        """
        @summary 拉取协议变更识别模型
        
        @param request: PullRpaModelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PullRpaModelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullRpaModel',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.PullRpaModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def pull_rpa_model_with_options_async(
        self,
        request: mseap_20210118_models.PullRpaModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.PullRpaModelResponse:
        """
        @summary 拉取协议变更识别模型
        
        @param request: PullRpaModelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PullRpaModelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullRpaModel',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.PullRpaModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pull_rpa_model(
        self,
        request: mseap_20210118_models.PullRpaModelRequest,
    ) -> mseap_20210118_models.PullRpaModelResponse:
        """
        @summary 拉取协议变更识别模型
        
        @param request: PullRpaModelRequest
        @return: PullRpaModelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pull_rpa_model_with_options(request, runtime)

    async def pull_rpa_model_async(
        self,
        request: mseap_20210118_models.PullRpaModelRequest,
    ) -> mseap_20210118_models.PullRpaModelResponse:
        """
        @summary 拉取协议变更识别模型
        
        @param request: PullRpaModelRequest
        @return: PullRpaModelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pull_rpa_model_with_options_async(request, runtime)

    def pull_task_with_options(
        self,
        request: mseap_20210118_models.PullTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.PullTaskResponse:
        """
        @summary RPA拉取任务
        
        @param request: PullTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PullTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.principal_key):
            query['PrincipalKey'] = request.principal_key
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullTask',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.PullTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def pull_task_with_options_async(
        self,
        request: mseap_20210118_models.PullTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.PullTaskResponse:
        """
        @summary RPA拉取任务
        
        @param request: PullTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PullTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.principal_key):
            query['PrincipalKey'] = request.principal_key
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_security_transport):
            query['UserCallerSecurityTransport'] = request.user_caller_security_transport
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullTask',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.PullTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pull_task(
        self,
        request: mseap_20210118_models.PullTaskRequest,
    ) -> mseap_20210118_models.PullTaskResponse:
        """
        @summary RPA拉取任务
        
        @param request: PullTaskRequest
        @return: PullTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pull_task_with_options(request, runtime)

    async def pull_task_async(
        self,
        request: mseap_20210118_models.PullTaskRequest,
    ) -> mseap_20210118_models.PullTaskResponse:
        """
        @summary RPA拉取任务
        
        @param request: PullTaskRequest
        @return: PullTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pull_task_with_options_async(request, runtime)

    def push_rpa_task_with_options(
        self,
        request: mseap_20210118_models.PushRpaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.PushRpaTaskResponse:
        """
        @summary 推送RPA运行时任务
        
        @param request: PushRpaTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushRpaTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.request):
            query['Request'] = request.request
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushRpaTask',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.PushRpaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_rpa_task_with_options_async(
        self,
        request: mseap_20210118_models.PushRpaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.PushRpaTaskResponse:
        """
        @summary 推送RPA运行时任务
        
        @param request: PushRpaTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushRpaTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.request):
            query['Request'] = request.request
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushRpaTask',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.PushRpaTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_rpa_task(
        self,
        request: mseap_20210118_models.PushRpaTaskRequest,
    ) -> mseap_20210118_models.PushRpaTaskResponse:
        """
        @summary 推送RPA运行时任务
        
        @param request: PushRpaTaskRequest
        @return: PushRpaTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_rpa_task_with_options(request, runtime)

    async def push_rpa_task_async(
        self,
        request: mseap_20210118_models.PushRpaTaskRequest,
    ) -> mseap_20210118_models.PushRpaTaskResponse:
        """
        @summary 推送RPA运行时任务
        
        @param request: PushRpaTaskRequest
        @return: PushRpaTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_rpa_task_with_options_async(request, runtime)

    def push_rpa_task_detail_with_options(
        self,
        request: mseap_20210118_models.PushRpaTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.PushRpaTaskDetailResponse:
        """
        @summary 推送运行时任务明细
        
        @param request: PushRpaTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushRpaTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.input_data):
            query['InputData'] = request.input_data
        if not UtilClient.is_unset(request.input_html):
            query['InputHtml'] = request.input_html
        if not UtilClient.is_unset(request.input_screenshot):
            query['InputScreenshot'] = request.input_screenshot
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.model_detail_id):
            query['ModelDetailId'] = request.model_detail_id
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.output_data):
            query['OutputData'] = request.output_data
        if not UtilClient.is_unset(request.output_html):
            query['OutputHtml'] = request.output_html
        if not UtilClient.is_unset(request.output_screenshot):
            query['OutputScreenshot'] = request.output_screenshot
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_detail_id):
            query['TaskDetailId'] = request.task_detail_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushRpaTaskDetail',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.PushRpaTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_rpa_task_detail_with_options_async(
        self,
        request: mseap_20210118_models.PushRpaTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.PushRpaTaskDetailResponse:
        """
        @summary 推送运行时任务明细
        
        @param request: PushRpaTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushRpaTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.input_data):
            query['InputData'] = request.input_data
        if not UtilClient.is_unset(request.input_html):
            query['InputHtml'] = request.input_html
        if not UtilClient.is_unset(request.input_screenshot):
            query['InputScreenshot'] = request.input_screenshot
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.model_detail_id):
            query['ModelDetailId'] = request.model_detail_id
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.output_data):
            query['OutputData'] = request.output_data
        if not UtilClient.is_unset(request.output_html):
            query['OutputHtml'] = request.output_html
        if not UtilClient.is_unset(request.output_screenshot):
            query['OutputScreenshot'] = request.output_screenshot
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_detail_id):
            query['TaskDetailId'] = request.task_detail_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushRpaTaskDetail',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.PushRpaTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_rpa_task_detail(
        self,
        request: mseap_20210118_models.PushRpaTaskDetailRequest,
    ) -> mseap_20210118_models.PushRpaTaskDetailResponse:
        """
        @summary 推送运行时任务明细
        
        @param request: PushRpaTaskDetailRequest
        @return: PushRpaTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_rpa_task_detail_with_options(request, runtime)

    async def push_rpa_task_detail_async(
        self,
        request: mseap_20210118_models.PushRpaTaskDetailRequest,
    ) -> mseap_20210118_models.PushRpaTaskDetailResponse:
        """
        @summary 推送运行时任务明细
        
        @param request: PushRpaTaskDetailRequest
        @return: PushRpaTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_rpa_task_detail_with_options_async(request, runtime)

    def send_notification_for_partner_with_options(
        self,
        tmp_req: mseap_20210118_models.SendNotificationForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.SendNotificationForPartnerResponse:
        """
        @summary 合作伙伴发送消息通知
        
        @param tmp_req: SendNotificationForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendNotificationForPartnerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mseap_20210118_models.SendNotificationForPartnerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param_map):
            request.param_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.param_map, 'ParamMap', 'json')
        if not UtilClient.is_unset(tmp_req.smart_sub_channels):
            request.smart_sub_channels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.smart_sub_channels, 'SmartSubChannels', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.notifycation_event_type):
            query['NotifycationEventType'] = request.notifycation_event_type
        if not UtilClient.is_unset(request.param_map_shrink):
            query['ParamMap'] = request.param_map_shrink
        if not UtilClient.is_unset(request.send_target):
            query['SendTarget'] = request.send_target
        if not UtilClient.is_unset(request.smart_sub_channels_shrink):
            query['SmartSubChannels'] = request.smart_sub_channels_shrink
        if not UtilClient.is_unset(request.track_id):
            query['TrackId'] = request.track_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendNotificationForPartner',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.SendNotificationForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_notification_for_partner_with_options_async(
        self,
        tmp_req: mseap_20210118_models.SendNotificationForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.SendNotificationForPartnerResponse:
        """
        @summary 合作伙伴发送消息通知
        
        @param tmp_req: SendNotificationForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendNotificationForPartnerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mseap_20210118_models.SendNotificationForPartnerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param_map):
            request.param_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.param_map, 'ParamMap', 'json')
        if not UtilClient.is_unset(tmp_req.smart_sub_channels):
            request.smart_sub_channels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.smart_sub_channels, 'SmartSubChannels', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.notifycation_event_type):
            query['NotifycationEventType'] = request.notifycation_event_type
        if not UtilClient.is_unset(request.param_map_shrink):
            query['ParamMap'] = request.param_map_shrink
        if not UtilClient.is_unset(request.send_target):
            query['SendTarget'] = request.send_target
        if not UtilClient.is_unset(request.smart_sub_channels_shrink):
            query['SmartSubChannels'] = request.smart_sub_channels_shrink
        if not UtilClient.is_unset(request.track_id):
            query['TrackId'] = request.track_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendNotificationForPartner',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.SendNotificationForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_notification_for_partner(
        self,
        request: mseap_20210118_models.SendNotificationForPartnerRequest,
    ) -> mseap_20210118_models.SendNotificationForPartnerResponse:
        """
        @summary 合作伙伴发送消息通知
        
        @param request: SendNotificationForPartnerRequest
        @return: SendNotificationForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_notification_for_partner_with_options(request, runtime)

    async def send_notification_for_partner_async(
        self,
        request: mseap_20210118_models.SendNotificationForPartnerRequest,
    ) -> mseap_20210118_models.SendNotificationForPartnerResponse:
        """
        @summary 合作伙伴发送消息通知
        
        @param request: SendNotificationForPartnerRequest
        @return: SendNotificationForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_notification_for_partner_with_options_async(request, runtime)

    def set_redis_value_with_options(
        self,
        request: mseap_20210118_models.SetRedisValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.SetRedisValueResponse:
        """
        @summary redis设置
        
        @param request: SetRedisValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetRedisValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRedisValue',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.SetRedisValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_redis_value_with_options_async(
        self,
        request: mseap_20210118_models.SetRedisValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.SetRedisValueResponse:
        """
        @summary redis设置
        
        @param request: SetRedisValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetRedisValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_kp):
            query['AliyunKp'] = request.aliyun_kp
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.original_request):
            query['OriginalRequest'] = request.original_request
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_bid):
            query['UserBid'] = request.user_bid
        if not UtilClient.is_unset(request.user_caller_parent_id):
            query['UserCallerParentId'] = request.user_caller_parent_id
        if not UtilClient.is_unset(request.user_caller_type):
            query['UserCallerType'] = request.user_caller_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_kp):
            query['UserKp'] = request.user_kp
        if not UtilClient.is_unset(request.user_mfa_present):
            query['UserMfaPresent'] = request.user_mfa_present
        if not UtilClient.is_unset(request.user_security_token):
            query['UserSecurityToken'] = request.user_security_token
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRedisValue',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.SetRedisValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_redis_value(
        self,
        request: mseap_20210118_models.SetRedisValueRequest,
    ) -> mseap_20210118_models.SetRedisValueResponse:
        """
        @summary redis设置
        
        @param request: SetRedisValueRequest
        @return: SetRedisValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_redis_value_with_options(request, runtime)

    async def set_redis_value_async(
        self,
        request: mseap_20210118_models.SetRedisValueRequest,
    ) -> mseap_20210118_models.SetRedisValueResponse:
        """
        @summary redis设置
        
        @param request: SetRedisValueRequest
        @return: SetRedisValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_redis_value_with_options_async(request, runtime)

    def update_agreement_status_with_options(
        self,
        request: mseap_20210118_models.UpdateAgreementStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.UpdateAgreementStatusResponse:
        """
        @param request: UpdateAgreementStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAgreementStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement_code):
            query['AgreementCode'] = request.agreement_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAgreementStatus',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.UpdateAgreementStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agreement_status_with_options_async(
        self,
        request: mseap_20210118_models.UpdateAgreementStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mseap_20210118_models.UpdateAgreementStatusResponse:
        """
        @param request: UpdateAgreementStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAgreementStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement_code):
            query['AgreementCode'] = request.agreement_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAgreementStatus',
            version='2021-01-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mseap_20210118_models.UpdateAgreementStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agreement_status(
        self,
        request: mseap_20210118_models.UpdateAgreementStatusRequest,
    ) -> mseap_20210118_models.UpdateAgreementStatusResponse:
        """
        @param request: UpdateAgreementStatusRequest
        @return: UpdateAgreementStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_agreement_status_with_options(request, runtime)

    async def update_agreement_status_async(
        self,
        request: mseap_20210118_models.UpdateAgreementStatusRequest,
    ) -> mseap_20210118_models.UpdateAgreementStatusResponse:
        """
        @param request: UpdateAgreementStatusRequest
        @return: UpdateAgreementStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_agreement_status_with_options_async(request, runtime)
