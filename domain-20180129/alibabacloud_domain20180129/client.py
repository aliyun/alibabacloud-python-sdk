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
        runtime = util_models.RuntimeOptions()
        return self.acknowledge_task_result_with_options(request, runtime)

    async def acknowledge_task_result_async(
        self,
        request: domain_20180129_models.AcknowledgeTaskResultRequest,
    ) -> domain_20180129_models.AcknowledgeTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.acknowledge_task_result_with_options_async(request, runtime)

    def batch_fuzzy_match_domain_sensitive_word_with_options(
        self,
        request: domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.batch_fuzzy_match_domain_sensitive_word_with_options(request, runtime)

    async def batch_fuzzy_match_domain_sensitive_word_async(
        self,
        request: domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordRequest,
    ) -> domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_fuzzy_match_domain_sensitive_word_with_options_async(request, runtime)

    def cancel_domain_verification_with_options(
        self,
        request: domain_20180129_models.CancelDomainVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelDomainVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.cancel_domain_verification_with_options(request, runtime)

    async def cancel_domain_verification_async(
        self,
        request: domain_20180129_models.CancelDomainVerificationRequest,
    ) -> domain_20180129_models.CancelDomainVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_domain_verification_with_options_async(request, runtime)

    def cancel_operation_audit_with_options(
        self,
        request: domain_20180129_models.CancelOperationAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelOperationAuditResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.cancel_operation_audit_with_options(request, runtime)

    async def cancel_operation_audit_async(
        self,
        request: domain_20180129_models.CancelOperationAuditRequest,
    ) -> domain_20180129_models.CancelOperationAuditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_operation_audit_with_options_async(request, runtime)

    def cancel_qualification_verification_with_options(
        self,
        request: domain_20180129_models.CancelQualificationVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelQualificationVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.cancel_qualification_verification_with_options(request, runtime)

    async def cancel_qualification_verification_async(
        self,
        request: domain_20180129_models.CancelQualificationVerificationRequest,
    ) -> domain_20180129_models.CancelQualificationVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_qualification_verification_with_options_async(request, runtime)

    def cancel_task_with_options(
        self,
        request: domain_20180129_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    async def cancel_task_async(
        self,
        request: domain_20180129_models.CancelTaskRequest,
    ) -> domain_20180129_models.CancelTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_task_with_options_async(request, runtime)

    def check_domain_with_options(
        self,
        request: domain_20180129_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    async def check_domain_async(
        self,
        request: domain_20180129_models.CheckDomainRequest,
    ) -> domain_20180129_models.CheckDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_domain_with_options_async(request, runtime)

    def check_domain_sunrise_claim_with_options(
        self,
        request: domain_20180129_models.CheckDomainSunriseClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckDomainSunriseClaimResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.check_domain_sunrise_claim_with_options(request, runtime)

    async def check_domain_sunrise_claim_async(
        self,
        request: domain_20180129_models.CheckDomainSunriseClaimRequest,
    ) -> domain_20180129_models.CheckDomainSunriseClaimResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_domain_sunrise_claim_with_options_async(request, runtime)

    def check_max_year_of_server_lock_with_options(
        self,
        request: domain_20180129_models.CheckMaxYearOfServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckMaxYearOfServerLockResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.check_max_year_of_server_lock_with_options(request, runtime)

    async def check_max_year_of_server_lock_async(
        self,
        request: domain_20180129_models.CheckMaxYearOfServerLockRequest,
    ) -> domain_20180129_models.CheckMaxYearOfServerLockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_max_year_of_server_lock_with_options_async(request, runtime)

    def check_processing_server_lock_apply_with_options(
        self,
        request: domain_20180129_models.CheckProcessingServerLockApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckProcessingServerLockApplyResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.check_processing_server_lock_apply_with_options(request, runtime)

    async def check_processing_server_lock_apply_async(
        self,
        request: domain_20180129_models.CheckProcessingServerLockApplyRequest,
    ) -> domain_20180129_models.CheckProcessingServerLockApplyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_processing_server_lock_apply_with_options_async(request, runtime)

    def check_transfer_in_feasibility_with_options(
        self,
        request: domain_20180129_models.CheckTransferInFeasibilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckTransferInFeasibilityResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.check_transfer_in_feasibility_with_options(request, runtime)

    async def check_transfer_in_feasibility_async(
        self,
        request: domain_20180129_models.CheckTransferInFeasibilityRequest,
    ) -> domain_20180129_models.CheckTransferInFeasibilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_transfer_in_feasibility_with_options_async(request, runtime)

    def confirm_transfer_in_email_with_options(
        self,
        request: domain_20180129_models.ConfirmTransferInEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ConfirmTransferInEmailResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.confirm_transfer_in_email_with_options(request, runtime)

    async def confirm_transfer_in_email_async(
        self,
        request: domain_20180129_models.ConfirmTransferInEmailRequest,
    ) -> domain_20180129_models.ConfirmTransferInEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_transfer_in_email_with_options_async(request, runtime)

    def delete_contact_templates_with_options(
        self,
        request: domain_20180129_models.DeleteContactTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteContactTemplatesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_templates_with_options(request, runtime)

    async def delete_contact_templates_async(
        self,
        request: domain_20180129_models.DeleteContactTemplatesRequest,
    ) -> domain_20180129_models.DeleteContactTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_contact_templates_with_options_async(request, runtime)

    def delete_domain_group_with_options(
        self,
        request: domain_20180129_models.DeleteDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteDomainGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_group_with_options(request, runtime)

    async def delete_domain_group_async(
        self,
        request: domain_20180129_models.DeleteDomainGroupRequest,
    ) -> domain_20180129_models.DeleteDomainGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_group_with_options_async(request, runtime)

    def delete_email_verification_with_options(
        self,
        request: domain_20180129_models.DeleteEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteEmailVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_email_verification_with_options(request, runtime)

    async def delete_email_verification_async(
        self,
        request: domain_20180129_models.DeleteEmailVerificationRequest,
    ) -> domain_20180129_models.DeleteEmailVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_email_verification_with_options_async(request, runtime)

    def delete_registrant_profile_with_options(
        self,
        request: domain_20180129_models.DeleteRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteRegistrantProfileResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_registrant_profile_with_options(request, runtime)

    async def delete_registrant_profile_async(
        self,
        request: domain_20180129_models.DeleteRegistrantProfileRequest,
    ) -> domain_20180129_models.DeleteRegistrantProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_registrant_profile_with_options_async(request, runtime)

    def email_verified_with_options(
        self,
        request: domain_20180129_models.EmailVerifiedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.EmailVerifiedResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.email_verified_with_options(request, runtime)

    async def email_verified_async(
        self,
        request: domain_20180129_models.EmailVerifiedRequest,
    ) -> domain_20180129_models.EmailVerifiedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.email_verified_with_options_async(request, runtime)

    def fuzzy_match_domain_sensitive_word_with_options(
        self,
        request: domain_20180129_models.FuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.FuzzyMatchDomainSensitiveWordResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.fuzzy_match_domain_sensitive_word_with_options(request, runtime)

    async def fuzzy_match_domain_sensitive_word_async(
        self,
        request: domain_20180129_models.FuzzyMatchDomainSensitiveWordRequest,
    ) -> domain_20180129_models.FuzzyMatchDomainSensitiveWordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fuzzy_match_domain_sensitive_word_with_options_async(request, runtime)

    def get_operation_oss_upload_policy_with_options(
        self,
        request: domain_20180129_models.GetOperationOssUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.GetOperationOssUploadPolicyResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_operation_oss_upload_policy_with_options(request, runtime)

    async def get_operation_oss_upload_policy_async(
        self,
        request: domain_20180129_models.GetOperationOssUploadPolicyRequest,
    ) -> domain_20180129_models.GetOperationOssUploadPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_operation_oss_upload_policy_with_options_async(request, runtime)

    def get_qualification_upload_policy_with_options(
        self,
        request: domain_20180129_models.GetQualificationUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.GetQualificationUploadPolicyResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_qualification_upload_policy_with_options(request, runtime)

    async def get_qualification_upload_policy_async(
        self,
        request: domain_20180129_models.GetQualificationUploadPolicyRequest,
    ) -> domain_20180129_models.GetQualificationUploadPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_qualification_upload_policy_with_options_async(request, runtime)

    def list_email_verification_with_options(
        self,
        request: domain_20180129_models.ListEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ListEmailVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_email_verification_with_options(request, runtime)

    async def list_email_verification_async(
        self,
        request: domain_20180129_models.ListEmailVerificationRequest,
    ) -> domain_20180129_models.ListEmailVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_email_verification_with_options_async(request, runtime)

    def list_server_lock_with_options(
        self,
        request: domain_20180129_models.ListServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ListServerLockResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_server_lock_with_options(request, runtime)

    async def list_server_lock_async(
        self,
        request: domain_20180129_models.ListServerLockRequest,
    ) -> domain_20180129_models.ListServerLockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_server_lock_with_options_async(request, runtime)

    def lookup_tmch_notice_with_options(
        self,
        request: domain_20180129_models.LookupTmchNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.LookupTmchNoticeResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.lookup_tmch_notice_with_options(request, runtime)

    async def lookup_tmch_notice_async(
        self,
        request: domain_20180129_models.LookupTmchNoticeRequest,
    ) -> domain_20180129_models.LookupTmchNoticeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lookup_tmch_notice_with_options_async(request, runtime)

    def poll_task_result_with_options(
        self,
        request: domain_20180129_models.PollTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.PollTaskResultResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.poll_task_result_with_options(request, runtime)

    async def poll_task_result_async(
        self,
        request: domain_20180129_models.PollTaskResultRequest,
    ) -> domain_20180129_models.PollTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.poll_task_result_with_options_async(request, runtime)

    def query_advanced_domain_list_with_options(
        self,
        request: domain_20180129_models.QueryAdvancedDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryAdvancedDomainListResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_advanced_domain_list_with_options(request, runtime)

    async def query_advanced_domain_list_async(
        self,
        request: domain_20180129_models.QueryAdvancedDomainListRequest,
    ) -> domain_20180129_models.QueryAdvancedDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_advanced_domain_list_with_options_async(request, runtime)

    def query_art_extension_with_options(
        self,
        request: domain_20180129_models.QueryArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryArtExtensionResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_art_extension_with_options(request, runtime)

    async def query_art_extension_async(
        self,
        request: domain_20180129_models.QueryArtExtensionRequest,
    ) -> domain_20180129_models.QueryArtExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_art_extension_with_options_async(request, runtime)

    def query_change_log_list_with_options(
        self,
        request: domain_20180129_models.QueryChangeLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryChangeLogListResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_change_log_list_with_options(request, runtime)

    async def query_change_log_list_async(
        self,
        request: domain_20180129_models.QueryChangeLogListRequest,
    ) -> domain_20180129_models.QueryChangeLogListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_change_log_list_with_options_async(request, runtime)

    def query_contact_info_with_options(
        self,
        request: domain_20180129_models.QueryContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryContactInfoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_contact_info_with_options(request, runtime)

    async def query_contact_info_async(
        self,
        request: domain_20180129_models.QueryContactInfoRequest,
    ) -> domain_20180129_models.QueryContactInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_contact_info_with_options_async(request, runtime)

    def query_dsrecord_with_options(
        self,
        request: domain_20180129_models.QueryDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDSRecordResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_dsrecord_with_options(request, runtime)

    async def query_dsrecord_async(
        self,
        request: domain_20180129_models.QueryDSRecordRequest,
    ) -> domain_20180129_models.QueryDSRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dsrecord_with_options_async(request, runtime)

    def query_dns_host_with_options(
        self,
        request: domain_20180129_models.QueryDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDnsHostResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_dns_host_with_options(request, runtime)

    async def query_dns_host_async(
        self,
        request: domain_20180129_models.QueryDnsHostRequest,
    ) -> domain_20180129_models.QueryDnsHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dns_host_with_options_async(request, runtime)

    def query_domain_admin_division_with_options(
        self,
        request: domain_20180129_models.QueryDomainAdminDivisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainAdminDivisionResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_domain_admin_division_with_options(request, runtime)

    async def query_domain_admin_division_async(
        self,
        request: domain_20180129_models.QueryDomainAdminDivisionRequest,
    ) -> domain_20180129_models.QueryDomainAdminDivisionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_admin_division_with_options_async(request, runtime)

    def query_domain_by_domain_name_with_options(
        self,
        request: domain_20180129_models.QueryDomainByDomainNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainByDomainNameResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_domain_by_domain_name_with_options(request, runtime)

    async def query_domain_by_domain_name_async(
        self,
        request: domain_20180129_models.QueryDomainByDomainNameRequest,
    ) -> domain_20180129_models.QueryDomainByDomainNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_by_domain_name_with_options_async(request, runtime)

    def query_domain_by_instance_id_with_options(
        self,
        request: domain_20180129_models.QueryDomainByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainByInstanceIdResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_domain_by_instance_id_with_options(request, runtime)

    async def query_domain_by_instance_id_async(
        self,
        request: domain_20180129_models.QueryDomainByInstanceIdRequest,
    ) -> domain_20180129_models.QueryDomainByInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_by_instance_id_with_options_async(request, runtime)

    def query_domain_group_list_with_options(
        self,
        request: domain_20180129_models.QueryDomainGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainGroupListResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_domain_group_list_with_options(request, runtime)

    async def query_domain_group_list_async(
        self,
        request: domain_20180129_models.QueryDomainGroupListRequest,
    ) -> domain_20180129_models.QueryDomainGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_group_list_with_options_async(request, runtime)

    def query_domain_list_with_options(
        self,
        request: domain_20180129_models.QueryDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainListResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not UtilClient.is_unset(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
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
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not UtilClient.is_unset(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
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
        runtime = util_models.RuntimeOptions()
        return self.query_domain_list_with_options(request, runtime)

    async def query_domain_list_async(
        self,
        request: domain_20180129_models.QueryDomainListRequest,
    ) -> domain_20180129_models.QueryDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_list_with_options_async(request, runtime)

    def query_domain_real_name_verification_info_with_options(
        self,
        request: domain_20180129_models.QueryDomainRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainRealNameVerificationInfoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_domain_real_name_verification_info_with_options(request, runtime)

    async def query_domain_real_name_verification_info_async(
        self,
        request: domain_20180129_models.QueryDomainRealNameVerificationInfoRequest,
    ) -> domain_20180129_models.QueryDomainRealNameVerificationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_real_name_verification_info_with_options_async(request, runtime)

    def query_domain_suffix_with_options(
        self,
        request: domain_20180129_models.QueryDomainSuffixRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainSuffixResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_domain_suffix_with_options(request, runtime)

    async def query_domain_suffix_async(
        self,
        request: domain_20180129_models.QueryDomainSuffixRequest,
    ) -> domain_20180129_models.QueryDomainSuffixResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_suffix_with_options_async(request, runtime)

    def query_email_verification_with_options(
        self,
        request: domain_20180129_models.QueryEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryEmailVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_email_verification_with_options(request, runtime)

    async def query_email_verification_async(
        self,
        request: domain_20180129_models.QueryEmailVerificationRequest,
    ) -> domain_20180129_models.QueryEmailVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_email_verification_with_options_async(request, runtime)

    def query_ens_association_with_options(
        self,
        request: domain_20180129_models.QueryEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryEnsAssociationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_ens_association_with_options(request, runtime)

    async def query_ens_association_async(
        self,
        request: domain_20180129_models.QueryEnsAssociationRequest,
    ) -> domain_20180129_models.QueryEnsAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ens_association_with_options_async(request, runtime)

    def query_fail_reason_for_domain_real_name_verification_with_options(
        self,
        request: domain_20180129_models.QueryFailReasonForDomainRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_fail_reason_for_domain_real_name_verification_with_options(request, runtime)

    async def query_fail_reason_for_domain_real_name_verification_async(
        self,
        request: domain_20180129_models.QueryFailReasonForDomainRealNameVerificationRequest,
    ) -> domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_fail_reason_for_domain_real_name_verification_with_options_async(request, runtime)

    def query_fail_reason_for_registrant_profile_real_name_verification_with_options(
        self,
        request: domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_fail_reason_for_registrant_profile_real_name_verification_with_options(request, runtime)

    async def query_fail_reason_for_registrant_profile_real_name_verification_async(
        self,
        request: domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
    ) -> domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_fail_reason_for_registrant_profile_real_name_verification_with_options_async(request, runtime)

    def query_failing_reason_list_for_qualification_with_options(
        self,
        request: domain_20180129_models.QueryFailingReasonListForQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailingReasonListForQualificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_failing_reason_list_for_qualification_with_options(request, runtime)

    async def query_failing_reason_list_for_qualification_async(
        self,
        request: domain_20180129_models.QueryFailingReasonListForQualificationRequest,
    ) -> domain_20180129_models.QueryFailingReasonListForQualificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_failing_reason_list_for_qualification_with_options_async(request, runtime)

    def query_local_ens_association_with_options(
        self,
        request: domain_20180129_models.QueryLocalEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryLocalEnsAssociationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_local_ens_association_with_options(request, runtime)

    async def query_local_ens_association_async(
        self,
        request: domain_20180129_models.QueryLocalEnsAssociationRequest,
    ) -> domain_20180129_models.QueryLocalEnsAssociationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_local_ens_association_with_options_async(request, runtime)

    def query_operation_audit_info_detail_with_options(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryOperationAuditInfoDetailResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_operation_audit_info_detail_with_options(request, runtime)

    async def query_operation_audit_info_detail_async(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoDetailRequest,
    ) -> domain_20180129_models.QueryOperationAuditInfoDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_operation_audit_info_detail_with_options_async(request, runtime)

    def query_operation_audit_info_list_with_options(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryOperationAuditInfoListResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_operation_audit_info_list_with_options(request, runtime)

    async def query_operation_audit_info_list_async(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoListRequest,
    ) -> domain_20180129_models.QueryOperationAuditInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_operation_audit_info_list_with_options_async(request, runtime)

    def query_qualification_detail_with_options(
        self,
        request: domain_20180129_models.QueryQualificationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryQualificationDetailResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_qualification_detail_with_options(request, runtime)

    async def query_qualification_detail_async(
        self,
        request: domain_20180129_models.QueryQualificationDetailRequest,
    ) -> domain_20180129_models.QueryQualificationDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_qualification_detail_with_options_async(request, runtime)

    def query_registrant_profile_real_name_verification_info_with_options(
        self,
        request: domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_registrant_profile_real_name_verification_info_with_options(request, runtime)

    async def query_registrant_profile_real_name_verification_info_async(
        self,
        request: domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
    ) -> domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_registrant_profile_real_name_verification_info_with_options_async(request, runtime)

    def query_registrant_profiles_with_options(
        self,
        request: domain_20180129_models.QueryRegistrantProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryRegistrantProfilesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_registrant_profiles_with_options(request, runtime)

    async def query_registrant_profiles_async(
        self,
        request: domain_20180129_models.QueryRegistrantProfilesRequest,
    ) -> domain_20180129_models.QueryRegistrantProfilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_registrant_profiles_with_options_async(request, runtime)

    def query_server_lock_with_options(
        self,
        request: domain_20180129_models.QueryServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryServerLockResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_server_lock_with_options(request, runtime)

    async def query_server_lock_async(
        self,
        request: domain_20180129_models.QueryServerLockRequest,
    ) -> domain_20180129_models.QueryServerLockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_server_lock_with_options_async(request, runtime)

    def query_task_detail_history_with_options(
        self,
        request: domain_20180129_models.QueryTaskDetailHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskDetailHistoryResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_task_detail_history_with_options(request, runtime)

    async def query_task_detail_history_async(
        self,
        request: domain_20180129_models.QueryTaskDetailHistoryRequest,
    ) -> domain_20180129_models.QueryTaskDetailHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_task_detail_history_with_options_async(request, runtime)

    def query_task_detail_list_with_options(
        self,
        request: domain_20180129_models.QueryTaskDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskDetailListResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_task_detail_list_with_options(request, runtime)

    async def query_task_detail_list_async(
        self,
        request: domain_20180129_models.QueryTaskDetailListRequest,
    ) -> domain_20180129_models.QueryTaskDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_task_detail_list_with_options_async(request, runtime)

    def query_task_info_history_with_options(
        self,
        request: domain_20180129_models.QueryTaskInfoHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskInfoHistoryResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_task_info_history_with_options(request, runtime)

    async def query_task_info_history_async(
        self,
        request: domain_20180129_models.QueryTaskInfoHistoryRequest,
    ) -> domain_20180129_models.QueryTaskInfoHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_task_info_history_with_options_async(request, runtime)

    def query_task_list_with_options(
        self,
        request: domain_20180129_models.QueryTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskListResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_task_list_with_options(request, runtime)

    async def query_task_list_async(
        self,
        request: domain_20180129_models.QueryTaskListRequest,
    ) -> domain_20180129_models.QueryTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_task_list_with_options_async(request, runtime)

    def query_transfer_in_by_instance_id_with_options(
        self,
        request: domain_20180129_models.QueryTransferInByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferInByInstanceIdResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_in_by_instance_id_with_options(request, runtime)

    async def query_transfer_in_by_instance_id_async(
        self,
        request: domain_20180129_models.QueryTransferInByInstanceIdRequest,
    ) -> domain_20180129_models.QueryTransferInByInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_in_by_instance_id_with_options_async(request, runtime)

    def query_transfer_in_list_with_options(
        self,
        request: domain_20180129_models.QueryTransferInListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferInListResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_in_list_with_options(request, runtime)

    async def query_transfer_in_list_async(
        self,
        request: domain_20180129_models.QueryTransferInListRequest,
    ) -> domain_20180129_models.QueryTransferInListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_in_list_with_options_async(request, runtime)

    def query_transfer_out_info_with_options(
        self,
        request: domain_20180129_models.QueryTransferOutInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferOutInfoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_out_info_with_options(request, runtime)

    async def query_transfer_out_info_async(
        self,
        request: domain_20180129_models.QueryTransferOutInfoRequest,
    ) -> domain_20180129_models.QueryTransferOutInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_out_info_with_options_async(request, runtime)

    def registrant_profile_real_name_verification_with_options(
        self,
        request: domain_20180129_models.RegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.RegistrantProfileRealNameVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.registrant_profile_real_name_verification_with_options(request, runtime)

    async def registrant_profile_real_name_verification_async(
        self,
        request: domain_20180129_models.RegistrantProfileRealNameVerificationRequest,
    ) -> domain_20180129_models.RegistrantProfileRealNameVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.registrant_profile_real_name_verification_with_options_async(request, runtime)

    def resend_email_verification_with_options(
        self,
        request: domain_20180129_models.ResendEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ResendEmailVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.resend_email_verification_with_options(request, runtime)

    async def resend_email_verification_async(
        self,
        request: domain_20180129_models.ResendEmailVerificationRequest,
    ) -> domain_20180129_models.ResendEmailVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resend_email_verification_with_options_async(request, runtime)

    def reset_qualification_verification_with_options(
        self,
        request: domain_20180129_models.ResetQualificationVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ResetQualificationVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.reset_qualification_verification_with_options(request, runtime)

    async def reset_qualification_verification_async(
        self,
        request: domain_20180129_models.ResetQualificationVerificationRequest,
    ) -> domain_20180129_models.ResetQualificationVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_qualification_verification_with_options_async(request, runtime)

    def save_batch_domain_remark_with_options(
        self,
        request: domain_20180129_models.SaveBatchDomainRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchDomainRemarkResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_domain_remark_with_options(request, runtime)

    async def save_batch_domain_remark_async(
        self,
        request: domain_20180129_models.SaveBatchDomainRemarkRequest,
    ) -> domain_20180129_models.SaveBatchDomainRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_domain_remark_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_activate_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderActivateResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_activate_with_options(request, runtime)

    async def save_batch_task_for_creating_order_activate_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderActivateRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderActivateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_activate_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_redeem_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_redeem_with_options(request, runtime)

    async def save_batch_task_for_creating_order_redeem_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_redeem_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_renew_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRenewResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_renew_with_options(request, runtime)

    async def save_batch_task_for_creating_order_renew_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRenewRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRenewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_renew_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_transfer_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderTransferResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_transfer_with_options(request, runtime)

    async def save_batch_task_for_creating_order_transfer_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderTransferRequest,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_transfer_with_options_async(request, runtime)

    def save_batch_task_for_domain_name_proxy_service_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_domain_name_proxy_service_with_options(request, runtime)

    async def save_batch_task_for_domain_name_proxy_service_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceRequest,
    ) -> domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_domain_name_proxy_service_with_options_async(request, runtime)

    def save_batch_task_for_modifying_domain_dns_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForModifyingDomainDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForModifyingDomainDnsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_modifying_domain_dns_with_options(request, runtime)

    async def save_batch_task_for_modifying_domain_dns_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForModifyingDomainDnsRequest,
    ) -> domain_20180129_models.SaveBatchTaskForModifyingDomainDnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_modifying_domain_dns_with_options_async(request, runtime)

    def save_batch_task_for_reserve_drop_list_domain_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForReserveDropListDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForReserveDropListDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_reserve_drop_list_domain_with_options(request, runtime)

    async def save_batch_task_for_reserve_drop_list_domain_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForReserveDropListDomainRequest,
    ) -> domain_20180129_models.SaveBatchTaskForReserveDropListDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_reserve_drop_list_domain_with_options_async(request, runtime)

    def save_batch_task_for_transfer_prohibition_lock_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_transfer_prohibition_lock_with_options(request, runtime)

    async def save_batch_task_for_transfer_prohibition_lock_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForTransferProhibitionLockRequest,
    ) -> domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_transfer_prohibition_lock_with_options_async(request, runtime)

    def save_batch_task_for_update_prohibition_lock_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_update_prohibition_lock_with_options(request, runtime)

    async def save_batch_task_for_update_prohibition_lock_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockRequest,
    ) -> domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_update_prohibition_lock_with_options_async(request, runtime)

    def save_batch_task_for_updating_contact_info_by_new_contact_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_updating_contact_info_by_new_contact_with_options(request, runtime)

    async def save_batch_task_for_updating_contact_info_by_new_contact_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_updating_contact_info_by_new_contact_with_options_async(request, runtime)

    def save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options(request, runtime)

    async def save_batch_task_for_updating_contact_info_by_registrant_profile_id_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options_async(request, runtime)

    def save_domain_group_with_options(
        self,
        request: domain_20180129_models.SaveDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveDomainGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_domain_group_with_options(request, runtime)

    async def save_domain_group_async(
        self,
        request: domain_20180129_models.SaveDomainGroupRequest,
    ) -> domain_20180129_models.SaveDomainGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_domain_group_with_options_async(request, runtime)

    def save_registrant_profile_with_options(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveRegistrantProfileResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_registrant_profile_with_options(request, runtime)

    async def save_registrant_profile_async(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRequest,
    ) -> domain_20180129_models.SaveRegistrantProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_registrant_profile_with_options_async(request, runtime)

    def save_registrant_profile_real_name_verification_with_options(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveRegistrantProfileRealNameVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_registrant_profile_real_name_verification_with_options(request, runtime)

    async def save_registrant_profile_real_name_verification_async(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRealNameVerificationRequest,
    ) -> domain_20180129_models.SaveRegistrantProfileRealNameVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_registrant_profile_real_name_verification_with_options_async(request, runtime)

    def save_single_task_for_adding_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForAddingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_adding_dsrecord_with_options(request, runtime)

    async def save_single_task_for_adding_dsrecord_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForAddingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_adding_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_approving_transfer_out_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForApprovingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForApprovingTransferOutResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_approving_transfer_out_with_options(request, runtime)

    async def save_single_task_for_approving_transfer_out_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForApprovingTransferOutRequest,
    ) -> domain_20180129_models.SaveSingleTaskForApprovingTransferOutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_approving_transfer_out_with_options_async(request, runtime)

    def save_single_task_for_associating_ens_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForAssociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForAssociatingEnsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_associating_ens_with_options(request, runtime)

    async def save_single_task_for_associating_ens_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForAssociatingEnsRequest,
    ) -> domain_20180129_models.SaveSingleTaskForAssociatingEnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_associating_ens_with_options_async(request, runtime)

    def save_single_task_for_canceling_transfer_in_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferInRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferInResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_canceling_transfer_in_with_options(request, runtime)

    async def save_single_task_for_canceling_transfer_in_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferInRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferInResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_canceling_transfer_in_with_options_async(request, runtime)

    def save_single_task_for_canceling_transfer_out_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferOutResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_canceling_transfer_out_with_options(request, runtime)

    async def save_single_task_for_canceling_transfer_out_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferOutRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferOutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_canceling_transfer_out_with_options_async(request, runtime)

    def save_single_task_for_creating_dns_host_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingDnsHostResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_dns_host_with_options(request, runtime)

    async def save_single_task_for_creating_dns_host_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingDnsHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_dns_host_with_options_async(request, runtime)

    def save_single_task_for_creating_order_activate_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderActivateResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_activate_with_options(request, runtime)

    async def save_single_task_for_creating_order_activate_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderActivateRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderActivateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_activate_with_options_async(request, runtime)

    def save_single_task_for_creating_order_redeem_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_redeem_with_options(request, runtime)

    async def save_single_task_for_creating_order_redeem_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_redeem_with_options_async(request, runtime)

    def save_single_task_for_creating_order_renew_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRenewResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_renew_with_options(request, runtime)

    async def save_single_task_for_creating_order_renew_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRenewRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRenewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_renew_with_options_async(request, runtime)

    def save_single_task_for_creating_order_transfer_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderTransferResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_transfer_with_options(request, runtime)

    async def save_single_task_for_creating_order_transfer_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderTransferRequest,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_transfer_with_options_async(request, runtime)

    def save_single_task_for_deleting_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_deleting_dsrecord_with_options(request, runtime)

    async def save_single_task_for_deleting_dsrecord_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_deleting_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_deleting_dns_host_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_deleting_dns_host_with_options(request, runtime)

    async def save_single_task_for_deleting_dns_host_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_deleting_dns_host_with_options_async(request, runtime)

    def save_single_task_for_disassociating_ens_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForDisassociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_disassociating_ens_with_options(request, runtime)

    async def save_single_task_for_disassociating_ens_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDisassociatingEnsRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_disassociating_ens_with_options_async(request, runtime)

    def save_single_task_for_domain_name_proxy_service_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_domain_name_proxy_service_with_options(request, runtime)

    async def save_single_task_for_domain_name_proxy_service_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceRequest,
    ) -> domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_domain_name_proxy_service_with_options_async(request, runtime)

    def save_single_task_for_modifying_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_modifying_dsrecord_with_options(request, runtime)

    async def save_single_task_for_modifying_dsrecord_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_modifying_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_modifying_dns_host_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_modifying_dns_host_with_options(request, runtime)

    async def save_single_task_for_modifying_dns_host_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_modifying_dns_host_with_options_async(request, runtime)

    def save_single_task_for_querying_transfer_authorization_code_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_querying_transfer_authorization_code_with_options(request, runtime)

    async def save_single_task_for_querying_transfer_authorization_code_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
    ) -> domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_querying_transfer_authorization_code_with_options_async(request, runtime)

    def save_single_task_for_save_art_extension_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForSaveArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSaveArtExtensionResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_save_art_extension_with_options(request, runtime)

    async def save_single_task_for_save_art_extension_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSaveArtExtensionRequest,
    ) -> domain_20180129_models.SaveSingleTaskForSaveArtExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_save_art_extension_with_options_async(request, runtime)

    def save_single_task_for_synchronizing_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_synchronizing_dsrecord_with_options(request, runtime)

    async def save_single_task_for_synchronizing_dsrecord_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordRequest,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_synchronizing_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_synchronizing_dns_host_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_synchronizing_dns_host_with_options(request, runtime)

    async def save_single_task_for_synchronizing_dns_host_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostRequest,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_synchronizing_dns_host_with_options_async(request, runtime)

    def save_single_task_for_transfer_prohibition_lock_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_transfer_prohibition_lock_with_options(request, runtime)

    async def save_single_task_for_transfer_prohibition_lock_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForTransferProhibitionLockRequest,
    ) -> domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_transfer_prohibition_lock_with_options_async(request, runtime)

    def save_single_task_for_update_prohibition_lock_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_update_prohibition_lock_with_options(request, runtime)

    async def save_single_task_for_update_prohibition_lock_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockRequest,
    ) -> domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_update_prohibition_lock_with_options_async(request, runtime)

    def save_single_task_for_updating_contact_info_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdatingContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForUpdatingContactInfoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_updating_contact_info_with_options(request, runtime)

    async def save_single_task_for_updating_contact_info_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdatingContactInfoRequest,
    ) -> domain_20180129_models.SaveSingleTaskForUpdatingContactInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_updating_contact_info_with_options_async(request, runtime)

    def save_task_for_submitting_domain_delete_with_options(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainDeleteResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_delete_with_options(request, runtime)

    async def save_task_for_submitting_domain_delete_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainDeleteRequest,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_submitting_domain_delete_with_options_async(request, runtime)

    def save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options(request, runtime)

    async def save_task_for_submitting_domain_real_name_verification_by_identity_credential_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options_async(request, runtime)

    def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options(request, runtime)

    async def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_id_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options_async(request, runtime)

    def save_task_for_updating_registrant_info_by_identity_credential_with_options(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_updating_registrant_info_by_identity_credential_with_options(request, runtime)

    async def save_task_for_updating_registrant_info_by_identity_credential_async(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_updating_registrant_info_by_identity_credential_with_options_async(request, runtime)

    def save_task_for_updating_registrant_info_by_registrant_profile_idwith_options(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_updating_registrant_info_by_registrant_profile_idwith_options(request, runtime)

    async def save_task_for_updating_registrant_info_by_registrant_profile_id_async(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_updating_registrant_info_by_registrant_profile_idwith_options_async(request, runtime)

    def scroll_domain_list_with_options(
        self,
        request: domain_20180129_models.ScrollDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ScrollDomainListResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.scroll_domain_list_with_options(request, runtime)

    async def scroll_domain_list_async(
        self,
        request: domain_20180129_models.ScrollDomainListRequest,
    ) -> domain_20180129_models.ScrollDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scroll_domain_list_with_options_async(request, runtime)

    def set_default_registrant_profile_with_options(
        self,
        request: domain_20180129_models.SetDefaultRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SetDefaultRegistrantProfileResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.set_default_registrant_profile_with_options(request, runtime)

    async def set_default_registrant_profile_async(
        self,
        request: domain_20180129_models.SetDefaultRegistrantProfileRequest,
    ) -> domain_20180129_models.SetDefaultRegistrantProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_registrant_profile_with_options_async(request, runtime)

    def submit_email_verification_with_options(
        self,
        request: domain_20180129_models.SubmitEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitEmailVerificationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.submit_email_verification_with_options(request, runtime)

    async def submit_email_verification_async(
        self,
        request: domain_20180129_models.SubmitEmailVerificationRequest,
    ) -> domain_20180129_models.SubmitEmailVerificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_email_verification_with_options_async(request, runtime)

    def submit_operation_audit_info_with_options(
        self,
        request: domain_20180129_models.SubmitOperationAuditInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitOperationAuditInfoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.submit_operation_audit_info_with_options(request, runtime)

    async def submit_operation_audit_info_async(
        self,
        request: domain_20180129_models.SubmitOperationAuditInfoRequest,
    ) -> domain_20180129_models.SubmitOperationAuditInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_operation_audit_info_with_options_async(request, runtime)

    def submit_operation_credentials_with_options(
        self,
        request: domain_20180129_models.SubmitOperationCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitOperationCredentialsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.submit_operation_credentials_with_options(request, runtime)

    async def submit_operation_credentials_async(
        self,
        request: domain_20180129_models.SubmitOperationCredentialsRequest,
    ) -> domain_20180129_models.SubmitOperationCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_operation_credentials_with_options_async(request, runtime)

    def transfer_in_check_mail_token_with_options(
        self,
        request: domain_20180129_models.TransferInCheckMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInCheckMailTokenResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_check_mail_token_with_options(request, runtime)

    async def transfer_in_check_mail_token_async(
        self,
        request: domain_20180129_models.TransferInCheckMailTokenRequest,
    ) -> domain_20180129_models.TransferInCheckMailTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_check_mail_token_with_options_async(request, runtime)

    def transfer_in_reenter_transfer_authorization_code_with_options(
        self,
        request: domain_20180129_models.TransferInReenterTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInReenterTransferAuthorizationCodeResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_reenter_transfer_authorization_code_with_options(request, runtime)

    async def transfer_in_reenter_transfer_authorization_code_async(
        self,
        request: domain_20180129_models.TransferInReenterTransferAuthorizationCodeRequest,
    ) -> domain_20180129_models.TransferInReenterTransferAuthorizationCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_reenter_transfer_authorization_code_with_options_async(request, runtime)

    def transfer_in_refetch_whois_email_with_options(
        self,
        request: domain_20180129_models.TransferInRefetchWhoisEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInRefetchWhoisEmailResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_refetch_whois_email_with_options(request, runtime)

    async def transfer_in_refetch_whois_email_async(
        self,
        request: domain_20180129_models.TransferInRefetchWhoisEmailRequest,
    ) -> domain_20180129_models.TransferInRefetchWhoisEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_refetch_whois_email_with_options_async(request, runtime)

    def transfer_in_resend_mail_token_with_options(
        self,
        request: domain_20180129_models.TransferInResendMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInResendMailTokenResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_resend_mail_token_with_options(request, runtime)

    async def transfer_in_resend_mail_token_async(
        self,
        request: domain_20180129_models.TransferInResendMailTokenRequest,
    ) -> domain_20180129_models.TransferInResendMailTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_resend_mail_token_with_options_async(request, runtime)

    def update_domain_to_domain_group_with_options(
        self,
        request: domain_20180129_models.UpdateDomainToDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.UpdateDomainToDomainGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_domain_to_domain_group_with_options(request, runtime)

    async def update_domain_to_domain_group_async(
        self,
        request: domain_20180129_models.UpdateDomainToDomainGroupRequest,
    ) -> domain_20180129_models.UpdateDomainToDomainGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_to_domain_group_with_options_async(request, runtime)

    def verify_contact_field_with_options(
        self,
        request: domain_20180129_models.VerifyContactFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.VerifyContactFieldResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.verify_contact_field_with_options(request, runtime)

    async def verify_contact_field_async(
        self,
        request: domain_20180129_models.VerifyContactFieldRequest,
    ) -> domain_20180129_models.VerifyContactFieldResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_contact_field_with_options_async(request, runtime)

    def verify_email_with_options(
        self,
        request: domain_20180129_models.VerifyEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.VerifyEmailResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.verify_email_with_options(request, runtime)

    async def verify_email_async(
        self,
        request: domain_20180129_models.VerifyEmailRequest,
    ) -> domain_20180129_models.VerifyEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_email_with_options_async(request, runtime)
