# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_domain20180129 import models as domain_20180129_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('domain', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def acknowledge_task_result_with_options(
        self,
        request: domain_20180129_models.AcknowledgeTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.AcknowledgeTaskResultResponse:
        """
        @summary 确认任务结果
        
        @param request: AcknowledgeTaskResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcknowledgeTaskResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_detail_no):
            query['TaskDetailNo'] = request.task_detail_no
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcknowledgeTaskResult',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.AcknowledgeTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def acknowledge_task_result_with_options_async(
        self,
        request: domain_20180129_models.AcknowledgeTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.AcknowledgeTaskResultResponse:
        """
        @summary 确认任务结果
        
        @param request: AcknowledgeTaskResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcknowledgeTaskResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_detail_no):
            query['TaskDetailNo'] = request.task_detail_no
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcknowledgeTaskResult',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.AcknowledgeTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def acknowledge_task_result(
        self,
        request: domain_20180129_models.AcknowledgeTaskResultRequest,
    ) -> domain_20180129_models.AcknowledgeTaskResultResponse:
        """
        @summary 确认任务结果
        
        @param request: AcknowledgeTaskResultRequest
        @return: AcknowledgeTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.acknowledge_task_result_with_options(request, runtime)

    async def acknowledge_task_result_async(
        self,
        request: domain_20180129_models.AcknowledgeTaskResultRequest,
    ) -> domain_20180129_models.AcknowledgeTaskResultResponse:
        """
        @summary 确认任务结果
        
        @param request: AcknowledgeTaskResultRequest
        @return: AcknowledgeTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.acknowledge_task_result_with_options_async(request, runtime)

    def batch_fuzzy_match_domain_sensitive_word_with_options(
        self,
        request: domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        """
        @summary 通过关键字进行批量模糊匹配
        
        @param request: BatchFuzzyMatchDomainSensitiveWordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchFuzzyMatchDomainSensitiveWordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchFuzzyMatchDomainSensitiveWord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_fuzzy_match_domain_sensitive_word_with_options_async(
        self,
        request: domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        """
        @summary 通过关键字进行批量模糊匹配
        
        @param request: BatchFuzzyMatchDomainSensitiveWordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchFuzzyMatchDomainSensitiveWordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchFuzzyMatchDomainSensitiveWord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_fuzzy_match_domain_sensitive_word(
        self,
        request: domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordRequest,
    ) -> domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        """
        @summary 通过关键字进行批量模糊匹配
        
        @param request: BatchFuzzyMatchDomainSensitiveWordRequest
        @return: BatchFuzzyMatchDomainSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_fuzzy_match_domain_sensitive_word_with_options(request, runtime)

    async def batch_fuzzy_match_domain_sensitive_word_async(
        self,
        request: domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordRequest,
    ) -> domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        """
        @summary 通过关键字进行批量模糊匹配
        
        @param request: BatchFuzzyMatchDomainSensitiveWordRequest
        @return: BatchFuzzyMatchDomainSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_fuzzy_match_domain_sensitive_word_with_options_async(request, runtime)

    def cancel_domain_verification_with_options(
        self,
        request: domain_20180129_models.CancelDomainVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelDomainVerificationResponse:
        """
        @summary Cancels real-name verification for a domain name.
        
        @param request: CancelDomainVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDomainVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDomainVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CancelDomainVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_domain_verification_with_options_async(
        self,
        request: domain_20180129_models.CancelDomainVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelDomainVerificationResponse:
        """
        @summary Cancels real-name verification for a domain name.
        
        @param request: CancelDomainVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDomainVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDomainVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CancelDomainVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_domain_verification(
        self,
        request: domain_20180129_models.CancelDomainVerificationRequest,
    ) -> domain_20180129_models.CancelDomainVerificationResponse:
        """
        @summary Cancels real-name verification for a domain name.
        
        @param request: CancelDomainVerificationRequest
        @return: CancelDomainVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_domain_verification_with_options(request, runtime)

    async def cancel_domain_verification_async(
        self,
        request: domain_20180129_models.CancelDomainVerificationRequest,
    ) -> domain_20180129_models.CancelDomainVerificationResponse:
        """
        @summary Cancels real-name verification for a domain name.
        
        @param request: CancelDomainVerificationRequest
        @return: CancelDomainVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_domain_verification_with_options_async(request, runtime)

    def cancel_operation_audit_with_options(
        self,
        request: domain_20180129_models.CancelOperationAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelOperationAuditResponse:
        """
        @summary 取消审核
        
        @param request: CancelOperationAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelOperationAuditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOperationAudit',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CancelOperationAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_operation_audit_with_options_async(
        self,
        request: domain_20180129_models.CancelOperationAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelOperationAuditResponse:
        """
        @summary 取消审核
        
        @param request: CancelOperationAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelOperationAuditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOperationAudit',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CancelOperationAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_operation_audit(
        self,
        request: domain_20180129_models.CancelOperationAuditRequest,
    ) -> domain_20180129_models.CancelOperationAuditResponse:
        """
        @summary 取消审核
        
        @param request: CancelOperationAuditRequest
        @return: CancelOperationAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_operation_audit_with_options(request, runtime)

    async def cancel_operation_audit_async(
        self,
        request: domain_20180129_models.CancelOperationAuditRequest,
    ) -> domain_20180129_models.CancelOperationAuditResponse:
        """
        @summary 取消审核
        
        @param request: CancelOperationAuditRequest
        @return: CancelOperationAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_operation_audit_with_options_async(request, runtime)

    def cancel_qualification_verification_with_options(
        self,
        request: domain_20180129_models.CancelQualificationVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelQualificationVerificationResponse:
        """
        @param request: CancelQualificationVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelQualificationVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelQualificationVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CancelQualificationVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_qualification_verification_with_options_async(
        self,
        request: domain_20180129_models.CancelQualificationVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelQualificationVerificationResponse:
        """
        @param request: CancelQualificationVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelQualificationVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelQualificationVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CancelQualificationVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_qualification_verification(
        self,
        request: domain_20180129_models.CancelQualificationVerificationRequest,
    ) -> domain_20180129_models.CancelQualificationVerificationResponse:
        """
        @param request: CancelQualificationVerificationRequest
        @return: CancelQualificationVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_qualification_verification_with_options(request, runtime)

    async def cancel_qualification_verification_async(
        self,
        request: domain_20180129_models.CancelQualificationVerificationRequest,
    ) -> domain_20180129_models.CancelQualificationVerificationResponse:
        """
        @param request: CancelQualificationVerificationRequest
        @return: CancelQualificationVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_qualification_verification_with_options_async(request, runtime)

    def cancel_task_with_options(
        self,
        request: domain_20180129_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelTaskResponse:
        """
        @param request: CancelTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        request: domain_20180129_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelTaskResponse:
        """
        @param request: CancelTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        request: domain_20180129_models.CancelTaskRequest,
    ) -> domain_20180129_models.CancelTaskResponse:
        """
        @param request: CancelTaskRequest
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    async def cancel_task_async(
        self,
        request: domain_20180129_models.CancelTaskRequest,
    ) -> domain_20180129_models.CancelTaskResponse:
        """
        @param request: CancelTaskRequest
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_task_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: domain_20180129_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ChangeResourceGroupResponse:
        """
        @summary 修改实例所在资源组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: domain_20180129_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ChangeResourceGroupResponse:
        """
        @summary 修改实例所在资源组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: domain_20180129_models.ChangeResourceGroupRequest,
    ) -> domain_20180129_models.ChangeResourceGroupResponse:
        """
        @summary 修改实例所在资源组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: domain_20180129_models.ChangeResourceGroupRequest,
    ) -> domain_20180129_models.ChangeResourceGroupResponse:
        """
        @summary 修改实例所在资源组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_domain_with_options(
        self,
        request: domain_20180129_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckDomainResponse:
        """
        @param request: CheckDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.fee_command):
            query['FeeCommand'] = request.fee_command
        if not UtilClient.is_unset(request.fee_currency):
            query['FeeCurrency'] = request.fee_currency
        if not UtilClient.is_unset(request.fee_period):
            query['FeePeriod'] = request.fee_period
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomain',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CheckDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_with_options_async(
        self,
        request: domain_20180129_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckDomainResponse:
        """
        @param request: CheckDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.fee_command):
            query['FeeCommand'] = request.fee_command
        if not UtilClient.is_unset(request.fee_currency):
            query['FeeCurrency'] = request.fee_currency
        if not UtilClient.is_unset(request.fee_period):
            query['FeePeriod'] = request.fee_period
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomain',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CheckDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain(
        self,
        request: domain_20180129_models.CheckDomainRequest,
    ) -> domain_20180129_models.CheckDomainResponse:
        """
        @param request: CheckDomainRequest
        @return: CheckDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    async def check_domain_async(
        self,
        request: domain_20180129_models.CheckDomainRequest,
    ) -> domain_20180129_models.CheckDomainResponse:
        """
        @param request: CheckDomainRequest
        @return: CheckDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_domain_with_options_async(request, runtime)

    def check_domain_sunrise_claim_with_options(
        self,
        request: domain_20180129_models.CheckDomainSunriseClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckDomainSunriseClaimResponse:
        """
        @param request: CheckDomainSunriseClaimRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDomainSunriseClaimResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomainSunriseClaim',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CheckDomainSunriseClaimResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_sunrise_claim_with_options_async(
        self,
        request: domain_20180129_models.CheckDomainSunriseClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckDomainSunriseClaimResponse:
        """
        @param request: CheckDomainSunriseClaimRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDomainSunriseClaimResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomainSunriseClaim',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CheckDomainSunriseClaimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain_sunrise_claim(
        self,
        request: domain_20180129_models.CheckDomainSunriseClaimRequest,
    ) -> domain_20180129_models.CheckDomainSunriseClaimResponse:
        """
        @param request: CheckDomainSunriseClaimRequest
        @return: CheckDomainSunriseClaimResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_domain_sunrise_claim_with_options(request, runtime)

    async def check_domain_sunrise_claim_async(
        self,
        request: domain_20180129_models.CheckDomainSunriseClaimRequest,
    ) -> domain_20180129_models.CheckDomainSunriseClaimResponse:
        """
        @param request: CheckDomainSunriseClaimRequest
        @return: CheckDomainSunriseClaimResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_domain_sunrise_claim_with_options_async(request, runtime)

    def check_max_year_of_server_lock_with_options(
        self,
        request: domain_20180129_models.CheckMaxYearOfServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckMaxYearOfServerLockResponse:
        """
        @param request: CheckMaxYearOfServerLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckMaxYearOfServerLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_action):
            query['CheckAction'] = request.check_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMaxYearOfServerLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CheckMaxYearOfServerLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_max_year_of_server_lock_with_options_async(
        self,
        request: domain_20180129_models.CheckMaxYearOfServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckMaxYearOfServerLockResponse:
        """
        @param request: CheckMaxYearOfServerLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckMaxYearOfServerLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_action):
            query['CheckAction'] = request.check_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMaxYearOfServerLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CheckMaxYearOfServerLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_max_year_of_server_lock(
        self,
        request: domain_20180129_models.CheckMaxYearOfServerLockRequest,
    ) -> domain_20180129_models.CheckMaxYearOfServerLockResponse:
        """
        @param request: CheckMaxYearOfServerLockRequest
        @return: CheckMaxYearOfServerLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_max_year_of_server_lock_with_options(request, runtime)

    async def check_max_year_of_server_lock_async(
        self,
        request: domain_20180129_models.CheckMaxYearOfServerLockRequest,
    ) -> domain_20180129_models.CheckMaxYearOfServerLockResponse:
        """
        @param request: CheckMaxYearOfServerLockRequest
        @return: CheckMaxYearOfServerLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_max_year_of_server_lock_with_options_async(request, runtime)

    def check_processing_server_lock_apply_with_options(
        self,
        request: domain_20180129_models.CheckProcessingServerLockApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckProcessingServerLockApplyResponse:
        """
        @param request: CheckProcessingServerLockApplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckProcessingServerLockApplyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.fee_period):
            query['FeePeriod'] = request.fee_period
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckProcessingServerLockApply',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CheckProcessingServerLockApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_processing_server_lock_apply_with_options_async(
        self,
        request: domain_20180129_models.CheckProcessingServerLockApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckProcessingServerLockApplyResponse:
        """
        @param request: CheckProcessingServerLockApplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckProcessingServerLockApplyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.fee_period):
            query['FeePeriod'] = request.fee_period
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckProcessingServerLockApply',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CheckProcessingServerLockApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_processing_server_lock_apply(
        self,
        request: domain_20180129_models.CheckProcessingServerLockApplyRequest,
    ) -> domain_20180129_models.CheckProcessingServerLockApplyResponse:
        """
        @param request: CheckProcessingServerLockApplyRequest
        @return: CheckProcessingServerLockApplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_processing_server_lock_apply_with_options(request, runtime)

    async def check_processing_server_lock_apply_async(
        self,
        request: domain_20180129_models.CheckProcessingServerLockApplyRequest,
    ) -> domain_20180129_models.CheckProcessingServerLockApplyResponse:
        """
        @param request: CheckProcessingServerLockApplyRequest
        @return: CheckProcessingServerLockApplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_processing_server_lock_apply_with_options_async(request, runtime)

    def check_transfer_in_feasibility_with_options(
        self,
        request: domain_20180129_models.CheckTransferInFeasibilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckTransferInFeasibilityResponse:
        """
        @param request: CheckTransferInFeasibilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckTransferInFeasibilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.transfer_authorization_code):
            query['TransferAuthorizationCode'] = request.transfer_authorization_code
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckTransferInFeasibility',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CheckTransferInFeasibilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_transfer_in_feasibility_with_options_async(
        self,
        request: domain_20180129_models.CheckTransferInFeasibilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckTransferInFeasibilityResponse:
        """
        @param request: CheckTransferInFeasibilityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckTransferInFeasibilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.transfer_authorization_code):
            query['TransferAuthorizationCode'] = request.transfer_authorization_code
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckTransferInFeasibility',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.CheckTransferInFeasibilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_transfer_in_feasibility(
        self,
        request: domain_20180129_models.CheckTransferInFeasibilityRequest,
    ) -> domain_20180129_models.CheckTransferInFeasibilityResponse:
        """
        @param request: CheckTransferInFeasibilityRequest
        @return: CheckTransferInFeasibilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_transfer_in_feasibility_with_options(request, runtime)

    async def check_transfer_in_feasibility_async(
        self,
        request: domain_20180129_models.CheckTransferInFeasibilityRequest,
    ) -> domain_20180129_models.CheckTransferInFeasibilityResponse:
        """
        @param request: CheckTransferInFeasibilityRequest
        @return: CheckTransferInFeasibilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_transfer_in_feasibility_with_options_async(request, runtime)

    def confirm_transfer_in_email_with_options(
        self,
        request: domain_20180129_models.ConfirmTransferInEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ConfirmTransferInEmailResponse:
        """
        @param request: ConfirmTransferInEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmTransferInEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmTransferInEmail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ConfirmTransferInEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_transfer_in_email_with_options_async(
        self,
        request: domain_20180129_models.ConfirmTransferInEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ConfirmTransferInEmailResponse:
        """
        @param request: ConfirmTransferInEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmTransferInEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmTransferInEmail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ConfirmTransferInEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_transfer_in_email(
        self,
        request: domain_20180129_models.ConfirmTransferInEmailRequest,
    ) -> domain_20180129_models.ConfirmTransferInEmailResponse:
        """
        @param request: ConfirmTransferInEmailRequest
        @return: ConfirmTransferInEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.confirm_transfer_in_email_with_options(request, runtime)

    async def confirm_transfer_in_email_async(
        self,
        request: domain_20180129_models.ConfirmTransferInEmailRequest,
    ) -> domain_20180129_models.ConfirmTransferInEmailResponse:
        """
        @param request: ConfirmTransferInEmailRequest
        @return: ConfirmTransferInEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.confirm_transfer_in_email_with_options_async(request, runtime)

    def delete_contact_templates_with_options(
        self,
        request: domain_20180129_models.DeleteContactTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteContactTemplatesResponse:
        """
        @summary 批量删除联系人模板
        
        @param request: DeleteContactTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.registrant_profile_ids):
            query['RegistrantProfileIds'] = request.registrant_profile_ids
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactTemplates',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.DeleteContactTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_templates_with_options_async(
        self,
        request: domain_20180129_models.DeleteContactTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteContactTemplatesResponse:
        """
        @summary 批量删除联系人模板
        
        @param request: DeleteContactTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.registrant_profile_ids):
            query['RegistrantProfileIds'] = request.registrant_profile_ids
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactTemplates',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.DeleteContactTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_templates(
        self,
        request: domain_20180129_models.DeleteContactTemplatesRequest,
    ) -> domain_20180129_models.DeleteContactTemplatesResponse:
        """
        @summary 批量删除联系人模板
        
        @param request: DeleteContactTemplatesRequest
        @return: DeleteContactTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_templates_with_options(request, runtime)

    async def delete_contact_templates_async(
        self,
        request: domain_20180129_models.DeleteContactTemplatesRequest,
    ) -> domain_20180129_models.DeleteContactTemplatesResponse:
        """
        @summary 批量删除联系人模板
        
        @param request: DeleteContactTemplatesRequest
        @return: DeleteContactTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_contact_templates_with_options_async(request, runtime)

    def delete_domain_group_with_options(
        self,
        request: domain_20180129_models.DeleteDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteDomainGroupResponse:
        """
        @summary 删除域名分组
        
        @param request: DeleteDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainGroup',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.DeleteDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_group_with_options_async(
        self,
        request: domain_20180129_models.DeleteDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteDomainGroupResponse:
        """
        @summary 删除域名分组
        
        @param request: DeleteDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainGroup',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.DeleteDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_group(
        self,
        request: domain_20180129_models.DeleteDomainGroupRequest,
    ) -> domain_20180129_models.DeleteDomainGroupResponse:
        """
        @summary 删除域名分组
        
        @param request: DeleteDomainGroupRequest
        @return: DeleteDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_group_with_options(request, runtime)

    async def delete_domain_group_async(
        self,
        request: domain_20180129_models.DeleteDomainGroupRequest,
    ) -> domain_20180129_models.DeleteDomainGroupResponse:
        """
        @summary 删除域名分组
        
        @param request: DeleteDomainGroupRequest
        @return: DeleteDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_group_with_options_async(request, runtime)

    def delete_email_verification_with_options(
        self,
        request: domain_20180129_models.DeleteEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteEmailVerificationResponse:
        """
        @summary 删除邮箱验证
        
        @param request: DeleteEmailVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEmailVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEmailVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.DeleteEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_email_verification_with_options_async(
        self,
        request: domain_20180129_models.DeleteEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteEmailVerificationResponse:
        """
        @summary 删除邮箱验证
        
        @param request: DeleteEmailVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEmailVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEmailVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.DeleteEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_email_verification(
        self,
        request: domain_20180129_models.DeleteEmailVerificationRequest,
    ) -> domain_20180129_models.DeleteEmailVerificationResponse:
        """
        @summary 删除邮箱验证
        
        @param request: DeleteEmailVerificationRequest
        @return: DeleteEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_email_verification_with_options(request, runtime)

    async def delete_email_verification_async(
        self,
        request: domain_20180129_models.DeleteEmailVerificationRequest,
    ) -> domain_20180129_models.DeleteEmailVerificationResponse:
        """
        @summary 删除邮箱验证
        
        @param request: DeleteEmailVerificationRequest
        @return: DeleteEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_email_verification_with_options_async(request, runtime)

    def delete_registrant_profile_with_options(
        self,
        request: domain_20180129_models.DeleteRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteRegistrantProfileResponse:
        """
        @summary 删除联系人模板
        
        @param request: DeleteRegistrantProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRegistrantProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRegistrantProfile',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.DeleteRegistrantProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_registrant_profile_with_options_async(
        self,
        request: domain_20180129_models.DeleteRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteRegistrantProfileResponse:
        """
        @summary 删除联系人模板
        
        @param request: DeleteRegistrantProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRegistrantProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRegistrantProfile',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.DeleteRegistrantProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_registrant_profile(
        self,
        request: domain_20180129_models.DeleteRegistrantProfileRequest,
    ) -> domain_20180129_models.DeleteRegistrantProfileResponse:
        """
        @summary 删除联系人模板
        
        @param request: DeleteRegistrantProfileRequest
        @return: DeleteRegistrantProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_registrant_profile_with_options(request, runtime)

    async def delete_registrant_profile_async(
        self,
        request: domain_20180129_models.DeleteRegistrantProfileRequest,
    ) -> domain_20180129_models.DeleteRegistrantProfileResponse:
        """
        @summary 删除联系人模板
        
        @param request: DeleteRegistrantProfileRequest
        @return: DeleteRegistrantProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_registrant_profile_with_options_async(request, runtime)

    def domain_special_biz_cancel_with_options(
        self,
        request: domain_20180129_models.DomainSpecialBizCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DomainSpecialBizCancelResponse:
        """
        @summary 取消域名特殊业务流程
        
        @param request: DomainSpecialBizCancelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DomainSpecialBizCancelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DomainSpecialBizCancel',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.DomainSpecialBizCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def domain_special_biz_cancel_with_options_async(
        self,
        request: domain_20180129_models.DomainSpecialBizCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DomainSpecialBizCancelResponse:
        """
        @summary 取消域名特殊业务流程
        
        @param request: DomainSpecialBizCancelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DomainSpecialBizCancelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DomainSpecialBizCancel',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.DomainSpecialBizCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def domain_special_biz_cancel(
        self,
        request: domain_20180129_models.DomainSpecialBizCancelRequest,
    ) -> domain_20180129_models.DomainSpecialBizCancelResponse:
        """
        @summary 取消域名特殊业务流程
        
        @param request: DomainSpecialBizCancelRequest
        @return: DomainSpecialBizCancelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.domain_special_biz_cancel_with_options(request, runtime)

    async def domain_special_biz_cancel_async(
        self,
        request: domain_20180129_models.DomainSpecialBizCancelRequest,
    ) -> domain_20180129_models.DomainSpecialBizCancelResponse:
        """
        @summary 取消域名特殊业务流程
        
        @param request: DomainSpecialBizCancelRequest
        @return: DomainSpecialBizCancelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.domain_special_biz_cancel_with_options_async(request, runtime)

    def email_verified_with_options(
        self,
        request: domain_20180129_models.EmailVerifiedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.EmailVerifiedResponse:
        """
        @summary 邮箱验证通过
        
        @param request: EmailVerifiedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EmailVerifiedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmailVerified',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.EmailVerifiedResponse(),
            self.call_api(params, req, runtime)
        )

    async def email_verified_with_options_async(
        self,
        request: domain_20180129_models.EmailVerifiedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.EmailVerifiedResponse:
        """
        @summary 邮箱验证通过
        
        @param request: EmailVerifiedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EmailVerifiedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmailVerified',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.EmailVerifiedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def email_verified(
        self,
        request: domain_20180129_models.EmailVerifiedRequest,
    ) -> domain_20180129_models.EmailVerifiedResponse:
        """
        @summary 邮箱验证通过
        
        @param request: EmailVerifiedRequest
        @return: EmailVerifiedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.email_verified_with_options(request, runtime)

    async def email_verified_async(
        self,
        request: domain_20180129_models.EmailVerifiedRequest,
    ) -> domain_20180129_models.EmailVerifiedResponse:
        """
        @summary 邮箱验证通过
        
        @param request: EmailVerifiedRequest
        @return: EmailVerifiedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.email_verified_with_options_async(request, runtime)

    def fuzzy_match_domain_sensitive_word_with_options(
        self,
        request: domain_20180129_models.FuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.FuzzyMatchDomainSensitiveWordResponse:
        """
        @summary 通过关键字进行模糊匹配
        
        @param request: FuzzyMatchDomainSensitiveWordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FuzzyMatchDomainSensitiveWordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FuzzyMatchDomainSensitiveWord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.FuzzyMatchDomainSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def fuzzy_match_domain_sensitive_word_with_options_async(
        self,
        request: domain_20180129_models.FuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.FuzzyMatchDomainSensitiveWordResponse:
        """
        @summary 通过关键字进行模糊匹配
        
        @param request: FuzzyMatchDomainSensitiveWordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FuzzyMatchDomainSensitiveWordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FuzzyMatchDomainSensitiveWord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.FuzzyMatchDomainSensitiveWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fuzzy_match_domain_sensitive_word(
        self,
        request: domain_20180129_models.FuzzyMatchDomainSensitiveWordRequest,
    ) -> domain_20180129_models.FuzzyMatchDomainSensitiveWordResponse:
        """
        @summary 通过关键字进行模糊匹配
        
        @param request: FuzzyMatchDomainSensitiveWordRequest
        @return: FuzzyMatchDomainSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fuzzy_match_domain_sensitive_word_with_options(request, runtime)

    async def fuzzy_match_domain_sensitive_word_async(
        self,
        request: domain_20180129_models.FuzzyMatchDomainSensitiveWordRequest,
    ) -> domain_20180129_models.FuzzyMatchDomainSensitiveWordResponse:
        """
        @summary 通过关键字进行模糊匹配
        
        @param request: FuzzyMatchDomainSensitiveWordRequest
        @return: FuzzyMatchDomainSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fuzzy_match_domain_sensitive_word_with_options_async(request, runtime)

    def get_operation_oss_upload_policy_with_options(
        self,
        request: domain_20180129_models.GetOperationOssUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.GetOperationOssUploadPolicyResponse:
        """
        @param request: GetOperationOssUploadPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOperationOssUploadPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_type):
            query['AuditType'] = request.audit_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOperationOssUploadPolicy',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.GetOperationOssUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_operation_oss_upload_policy_with_options_async(
        self,
        request: domain_20180129_models.GetOperationOssUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.GetOperationOssUploadPolicyResponse:
        """
        @param request: GetOperationOssUploadPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOperationOssUploadPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_type):
            query['AuditType'] = request.audit_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOperationOssUploadPolicy',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.GetOperationOssUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_operation_oss_upload_policy(
        self,
        request: domain_20180129_models.GetOperationOssUploadPolicyRequest,
    ) -> domain_20180129_models.GetOperationOssUploadPolicyResponse:
        """
        @param request: GetOperationOssUploadPolicyRequest
        @return: GetOperationOssUploadPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_operation_oss_upload_policy_with_options(request, runtime)

    async def get_operation_oss_upload_policy_async(
        self,
        request: domain_20180129_models.GetOperationOssUploadPolicyRequest,
    ) -> domain_20180129_models.GetOperationOssUploadPolicyResponse:
        """
        @param request: GetOperationOssUploadPolicyRequest
        @return: GetOperationOssUploadPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_operation_oss_upload_policy_with_options_async(request, runtime)

    def get_qualification_upload_policy_with_options(
        self,
        request: domain_20180129_models.GetQualificationUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.GetQualificationUploadPolicyResponse:
        """
        @param request: GetQualificationUploadPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualificationUploadPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualificationUploadPolicy',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.GetQualificationUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qualification_upload_policy_with_options_async(
        self,
        request: domain_20180129_models.GetQualificationUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.GetQualificationUploadPolicyResponse:
        """
        @param request: GetQualificationUploadPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualificationUploadPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualificationUploadPolicy',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.GetQualificationUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qualification_upload_policy(
        self,
        request: domain_20180129_models.GetQualificationUploadPolicyRequest,
    ) -> domain_20180129_models.GetQualificationUploadPolicyResponse:
        """
        @param request: GetQualificationUploadPolicyRequest
        @return: GetQualificationUploadPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_qualification_upload_policy_with_options(request, runtime)

    async def get_qualification_upload_policy_async(
        self,
        request: domain_20180129_models.GetQualificationUploadPolicyRequest,
    ) -> domain_20180129_models.GetQualificationUploadPolicyResponse:
        """
        @param request: GetQualificationUploadPolicyRequest
        @return: GetQualificationUploadPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_qualification_upload_policy_with_options_async(request, runtime)

    def list_email_verification_with_options(
        self,
        request: domain_20180129_models.ListEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ListEmailVerificationResponse:
        """
        @param request: ListEmailVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEmailVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.verification_status):
            query['VerificationStatus'] = request.verification_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEmailVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ListEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_email_verification_with_options_async(
        self,
        request: domain_20180129_models.ListEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ListEmailVerificationResponse:
        """
        @param request: ListEmailVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEmailVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.verification_status):
            query['VerificationStatus'] = request.verification_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEmailVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ListEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_email_verification(
        self,
        request: domain_20180129_models.ListEmailVerificationRequest,
    ) -> domain_20180129_models.ListEmailVerificationResponse:
        """
        @param request: ListEmailVerificationRequest
        @return: ListEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_email_verification_with_options(request, runtime)

    async def list_email_verification_async(
        self,
        request: domain_20180129_models.ListEmailVerificationRequest,
    ) -> domain_20180129_models.ListEmailVerificationResponse:
        """
        @param request: ListEmailVerificationRequest
        @return: ListEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_email_verification_with_options_async(request, runtime)

    def list_server_lock_with_options(
        self,
        request: domain_20180129_models.ListServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ListServerLockResponse:
        """
        @summary Queries information about domain names for which registry locks are enabled.
        
        @param request: ListServerLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_start_date):
            query['BeginStartDate'] = request.begin_start_date
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_expire_date):
            query['EndExpireDate'] = request.end_expire_date
        if not UtilClient.is_unset(request.end_start_date):
            query['EndStartDate'] = request.end_start_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lock_product_id):
            query['LockProductId'] = request.lock_product_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.server_lock_status):
            query['ServerLockStatus'] = request.server_lock_status
        if not UtilClient.is_unset(request.start_expire_date):
            query['StartExpireDate'] = request.start_expire_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ListServerLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_lock_with_options_async(
        self,
        request: domain_20180129_models.ListServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ListServerLockResponse:
        """
        @summary Queries information about domain names for which registry locks are enabled.
        
        @param request: ListServerLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_start_date):
            query['BeginStartDate'] = request.begin_start_date
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_expire_date):
            query['EndExpireDate'] = request.end_expire_date
        if not UtilClient.is_unset(request.end_start_date):
            query['EndStartDate'] = request.end_start_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lock_product_id):
            query['LockProductId'] = request.lock_product_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.server_lock_status):
            query['ServerLockStatus'] = request.server_lock_status
        if not UtilClient.is_unset(request.start_expire_date):
            query['StartExpireDate'] = request.start_expire_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ListServerLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_lock(
        self,
        request: domain_20180129_models.ListServerLockRequest,
    ) -> domain_20180129_models.ListServerLockResponse:
        """
        @summary Queries information about domain names for which registry locks are enabled.
        
        @param request: ListServerLockRequest
        @return: ListServerLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_server_lock_with_options(request, runtime)

    async def list_server_lock_async(
        self,
        request: domain_20180129_models.ListServerLockRequest,
    ) -> domain_20180129_models.ListServerLockResponse:
        """
        @summary Queries information about domain names for which registry locks are enabled.
        
        @param request: ListServerLockRequest
        @return: ListServerLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_server_lock_with_options_async(request, runtime)

    def lookup_tmch_notice_with_options(
        self,
        request: domain_20180129_models.LookupTmchNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.LookupTmchNoticeResponse:
        """
        @param request: LookupTmchNoticeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LookupTmchNoticeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.claim_key):
            query['ClaimKey'] = request.claim_key
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LookupTmchNotice',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.LookupTmchNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def lookup_tmch_notice_with_options_async(
        self,
        request: domain_20180129_models.LookupTmchNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.LookupTmchNoticeResponse:
        """
        @param request: LookupTmchNoticeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LookupTmchNoticeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.claim_key):
            query['ClaimKey'] = request.claim_key
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LookupTmchNotice',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.LookupTmchNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lookup_tmch_notice(
        self,
        request: domain_20180129_models.LookupTmchNoticeRequest,
    ) -> domain_20180129_models.LookupTmchNoticeResponse:
        """
        @param request: LookupTmchNoticeRequest
        @return: LookupTmchNoticeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lookup_tmch_notice_with_options(request, runtime)

    async def lookup_tmch_notice_async(
        self,
        request: domain_20180129_models.LookupTmchNoticeRequest,
    ) -> domain_20180129_models.LookupTmchNoticeResponse:
        """
        @param request: LookupTmchNoticeRequest
        @return: LookupTmchNoticeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.lookup_tmch_notice_with_options_async(request, runtime)

    def poll_task_result_with_options(
        self,
        request: domain_20180129_models.PollTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.PollTaskResultResponse:
        """
        @param request: PollTaskResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PollTaskResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.task_result_status):
            query['TaskResultStatus'] = request.task_result_status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PollTaskResult',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.PollTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def poll_task_result_with_options_async(
        self,
        request: domain_20180129_models.PollTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.PollTaskResultResponse:
        """
        @param request: PollTaskResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PollTaskResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.task_result_status):
            query['TaskResultStatus'] = request.task_result_status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PollTaskResult',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.PollTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poll_task_result(
        self,
        request: domain_20180129_models.PollTaskResultRequest,
    ) -> domain_20180129_models.PollTaskResultResponse:
        """
        @param request: PollTaskResultRequest
        @return: PollTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.poll_task_result_with_options(request, runtime)

    async def poll_task_result_async(
        self,
        request: domain_20180129_models.PollTaskResultRequest,
    ) -> domain_20180129_models.PollTaskResultResponse:
        """
        @param request: PollTaskResultRequest
        @return: PollTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.poll_task_result_with_options_async(request, runtime)

    def query_advanced_domain_list_with_options(
        self,
        request: domain_20180129_models.QueryAdvancedDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryAdvancedDomainListResponse:
        """
        @summary 搜索域名列表
        
        @param request: QueryAdvancedDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAdvancedDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.domain_name_sort):
            query['DomainNameSort'] = request.domain_name_sort
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not UtilClient.is_unset(request.end_length):
            query['EndLength'] = request.end_length
        if not UtilClient.is_unset(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not UtilClient.is_unset(request.excluded):
            query['Excluded'] = request.excluded
        if not UtilClient.is_unset(request.excluded_prefix):
            query['ExcludedPrefix'] = request.excluded_prefix
        if not UtilClient.is_unset(request.excluded_suffix):
            query['ExcludedSuffix'] = request.excluded_suffix
        if not UtilClient.is_unset(request.expiration_date_sort):
            query['ExpirationDateSort'] = request.expiration_date_sort
        if not UtilClient.is_unset(request.form):
            query['Form'] = request.form
        if not UtilClient.is_unset(request.is_premium_domain):
            query['IsPremiumDomain'] = request.is_premium_domain
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.key_word_prefix):
            query['KeyWordPrefix'] = request.key_word_prefix
        if not UtilClient.is_unset(request.key_word_suffix):
            query['KeyWordSuffix'] = request.key_word_suffix
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not UtilClient.is_unset(request.product_domain_type_sort):
            query['ProductDomainTypeSort'] = request.product_domain_type_sort
        if not UtilClient.is_unset(request.registration_date_sort):
            query['RegistrationDateSort'] = request.registration_date_sort
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not UtilClient.is_unset(request.start_length):
            query['StartLength'] = request.start_length
        if not UtilClient.is_unset(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not UtilClient.is_unset(request.suffixs):
            query['Suffixs'] = request.suffixs
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.trade_type):
            query['TradeType'] = request.trade_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAdvancedDomainList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryAdvancedDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_advanced_domain_list_with_options_async(
        self,
        request: domain_20180129_models.QueryAdvancedDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryAdvancedDomainListResponse:
        """
        @summary 搜索域名列表
        
        @param request: QueryAdvancedDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAdvancedDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.domain_name_sort):
            query['DomainNameSort'] = request.domain_name_sort
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not UtilClient.is_unset(request.end_length):
            query['EndLength'] = request.end_length
        if not UtilClient.is_unset(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not UtilClient.is_unset(request.excluded):
            query['Excluded'] = request.excluded
        if not UtilClient.is_unset(request.excluded_prefix):
            query['ExcludedPrefix'] = request.excluded_prefix
        if not UtilClient.is_unset(request.excluded_suffix):
            query['ExcludedSuffix'] = request.excluded_suffix
        if not UtilClient.is_unset(request.expiration_date_sort):
            query['ExpirationDateSort'] = request.expiration_date_sort
        if not UtilClient.is_unset(request.form):
            query['Form'] = request.form
        if not UtilClient.is_unset(request.is_premium_domain):
            query['IsPremiumDomain'] = request.is_premium_domain
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.key_word_prefix):
            query['KeyWordPrefix'] = request.key_word_prefix
        if not UtilClient.is_unset(request.key_word_suffix):
            query['KeyWordSuffix'] = request.key_word_suffix
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not UtilClient.is_unset(request.product_domain_type_sort):
            query['ProductDomainTypeSort'] = request.product_domain_type_sort
        if not UtilClient.is_unset(request.registration_date_sort):
            query['RegistrationDateSort'] = request.registration_date_sort
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not UtilClient.is_unset(request.start_length):
            query['StartLength'] = request.start_length
        if not UtilClient.is_unset(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not UtilClient.is_unset(request.suffixs):
            query['Suffixs'] = request.suffixs
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.trade_type):
            query['TradeType'] = request.trade_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAdvancedDomainList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryAdvancedDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_advanced_domain_list(
        self,
        request: domain_20180129_models.QueryAdvancedDomainListRequest,
    ) -> domain_20180129_models.QueryAdvancedDomainListResponse:
        """
        @summary 搜索域名列表
        
        @param request: QueryAdvancedDomainListRequest
        @return: QueryAdvancedDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_advanced_domain_list_with_options(request, runtime)

    async def query_advanced_domain_list_async(
        self,
        request: domain_20180129_models.QueryAdvancedDomainListRequest,
    ) -> domain_20180129_models.QueryAdvancedDomainListResponse:
        """
        @summary 搜索域名列表
        
        @param request: QueryAdvancedDomainListRequest
        @return: QueryAdvancedDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_advanced_domain_list_with_options_async(request, runtime)

    def query_art_extension_with_options(
        self,
        request: domain_20180129_models.QueryArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryArtExtensionResponse:
        """
        @param request: QueryArtExtensionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryArtExtensionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryArtExtension',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryArtExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_art_extension_with_options_async(
        self,
        request: domain_20180129_models.QueryArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryArtExtensionResponse:
        """
        @param request: QueryArtExtensionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryArtExtensionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryArtExtension',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryArtExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_art_extension(
        self,
        request: domain_20180129_models.QueryArtExtensionRequest,
    ) -> domain_20180129_models.QueryArtExtensionResponse:
        """
        @param request: QueryArtExtensionRequest
        @return: QueryArtExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_art_extension_with_options(request, runtime)

    async def query_art_extension_async(
        self,
        request: domain_20180129_models.QueryArtExtensionRequest,
    ) -> domain_20180129_models.QueryArtExtensionResponse:
        """
        @param request: QueryArtExtensionRequest
        @return: QueryArtExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_art_extension_with_options_async(request, runtime)

    def query_change_log_list_with_options(
        self,
        request: domain_20180129_models.QueryChangeLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryChangeLogListResponse:
        """
        @param request: QueryChangeLogListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChangeLogListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryChangeLogList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryChangeLogListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_change_log_list_with_options_async(
        self,
        request: domain_20180129_models.QueryChangeLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryChangeLogListResponse:
        """
        @param request: QueryChangeLogListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChangeLogListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryChangeLogList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryChangeLogListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_change_log_list(
        self,
        request: domain_20180129_models.QueryChangeLogListRequest,
    ) -> domain_20180129_models.QueryChangeLogListResponse:
        """
        @param request: QueryChangeLogListRequest
        @return: QueryChangeLogListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_change_log_list_with_options(request, runtime)

    async def query_change_log_list_async(
        self,
        request: domain_20180129_models.QueryChangeLogListRequest,
    ) -> domain_20180129_models.QueryChangeLogListResponse:
        """
        @param request: QueryChangeLogListRequest
        @return: QueryChangeLogListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_change_log_list_with_options_async(request, runtime)

    def query_contact_info_with_options(
        self,
        request: domain_20180129_models.QueryContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryContactInfoResponse:
        """
        @param request: QueryContactInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryContactInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryContactInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryContactInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_contact_info_with_options_async(
        self,
        request: domain_20180129_models.QueryContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryContactInfoResponse:
        """
        @param request: QueryContactInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryContactInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryContactInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryContactInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_contact_info(
        self,
        request: domain_20180129_models.QueryContactInfoRequest,
    ) -> domain_20180129_models.QueryContactInfoResponse:
        """
        @param request: QueryContactInfoRequest
        @return: QueryContactInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_contact_info_with_options(request, runtime)

    async def query_contact_info_async(
        self,
        request: domain_20180129_models.QueryContactInfoRequest,
    ) -> domain_20180129_models.QueryContactInfoResponse:
        """
        @param request: QueryContactInfoRequest
        @return: QueryContactInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_contact_info_with_options_async(request, runtime)

    def query_dsrecord_with_options(
        self,
        request: domain_20180129_models.QueryDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDSRecordResponse:
        """
        @param request: QueryDSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDSRecord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dsrecord_with_options_async(
        self,
        request: domain_20180129_models.QueryDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDSRecordResponse:
        """
        @param request: QueryDSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDSRecord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dsrecord(
        self,
        request: domain_20180129_models.QueryDSRecordRequest,
    ) -> domain_20180129_models.QueryDSRecordResponse:
        """
        @param request: QueryDSRecordRequest
        @return: QueryDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_dsrecord_with_options(request, runtime)

    async def query_dsrecord_async(
        self,
        request: domain_20180129_models.QueryDSRecordRequest,
    ) -> domain_20180129_models.QueryDSRecordResponse:
        """
        @param request: QueryDSRecordRequest
        @return: QueryDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_dsrecord_with_options_async(request, runtime)

    def query_dns_host_with_options(
        self,
        request: domain_20180129_models.QueryDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDnsHostResponse:
        """
        @param request: QueryDnsHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDnsHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDnsHost',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dns_host_with_options_async(
        self,
        request: domain_20180129_models.QueryDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDnsHostResponse:
        """
        @param request: QueryDnsHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDnsHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDnsHost',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dns_host(
        self,
        request: domain_20180129_models.QueryDnsHostRequest,
    ) -> domain_20180129_models.QueryDnsHostResponse:
        """
        @param request: QueryDnsHostRequest
        @return: QueryDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_dns_host_with_options(request, runtime)

    async def query_dns_host_async(
        self,
        request: domain_20180129_models.QueryDnsHostRequest,
    ) -> domain_20180129_models.QueryDnsHostResponse:
        """
        @param request: QueryDnsHostRequest
        @return: QueryDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_dns_host_with_options_async(request, runtime)

    def query_domain_admin_division_with_options(
        self,
        request: domain_20180129_models.QueryDomainAdminDivisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainAdminDivisionResponse:
        """
        @param request: QueryDomainAdminDivisionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainAdminDivisionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainAdminDivision',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainAdminDivisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_admin_division_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainAdminDivisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainAdminDivisionResponse:
        """
        @param request: QueryDomainAdminDivisionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainAdminDivisionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainAdminDivision',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainAdminDivisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_admin_division(
        self,
        request: domain_20180129_models.QueryDomainAdminDivisionRequest,
    ) -> domain_20180129_models.QueryDomainAdminDivisionResponse:
        """
        @param request: QueryDomainAdminDivisionRequest
        @return: QueryDomainAdminDivisionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_admin_division_with_options(request, runtime)

    async def query_domain_admin_division_async(
        self,
        request: domain_20180129_models.QueryDomainAdminDivisionRequest,
    ) -> domain_20180129_models.QueryDomainAdminDivisionResponse:
        """
        @param request: QueryDomainAdminDivisionRequest
        @return: QueryDomainAdminDivisionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_admin_division_with_options_async(request, runtime)

    def query_domain_by_domain_name_with_options(
        self,
        request: domain_20180129_models.QueryDomainByDomainNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainByDomainNameResponse:
        """
        @summary Queries the information about a domain name.
        
        @param request: QueryDomainByDomainNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainByDomainNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainByDomainName',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainByDomainNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_by_domain_name_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainByDomainNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainByDomainNameResponse:
        """
        @summary Queries the information about a domain name.
        
        @param request: QueryDomainByDomainNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainByDomainNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainByDomainName',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainByDomainNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_by_domain_name(
        self,
        request: domain_20180129_models.QueryDomainByDomainNameRequest,
    ) -> domain_20180129_models.QueryDomainByDomainNameResponse:
        """
        @summary Queries the information about a domain name.
        
        @param request: QueryDomainByDomainNameRequest
        @return: QueryDomainByDomainNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_by_domain_name_with_options(request, runtime)

    async def query_domain_by_domain_name_async(
        self,
        request: domain_20180129_models.QueryDomainByDomainNameRequest,
    ) -> domain_20180129_models.QueryDomainByDomainNameResponse:
        """
        @summary Queries the information about a domain name.
        
        @param request: QueryDomainByDomainNameRequest
        @return: QueryDomainByDomainNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_by_domain_name_with_options_async(request, runtime)

    def query_domain_by_instance_id_with_options(
        self,
        request: domain_20180129_models.QueryDomainByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainByInstanceIdResponse:
        """
        @summary 根据实例id查询域名信息
        
        @param request: QueryDomainByInstanceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainByInstanceIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainByInstanceId',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_by_instance_id_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainByInstanceIdResponse:
        """
        @summary 根据实例id查询域名信息
        
        @param request: QueryDomainByInstanceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainByInstanceIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainByInstanceId',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_by_instance_id(
        self,
        request: domain_20180129_models.QueryDomainByInstanceIdRequest,
    ) -> domain_20180129_models.QueryDomainByInstanceIdResponse:
        """
        @summary 根据实例id查询域名信息
        
        @param request: QueryDomainByInstanceIdRequest
        @return: QueryDomainByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_by_instance_id_with_options(request, runtime)

    async def query_domain_by_instance_id_async(
        self,
        request: domain_20180129_models.QueryDomainByInstanceIdRequest,
    ) -> domain_20180129_models.QueryDomainByInstanceIdResponse:
        """
        @summary 根据实例id查询域名信息
        
        @param request: QueryDomainByInstanceIdRequest
        @return: QueryDomainByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_by_instance_id_with_options_async(request, runtime)

    def query_domain_group_list_with_options(
        self,
        request: domain_20180129_models.QueryDomainGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainGroupListResponse:
        """
        @param request: QueryDomainGroupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainGroupListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_group_name):
            query['DomainGroupName'] = request.domain_group_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.show_deleting_group):
            query['ShowDeletingGroup'] = request.show_deleting_group
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainGroupList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_group_list_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainGroupListResponse:
        """
        @param request: QueryDomainGroupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainGroupListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_group_name):
            query['DomainGroupName'] = request.domain_group_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.show_deleting_group):
            query['ShowDeletingGroup'] = request.show_deleting_group
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainGroupList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_group_list(
        self,
        request: domain_20180129_models.QueryDomainGroupListRequest,
    ) -> domain_20180129_models.QueryDomainGroupListResponse:
        """
        @param request: QueryDomainGroupListRequest
        @return: QueryDomainGroupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_group_list_with_options(request, runtime)

    async def query_domain_group_list_async(
        self,
        request: domain_20180129_models.QueryDomainGroupListRequest,
    ) -> domain_20180129_models.QueryDomainGroupListResponse:
        """
        @param request: QueryDomainGroupListRequest
        @return: QueryDomainGroupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_group_list_with_options_async(request, runtime)

    def query_domain_list_with_options(
        self,
        request: domain_20180129_models.QueryDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainListResponse:
        """
        @summary Queries a list of domain names within your Alibaba Cloud account by page.
        
        @param request: QueryDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccompany):
            query['Ccompany'] = request.ccompany
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not UtilClient.is_unset(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not UtilClient.is_unset(request.order_key_type):
            query['OrderKeyType'] = request.order_key_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not UtilClient.is_unset(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_list_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainListResponse:
        """
        @summary Queries a list of domain names within your Alibaba Cloud account by page.
        
        @param request: QueryDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccompany):
            query['Ccompany'] = request.ccompany
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not UtilClient.is_unset(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not UtilClient.is_unset(request.order_key_type):
            query['OrderKeyType'] = request.order_key_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not UtilClient.is_unset(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_list(
        self,
        request: domain_20180129_models.QueryDomainListRequest,
    ) -> domain_20180129_models.QueryDomainListResponse:
        """
        @summary Queries a list of domain names within your Alibaba Cloud account by page.
        
        @param request: QueryDomainListRequest
        @return: QueryDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_list_with_options(request, runtime)

    async def query_domain_list_async(
        self,
        request: domain_20180129_models.QueryDomainListRequest,
    ) -> domain_20180129_models.QueryDomainListResponse:
        """
        @summary Queries a list of domain names within your Alibaba Cloud account by page.
        
        @param request: QueryDomainListRequest
        @return: QueryDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_list_with_options_async(request, runtime)

    def query_domain_real_name_verification_info_with_options(
        self,
        request: domain_20180129_models.QueryDomainRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainRealNameVerificationInfoResponse:
        """
        @param request: QueryDomainRealNameVerificationInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainRealNameVerificationInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.fetch_image):
            query['FetchImage'] = request.fetch_image
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainRealNameVerificationInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainRealNameVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_real_name_verification_info_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainRealNameVerificationInfoResponse:
        """
        @param request: QueryDomainRealNameVerificationInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainRealNameVerificationInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.fetch_image):
            query['FetchImage'] = request.fetch_image
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainRealNameVerificationInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainRealNameVerificationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_real_name_verification_info(
        self,
        request: domain_20180129_models.QueryDomainRealNameVerificationInfoRequest,
    ) -> domain_20180129_models.QueryDomainRealNameVerificationInfoResponse:
        """
        @param request: QueryDomainRealNameVerificationInfoRequest
        @return: QueryDomainRealNameVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_real_name_verification_info_with_options(request, runtime)

    async def query_domain_real_name_verification_info_async(
        self,
        request: domain_20180129_models.QueryDomainRealNameVerificationInfoRequest,
    ) -> domain_20180129_models.QueryDomainRealNameVerificationInfoResponse:
        """
        @param request: QueryDomainRealNameVerificationInfoRequest
        @return: QueryDomainRealNameVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_real_name_verification_info_with_options_async(request, runtime)

    def query_domain_special_biz_detail_with_options(
        self,
        request: domain_20180129_models.QueryDomainSpecialBizDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainSpecialBizDetailResponse:
        """
        @summary 查询域名特殊业务详情
        
        @param request: QueryDomainSpecialBizDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainSpecialBizDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDomainSpecialBizDetail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainSpecialBizDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_special_biz_detail_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainSpecialBizDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainSpecialBizDetailResponse:
        """
        @summary 查询域名特殊业务详情
        
        @param request: QueryDomainSpecialBizDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainSpecialBizDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDomainSpecialBizDetail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainSpecialBizDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_special_biz_detail(
        self,
        request: domain_20180129_models.QueryDomainSpecialBizDetailRequest,
    ) -> domain_20180129_models.QueryDomainSpecialBizDetailResponse:
        """
        @summary 查询域名特殊业务详情
        
        @param request: QueryDomainSpecialBizDetailRequest
        @return: QueryDomainSpecialBizDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_special_biz_detail_with_options(request, runtime)

    async def query_domain_special_biz_detail_async(
        self,
        request: domain_20180129_models.QueryDomainSpecialBizDetailRequest,
    ) -> domain_20180129_models.QueryDomainSpecialBizDetailResponse:
        """
        @summary 查询域名特殊业务详情
        
        @param request: QueryDomainSpecialBizDetailRequest
        @return: QueryDomainSpecialBizDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_special_biz_detail_with_options_async(request, runtime)

    def query_domain_special_biz_info_by_domain_with_options(
        self,
        request: domain_20180129_models.QueryDomainSpecialBizInfoByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainSpecialBizInfoByDomainResponse:
        """
        @summary 通过域名查询域名特殊业务详情
        
        @param request: QueryDomainSpecialBizInfoByDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainSpecialBizInfoByDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDomainSpecialBizInfoByDomain',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainSpecialBizInfoByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_special_biz_info_by_domain_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainSpecialBizInfoByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainSpecialBizInfoByDomainResponse:
        """
        @summary 通过域名查询域名特殊业务详情
        
        @param request: QueryDomainSpecialBizInfoByDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainSpecialBizInfoByDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDomainSpecialBizInfoByDomain',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainSpecialBizInfoByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_special_biz_info_by_domain(
        self,
        request: domain_20180129_models.QueryDomainSpecialBizInfoByDomainRequest,
    ) -> domain_20180129_models.QueryDomainSpecialBizInfoByDomainResponse:
        """
        @summary 通过域名查询域名特殊业务详情
        
        @param request: QueryDomainSpecialBizInfoByDomainRequest
        @return: QueryDomainSpecialBizInfoByDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_special_biz_info_by_domain_with_options(request, runtime)

    async def query_domain_special_biz_info_by_domain_async(
        self,
        request: domain_20180129_models.QueryDomainSpecialBizInfoByDomainRequest,
    ) -> domain_20180129_models.QueryDomainSpecialBizInfoByDomainResponse:
        """
        @summary 通过域名查询域名特殊业务详情
        
        @param request: QueryDomainSpecialBizInfoByDomainRequest
        @return: QueryDomainSpecialBizInfoByDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_special_biz_info_by_domain_with_options_async(request, runtime)

    def query_domain_suffix_with_options(
        self,
        request: domain_20180129_models.QueryDomainSuffixRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainSuffixResponse:
        """
        @param request: QueryDomainSuffixRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainSuffixResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainSuffix',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainSuffixResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_suffix_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainSuffixRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainSuffixResponse:
        """
        @param request: QueryDomainSuffixRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainSuffixResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainSuffix',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryDomainSuffixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_suffix(
        self,
        request: domain_20180129_models.QueryDomainSuffixRequest,
    ) -> domain_20180129_models.QueryDomainSuffixResponse:
        """
        @param request: QueryDomainSuffixRequest
        @return: QueryDomainSuffixResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_suffix_with_options(request, runtime)

    async def query_domain_suffix_async(
        self,
        request: domain_20180129_models.QueryDomainSuffixRequest,
    ) -> domain_20180129_models.QueryDomainSuffixResponse:
        """
        @param request: QueryDomainSuffixRequest
        @return: QueryDomainSuffixResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_suffix_with_options_async(request, runtime)

    def query_email_verification_with_options(
        self,
        request: domain_20180129_models.QueryEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryEmailVerificationResponse:
        """
        @summary 查询邮箱验证状态
        
        @param request: QueryEmailVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEmailVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEmailVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_email_verification_with_options_async(
        self,
        request: domain_20180129_models.QueryEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryEmailVerificationResponse:
        """
        @summary 查询邮箱验证状态
        
        @param request: QueryEmailVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEmailVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEmailVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_email_verification(
        self,
        request: domain_20180129_models.QueryEmailVerificationRequest,
    ) -> domain_20180129_models.QueryEmailVerificationResponse:
        """
        @summary 查询邮箱验证状态
        
        @param request: QueryEmailVerificationRequest
        @return: QueryEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_email_verification_with_options(request, runtime)

    async def query_email_verification_async(
        self,
        request: domain_20180129_models.QueryEmailVerificationRequest,
    ) -> domain_20180129_models.QueryEmailVerificationResponse:
        """
        @summary 查询邮箱验证状态
        
        @param request: QueryEmailVerificationRequest
        @return: QueryEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_email_verification_with_options_async(request, runtime)

    def query_ens_association_with_options(
        self,
        request: domain_20180129_models.QueryEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryEnsAssociationResponse:
        """
        @param request: QueryEnsAssociationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEnsAssociationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnsAssociation',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryEnsAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ens_association_with_options_async(
        self,
        request: domain_20180129_models.QueryEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryEnsAssociationResponse:
        """
        @param request: QueryEnsAssociationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEnsAssociationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnsAssociation',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryEnsAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ens_association(
        self,
        request: domain_20180129_models.QueryEnsAssociationRequest,
    ) -> domain_20180129_models.QueryEnsAssociationResponse:
        """
        @param request: QueryEnsAssociationRequest
        @return: QueryEnsAssociationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_ens_association_with_options(request, runtime)

    async def query_ens_association_async(
        self,
        request: domain_20180129_models.QueryEnsAssociationRequest,
    ) -> domain_20180129_models.QueryEnsAssociationResponse:
        """
        @param request: QueryEnsAssociationRequest
        @return: QueryEnsAssociationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_ens_association_with_options_async(request, runtime)

    def query_fail_reason_for_domain_real_name_verification_with_options(
        self,
        request: domain_20180129_models.QueryFailReasonForDomainRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForDomainRealNameVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFailReasonForDomainRealNameVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.real_name_verification_action):
            query['RealNameVerificationAction'] = request.real_name_verification_action
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailReasonForDomainRealNameVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fail_reason_for_domain_real_name_verification_with_options_async(
        self,
        request: domain_20180129_models.QueryFailReasonForDomainRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForDomainRealNameVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFailReasonForDomainRealNameVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.real_name_verification_action):
            query['RealNameVerificationAction'] = request.real_name_verification_action
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailReasonForDomainRealNameVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fail_reason_for_domain_real_name_verification(
        self,
        request: domain_20180129_models.QueryFailReasonForDomainRealNameVerificationRequest,
    ) -> domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForDomainRealNameVerificationRequest
        @return: QueryFailReasonForDomainRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_fail_reason_for_domain_real_name_verification_with_options(request, runtime)

    async def query_fail_reason_for_domain_real_name_verification_async(
        self,
        request: domain_20180129_models.QueryFailReasonForDomainRealNameVerificationRequest,
    ) -> domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForDomainRealNameVerificationRequest
        @return: QueryFailReasonForDomainRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_fail_reason_for_domain_real_name_verification_with_options_async(request, runtime)

    def query_fail_reason_for_registrant_profile_real_name_verification_with_options(
        self,
        request: domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForRegistrantProfileRealNameVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFailReasonForRegistrantProfileRealNameVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileID'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailReasonForRegistrantProfileRealNameVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fail_reason_for_registrant_profile_real_name_verification_with_options_async(
        self,
        request: domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForRegistrantProfileRealNameVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFailReasonForRegistrantProfileRealNameVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileID'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailReasonForRegistrantProfileRealNameVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fail_reason_for_registrant_profile_real_name_verification(
        self,
        request: domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
    ) -> domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForRegistrantProfileRealNameVerificationRequest
        @return: QueryFailReasonForRegistrantProfileRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_fail_reason_for_registrant_profile_real_name_verification_with_options(request, runtime)

    async def query_fail_reason_for_registrant_profile_real_name_verification_async(
        self,
        request: domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
    ) -> domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForRegistrantProfileRealNameVerificationRequest
        @return: QueryFailReasonForRegistrantProfileRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_fail_reason_for_registrant_profile_real_name_verification_with_options_async(request, runtime)

    def query_failing_reason_list_for_qualification_with_options(
        self,
        request: domain_20180129_models.QueryFailingReasonListForQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailingReasonListForQualificationResponse:
        """
        @param request: QueryFailingReasonListForQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFailingReasonListForQualificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailingReasonListForQualification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryFailingReasonListForQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_failing_reason_list_for_qualification_with_options_async(
        self,
        request: domain_20180129_models.QueryFailingReasonListForQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailingReasonListForQualificationResponse:
        """
        @param request: QueryFailingReasonListForQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFailingReasonListForQualificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailingReasonListForQualification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryFailingReasonListForQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_failing_reason_list_for_qualification(
        self,
        request: domain_20180129_models.QueryFailingReasonListForQualificationRequest,
    ) -> domain_20180129_models.QueryFailingReasonListForQualificationResponse:
        """
        @param request: QueryFailingReasonListForQualificationRequest
        @return: QueryFailingReasonListForQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_failing_reason_list_for_qualification_with_options(request, runtime)

    async def query_failing_reason_list_for_qualification_async(
        self,
        request: domain_20180129_models.QueryFailingReasonListForQualificationRequest,
    ) -> domain_20180129_models.QueryFailingReasonListForQualificationResponse:
        """
        @param request: QueryFailingReasonListForQualificationRequest
        @return: QueryFailingReasonListForQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_failing_reason_list_for_qualification_with_options_async(request, runtime)

    def query_local_ens_association_with_options(
        self,
        request: domain_20180129_models.QueryLocalEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryLocalEnsAssociationResponse:
        """
        @param request: QueryLocalEnsAssociationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLocalEnsAssociationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLocalEnsAssociation',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryLocalEnsAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_local_ens_association_with_options_async(
        self,
        request: domain_20180129_models.QueryLocalEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryLocalEnsAssociationResponse:
        """
        @param request: QueryLocalEnsAssociationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLocalEnsAssociationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLocalEnsAssociation',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryLocalEnsAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_local_ens_association(
        self,
        request: domain_20180129_models.QueryLocalEnsAssociationRequest,
    ) -> domain_20180129_models.QueryLocalEnsAssociationResponse:
        """
        @param request: QueryLocalEnsAssociationRequest
        @return: QueryLocalEnsAssociationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_local_ens_association_with_options(request, runtime)

    async def query_local_ens_association_async(
        self,
        request: domain_20180129_models.QueryLocalEnsAssociationRequest,
    ) -> domain_20180129_models.QueryLocalEnsAssociationResponse:
        """
        @param request: QueryLocalEnsAssociationRequest
        @return: QueryLocalEnsAssociationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_local_ens_association_with_options_async(request, runtime)

    def query_operation_audit_info_detail_with_options(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryOperationAuditInfoDetailResponse:
        """
        @param request: QueryOperationAuditInfoDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOperationAuditInfoDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOperationAuditInfoDetail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryOperationAuditInfoDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_operation_audit_info_detail_with_options_async(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryOperationAuditInfoDetailResponse:
        """
        @param request: QueryOperationAuditInfoDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOperationAuditInfoDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOperationAuditInfoDetail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryOperationAuditInfoDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_operation_audit_info_detail(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoDetailRequest,
    ) -> domain_20180129_models.QueryOperationAuditInfoDetailResponse:
        """
        @param request: QueryOperationAuditInfoDetailRequest
        @return: QueryOperationAuditInfoDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_operation_audit_info_detail_with_options(request, runtime)

    async def query_operation_audit_info_detail_async(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoDetailRequest,
    ) -> domain_20180129_models.QueryOperationAuditInfoDetailResponse:
        """
        @param request: QueryOperationAuditInfoDetailRequest
        @return: QueryOperationAuditInfoDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_operation_audit_info_detail_with_options_async(request, runtime)

    def query_operation_audit_info_list_with_options(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryOperationAuditInfoListResponse:
        """
        @param request: QueryOperationAuditInfoListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOperationAuditInfoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.audit_type):
            query['AuditType'] = request.audit_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOperationAuditInfoList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryOperationAuditInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_operation_audit_info_list_with_options_async(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryOperationAuditInfoListResponse:
        """
        @param request: QueryOperationAuditInfoListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOperationAuditInfoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.audit_type):
            query['AuditType'] = request.audit_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOperationAuditInfoList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryOperationAuditInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_operation_audit_info_list(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoListRequest,
    ) -> domain_20180129_models.QueryOperationAuditInfoListResponse:
        """
        @param request: QueryOperationAuditInfoListRequest
        @return: QueryOperationAuditInfoListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_operation_audit_info_list_with_options(request, runtime)

    async def query_operation_audit_info_list_async(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoListRequest,
    ) -> domain_20180129_models.QueryOperationAuditInfoListResponse:
        """
        @param request: QueryOperationAuditInfoListRequest
        @return: QueryOperationAuditInfoListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_operation_audit_info_list_with_options_async(request, runtime)

    def query_qualification_detail_with_options(
        self,
        request: domain_20180129_models.QueryQualificationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryQualificationDetailResponse:
        """
        @param request: QueryQualificationDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryQualificationDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryQualificationDetail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryQualificationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_qualification_detail_with_options_async(
        self,
        request: domain_20180129_models.QueryQualificationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryQualificationDetailResponse:
        """
        @param request: QueryQualificationDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryQualificationDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryQualificationDetail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryQualificationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_qualification_detail(
        self,
        request: domain_20180129_models.QueryQualificationDetailRequest,
    ) -> domain_20180129_models.QueryQualificationDetailResponse:
        """
        @param request: QueryQualificationDetailRequest
        @return: QueryQualificationDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_qualification_detail_with_options(request, runtime)

    async def query_qualification_detail_async(
        self,
        request: domain_20180129_models.QueryQualificationDetailRequest,
    ) -> domain_20180129_models.QueryQualificationDetailResponse:
        """
        @param request: QueryQualificationDetailRequest
        @return: QueryQualificationDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_qualification_detail_with_options_async(request, runtime)

    def query_registrant_profile_real_name_verification_info_with_options(
        self,
        request: domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        """
        @param request: QueryRegistrantProfileRealNameVerificationInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRegistrantProfileRealNameVerificationInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_image):
            query['FetchImage'] = request.fetch_image
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRegistrantProfileRealNameVerificationInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_registrant_profile_real_name_verification_info_with_options_async(
        self,
        request: domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        """
        @param request: QueryRegistrantProfileRealNameVerificationInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRegistrantProfileRealNameVerificationInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_image):
            query['FetchImage'] = request.fetch_image
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRegistrantProfileRealNameVerificationInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_registrant_profile_real_name_verification_info(
        self,
        request: domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
    ) -> domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        """
        @param request: QueryRegistrantProfileRealNameVerificationInfoRequest
        @return: QueryRegistrantProfileRealNameVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_registrant_profile_real_name_verification_info_with_options(request, runtime)

    async def query_registrant_profile_real_name_verification_info_async(
        self,
        request: domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
    ) -> domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        """
        @param request: QueryRegistrantProfileRealNameVerificationInfoRequest
        @return: QueryRegistrantProfileRealNameVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_registrant_profile_real_name_verification_info_with_options_async(request, runtime)

    def query_registrant_profiles_with_options(
        self,
        request: domain_20180129_models.QueryRegistrantProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryRegistrantProfilesResponse:
        """
        @param request: QueryRegistrantProfilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRegistrantProfilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_registrant_profile):
            query['DefaultRegistrantProfile'] = request.default_registrant_profile
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.real_name_status):
            query['RealNameStatus'] = request.real_name_status
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRegistrantProfiles',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryRegistrantProfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_registrant_profiles_with_options_async(
        self,
        request: domain_20180129_models.QueryRegistrantProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryRegistrantProfilesResponse:
        """
        @param request: QueryRegistrantProfilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRegistrantProfilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_registrant_profile):
            query['DefaultRegistrantProfile'] = request.default_registrant_profile
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.real_name_status):
            query['RealNameStatus'] = request.real_name_status
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRegistrantProfiles',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryRegistrantProfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_registrant_profiles(
        self,
        request: domain_20180129_models.QueryRegistrantProfilesRequest,
    ) -> domain_20180129_models.QueryRegistrantProfilesResponse:
        """
        @param request: QueryRegistrantProfilesRequest
        @return: QueryRegistrantProfilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_registrant_profiles_with_options(request, runtime)

    async def query_registrant_profiles_async(
        self,
        request: domain_20180129_models.QueryRegistrantProfilesRequest,
    ) -> domain_20180129_models.QueryRegistrantProfilesResponse:
        """
        @param request: QueryRegistrantProfilesRequest
        @return: QueryRegistrantProfilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_registrant_profiles_with_options_async(request, runtime)

    def query_server_lock_with_options(
        self,
        request: domain_20180129_models.QueryServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryServerLockResponse:
        """
        @param request: QueryServerLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryServerLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryServerLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryServerLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_server_lock_with_options_async(
        self,
        request: domain_20180129_models.QueryServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryServerLockResponse:
        """
        @param request: QueryServerLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryServerLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryServerLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryServerLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_server_lock(
        self,
        request: domain_20180129_models.QueryServerLockRequest,
    ) -> domain_20180129_models.QueryServerLockResponse:
        """
        @param request: QueryServerLockRequest
        @return: QueryServerLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_server_lock_with_options(request, runtime)

    async def query_server_lock_async(
        self,
        request: domain_20180129_models.QueryServerLockRequest,
    ) -> domain_20180129_models.QueryServerLockResponse:
        """
        @param request: QueryServerLockRequest
        @return: QueryServerLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_server_lock_with_options_async(request, runtime)

    def query_task_detail_history_with_options(
        self,
        request: domain_20180129_models.QueryTaskDetailHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskDetailHistoryResponse:
        """
        @param request: QueryTaskDetailHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskDetailHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_name_cursor):
            query['DomainNameCursor'] = request.domain_name_cursor
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_detail_no_cursor):
            query['TaskDetailNoCursor'] = request.task_detail_no_cursor
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskDetailHistory',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTaskDetailHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_detail_history_with_options_async(
        self,
        request: domain_20180129_models.QueryTaskDetailHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskDetailHistoryResponse:
        """
        @param request: QueryTaskDetailHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskDetailHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_name_cursor):
            query['DomainNameCursor'] = request.domain_name_cursor
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_detail_no_cursor):
            query['TaskDetailNoCursor'] = request.task_detail_no_cursor
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskDetailHistory',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTaskDetailHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_detail_history(
        self,
        request: domain_20180129_models.QueryTaskDetailHistoryRequest,
    ) -> domain_20180129_models.QueryTaskDetailHistoryResponse:
        """
        @param request: QueryTaskDetailHistoryRequest
        @return: QueryTaskDetailHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_detail_history_with_options(request, runtime)

    async def query_task_detail_history_async(
        self,
        request: domain_20180129_models.QueryTaskDetailHistoryRequest,
    ) -> domain_20180129_models.QueryTaskDetailHistoryResponse:
        """
        @param request: QueryTaskDetailHistoryRequest
        @return: QueryTaskDetailHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_detail_history_with_options_async(request, runtime)

    def query_task_detail_list_with_options(
        self,
        request: domain_20180129_models.QueryTaskDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskDetailListResponse:
        """
        @param request: QueryTaskDetailListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskDetailListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskDetailList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTaskDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_detail_list_with_options_async(
        self,
        request: domain_20180129_models.QueryTaskDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskDetailListResponse:
        """
        @param request: QueryTaskDetailListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskDetailListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskDetailList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTaskDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_detail_list(
        self,
        request: domain_20180129_models.QueryTaskDetailListRequest,
    ) -> domain_20180129_models.QueryTaskDetailListResponse:
        """
        @param request: QueryTaskDetailListRequest
        @return: QueryTaskDetailListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_detail_list_with_options(request, runtime)

    async def query_task_detail_list_async(
        self,
        request: domain_20180129_models.QueryTaskDetailListRequest,
    ) -> domain_20180129_models.QueryTaskDetailListResponse:
        """
        @param request: QueryTaskDetailListRequest
        @return: QueryTaskDetailListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_detail_list_with_options_async(request, runtime)

    def query_task_info_history_with_options(
        self,
        request: domain_20180129_models.QueryTaskInfoHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskInfoHistoryResponse:
        """
        @param request: QueryTaskInfoHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskInfoHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not UtilClient.is_unset(request.create_time_cursor):
            query['CreateTimeCursor'] = request.create_time_cursor
        if not UtilClient.is_unset(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_no_cursor):
            query['TaskNoCursor'] = request.task_no_cursor
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskInfoHistory',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTaskInfoHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_info_history_with_options_async(
        self,
        request: domain_20180129_models.QueryTaskInfoHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskInfoHistoryResponse:
        """
        @param request: QueryTaskInfoHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskInfoHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not UtilClient.is_unset(request.create_time_cursor):
            query['CreateTimeCursor'] = request.create_time_cursor
        if not UtilClient.is_unset(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_no_cursor):
            query['TaskNoCursor'] = request.task_no_cursor
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskInfoHistory',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTaskInfoHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_info_history(
        self,
        request: domain_20180129_models.QueryTaskInfoHistoryRequest,
    ) -> domain_20180129_models.QueryTaskInfoHistoryResponse:
        """
        @param request: QueryTaskInfoHistoryRequest
        @return: QueryTaskInfoHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_info_history_with_options(request, runtime)

    async def query_task_info_history_async(
        self,
        request: domain_20180129_models.QueryTaskInfoHistoryRequest,
    ) -> domain_20180129_models.QueryTaskInfoHistoryResponse:
        """
        @param request: QueryTaskInfoHistoryRequest
        @return: QueryTaskInfoHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_info_history_with_options_async(request, runtime)

    def query_task_list_with_options(
        self,
        request: domain_20180129_models.QueryTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskListResponse:
        """
        @param request: QueryTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not UtilClient.is_unset(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_list_with_options_async(
        self,
        request: domain_20180129_models.QueryTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskListResponse:
        """
        @param request: QueryTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not UtilClient.is_unset(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_list(
        self,
        request: domain_20180129_models.QueryTaskListRequest,
    ) -> domain_20180129_models.QueryTaskListResponse:
        """
        @param request: QueryTaskListRequest
        @return: QueryTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_list_with_options(request, runtime)

    async def query_task_list_async(
        self,
        request: domain_20180129_models.QueryTaskListRequest,
    ) -> domain_20180129_models.QueryTaskListResponse:
        """
        @param request: QueryTaskListRequest
        @return: QueryTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_list_with_options_async(request, runtime)

    def query_transfer_in_by_instance_id_with_options(
        self,
        request: domain_20180129_models.QueryTransferInByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferInByInstanceIdResponse:
        """
        @param request: QueryTransferInByInstanceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTransferInByInstanceIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferInByInstanceId',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTransferInByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_in_by_instance_id_with_options_async(
        self,
        request: domain_20180129_models.QueryTransferInByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferInByInstanceIdResponse:
        """
        @param request: QueryTransferInByInstanceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTransferInByInstanceIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferInByInstanceId',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTransferInByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_in_by_instance_id(
        self,
        request: domain_20180129_models.QueryTransferInByInstanceIdRequest,
    ) -> domain_20180129_models.QueryTransferInByInstanceIdResponse:
        """
        @param request: QueryTransferInByInstanceIdRequest
        @return: QueryTransferInByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_in_by_instance_id_with_options(request, runtime)

    async def query_transfer_in_by_instance_id_async(
        self,
        request: domain_20180129_models.QueryTransferInByInstanceIdRequest,
    ) -> domain_20180129_models.QueryTransferInByInstanceIdResponse:
        """
        @param request: QueryTransferInByInstanceIdRequest
        @return: QueryTransferInByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_in_by_instance_id_with_options_async(request, runtime)

    def query_transfer_in_list_with_options(
        self,
        request: domain_20180129_models.QueryTransferInListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferInListResponse:
        """
        @param request: QueryTransferInListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTransferInListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.simple_transfer_in_status):
            query['SimpleTransferInStatus'] = request.simple_transfer_in_status
        if not UtilClient.is_unset(request.submission_end_date):
            query['SubmissionEndDate'] = request.submission_end_date
        if not UtilClient.is_unset(request.submission_start_date):
            query['SubmissionStartDate'] = request.submission_start_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferInList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTransferInListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_in_list_with_options_async(
        self,
        request: domain_20180129_models.QueryTransferInListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferInListResponse:
        """
        @param request: QueryTransferInListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTransferInListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.simple_transfer_in_status):
            query['SimpleTransferInStatus'] = request.simple_transfer_in_status
        if not UtilClient.is_unset(request.submission_end_date):
            query['SubmissionEndDate'] = request.submission_end_date
        if not UtilClient.is_unset(request.submission_start_date):
            query['SubmissionStartDate'] = request.submission_start_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferInList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTransferInListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_in_list(
        self,
        request: domain_20180129_models.QueryTransferInListRequest,
    ) -> domain_20180129_models.QueryTransferInListResponse:
        """
        @param request: QueryTransferInListRequest
        @return: QueryTransferInListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_in_list_with_options(request, runtime)

    async def query_transfer_in_list_async(
        self,
        request: domain_20180129_models.QueryTransferInListRequest,
    ) -> domain_20180129_models.QueryTransferInListResponse:
        """
        @param request: QueryTransferInListRequest
        @return: QueryTransferInListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_in_list_with_options_async(request, runtime)

    def query_transfer_out_info_with_options(
        self,
        request: domain_20180129_models.QueryTransferOutInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferOutInfoResponse:
        """
        @param request: QueryTransferOutInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTransferOutInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferOutInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTransferOutInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_out_info_with_options_async(
        self,
        request: domain_20180129_models.QueryTransferOutInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferOutInfoResponse:
        """
        @param request: QueryTransferOutInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTransferOutInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferOutInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.QueryTransferOutInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_out_info(
        self,
        request: domain_20180129_models.QueryTransferOutInfoRequest,
    ) -> domain_20180129_models.QueryTransferOutInfoResponse:
        """
        @param request: QueryTransferOutInfoRequest
        @return: QueryTransferOutInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_out_info_with_options(request, runtime)

    async def query_transfer_out_info_async(
        self,
        request: domain_20180129_models.QueryTransferOutInfoRequest,
    ) -> domain_20180129_models.QueryTransferOutInfoResponse:
        """
        @param request: QueryTransferOutInfoRequest
        @return: QueryTransferOutInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_out_info_with_options_async(request, runtime)

    def registrant_profile_real_name_verification_with_options(
        self,
        request: domain_20180129_models.RegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.RegistrantProfileRealNameVerificationResponse:
        """
        @summary 保存联系人模板实名资料
        
        @param request: RegistrantProfileRealNameVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegistrantProfileRealNameVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not UtilClient.is_unset(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileID'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegistrantProfileRealNameVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.RegistrantProfileRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def registrant_profile_real_name_verification_with_options_async(
        self,
        request: domain_20180129_models.RegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.RegistrantProfileRealNameVerificationResponse:
        """
        @summary 保存联系人模板实名资料
        
        @param request: RegistrantProfileRealNameVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegistrantProfileRealNameVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not UtilClient.is_unset(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileID'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegistrantProfileRealNameVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.RegistrantProfileRealNameVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def registrant_profile_real_name_verification(
        self,
        request: domain_20180129_models.RegistrantProfileRealNameVerificationRequest,
    ) -> domain_20180129_models.RegistrantProfileRealNameVerificationResponse:
        """
        @summary 保存联系人模板实名资料
        
        @param request: RegistrantProfileRealNameVerificationRequest
        @return: RegistrantProfileRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.registrant_profile_real_name_verification_with_options(request, runtime)

    async def registrant_profile_real_name_verification_async(
        self,
        request: domain_20180129_models.RegistrantProfileRealNameVerificationRequest,
    ) -> domain_20180129_models.RegistrantProfileRealNameVerificationResponse:
        """
        @summary 保存联系人模板实名资料
        
        @param request: RegistrantProfileRealNameVerificationRequest
        @return: RegistrantProfileRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.registrant_profile_real_name_verification_with_options_async(request, runtime)

    def resend_email_verification_with_options(
        self,
        request: domain_20180129_models.ResendEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ResendEmailVerificationResponse:
        """
        @summary 重新发送验证邮件
        
        @param request: ResendEmailVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResendEmailVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendEmailVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ResendEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_email_verification_with_options_async(
        self,
        request: domain_20180129_models.ResendEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ResendEmailVerificationResponse:
        """
        @summary 重新发送验证邮件
        
        @param request: ResendEmailVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResendEmailVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendEmailVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ResendEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_email_verification(
        self,
        request: domain_20180129_models.ResendEmailVerificationRequest,
    ) -> domain_20180129_models.ResendEmailVerificationResponse:
        """
        @summary 重新发送验证邮件
        
        @param request: ResendEmailVerificationRequest
        @return: ResendEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resend_email_verification_with_options(request, runtime)

    async def resend_email_verification_async(
        self,
        request: domain_20180129_models.ResendEmailVerificationRequest,
    ) -> domain_20180129_models.ResendEmailVerificationResponse:
        """
        @summary 重新发送验证邮件
        
        @param request: ResendEmailVerificationRequest
        @return: ResendEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resend_email_verification_with_options_async(request, runtime)

    def reset_qualification_verification_with_options(
        self,
        request: domain_20180129_models.ResetQualificationVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ResetQualificationVerificationResponse:
        """
        @summary 重置资质审核状态
        
        @param request: ResetQualificationVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetQualificationVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetQualificationVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ResetQualificationVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_qualification_verification_with_options_async(
        self,
        request: domain_20180129_models.ResetQualificationVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ResetQualificationVerificationResponse:
        """
        @summary 重置资质审核状态
        
        @param request: ResetQualificationVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetQualificationVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetQualificationVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ResetQualificationVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_qualification_verification(
        self,
        request: domain_20180129_models.ResetQualificationVerificationRequest,
    ) -> domain_20180129_models.ResetQualificationVerificationResponse:
        """
        @summary 重置资质审核状态
        
        @param request: ResetQualificationVerificationRequest
        @return: ResetQualificationVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_qualification_verification_with_options(request, runtime)

    async def reset_qualification_verification_async(
        self,
        request: domain_20180129_models.ResetQualificationVerificationRequest,
    ) -> domain_20180129_models.ResetQualificationVerificationResponse:
        """
        @summary 重置资质审核状态
        
        @param request: ResetQualificationVerificationRequest
        @return: ResetQualificationVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_qualification_verification_with_options_async(request, runtime)

    def save_batch_domain_remark_with_options(
        self,
        request: domain_20180129_models.SaveBatchDomainRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchDomainRemarkResponse:
        """
        @summary 批量保存域名备注信息
        
        @param request: SaveBatchDomainRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchDomainRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchDomainRemark',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchDomainRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_domain_remark_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchDomainRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchDomainRemarkResponse:
        """
        @summary 批量保存域名备注信息
        
        @param request: SaveBatchDomainRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchDomainRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchDomainRemark',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchDomainRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_domain_remark(
        self,
        request: domain_20180129_models.SaveBatchDomainRemarkRequest,
    ) -> domain_20180129_models.SaveBatchDomainRemarkResponse:
        """
        @summary 批量保存域名备注信息
        
        @param request: SaveBatchDomainRemarkRequest
        @return: SaveBatchDomainRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_domain_remark_with_options(request, runtime)

    async def save_batch_domain_remark_async(
        self,
        request: domain_20180129_models.SaveBatchDomainRemarkRequest,
    ) -> domain_20180129_models.SaveBatchDomainRemarkResponse:
        """
        @summary 批量保存域名备注信息
        
        @param request: SaveBatchDomainRemarkRequest
        @return: SaveBatchDomainRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_domain_remark_with_options_async(request, runtime)

    def save_batch_task_for_apply_quick_transfer_out_openly_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForApplyQuickTransferOutOpenlyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse:
        """
        @summary 批量申请域名快速转出
        
        @param request: SaveBatchTaskForApplyQuickTransferOutOpenlyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForApplyQuickTransferOutOpenlyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForApplyQuickTransferOutOpenly',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_apply_quick_transfer_out_openly_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForApplyQuickTransferOutOpenlyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse:
        """
        @summary 批量申请域名快速转出
        
        @param request: SaveBatchTaskForApplyQuickTransferOutOpenlyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForApplyQuickTransferOutOpenlyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForApplyQuickTransferOutOpenly',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_apply_quick_transfer_out_openly(
        self,
        request: domain_20180129_models.SaveBatchTaskForApplyQuickTransferOutOpenlyRequest,
    ) -> domain_20180129_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse:
        """
        @summary 批量申请域名快速转出
        
        @param request: SaveBatchTaskForApplyQuickTransferOutOpenlyRequest
        @return: SaveBatchTaskForApplyQuickTransferOutOpenlyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_apply_quick_transfer_out_openly_with_options(request, runtime)

    async def save_batch_task_for_apply_quick_transfer_out_openly_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForApplyQuickTransferOutOpenlyRequest,
    ) -> domain_20180129_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse:
        """
        @summary 批量申请域名快速转出
        
        @param request: SaveBatchTaskForApplyQuickTransferOutOpenlyRequest
        @return: SaveBatchTaskForApplyQuickTransferOutOpenlyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_apply_quick_transfer_out_openly_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_activate_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderActivateResponse:
        """
        @summary 保存批量任务-注册订单
        
        @param request: SaveBatchTaskForCreatingOrderActivateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForCreatingOrderActivateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_activate_param):
            query['OrderActivateParam'] = request.order_activate_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderActivate',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForCreatingOrderActivateResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_activate_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderActivateResponse:
        """
        @summary 保存批量任务-注册订单
        
        @param request: SaveBatchTaskForCreatingOrderActivateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForCreatingOrderActivateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_activate_param):
            query['OrderActivateParam'] = request.order_activate_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderActivate',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForCreatingOrderActivateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_activate(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderActivateRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderActivateResponse:
        """
        @summary 保存批量任务-注册订单
        
        @param request: SaveBatchTaskForCreatingOrderActivateRequest
        @return: SaveBatchTaskForCreatingOrderActivateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_activate_with_options(request, runtime)

    async def save_batch_task_for_creating_order_activate_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderActivateRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderActivateResponse:
        """
        @summary 保存批量任务-注册订单
        
        @param request: SaveBatchTaskForCreatingOrderActivateRequest
        @return: SaveBatchTaskForCreatingOrderActivateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_activate_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_redeem_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderRedeemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForCreatingOrderRedeemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_redeem_param):
            query['OrderRedeemParam'] = request.order_redeem_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderRedeem',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_redeem_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderRedeemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForCreatingOrderRedeemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_redeem_param):
            query['OrderRedeemParam'] = request.order_redeem_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderRedeem',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_redeem(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderRedeemRequest
        @return: SaveBatchTaskForCreatingOrderRedeemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_redeem_with_options(request, runtime)

    async def save_batch_task_for_creating_order_redeem_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderRedeemRequest
        @return: SaveBatchTaskForCreatingOrderRedeemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_redeem_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_renew_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRenewResponse:
        """
        @summary 保存批量任务-续费订单
        
        @param request: SaveBatchTaskForCreatingOrderRenewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForCreatingOrderRenewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_renew_param):
            query['OrderRenewParam'] = request.order_renew_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderRenew',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForCreatingOrderRenewResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_renew_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRenewResponse:
        """
        @summary 保存批量任务-续费订单
        
        @param request: SaveBatchTaskForCreatingOrderRenewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForCreatingOrderRenewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_renew_param):
            query['OrderRenewParam'] = request.order_renew_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderRenew',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForCreatingOrderRenewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_renew(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRenewRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRenewResponse:
        """
        @summary 保存批量任务-续费订单
        
        @param request: SaveBatchTaskForCreatingOrderRenewRequest
        @return: SaveBatchTaskForCreatingOrderRenewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_renew_with_options(request, runtime)

    async def save_batch_task_for_creating_order_renew_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRenewRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRenewResponse:
        """
        @summary 保存批量任务-续费订单
        
        @param request: SaveBatchTaskForCreatingOrderRenewRequest
        @return: SaveBatchTaskForCreatingOrderRenewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_renew_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_transfer_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForCreatingOrderTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_transfer_param):
            query['OrderTransferParam'] = request.order_transfer_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderTransfer',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForCreatingOrderTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_transfer_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForCreatingOrderTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_transfer_param):
            query['OrderTransferParam'] = request.order_transfer_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderTransfer',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForCreatingOrderTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_transfer(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderTransferRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderTransferRequest
        @return: SaveBatchTaskForCreatingOrderTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_transfer_with_options(request, runtime)

    async def save_batch_task_for_creating_order_transfer_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderTransferRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderTransferRequest
        @return: SaveBatchTaskForCreatingOrderTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_transfer_with_options_async(request, runtime)

    def save_batch_task_for_domain_name_proxy_service_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        """
        @summary 保存批量任务-开启/关闭whois隐私保护锁
        
        @param request: SaveBatchTaskForDomainNameProxyServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForDomainNameProxyServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForDomainNameProxyService',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_domain_name_proxy_service_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        """
        @summary 保存批量任务-开启/关闭whois隐私保护锁
        
        @param request: SaveBatchTaskForDomainNameProxyServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForDomainNameProxyServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForDomainNameProxyService',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_domain_name_proxy_service(
        self,
        request: domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceRequest,
    ) -> domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        """
        @summary 保存批量任务-开启/关闭whois隐私保护锁
        
        @param request: SaveBatchTaskForDomainNameProxyServiceRequest
        @return: SaveBatchTaskForDomainNameProxyServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_domain_name_proxy_service_with_options(request, runtime)

    async def save_batch_task_for_domain_name_proxy_service_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceRequest,
    ) -> domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        """
        @summary 保存批量任务-开启/关闭whois隐私保护锁
        
        @param request: SaveBatchTaskForDomainNameProxyServiceRequest
        @return: SaveBatchTaskForDomainNameProxyServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_domain_name_proxy_service_with_options_async(request, runtime)

    def save_batch_task_for_generate_domain_certificate_with_options(
        self,
        tmp_req: domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateResponse:
        """
        @summary 提交批量生成证书的任务
        
        @param tmp_req: SaveBatchTaskForGenerateDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForGenerateDomainCertificateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_names):
            request.domain_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_names, 'DomainNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.domain_names_shrink):
            query['DomainNames'] = request.domain_names_shrink
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForGenerateDomainCertificate',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_generate_domain_certificate_with_options_async(
        self,
        tmp_req: domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateResponse:
        """
        @summary 提交批量生成证书的任务
        
        @param tmp_req: SaveBatchTaskForGenerateDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForGenerateDomainCertificateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_names):
            request.domain_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_names, 'DomainNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.domain_names_shrink):
            query['DomainNames'] = request.domain_names_shrink
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForGenerateDomainCertificate',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_generate_domain_certificate(
        self,
        request: domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateRequest,
    ) -> domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateResponse:
        """
        @summary 提交批量生成证书的任务
        
        @param request: SaveBatchTaskForGenerateDomainCertificateRequest
        @return: SaveBatchTaskForGenerateDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_generate_domain_certificate_with_options(request, runtime)

    async def save_batch_task_for_generate_domain_certificate_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateRequest,
    ) -> domain_20180129_models.SaveBatchTaskForGenerateDomainCertificateResponse:
        """
        @summary 提交批量生成证书的任务
        
        @param request: SaveBatchTaskForGenerateDomainCertificateRequest
        @return: SaveBatchTaskForGenerateDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_generate_domain_certificate_with_options_async(request, runtime)

    def save_batch_task_for_modifying_domain_dns_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForModifyingDomainDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForModifyingDomainDnsResponse:
        """
        @summary 批量修改dns
        
        @param request: SaveBatchTaskForModifyingDomainDnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForModifyingDomainDnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_name_server):
            query['DomainNameServer'] = request.domain_name_server
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForModifyingDomainDns',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForModifyingDomainDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_modifying_domain_dns_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForModifyingDomainDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForModifyingDomainDnsResponse:
        """
        @summary 批量修改dns
        
        @param request: SaveBatchTaskForModifyingDomainDnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForModifyingDomainDnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_name_server):
            query['DomainNameServer'] = request.domain_name_server
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForModifyingDomainDns',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForModifyingDomainDnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_modifying_domain_dns(
        self,
        request: domain_20180129_models.SaveBatchTaskForModifyingDomainDnsRequest,
    ) -> domain_20180129_models.SaveBatchTaskForModifyingDomainDnsResponse:
        """
        @summary 批量修改dns
        
        @param request: SaveBatchTaskForModifyingDomainDnsRequest
        @return: SaveBatchTaskForModifyingDomainDnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_modifying_domain_dns_with_options(request, runtime)

    async def save_batch_task_for_modifying_domain_dns_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForModifyingDomainDnsRequest,
    ) -> domain_20180129_models.SaveBatchTaskForModifyingDomainDnsResponse:
        """
        @summary 批量修改dns
        
        @param request: SaveBatchTaskForModifyingDomainDnsRequest
        @return: SaveBatchTaskForModifyingDomainDnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_modifying_domain_dns_with_options_async(request, runtime)

    def save_batch_task_for_reserve_drop_list_domain_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForReserveDropListDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForReserveDropListDomainResponse:
        """
        @param request: SaveBatchTaskForReserveDropListDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForReserveDropListDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForReserveDropListDomain',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForReserveDropListDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_reserve_drop_list_domain_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForReserveDropListDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForReserveDropListDomainResponse:
        """
        @param request: SaveBatchTaskForReserveDropListDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForReserveDropListDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForReserveDropListDomain',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForReserveDropListDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_reserve_drop_list_domain(
        self,
        request: domain_20180129_models.SaveBatchTaskForReserveDropListDomainRequest,
    ) -> domain_20180129_models.SaveBatchTaskForReserveDropListDomainResponse:
        """
        @param request: SaveBatchTaskForReserveDropListDomainRequest
        @return: SaveBatchTaskForReserveDropListDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_reserve_drop_list_domain_with_options(request, runtime)

    async def save_batch_task_for_reserve_drop_list_domain_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForReserveDropListDomainRequest,
    ) -> domain_20180129_models.SaveBatchTaskForReserveDropListDomainResponse:
        """
        @param request: SaveBatchTaskForReserveDropListDomainRequest
        @return: SaveBatchTaskForReserveDropListDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_reserve_drop_list_domain_with_options_async(request, runtime)

    def save_batch_task_for_transfer_prohibition_lock_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse:
        """
        @summary 保存批量任务-开启/关闭禁止转移锁
        
        @param request: SaveBatchTaskForTransferProhibitionLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForTransferProhibitionLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForTransferProhibitionLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_transfer_prohibition_lock_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse:
        """
        @summary 保存批量任务-开启/关闭禁止转移锁
        
        @param request: SaveBatchTaskForTransferProhibitionLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForTransferProhibitionLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForTransferProhibitionLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_transfer_prohibition_lock(
        self,
        request: domain_20180129_models.SaveBatchTaskForTransferProhibitionLockRequest,
    ) -> domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse:
        """
        @summary 保存批量任务-开启/关闭禁止转移锁
        
        @param request: SaveBatchTaskForTransferProhibitionLockRequest
        @return: SaveBatchTaskForTransferProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_transfer_prohibition_lock_with_options(request, runtime)

    async def save_batch_task_for_transfer_prohibition_lock_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForTransferProhibitionLockRequest,
    ) -> domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse:
        """
        @summary 保存批量任务-开启/关闭禁止转移锁
        
        @param request: SaveBatchTaskForTransferProhibitionLockRequest
        @return: SaveBatchTaskForTransferProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_transfer_prohibition_lock_with_options_async(request, runtime)

    def save_batch_task_for_update_prohibition_lock_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        """
        @param request: SaveBatchTaskForUpdateProhibitionLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForUpdateProhibitionLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForUpdateProhibitionLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_update_prohibition_lock_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        """
        @param request: SaveBatchTaskForUpdateProhibitionLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForUpdateProhibitionLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForUpdateProhibitionLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_update_prohibition_lock(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockRequest,
    ) -> domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        """
        @param request: SaveBatchTaskForUpdateProhibitionLockRequest
        @return: SaveBatchTaskForUpdateProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_update_prohibition_lock_with_options(request, runtime)

    async def save_batch_task_for_update_prohibition_lock_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockRequest,
    ) -> domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        """
        @param request: SaveBatchTaskForUpdateProhibitionLockRequest
        @return: SaveBatchTaskForUpdateProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_update_prohibition_lock_with_options_async(request, runtime)

    def save_batch_task_for_updating_contact_info_by_new_contact_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        """
        @summary 使用联系人信息修改联系人的批量任务
        
        @param request: SaveBatchTaskForUpdatingContactInfoByNewContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForUpdatingContactInfoByNewContactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForUpdatingContactInfoByNewContact',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_updating_contact_info_by_new_contact_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        """
        @summary 使用联系人信息修改联系人的批量任务
        
        @param request: SaveBatchTaskForUpdatingContactInfoByNewContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForUpdatingContactInfoByNewContactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForUpdatingContactInfoByNewContact',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_updating_contact_info_by_new_contact(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        """
        @summary 使用联系人信息修改联系人的批量任务
        
        @param request: SaveBatchTaskForUpdatingContactInfoByNewContactRequest
        @return: SaveBatchTaskForUpdatingContactInfoByNewContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_updating_contact_info_by_new_contact_with_options(request, runtime)

    async def save_batch_task_for_updating_contact_info_by_new_contact_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        """
        @summary 使用联系人信息修改联系人的批量任务
        
        @param request: SaveBatchTaskForUpdatingContactInfoByNewContactRequest
        @return: SaveBatchTaskForUpdatingContactInfoByNewContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_updating_contact_info_by_new_contact_with_options_async(request, runtime)

    def save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse:
        """
        @summary 使用模板修改联系人的批量任务
        
        @param request: SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForUpdatingContactInfoByRegistrantProfileId',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse:
        """
        @summary 使用模板修改联系人的批量任务
        
        @param request: SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForUpdatingContactInfoByRegistrantProfileId',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_updating_contact_info_by_registrant_profile_id(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse:
        """
        @summary 使用模板修改联系人的批量任务
        
        @param request: SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest
        @return: SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options(request, runtime)

    async def save_batch_task_for_updating_contact_info_by_registrant_profile_id_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse:
        """
        @summary 使用模板修改联系人的批量任务
        
        @param request: SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest
        @return: SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options_async(request, runtime)

    def save_domain_group_with_options(
        self,
        request: domain_20180129_models.SaveDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveDomainGroupResponse:
        """
        @summary 创建/更新域名分组
        
        @param request: SaveDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.domain_group_name):
            query['DomainGroupName'] = request.domain_group_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveDomainGroup',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_domain_group_with_options_async(
        self,
        request: domain_20180129_models.SaveDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveDomainGroupResponse:
        """
        @summary 创建/更新域名分组
        
        @param request: SaveDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.domain_group_name):
            query['DomainGroupName'] = request.domain_group_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveDomainGroup',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_domain_group(
        self,
        request: domain_20180129_models.SaveDomainGroupRequest,
    ) -> domain_20180129_models.SaveDomainGroupResponse:
        """
        @summary 创建/更新域名分组
        
        @param request: SaveDomainGroupRequest
        @return: SaveDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_domain_group_with_options(request, runtime)

    async def save_domain_group_async(
        self,
        request: domain_20180129_models.SaveDomainGroupRequest,
    ) -> domain_20180129_models.SaveDomainGroupResponse:
        """
        @summary 创建/更新域名分组
        
        @param request: SaveDomainGroupRequest
        @return: SaveDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_domain_group_with_options_async(request, runtime)

    def save_registrant_profile_with_options(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveRegistrantProfileResponse:
        """
        @summary 保存联系人模板
        
        @param request: SaveRegistrantProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveRegistrantProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.default_registrant_profile):
            query['DefaultRegistrantProfile'] = request.default_registrant_profile
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRegistrantProfile',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveRegistrantProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_registrant_profile_with_options_async(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveRegistrantProfileResponse:
        """
        @summary 保存联系人模板
        
        @param request: SaveRegistrantProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveRegistrantProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.default_registrant_profile):
            query['DefaultRegistrantProfile'] = request.default_registrant_profile
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRegistrantProfile',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveRegistrantProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_registrant_profile(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRequest,
    ) -> domain_20180129_models.SaveRegistrantProfileResponse:
        """
        @summary 保存联系人模板
        
        @param request: SaveRegistrantProfileRequest
        @return: SaveRegistrantProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_registrant_profile_with_options(request, runtime)

    async def save_registrant_profile_async(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRequest,
    ) -> domain_20180129_models.SaveRegistrantProfileResponse:
        """
        @summary 保存联系人模板
        
        @param request: SaveRegistrantProfileRequest
        @return: SaveRegistrantProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_registrant_profile_with_options_async(request, runtime)

    def save_registrant_profile_real_name_verification_with_options(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveRegistrantProfileRealNameVerificationResponse:
        """
        @summary 保存联系人模板和凭据
        
        @param request: SaveRegistrantProfileRealNameVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveRegistrantProfileRealNameVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.identity_credential):
            query['IdentityCredential'] = request.identity_credential
        if not UtilClient.is_unset(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not UtilClient.is_unset(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRegistrantProfileRealNameVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveRegistrantProfileRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_registrant_profile_real_name_verification_with_options_async(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveRegistrantProfileRealNameVerificationResponse:
        """
        @summary 保存联系人模板和凭据
        
        @param request: SaveRegistrantProfileRealNameVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveRegistrantProfileRealNameVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.identity_credential):
            query['IdentityCredential'] = request.identity_credential
        if not UtilClient.is_unset(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not UtilClient.is_unset(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRegistrantProfileRealNameVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveRegistrantProfileRealNameVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_registrant_profile_real_name_verification(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRealNameVerificationRequest,
    ) -> domain_20180129_models.SaveRegistrantProfileRealNameVerificationResponse:
        """
        @summary 保存联系人模板和凭据
        
        @param request: SaveRegistrantProfileRealNameVerificationRequest
        @return: SaveRegistrantProfileRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_registrant_profile_real_name_verification_with_options(request, runtime)

    async def save_registrant_profile_real_name_verification_async(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRealNameVerificationRequest,
    ) -> domain_20180129_models.SaveRegistrantProfileRealNameVerificationResponse:
        """
        @summary 保存联系人模板和凭据
        
        @param request: SaveRegistrantProfileRealNameVerificationRequest
        @return: SaveRegistrantProfileRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_registrant_profile_real_name_verification_with_options_async(request, runtime)

    def save_single_task_for_adding_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForAddingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse:
        """
        @summary 添加dnsSec记录
        
        @param request: SaveSingleTaskForAddingDSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForAddingDSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.digest_type):
            query['DigestType'] = request.digest_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForAddingDSRecord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_adding_dsrecord_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForAddingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse:
        """
        @summary 添加dnsSec记录
        
        @param request: SaveSingleTaskForAddingDSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForAddingDSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.digest_type):
            query['DigestType'] = request.digest_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForAddingDSRecord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_adding_dsrecord(
        self,
        request: domain_20180129_models.SaveSingleTaskForAddingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse:
        """
        @summary 添加dnsSec记录
        
        @param request: SaveSingleTaskForAddingDSRecordRequest
        @return: SaveSingleTaskForAddingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_adding_dsrecord_with_options(request, runtime)

    async def save_single_task_for_adding_dsrecord_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForAddingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse:
        """
        @summary 添加dnsSec记录
        
        @param request: SaveSingleTaskForAddingDSRecordRequest
        @return: SaveSingleTaskForAddingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_adding_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_apply_quick_transfer_out_openly_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForApplyQuickTransferOutOpenlyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse:
        """
        @summary 申请域名快速转出
        
        @param request: SaveSingleTaskForApplyQuickTransferOutOpenlyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForApplyQuickTransferOutOpenlyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForApplyQuickTransferOutOpenly',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_apply_quick_transfer_out_openly_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForApplyQuickTransferOutOpenlyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse:
        """
        @summary 申请域名快速转出
        
        @param request: SaveSingleTaskForApplyQuickTransferOutOpenlyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForApplyQuickTransferOutOpenlyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForApplyQuickTransferOutOpenly',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_apply_quick_transfer_out_openly(
        self,
        request: domain_20180129_models.SaveSingleTaskForApplyQuickTransferOutOpenlyRequest,
    ) -> domain_20180129_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse:
        """
        @summary 申请域名快速转出
        
        @param request: SaveSingleTaskForApplyQuickTransferOutOpenlyRequest
        @return: SaveSingleTaskForApplyQuickTransferOutOpenlyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_apply_quick_transfer_out_openly_with_options(request, runtime)

    async def save_single_task_for_apply_quick_transfer_out_openly_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForApplyQuickTransferOutOpenlyRequest,
    ) -> domain_20180129_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse:
        """
        @summary 申请域名快速转出
        
        @param request: SaveSingleTaskForApplyQuickTransferOutOpenlyRequest
        @return: SaveSingleTaskForApplyQuickTransferOutOpenlyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_apply_quick_transfer_out_openly_with_options_async(request, runtime)

    def save_single_task_for_approving_transfer_out_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForApprovingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForApprovingTransferOutResponse:
        """
        @summary 确认转出
        
        @param request: SaveSingleTaskForApprovingTransferOutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForApprovingTransferOutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForApprovingTransferOut',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForApprovingTransferOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_approving_transfer_out_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForApprovingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForApprovingTransferOutResponse:
        """
        @summary 确认转出
        
        @param request: SaveSingleTaskForApprovingTransferOutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForApprovingTransferOutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForApprovingTransferOut',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForApprovingTransferOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_approving_transfer_out(
        self,
        request: domain_20180129_models.SaveSingleTaskForApprovingTransferOutRequest,
    ) -> domain_20180129_models.SaveSingleTaskForApprovingTransferOutResponse:
        """
        @summary 确认转出
        
        @param request: SaveSingleTaskForApprovingTransferOutRequest
        @return: SaveSingleTaskForApprovingTransferOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_approving_transfer_out_with_options(request, runtime)

    async def save_single_task_for_approving_transfer_out_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForApprovingTransferOutRequest,
    ) -> domain_20180129_models.SaveSingleTaskForApprovingTransferOutResponse:
        """
        @summary 确认转出
        
        @param request: SaveSingleTaskForApprovingTransferOutRequest
        @return: SaveSingleTaskForApprovingTransferOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_approving_transfer_out_with_options_async(request, runtime)

    def save_single_task_for_associating_ens_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForAssociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForAssociatingEnsResponse:
        """
        @param request: SaveSingleTaskForAssociatingEnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForAssociatingEnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForAssociatingEns',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForAssociatingEnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_associating_ens_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForAssociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForAssociatingEnsResponse:
        """
        @param request: SaveSingleTaskForAssociatingEnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForAssociatingEnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForAssociatingEns',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForAssociatingEnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_associating_ens(
        self,
        request: domain_20180129_models.SaveSingleTaskForAssociatingEnsRequest,
    ) -> domain_20180129_models.SaveSingleTaskForAssociatingEnsResponse:
        """
        @param request: SaveSingleTaskForAssociatingEnsRequest
        @return: SaveSingleTaskForAssociatingEnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_associating_ens_with_options(request, runtime)

    async def save_single_task_for_associating_ens_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForAssociatingEnsRequest,
    ) -> domain_20180129_models.SaveSingleTaskForAssociatingEnsResponse:
        """
        @param request: SaveSingleTaskForAssociatingEnsRequest
        @return: SaveSingleTaskForAssociatingEnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_associating_ens_with_options_async(request, runtime)

    def save_single_task_for_canceling_transfer_in_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferInRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferInResponse:
        """
        @param request: SaveSingleTaskForCancelingTransferInRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCancelingTransferInResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCancelingTransferIn',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCancelingTransferInResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_canceling_transfer_in_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferInRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferInResponse:
        """
        @param request: SaveSingleTaskForCancelingTransferInRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCancelingTransferInResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCancelingTransferIn',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCancelingTransferInResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_canceling_transfer_in(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferInRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferInResponse:
        """
        @param request: SaveSingleTaskForCancelingTransferInRequest
        @return: SaveSingleTaskForCancelingTransferInResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_canceling_transfer_in_with_options(request, runtime)

    async def save_single_task_for_canceling_transfer_in_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferInRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferInResponse:
        """
        @param request: SaveSingleTaskForCancelingTransferInRequest
        @return: SaveSingleTaskForCancelingTransferInResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_canceling_transfer_in_with_options_async(request, runtime)

    def save_single_task_for_canceling_transfer_out_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferOutResponse:
        """
        @summary 取消转出
        
        @param request: SaveSingleTaskForCancelingTransferOutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCancelingTransferOutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCancelingTransferOut',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCancelingTransferOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_canceling_transfer_out_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferOutResponse:
        """
        @summary 取消转出
        
        @param request: SaveSingleTaskForCancelingTransferOutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCancelingTransferOutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCancelingTransferOut',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCancelingTransferOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_canceling_transfer_out(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferOutRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferOutResponse:
        """
        @summary 取消转出
        
        @param request: SaveSingleTaskForCancelingTransferOutRequest
        @return: SaveSingleTaskForCancelingTransferOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_canceling_transfer_out_with_options(request, runtime)

    async def save_single_task_for_canceling_transfer_out_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferOutRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferOutResponse:
        """
        @summary 取消转出
        
        @param request: SaveSingleTaskForCancelingTransferOutRequest
        @return: SaveSingleTaskForCancelingTransferOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_canceling_transfer_out_with_options_async(request, runtime)

    def save_single_task_for_creating_dns_host_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingDnsHostResponse:
        """
        @summary 保存创建dns服务器的任务请求
        
        @param request: SaveSingleTaskForCreatingDnsHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCreatingDnsHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_name):
            query['DnsName'] = request.dns_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingDnsHost',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCreatingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_dns_host_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingDnsHostResponse:
        """
        @summary 保存创建dns服务器的任务请求
        
        @param request: SaveSingleTaskForCreatingDnsHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCreatingDnsHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_name):
            query['DnsName'] = request.dns_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingDnsHost',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCreatingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_dns_host(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingDnsHostResponse:
        """
        @summary 保存创建dns服务器的任务请求
        
        @param request: SaveSingleTaskForCreatingDnsHostRequest
        @return: SaveSingleTaskForCreatingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_dns_host_with_options(request, runtime)

    async def save_single_task_for_creating_dns_host_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingDnsHostResponse:
        """
        @summary 保存创建dns服务器的任务请求
        
        @param request: SaveSingleTaskForCreatingDnsHostRequest
        @return: SaveSingleTaskForCreatingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_dns_host_with_options_async(request, runtime)

    def save_single_task_for_creating_order_activate_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderActivateResponse:
        """
        @summary 保存单个任务-注册订单
        
        @param request: SaveSingleTaskForCreatingOrderActivateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCreatingOrderActivateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dns_1):
            query['Dns1'] = request.dns_1
        if not UtilClient.is_unset(request.dns_2):
            query['Dns2'] = request.dns_2
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.enable_domain_proxy):
            query['EnableDomainProxy'] = request.enable_domain_proxy
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.permit_premium_activation):
            query['PermitPremiumActivation'] = request.permit_premium_activation
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_duration):
            query['SubscriptionDuration'] = request.subscription_duration
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.trademark_domain_activation):
            query['TrademarkDomainActivation'] = request.trademark_domain_activation
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderActivate',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCreatingOrderActivateResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_activate_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderActivateResponse:
        """
        @summary 保存单个任务-注册订单
        
        @param request: SaveSingleTaskForCreatingOrderActivateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCreatingOrderActivateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dns_1):
            query['Dns1'] = request.dns_1
        if not UtilClient.is_unset(request.dns_2):
            query['Dns2'] = request.dns_2
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.enable_domain_proxy):
            query['EnableDomainProxy'] = request.enable_domain_proxy
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.permit_premium_activation):
            query['PermitPremiumActivation'] = request.permit_premium_activation
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subscription_duration):
            query['SubscriptionDuration'] = request.subscription_duration
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.trademark_domain_activation):
            query['TrademarkDomainActivation'] = request.trademark_domain_activation
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderActivate',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCreatingOrderActivateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_activate(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderActivateRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderActivateResponse:
        """
        @summary 保存单个任务-注册订单
        
        @param request: SaveSingleTaskForCreatingOrderActivateRequest
        @return: SaveSingleTaskForCreatingOrderActivateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_activate_with_options(request, runtime)

    async def save_single_task_for_creating_order_activate_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderActivateRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderActivateResponse:
        """
        @summary 保存单个任务-注册订单
        
        @param request: SaveSingleTaskForCreatingOrderActivateRequest
        @return: SaveSingleTaskForCreatingOrderActivateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_activate_with_options_async(request, runtime)

    def save_single_task_for_creating_order_redeem_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderRedeemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCreatingOrderRedeemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.current_expiration_date):
            query['CurrentExpirationDate'] = request.current_expiration_date
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderRedeem',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_redeem_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderRedeemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCreatingOrderRedeemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.current_expiration_date):
            query['CurrentExpirationDate'] = request.current_expiration_date
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderRedeem',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_redeem(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderRedeemRequest
        @return: SaveSingleTaskForCreatingOrderRedeemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_redeem_with_options(request, runtime)

    async def save_single_task_for_creating_order_redeem_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderRedeemRequest
        @return: SaveSingleTaskForCreatingOrderRedeemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_redeem_with_options_async(request, runtime)

    def save_single_task_for_creating_order_renew_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRenewResponse:
        """
        @summary 保存单个任务-续费订单
        
        @param request: SaveSingleTaskForCreatingOrderRenewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCreatingOrderRenewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.current_expiration_date):
            query['CurrentExpirationDate'] = request.current_expiration_date
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.subscription_duration):
            query['SubscriptionDuration'] = request.subscription_duration
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderRenew',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCreatingOrderRenewResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_renew_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRenewResponse:
        """
        @summary 保存单个任务-续费订单
        
        @param request: SaveSingleTaskForCreatingOrderRenewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCreatingOrderRenewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.current_expiration_date):
            query['CurrentExpirationDate'] = request.current_expiration_date
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.subscription_duration):
            query['SubscriptionDuration'] = request.subscription_duration
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderRenew',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCreatingOrderRenewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_renew(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRenewRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRenewResponse:
        """
        @summary 保存单个任务-续费订单
        
        @param request: SaveSingleTaskForCreatingOrderRenewRequest
        @return: SaveSingleTaskForCreatingOrderRenewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_renew_with_options(request, runtime)

    async def save_single_task_for_creating_order_renew_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRenewRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRenewResponse:
        """
        @summary 保存单个任务-续费订单
        
        @param request: SaveSingleTaskForCreatingOrderRenewRequest
        @return: SaveSingleTaskForCreatingOrderRenewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_renew_with_options_async(request, runtime)

    def save_single_task_for_creating_order_transfer_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCreatingOrderTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_code):
            query['AuthorizationCode'] = request.authorization_code
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.permit_premium_transfer):
            query['PermitPremiumTransfer'] = request.permit_premium_transfer
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderTransfer',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCreatingOrderTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_transfer_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForCreatingOrderTransferResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_code):
            query['AuthorizationCode'] = request.authorization_code
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.permit_premium_transfer):
            query['PermitPremiumTransfer'] = request.permit_premium_transfer
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderTransfer',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForCreatingOrderTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_transfer(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderTransferRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderTransferRequest
        @return: SaveSingleTaskForCreatingOrderTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_transfer_with_options(request, runtime)

    async def save_single_task_for_creating_order_transfer_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderTransferRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderTransferRequest
        @return: SaveSingleTaskForCreatingOrderTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_transfer_with_options_async(request, runtime)

    def save_single_task_for_deleting_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse:
        """
        @summary 删除dnsSec记录
        
        @param request: SaveSingleTaskForDeletingDSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForDeletingDSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDeletingDSRecord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_deleting_dsrecord_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse:
        """
        @summary 删除dnsSec记录
        
        @param request: SaveSingleTaskForDeletingDSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForDeletingDSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDeletingDSRecord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_deleting_dsrecord(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse:
        """
        @summary 删除dnsSec记录
        
        @param request: SaveSingleTaskForDeletingDSRecordRequest
        @return: SaveSingleTaskForDeletingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_deleting_dsrecord_with_options(request, runtime)

    async def save_single_task_for_deleting_dsrecord_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse:
        """
        @summary 删除dnsSec记录
        
        @param request: SaveSingleTaskForDeletingDSRecordRequest
        @return: SaveSingleTaskForDeletingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_deleting_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_deleting_dns_host_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse:
        """
        @summary 删除DNS HOST任务
        
        @param request: SaveSingleTaskForDeletingDnsHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForDeletingDnsHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_name):
            query['DnsName'] = request.dns_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDeletingDnsHost',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_deleting_dns_host_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse:
        """
        @summary 删除DNS HOST任务
        
        @param request: SaveSingleTaskForDeletingDnsHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForDeletingDnsHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_name):
            query['DnsName'] = request.dns_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDeletingDnsHost',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_deleting_dns_host(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse:
        """
        @summary 删除DNS HOST任务
        
        @param request: SaveSingleTaskForDeletingDnsHostRequest
        @return: SaveSingleTaskForDeletingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_deleting_dns_host_with_options(request, runtime)

    async def save_single_task_for_deleting_dns_host_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse:
        """
        @summary 删除DNS HOST任务
        
        @param request: SaveSingleTaskForDeletingDnsHostRequest
        @return: SaveSingleTaskForDeletingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_deleting_dns_host_with_options_async(request, runtime)

    def save_single_task_for_disassociating_ens_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForDisassociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse:
        """
        @param request: SaveSingleTaskForDisassociatingEnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForDisassociatingEnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDisassociatingEns',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_disassociating_ens_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDisassociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse:
        """
        @param request: SaveSingleTaskForDisassociatingEnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForDisassociatingEnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDisassociatingEns',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_disassociating_ens(
        self,
        request: domain_20180129_models.SaveSingleTaskForDisassociatingEnsRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse:
        """
        @param request: SaveSingleTaskForDisassociatingEnsRequest
        @return: SaveSingleTaskForDisassociatingEnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_disassociating_ens_with_options(request, runtime)

    async def save_single_task_for_disassociating_ens_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDisassociatingEnsRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse:
        """
        @param request: SaveSingleTaskForDisassociatingEnsRequest
        @return: SaveSingleTaskForDisassociatingEnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_disassociating_ens_with_options_async(request, runtime)

    def save_single_task_for_domain_name_proxy_service_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        """
        @summary 保存单个任务-开启/关闭whois隐私保护锁
        
        @param request: SaveSingleTaskForDomainNameProxyServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForDomainNameProxyServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDomainNameProxyService',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_domain_name_proxy_service_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        """
        @summary 保存单个任务-开启/关闭whois隐私保护锁
        
        @param request: SaveSingleTaskForDomainNameProxyServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForDomainNameProxyServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDomainNameProxyService',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_domain_name_proxy_service(
        self,
        request: domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        """
        @summary 保存单个任务-开启/关闭whois隐私保护锁
        
        @param request: SaveSingleTaskForDomainNameProxyServiceRequest
        @return: SaveSingleTaskForDomainNameProxyServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_domain_name_proxy_service_with_options(request, runtime)

    async def save_single_task_for_domain_name_proxy_service_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        """
        @summary 保存单个任务-开启/关闭whois隐私保护锁
        
        @param request: SaveSingleTaskForDomainNameProxyServiceRequest
        @return: SaveSingleTaskForDomainNameProxyServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_domain_name_proxy_service_with_options_async(request, runtime)

    def save_single_task_for_generate_domain_certificate_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForGenerateDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForGenerateDomainCertificateResponse:
        """
        @summary 提交生成域名证书任务
        
        @param request: SaveSingleTaskForGenerateDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForGenerateDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForGenerateDomainCertificate',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForGenerateDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_generate_domain_certificate_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForGenerateDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForGenerateDomainCertificateResponse:
        """
        @summary 提交生成域名证书任务
        
        @param request: SaveSingleTaskForGenerateDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForGenerateDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForGenerateDomainCertificate',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForGenerateDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_generate_domain_certificate(
        self,
        request: domain_20180129_models.SaveSingleTaskForGenerateDomainCertificateRequest,
    ) -> domain_20180129_models.SaveSingleTaskForGenerateDomainCertificateResponse:
        """
        @summary 提交生成域名证书任务
        
        @param request: SaveSingleTaskForGenerateDomainCertificateRequest
        @return: SaveSingleTaskForGenerateDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_generate_domain_certificate_with_options(request, runtime)

    async def save_single_task_for_generate_domain_certificate_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForGenerateDomainCertificateRequest,
    ) -> domain_20180129_models.SaveSingleTaskForGenerateDomainCertificateResponse:
        """
        @summary 提交生成域名证书任务
        
        @param request: SaveSingleTaskForGenerateDomainCertificateRequest
        @return: SaveSingleTaskForGenerateDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_generate_domain_certificate_with_options_async(request, runtime)

    def save_single_task_for_modifying_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse:
        """
        @summary 修改DnsSec记录
        
        @param request: SaveSingleTaskForModifyingDSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForModifyingDSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.digest_type):
            query['DigestType'] = request.digest_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForModifyingDSRecord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_modifying_dsrecord_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse:
        """
        @summary 修改DnsSec记录
        
        @param request: SaveSingleTaskForModifyingDSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForModifyingDSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.digest_type):
            query['DigestType'] = request.digest_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForModifyingDSRecord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_modifying_dsrecord(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse:
        """
        @summary 修改DnsSec记录
        
        @param request: SaveSingleTaskForModifyingDSRecordRequest
        @return: SaveSingleTaskForModifyingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_modifying_dsrecord_with_options(request, runtime)

    async def save_single_task_for_modifying_dsrecord_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse:
        """
        @summary 修改DnsSec记录
        
        @param request: SaveSingleTaskForModifyingDSRecordRequest
        @return: SaveSingleTaskForModifyingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_modifying_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_modifying_dns_host_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse:
        """
        @summary 保存修改dns服务器的任务请求
        
        @param request: SaveSingleTaskForModifyingDnsHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForModifyingDnsHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_name):
            query['DnsName'] = request.dns_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForModifyingDnsHost',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_modifying_dns_host_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse:
        """
        @summary 保存修改dns服务器的任务请求
        
        @param request: SaveSingleTaskForModifyingDnsHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForModifyingDnsHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_name):
            query['DnsName'] = request.dns_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForModifyingDnsHost',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_modifying_dns_host(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse:
        """
        @summary 保存修改dns服务器的任务请求
        
        @param request: SaveSingleTaskForModifyingDnsHostRequest
        @return: SaveSingleTaskForModifyingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_modifying_dns_host_with_options(request, runtime)

    async def save_single_task_for_modifying_dns_host_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse:
        """
        @summary 保存修改dns服务器的任务请求
        
        @param request: SaveSingleTaskForModifyingDnsHostRequest
        @return: SaveSingleTaskForModifyingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_modifying_dns_host_with_options_async(request, runtime)

    def save_single_task_for_querying_transfer_authorization_code_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        """
        @summary 发送转移码
        
        @param request: SaveSingleTaskForQueryingTransferAuthorizationCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForQueryingTransferAuthorizationCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForQueryingTransferAuthorizationCode',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_querying_transfer_authorization_code_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        """
        @summary 发送转移码
        
        @param request: SaveSingleTaskForQueryingTransferAuthorizationCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForQueryingTransferAuthorizationCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForQueryingTransferAuthorizationCode',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_querying_transfer_authorization_code(
        self,
        request: domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
    ) -> domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        """
        @summary 发送转移码
        
        @param request: SaveSingleTaskForQueryingTransferAuthorizationCodeRequest
        @return: SaveSingleTaskForQueryingTransferAuthorizationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_querying_transfer_authorization_code_with_options(request, runtime)

    async def save_single_task_for_querying_transfer_authorization_code_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
    ) -> domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        """
        @summary 发送转移码
        
        @param request: SaveSingleTaskForQueryingTransferAuthorizationCodeRequest
        @return: SaveSingleTaskForQueryingTransferAuthorizationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_querying_transfer_authorization_code_with_options_async(request, runtime)

    def save_single_task_for_reserve_drop_list_domain_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForReserveDropListDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForReserveDropListDomainResponse:
        """
        @summary 单笔抢注批量接口
        
        @param request: SaveSingleTaskForReserveDropListDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForReserveDropListDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not UtilClient.is_unset(request.dns_1):
            query['Dns1'] = request.dns_1
        if not UtilClient.is_unset(request.dns_2):
            query['Dns2'] = request.dns_2
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForReserveDropListDomain',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForReserveDropListDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_reserve_drop_list_domain_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForReserveDropListDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForReserveDropListDomainResponse:
        """
        @summary 单笔抢注批量接口
        
        @param request: SaveSingleTaskForReserveDropListDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForReserveDropListDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not UtilClient.is_unset(request.dns_1):
            query['Dns1'] = request.dns_1
        if not UtilClient.is_unset(request.dns_2):
            query['Dns2'] = request.dns_2
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForReserveDropListDomain',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForReserveDropListDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_reserve_drop_list_domain(
        self,
        request: domain_20180129_models.SaveSingleTaskForReserveDropListDomainRequest,
    ) -> domain_20180129_models.SaveSingleTaskForReserveDropListDomainResponse:
        """
        @summary 单笔抢注批量接口
        
        @param request: SaveSingleTaskForReserveDropListDomainRequest
        @return: SaveSingleTaskForReserveDropListDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_reserve_drop_list_domain_with_options(request, runtime)

    async def save_single_task_for_reserve_drop_list_domain_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForReserveDropListDomainRequest,
    ) -> domain_20180129_models.SaveSingleTaskForReserveDropListDomainResponse:
        """
        @summary 单笔抢注批量接口
        
        @param request: SaveSingleTaskForReserveDropListDomainRequest
        @return: SaveSingleTaskForReserveDropListDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_reserve_drop_list_domain_with_options_async(request, runtime)

    def save_single_task_for_save_art_extension_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForSaveArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSaveArtExtensionResponse:
        """
        @summary 保存art扩展信息任务
        
        @param request: SaveSingleTaskForSaveArtExtensionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForSaveArtExtensionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_or_period):
            query['DateOrPeriod'] = request.date_or_period
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.features):
            query['Features'] = request.features
        if not UtilClient.is_unset(request.inscriptions_and_markings):
            query['InscriptionsAndMarkings'] = request.inscriptions_and_markings
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.maker):
            query['Maker'] = request.maker
        if not UtilClient.is_unset(request.materials_and_techniques):
            query['MaterialsAndTechniques'] = request.materials_and_techniques
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.reference):
            query['Reference'] = request.reference
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForSaveArtExtension',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForSaveArtExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_save_art_extension_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSaveArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSaveArtExtensionResponse:
        """
        @summary 保存art扩展信息任务
        
        @param request: SaveSingleTaskForSaveArtExtensionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForSaveArtExtensionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_or_period):
            query['DateOrPeriod'] = request.date_or_period
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.features):
            query['Features'] = request.features
        if not UtilClient.is_unset(request.inscriptions_and_markings):
            query['InscriptionsAndMarkings'] = request.inscriptions_and_markings
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.maker):
            query['Maker'] = request.maker
        if not UtilClient.is_unset(request.materials_and_techniques):
            query['MaterialsAndTechniques'] = request.materials_and_techniques
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.reference):
            query['Reference'] = request.reference
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForSaveArtExtension',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForSaveArtExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_save_art_extension(
        self,
        request: domain_20180129_models.SaveSingleTaskForSaveArtExtensionRequest,
    ) -> domain_20180129_models.SaveSingleTaskForSaveArtExtensionResponse:
        """
        @summary 保存art扩展信息任务
        
        @param request: SaveSingleTaskForSaveArtExtensionRequest
        @return: SaveSingleTaskForSaveArtExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_save_art_extension_with_options(request, runtime)

    async def save_single_task_for_save_art_extension_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSaveArtExtensionRequest,
    ) -> domain_20180129_models.SaveSingleTaskForSaveArtExtensionResponse:
        """
        @summary 保存art扩展信息任务
        
        @param request: SaveSingleTaskForSaveArtExtensionRequest
        @return: SaveSingleTaskForSaveArtExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_save_art_extension_with_options_async(request, runtime)

    def save_single_task_for_synchronizing_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        """
        @summary 同步DnsSec记录
        
        @param request: SaveSingleTaskForSynchronizingDSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForSynchronizingDSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForSynchronizingDSRecord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_synchronizing_dsrecord_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        """
        @summary 同步DnsSec记录
        
        @param request: SaveSingleTaskForSynchronizingDSRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForSynchronizingDSRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForSynchronizingDSRecord',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_synchronizing_dsrecord(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        """
        @summary 同步DnsSec记录
        
        @param request: SaveSingleTaskForSynchronizingDSRecordRequest
        @return: SaveSingleTaskForSynchronizingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_synchronizing_dsrecord_with_options(request, runtime)

    async def save_single_task_for_synchronizing_dsrecord_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        """
        @summary 同步DnsSec记录
        
        @param request: SaveSingleTaskForSynchronizingDSRecordRequest
        @return: SaveSingleTaskForSynchronizingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_synchronizing_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_synchronizing_dns_host_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        """
        @summary 保存同步dns服务器的任务请求
        
        @param request: SaveSingleTaskForSynchronizingDnsHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForSynchronizingDnsHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForSynchronizingDnsHost',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_synchronizing_dns_host_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        """
        @summary 保存同步dns服务器的任务请求
        
        @param request: SaveSingleTaskForSynchronizingDnsHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForSynchronizingDnsHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForSynchronizingDnsHost',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_synchronizing_dns_host(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        """
        @summary 保存同步dns服务器的任务请求
        
        @param request: SaveSingleTaskForSynchronizingDnsHostRequest
        @return: SaveSingleTaskForSynchronizingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_synchronizing_dns_host_with_options(request, runtime)

    async def save_single_task_for_synchronizing_dns_host_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        """
        @summary 保存同步dns服务器的任务请求
        
        @param request: SaveSingleTaskForSynchronizingDnsHostRequest
        @return: SaveSingleTaskForSynchronizingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_synchronizing_dns_host_with_options_async(request, runtime)

    def save_single_task_for_transfer_prohibition_lock_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse:
        """
        @summary 保存单个任务-开启/关闭禁止转移锁
        
        @param request: SaveSingleTaskForTransferProhibitionLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForTransferProhibitionLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForTransferProhibitionLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_transfer_prohibition_lock_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse:
        """
        @summary 保存单个任务-开启/关闭禁止转移锁
        
        @param request: SaveSingleTaskForTransferProhibitionLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForTransferProhibitionLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForTransferProhibitionLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_transfer_prohibition_lock(
        self,
        request: domain_20180129_models.SaveSingleTaskForTransferProhibitionLockRequest,
    ) -> domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse:
        """
        @summary 保存单个任务-开启/关闭禁止转移锁
        
        @param request: SaveSingleTaskForTransferProhibitionLockRequest
        @return: SaveSingleTaskForTransferProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_transfer_prohibition_lock_with_options(request, runtime)

    async def save_single_task_for_transfer_prohibition_lock_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForTransferProhibitionLockRequest,
    ) -> domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse:
        """
        @summary 保存单个任务-开启/关闭禁止转移锁
        
        @param request: SaveSingleTaskForTransferProhibitionLockRequest
        @return: SaveSingleTaskForTransferProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_transfer_prohibition_lock_with_options_async(request, runtime)

    def save_single_task_for_update_prohibition_lock_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        """
        @summary 保存单个任务-开启/关闭信息安全锁
        
        @param request: SaveSingleTaskForUpdateProhibitionLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForUpdateProhibitionLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForUpdateProhibitionLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_update_prohibition_lock_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        """
        @summary 保存单个任务-开启/关闭信息安全锁
        
        @param request: SaveSingleTaskForUpdateProhibitionLockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForUpdateProhibitionLockResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForUpdateProhibitionLock',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_update_prohibition_lock(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockRequest,
    ) -> domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        """
        @summary 保存单个任务-开启/关闭信息安全锁
        
        @param request: SaveSingleTaskForUpdateProhibitionLockRequest
        @return: SaveSingleTaskForUpdateProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_update_prohibition_lock_with_options(request, runtime)

    async def save_single_task_for_update_prohibition_lock_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockRequest,
    ) -> domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        """
        @summary 保存单个任务-开启/关闭信息安全锁
        
        @param request: SaveSingleTaskForUpdateProhibitionLockRequest
        @return: SaveSingleTaskForUpdateProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_update_prohibition_lock_with_options_async(request, runtime)

    def save_single_task_for_updating_contact_info_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdatingContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForUpdatingContactInfoResponse:
        """
        @summary 保存修改联系人的任务
        
        @param request: SaveSingleTaskForUpdatingContactInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForUpdatingContactInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForUpdatingContactInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForUpdatingContactInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_updating_contact_info_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdatingContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForUpdatingContactInfoResponse:
        """
        @summary 保存修改联系人的任务
        
        @param request: SaveSingleTaskForUpdatingContactInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSingleTaskForUpdatingContactInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForUpdatingContactInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveSingleTaskForUpdatingContactInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_updating_contact_info(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdatingContactInfoRequest,
    ) -> domain_20180129_models.SaveSingleTaskForUpdatingContactInfoResponse:
        """
        @summary 保存修改联系人的任务
        
        @param request: SaveSingleTaskForUpdatingContactInfoRequest
        @return: SaveSingleTaskForUpdatingContactInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_updating_contact_info_with_options(request, runtime)

    async def save_single_task_for_updating_contact_info_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdatingContactInfoRequest,
    ) -> domain_20180129_models.SaveSingleTaskForUpdatingContactInfoResponse:
        """
        @summary 保存修改联系人的任务
        
        @param request: SaveSingleTaskForUpdatingContactInfoRequest
        @return: SaveSingleTaskForUpdatingContactInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_updating_contact_info_with_options_async(request, runtime)

    def save_task_for_submitting_domain_delete_with_options(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainDeleteResponse:
        """
        @summary 保存删除域名的任务
        
        @param request: SaveTaskForSubmittingDomainDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTaskForSubmittingDomainDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTaskForSubmittingDomainDelete',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveTaskForSubmittingDomainDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_submitting_domain_delete_with_options_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainDeleteResponse:
        """
        @summary 保存删除域名的任务
        
        @param request: SaveTaskForSubmittingDomainDeleteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTaskForSubmittingDomainDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTaskForSubmittingDomainDelete',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveTaskForSubmittingDomainDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_submitting_domain_delete(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainDeleteRequest,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainDeleteResponse:
        """
        @summary 保存删除域名的任务
        
        @param request: SaveTaskForSubmittingDomainDeleteRequest
        @return: SaveTaskForSubmittingDomainDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_delete_with_options(request, runtime)

    async def save_task_for_submitting_domain_delete_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainDeleteRequest,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainDeleteResponse:
        """
        @summary 保存删除域名的任务
        
        @param request: SaveTaskForSubmittingDomainDeleteRequest
        @return: SaveTaskForSubmittingDomainDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_submitting_domain_delete_with_options_async(request, runtime)

    def save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        """
        @summary 批量提交域名资料
        
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not UtilClient.is_unset(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredential',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        """
        @summary 批量提交域名资料
        
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not UtilClient.is_unset(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredential',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_submitting_domain_real_name_verification_by_identity_credential(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        """
        @summary 批量提交域名资料
        
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest
        @return: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options(request, runtime)

    async def save_task_for_submitting_domain_real_name_verification_by_identity_credential_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        """
        @summary 批量提交域名资料
        
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest
        @return: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options_async(request, runtime)

    def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        """
        @summary 根据模板保存域名的实名认证信息
        
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileID',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        """
        @summary 根据模板保存域名的实名认证信息
        
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileID',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_id(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        """
        @summary 根据模板保存域名的实名认证信息
        
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest
        @return: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options(request, runtime)

    async def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_id_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        """
        @summary 根据模板保存域名的实名认证信息
        
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest
        @return: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options_async(request, runtime)

    def save_task_for_updating_registrant_info_by_identity_credential_with_options(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        """
        @summary 根据联系人信息批量修改注册联系人信息
        
        @param request: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not UtilClient.is_unset(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        body = {}
        if not UtilClient.is_unset(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveTaskForUpdatingRegistrantInfoByIdentityCredential',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_updating_registrant_info_by_identity_credential_with_options_async(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        """
        @summary 根据联系人信息批量修改注册联系人信息
        
        @param request: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not UtilClient.is_unset(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        body = {}
        if not UtilClient.is_unset(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveTaskForUpdatingRegistrantInfoByIdentityCredential',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_updating_registrant_info_by_identity_credential(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        """
        @summary 根据联系人信息批量修改注册联系人信息
        
        @param request: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest
        @return: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_updating_registrant_info_by_identity_credential_with_options(request, runtime)

    async def save_task_for_updating_registrant_info_by_identity_credential_async(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        """
        @summary 根据联系人信息批量修改注册联系人信息
        
        @param request: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest
        @return: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_updating_registrant_info_by_identity_credential_with_options_async(request, runtime)

    def save_task_for_updating_registrant_info_by_registrant_profile_idwith_options(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        """
        @summary 根据模板批量修改注册联系人
        
        @param request: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTaskForUpdatingRegistrantInfoByRegistrantProfileID',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_updating_registrant_info_by_registrant_profile_idwith_options_async(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        """
        @summary 根据模板批量修改注册联系人
        
        @param request: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTaskForUpdatingRegistrantInfoByRegistrantProfileID',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_updating_registrant_info_by_registrant_profile_id(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        """
        @summary 根据模板批量修改注册联系人
        
        @param request: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest
        @return: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_updating_registrant_info_by_registrant_profile_idwith_options(request, runtime)

    async def save_task_for_updating_registrant_info_by_registrant_profile_id_async(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        """
        @summary 根据模板批量修改注册联系人
        
        @param request: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest
        @return: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_updating_registrant_info_by_registrant_profile_idwith_options_async(request, runtime)

    def scroll_domain_list_with_options(
        self,
        request: domain_20180129_models.ScrollDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ScrollDomainListResponse:
        """
        @summary Traverses domain names.
        
        @description If you have a large number of domain names, a slow response may occur when you call an API operation to query domain names. In this case, you can call this operation to query domain names more quickly. When you call this operation for the first time, specify the request parameters except ScrollId. A scroll ID is returned without other data. In the second request, use the scroll ID obtained from the previous response. In subsequent requests, the newly specified request parameters do not take effect, and the request parameters that are specified in the first request prevail.
        
        @param request: ScrollDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScrollDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not UtilClient.is_unset(request.end_length):
            query['EndLength'] = request.end_length
        if not UtilClient.is_unset(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not UtilClient.is_unset(request.excluded):
            query['Excluded'] = request.excluded
        if not UtilClient.is_unset(request.excluded_prefix):
            query['ExcludedPrefix'] = request.excluded_prefix
        if not UtilClient.is_unset(request.excluded_suffix):
            query['ExcludedSuffix'] = request.excluded_suffix
        if not UtilClient.is_unset(request.form):
            query['Form'] = request.form
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.key_word_prefix):
            query['KeyWordPrefix'] = request.key_word_prefix
        if not UtilClient.is_unset(request.key_word_suffix):
            query['KeyWordSuffix'] = request.key_word_suffix
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scroll_id):
            query['ScrollId'] = request.scroll_id
        if not UtilClient.is_unset(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not UtilClient.is_unset(request.start_length):
            query['StartLength'] = request.start_length
        if not UtilClient.is_unset(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not UtilClient.is_unset(request.suffixs):
            query['Suffixs'] = request.suffixs
        if not UtilClient.is_unset(request.trade_type):
            query['TradeType'] = request.trade_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScrollDomainList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ScrollDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def scroll_domain_list_with_options_async(
        self,
        request: domain_20180129_models.ScrollDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ScrollDomainListResponse:
        """
        @summary Traverses domain names.
        
        @description If you have a large number of domain names, a slow response may occur when you call an API operation to query domain names. In this case, you can call this operation to query domain names more quickly. When you call this operation for the first time, specify the request parameters except ScrollId. A scroll ID is returned without other data. In the second request, use the scroll ID obtained from the previous response. In subsequent requests, the newly specified request parameters do not take effect, and the request parameters that are specified in the first request prevail.
        
        @param request: ScrollDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScrollDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not UtilClient.is_unset(request.end_length):
            query['EndLength'] = request.end_length
        if not UtilClient.is_unset(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not UtilClient.is_unset(request.excluded):
            query['Excluded'] = request.excluded
        if not UtilClient.is_unset(request.excluded_prefix):
            query['ExcludedPrefix'] = request.excluded_prefix
        if not UtilClient.is_unset(request.excluded_suffix):
            query['ExcludedSuffix'] = request.excluded_suffix
        if not UtilClient.is_unset(request.form):
            query['Form'] = request.form
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.key_word_prefix):
            query['KeyWordPrefix'] = request.key_word_prefix
        if not UtilClient.is_unset(request.key_word_suffix):
            query['KeyWordSuffix'] = request.key_word_suffix
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scroll_id):
            query['ScrollId'] = request.scroll_id
        if not UtilClient.is_unset(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not UtilClient.is_unset(request.start_length):
            query['StartLength'] = request.start_length
        if not UtilClient.is_unset(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not UtilClient.is_unset(request.suffixs):
            query['Suffixs'] = request.suffixs
        if not UtilClient.is_unset(request.trade_type):
            query['TradeType'] = request.trade_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScrollDomainList',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.ScrollDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scroll_domain_list(
        self,
        request: domain_20180129_models.ScrollDomainListRequest,
    ) -> domain_20180129_models.ScrollDomainListResponse:
        """
        @summary Traverses domain names.
        
        @description If you have a large number of domain names, a slow response may occur when you call an API operation to query domain names. In this case, you can call this operation to query domain names more quickly. When you call this operation for the first time, specify the request parameters except ScrollId. A scroll ID is returned without other data. In the second request, use the scroll ID obtained from the previous response. In subsequent requests, the newly specified request parameters do not take effect, and the request parameters that are specified in the first request prevail.
        
        @param request: ScrollDomainListRequest
        @return: ScrollDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.scroll_domain_list_with_options(request, runtime)

    async def scroll_domain_list_async(
        self,
        request: domain_20180129_models.ScrollDomainListRequest,
    ) -> domain_20180129_models.ScrollDomainListResponse:
        """
        @summary Traverses domain names.
        
        @description If you have a large number of domain names, a slow response may occur when you call an API operation to query domain names. In this case, you can call this operation to query domain names more quickly. When you call this operation for the first time, specify the request parameters except ScrollId. A scroll ID is returned without other data. In the second request, use the scroll ID obtained from the previous response. In subsequent requests, the newly specified request parameters do not take effect, and the request parameters that are specified in the first request prevail.
        
        @param request: ScrollDomainListRequest
        @return: ScrollDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.scroll_domain_list_with_options_async(request, runtime)

    def set_default_registrant_profile_with_options(
        self,
        request: domain_20180129_models.SetDefaultRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SetDefaultRegistrantProfileResponse:
        """
        @summary 设置默认模板
        
        @param request: SetDefaultRegistrantProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultRegistrantProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultRegistrantProfile',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SetDefaultRegistrantProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_registrant_profile_with_options_async(
        self,
        request: domain_20180129_models.SetDefaultRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SetDefaultRegistrantProfileResponse:
        """
        @summary 设置默认模板
        
        @param request: SetDefaultRegistrantProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultRegistrantProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultRegistrantProfile',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SetDefaultRegistrantProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_registrant_profile(
        self,
        request: domain_20180129_models.SetDefaultRegistrantProfileRequest,
    ) -> domain_20180129_models.SetDefaultRegistrantProfileResponse:
        """
        @summary 设置默认模板
        
        @param request: SetDefaultRegistrantProfileRequest
        @return: SetDefaultRegistrantProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_default_registrant_profile_with_options(request, runtime)

    async def set_default_registrant_profile_async(
        self,
        request: domain_20180129_models.SetDefaultRegistrantProfileRequest,
    ) -> domain_20180129_models.SetDefaultRegistrantProfileResponse:
        """
        @summary 设置默认模板
        
        @param request: SetDefaultRegistrantProfileRequest
        @return: SetDefaultRegistrantProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_default_registrant_profile_with_options_async(request, runtime)

    def setup_domain_auto_renew_with_options(
        self,
        request: domain_20180129_models.SetupDomainAutoRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SetupDomainAutoRenewResponse:
        """
        @summary 域名设置自动续费
        
        @param request: SetupDomainAutoRenewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetupDomainAutoRenewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetupDomainAutoRenew',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SetupDomainAutoRenewResponse(),
            self.call_api(params, req, runtime)
        )

    async def setup_domain_auto_renew_with_options_async(
        self,
        request: domain_20180129_models.SetupDomainAutoRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SetupDomainAutoRenewResponse:
        """
        @summary 域名设置自动续费
        
        @param request: SetupDomainAutoRenewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetupDomainAutoRenewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetupDomainAutoRenew',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SetupDomainAutoRenewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def setup_domain_auto_renew(
        self,
        request: domain_20180129_models.SetupDomainAutoRenewRequest,
    ) -> domain_20180129_models.SetupDomainAutoRenewResponse:
        """
        @summary 域名设置自动续费
        
        @param request: SetupDomainAutoRenewRequest
        @return: SetupDomainAutoRenewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.setup_domain_auto_renew_with_options(request, runtime)

    async def setup_domain_auto_renew_async(
        self,
        request: domain_20180129_models.SetupDomainAutoRenewRequest,
    ) -> domain_20180129_models.SetupDomainAutoRenewResponse:
        """
        @summary 域名设置自动续费
        
        @param request: SetupDomainAutoRenewRequest
        @return: SetupDomainAutoRenewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.setup_domain_auto_renew_with_options_async(request, runtime)

    def submit_domain_special_biz_credentials_with_options(
        self,
        request: domain_20180129_models.SubmitDomainSpecialBizCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitDomainSpecialBizCredentialsResponse:
        """
        @summary 域名特殊业务提交资料
        
        @param request: SubmitDomainSpecialBizCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDomainSpecialBizCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.credentials):
            body['Credentials'] = request.credentials
        if not UtilClient.is_unset(request.extend):
            body['Extend'] = request.extend
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitDomainSpecialBizCredentials',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SubmitDomainSpecialBizCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_domain_special_biz_credentials_with_options_async(
        self,
        request: domain_20180129_models.SubmitDomainSpecialBizCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitDomainSpecialBizCredentialsResponse:
        """
        @summary 域名特殊业务提交资料
        
        @param request: SubmitDomainSpecialBizCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDomainSpecialBizCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.credentials):
            body['Credentials'] = request.credentials
        if not UtilClient.is_unset(request.extend):
            body['Extend'] = request.extend
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitDomainSpecialBizCredentials',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SubmitDomainSpecialBizCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_domain_special_biz_credentials(
        self,
        request: domain_20180129_models.SubmitDomainSpecialBizCredentialsRequest,
    ) -> domain_20180129_models.SubmitDomainSpecialBizCredentialsResponse:
        """
        @summary 域名特殊业务提交资料
        
        @param request: SubmitDomainSpecialBizCredentialsRequest
        @return: SubmitDomainSpecialBizCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_domain_special_biz_credentials_with_options(request, runtime)

    async def submit_domain_special_biz_credentials_async(
        self,
        request: domain_20180129_models.SubmitDomainSpecialBizCredentialsRequest,
    ) -> domain_20180129_models.SubmitDomainSpecialBizCredentialsResponse:
        """
        @summary 域名特殊业务提交资料
        
        @param request: SubmitDomainSpecialBizCredentialsRequest
        @return: SubmitDomainSpecialBizCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_domain_special_biz_credentials_with_options_async(request, runtime)

    def submit_email_verification_with_options(
        self,
        request: domain_20180129_models.SubmitEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitEmailVerificationResponse:
        """
        @summary 提交邮箱验证
        
        @param request: SubmitEmailVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitEmailVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.send_if_exist):
            query['SendIfExist'] = request.send_if_exist
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitEmailVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SubmitEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_email_verification_with_options_async(
        self,
        request: domain_20180129_models.SubmitEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitEmailVerificationResponse:
        """
        @summary 提交邮箱验证
        
        @param request: SubmitEmailVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitEmailVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.send_if_exist):
            query['SendIfExist'] = request.send_if_exist
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitEmailVerification',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SubmitEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_email_verification(
        self,
        request: domain_20180129_models.SubmitEmailVerificationRequest,
    ) -> domain_20180129_models.SubmitEmailVerificationResponse:
        """
        @summary 提交邮箱验证
        
        @param request: SubmitEmailVerificationRequest
        @return: SubmitEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_email_verification_with_options(request, runtime)

    async def submit_email_verification_async(
        self,
        request: domain_20180129_models.SubmitEmailVerificationRequest,
    ) -> domain_20180129_models.SubmitEmailVerificationResponse:
        """
        @summary 提交邮箱验证
        
        @param request: SubmitEmailVerificationRequest
        @return: SubmitEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_email_verification_with_options_async(request, runtime)

    def submit_operation_audit_info_with_options(
        self,
        request: domain_20180129_models.SubmitOperationAuditInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitOperationAuditInfoResponse:
        """
        @summary 提交申请信息
        
        @param request: SubmitOperationAuditInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitOperationAuditInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_info):
            query['AuditInfo'] = request.audit_info
        if not UtilClient.is_unset(request.audit_type):
            query['AuditType'] = request.audit_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitOperationAuditInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SubmitOperationAuditInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_operation_audit_info_with_options_async(
        self,
        request: domain_20180129_models.SubmitOperationAuditInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitOperationAuditInfoResponse:
        """
        @summary 提交申请信息
        
        @param request: SubmitOperationAuditInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitOperationAuditInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_info):
            query['AuditInfo'] = request.audit_info
        if not UtilClient.is_unset(request.audit_type):
            query['AuditType'] = request.audit_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitOperationAuditInfo',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SubmitOperationAuditInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_operation_audit_info(
        self,
        request: domain_20180129_models.SubmitOperationAuditInfoRequest,
    ) -> domain_20180129_models.SubmitOperationAuditInfoResponse:
        """
        @summary 提交申请信息
        
        @param request: SubmitOperationAuditInfoRequest
        @return: SubmitOperationAuditInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_operation_audit_info_with_options(request, runtime)

    async def submit_operation_audit_info_async(
        self,
        request: domain_20180129_models.SubmitOperationAuditInfoRequest,
    ) -> domain_20180129_models.SubmitOperationAuditInfoResponse:
        """
        @summary 提交申请信息
        
        @param request: SubmitOperationAuditInfoRequest
        @return: SubmitOperationAuditInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_operation_audit_info_with_options_async(request, runtime)

    def submit_operation_credentials_with_options(
        self,
        request: domain_20180129_models.SubmitOperationCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitOperationCredentialsResponse:
        """
        @summary 提交证件资料
        
        @param request: SubmitOperationCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitOperationCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not UtilClient.is_unset(request.audit_type):
            query['AuditType'] = request.audit_type
        if not UtilClient.is_unset(request.credentials):
            query['Credentials'] = request.credentials
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_type):
            query['RegType'] = request.reg_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitOperationCredentials',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SubmitOperationCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_operation_credentials_with_options_async(
        self,
        request: domain_20180129_models.SubmitOperationCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitOperationCredentialsResponse:
        """
        @summary 提交证件资料
        
        @param request: SubmitOperationCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitOperationCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not UtilClient.is_unset(request.audit_type):
            query['AuditType'] = request.audit_type
        if not UtilClient.is_unset(request.credentials):
            query['Credentials'] = request.credentials
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_type):
            query['RegType'] = request.reg_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitOperationCredentials',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.SubmitOperationCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_operation_credentials(
        self,
        request: domain_20180129_models.SubmitOperationCredentialsRequest,
    ) -> domain_20180129_models.SubmitOperationCredentialsResponse:
        """
        @summary 提交证件资料
        
        @param request: SubmitOperationCredentialsRequest
        @return: SubmitOperationCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_operation_credentials_with_options(request, runtime)

    async def submit_operation_credentials_async(
        self,
        request: domain_20180129_models.SubmitOperationCredentialsRequest,
    ) -> domain_20180129_models.SubmitOperationCredentialsResponse:
        """
        @summary 提交证件资料
        
        @param request: SubmitOperationCredentialsRequest
        @return: SubmitOperationCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_operation_credentials_with_options_async(request, runtime)

    def transfer_in_check_mail_token_with_options(
        self,
        request: domain_20180129_models.TransferInCheckMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInCheckMailTokenResponse:
        """
        @param request: TransferInCheckMailTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferInCheckMailTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInCheckMailToken',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.TransferInCheckMailTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_check_mail_token_with_options_async(
        self,
        request: domain_20180129_models.TransferInCheckMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInCheckMailTokenResponse:
        """
        @param request: TransferInCheckMailTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferInCheckMailTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInCheckMailToken',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.TransferInCheckMailTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_check_mail_token(
        self,
        request: domain_20180129_models.TransferInCheckMailTokenRequest,
    ) -> domain_20180129_models.TransferInCheckMailTokenResponse:
        """
        @param request: TransferInCheckMailTokenRequest
        @return: TransferInCheckMailTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_check_mail_token_with_options(request, runtime)

    async def transfer_in_check_mail_token_async(
        self,
        request: domain_20180129_models.TransferInCheckMailTokenRequest,
    ) -> domain_20180129_models.TransferInCheckMailTokenResponse:
        """
        @param request: TransferInCheckMailTokenRequest
        @return: TransferInCheckMailTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_check_mail_token_with_options_async(request, runtime)

    def transfer_in_reenter_transfer_authorization_code_with_options(
        self,
        request: domain_20180129_models.TransferInReenterTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInReenterTransferAuthorizationCodeResponse:
        """
        @param request: TransferInReenterTransferAuthorizationCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferInReenterTransferAuthorizationCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.transfer_authorization_code):
            query['TransferAuthorizationCode'] = request.transfer_authorization_code
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInReenterTransferAuthorizationCode',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.TransferInReenterTransferAuthorizationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_reenter_transfer_authorization_code_with_options_async(
        self,
        request: domain_20180129_models.TransferInReenterTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInReenterTransferAuthorizationCodeResponse:
        """
        @param request: TransferInReenterTransferAuthorizationCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferInReenterTransferAuthorizationCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.transfer_authorization_code):
            query['TransferAuthorizationCode'] = request.transfer_authorization_code
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInReenterTransferAuthorizationCode',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.TransferInReenterTransferAuthorizationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_reenter_transfer_authorization_code(
        self,
        request: domain_20180129_models.TransferInReenterTransferAuthorizationCodeRequest,
    ) -> domain_20180129_models.TransferInReenterTransferAuthorizationCodeResponse:
        """
        @param request: TransferInReenterTransferAuthorizationCodeRequest
        @return: TransferInReenterTransferAuthorizationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_reenter_transfer_authorization_code_with_options(request, runtime)

    async def transfer_in_reenter_transfer_authorization_code_async(
        self,
        request: domain_20180129_models.TransferInReenterTransferAuthorizationCodeRequest,
    ) -> domain_20180129_models.TransferInReenterTransferAuthorizationCodeResponse:
        """
        @param request: TransferInReenterTransferAuthorizationCodeRequest
        @return: TransferInReenterTransferAuthorizationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_reenter_transfer_authorization_code_with_options_async(request, runtime)

    def transfer_in_refetch_whois_email_with_options(
        self,
        request: domain_20180129_models.TransferInRefetchWhoisEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInRefetchWhoisEmailResponse:
        """
        @param request: TransferInRefetchWhoisEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferInRefetchWhoisEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInRefetchWhoisEmail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.TransferInRefetchWhoisEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_refetch_whois_email_with_options_async(
        self,
        request: domain_20180129_models.TransferInRefetchWhoisEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInRefetchWhoisEmailResponse:
        """
        @param request: TransferInRefetchWhoisEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferInRefetchWhoisEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInRefetchWhoisEmail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.TransferInRefetchWhoisEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_refetch_whois_email(
        self,
        request: domain_20180129_models.TransferInRefetchWhoisEmailRequest,
    ) -> domain_20180129_models.TransferInRefetchWhoisEmailResponse:
        """
        @param request: TransferInRefetchWhoisEmailRequest
        @return: TransferInRefetchWhoisEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_refetch_whois_email_with_options(request, runtime)

    async def transfer_in_refetch_whois_email_async(
        self,
        request: domain_20180129_models.TransferInRefetchWhoisEmailRequest,
    ) -> domain_20180129_models.TransferInRefetchWhoisEmailResponse:
        """
        @param request: TransferInRefetchWhoisEmailRequest
        @return: TransferInRefetchWhoisEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_refetch_whois_email_with_options_async(request, runtime)

    def transfer_in_resend_mail_token_with_options(
        self,
        request: domain_20180129_models.TransferInResendMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInResendMailTokenResponse:
        """
        @param request: TransferInResendMailTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferInResendMailTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInResendMailToken',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.TransferInResendMailTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_resend_mail_token_with_options_async(
        self,
        request: domain_20180129_models.TransferInResendMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInResendMailTokenResponse:
        """
        @param request: TransferInResendMailTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferInResendMailTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInResendMailToken',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.TransferInResendMailTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_resend_mail_token(
        self,
        request: domain_20180129_models.TransferInResendMailTokenRequest,
    ) -> domain_20180129_models.TransferInResendMailTokenResponse:
        """
        @param request: TransferInResendMailTokenRequest
        @return: TransferInResendMailTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_resend_mail_token_with_options(request, runtime)

    async def transfer_in_resend_mail_token_async(
        self,
        request: domain_20180129_models.TransferInResendMailTokenRequest,
    ) -> domain_20180129_models.TransferInResendMailTokenResponse:
        """
        @param request: TransferInResendMailTokenRequest
        @return: TransferInResendMailTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_resend_mail_token_with_options_async(request, runtime)

    def update_domain_to_domain_group_with_options(
        self,
        request: domain_20180129_models.UpdateDomainToDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.UpdateDomainToDomainGroupResponse:
        """
        @summary 向分组设置域名
        
        @param request: UpdateDomainToDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainToDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source):
            query['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.file_to_upload):
            body['FileToUpload'] = request.file_to_upload
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDomainToDomainGroup',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.UpdateDomainToDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_to_domain_group_with_options_async(
        self,
        request: domain_20180129_models.UpdateDomainToDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.UpdateDomainToDomainGroupResponse:
        """
        @summary 向分组设置域名
        
        @param request: UpdateDomainToDomainGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainToDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source):
            query['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.file_to_upload):
            body['FileToUpload'] = request.file_to_upload
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDomainToDomainGroup',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.UpdateDomainToDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_to_domain_group(
        self,
        request: domain_20180129_models.UpdateDomainToDomainGroupRequest,
    ) -> domain_20180129_models.UpdateDomainToDomainGroupResponse:
        """
        @summary 向分组设置域名
        
        @param request: UpdateDomainToDomainGroupRequest
        @return: UpdateDomainToDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_domain_to_domain_group_with_options(request, runtime)

    async def update_domain_to_domain_group_async(
        self,
        request: domain_20180129_models.UpdateDomainToDomainGroupRequest,
    ) -> domain_20180129_models.UpdateDomainToDomainGroupResponse:
        """
        @summary 向分组设置域名
        
        @param request: UpdateDomainToDomainGroupRequest
        @return: UpdateDomainToDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_to_domain_group_with_options_async(request, runtime)

    def verify_contact_field_with_options(
        self,
        request: domain_20180129_models.VerifyContactFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.VerifyContactFieldResponse:
        """
        @summary 校验联系人信息
        
        @param request: VerifyContactFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyContactFieldResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyContactField',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.VerifyContactFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_contact_field_with_options_async(
        self,
        request: domain_20180129_models.VerifyContactFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.VerifyContactFieldResponse:
        """
        @summary 校验联系人信息
        
        @param request: VerifyContactFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyContactFieldResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not UtilClient.is_unset(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not UtilClient.is_unset(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not UtilClient.is_unset(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not UtilClient.is_unset(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyContactField',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.VerifyContactFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_contact_field(
        self,
        request: domain_20180129_models.VerifyContactFieldRequest,
    ) -> domain_20180129_models.VerifyContactFieldResponse:
        """
        @summary 校验联系人信息
        
        @param request: VerifyContactFieldRequest
        @return: VerifyContactFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_contact_field_with_options(request, runtime)

    async def verify_contact_field_async(
        self,
        request: domain_20180129_models.VerifyContactFieldRequest,
    ) -> domain_20180129_models.VerifyContactFieldResponse:
        """
        @summary 校验联系人信息
        
        @param request: VerifyContactFieldRequest
        @return: VerifyContactFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_contact_field_with_options_async(request, runtime)

    def verify_email_with_options(
        self,
        request: domain_20180129_models.VerifyEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.VerifyEmailResponse:
        """
        @summary 验证邮箱Token
        
        @param request: VerifyEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyEmail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.VerifyEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_email_with_options_async(
        self,
        request: domain_20180129_models.VerifyEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.VerifyEmailResponse:
        """
        @summary 验证邮箱Token
        
        @param request: VerifyEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyEmail',
            version='2018-01-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_20180129_models.VerifyEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_email(
        self,
        request: domain_20180129_models.VerifyEmailRequest,
    ) -> domain_20180129_models.VerifyEmailResponse:
        """
        @summary 验证邮箱Token
        
        @param request: VerifyEmailRequest
        @return: VerifyEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_email_with_options(request, runtime)

    async def verify_email_async(
        self,
        request: domain_20180129_models.VerifyEmailRequest,
    ) -> domain_20180129_models.VerifyEmailResponse:
        """
        @summary 验证邮箱Token
        
        @param request: VerifyEmailRequest
        @return: VerifyEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_email_with_options_async(request, runtime)
