# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_domain_intl20171218 import models as domain_intl_20171218_models
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
        self._endpoint = self.get_endpoint('domain-intl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: domain_intl_20171218_models.AcknowledgeTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.AcknowledgeTaskResultResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.AcknowledgeTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def acknowledge_task_result_with_options_async(
        self,
        request: domain_intl_20171218_models.AcknowledgeTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.AcknowledgeTaskResultResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.AcknowledgeTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def acknowledge_task_result(
        self,
        request: domain_intl_20171218_models.AcknowledgeTaskResultRequest,
    ) -> domain_intl_20171218_models.AcknowledgeTaskResultResponse:
        """
        @param request: AcknowledgeTaskResultRequest
        @return: AcknowledgeTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.acknowledge_task_result_with_options(request, runtime)

    async def acknowledge_task_result_async(
        self,
        request: domain_intl_20171218_models.AcknowledgeTaskResultRequest,
    ) -> domain_intl_20171218_models.AcknowledgeTaskResultResponse:
        """
        @param request: AcknowledgeTaskResultRequest
        @return: AcknowledgeTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.acknowledge_task_result_with_options_async(request, runtime)

    def batch_fuzzy_match_domain_sensitive_word_with_options(
        self,
        request: domain_intl_20171218_models.BatchFuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.BatchFuzzyMatchDomainSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_fuzzy_match_domain_sensitive_word_with_options_async(
        self,
        request: domain_intl_20171218_models.BatchFuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.BatchFuzzyMatchDomainSensitiveWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_fuzzy_match_domain_sensitive_word(
        self,
        request: domain_intl_20171218_models.BatchFuzzyMatchDomainSensitiveWordRequest,
    ) -> domain_intl_20171218_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        """
        @param request: BatchFuzzyMatchDomainSensitiveWordRequest
        @return: BatchFuzzyMatchDomainSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_fuzzy_match_domain_sensitive_word_with_options(request, runtime)

    async def batch_fuzzy_match_domain_sensitive_word_async(
        self,
        request: domain_intl_20171218_models.BatchFuzzyMatchDomainSensitiveWordRequest,
    ) -> domain_intl_20171218_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        """
        @param request: BatchFuzzyMatchDomainSensitiveWordRequest
        @return: BatchFuzzyMatchDomainSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_fuzzy_match_domain_sensitive_word_with_options_async(request, runtime)

    def cancel_domain_verification_with_options(
        self,
        request: domain_intl_20171218_models.CancelDomainVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.CancelDomainVerificationResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CancelDomainVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_domain_verification_with_options_async(
        self,
        request: domain_intl_20171218_models.CancelDomainVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.CancelDomainVerificationResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CancelDomainVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_domain_verification(
        self,
        request: domain_intl_20171218_models.CancelDomainVerificationRequest,
    ) -> domain_intl_20171218_models.CancelDomainVerificationResponse:
        """
        @param request: CancelDomainVerificationRequest
        @return: CancelDomainVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_domain_verification_with_options(request, runtime)

    async def cancel_domain_verification_async(
        self,
        request: domain_intl_20171218_models.CancelDomainVerificationRequest,
    ) -> domain_intl_20171218_models.CancelDomainVerificationResponse:
        """
        @param request: CancelDomainVerificationRequest
        @return: CancelDomainVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_domain_verification_with_options_async(request, runtime)

    def cancel_task_with_options(
        self,
        request: domain_intl_20171218_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.CancelTaskResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        request: domain_intl_20171218_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.CancelTaskResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        request: domain_intl_20171218_models.CancelTaskRequest,
    ) -> domain_intl_20171218_models.CancelTaskResponse:
        """
        @param request: CancelTaskRequest
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    async def cancel_task_async(
        self,
        request: domain_intl_20171218_models.CancelTaskRequest,
    ) -> domain_intl_20171218_models.CancelTaskResponse:
        """
        @param request: CancelTaskRequest
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_task_with_options_async(request, runtime)

    def check_domain_with_options(
        self,
        request: domain_intl_20171218_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.CheckDomainResponse:
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
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomain',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CheckDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_with_options_async(
        self,
        request: domain_intl_20171218_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.CheckDomainResponse:
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
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomain',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CheckDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain(
        self,
        request: domain_intl_20171218_models.CheckDomainRequest,
    ) -> domain_intl_20171218_models.CheckDomainResponse:
        """
        @param request: CheckDomainRequest
        @return: CheckDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    async def check_domain_async(
        self,
        request: domain_intl_20171218_models.CheckDomainRequest,
    ) -> domain_intl_20171218_models.CheckDomainResponse:
        """
        @param request: CheckDomainRequest
        @return: CheckDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_domain_with_options_async(request, runtime)

    def check_domain_sunrise_claim_with_options(
        self,
        request: domain_intl_20171218_models.CheckDomainSunriseClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.CheckDomainSunriseClaimResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CheckDomainSunriseClaimResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_sunrise_claim_with_options_async(
        self,
        request: domain_intl_20171218_models.CheckDomainSunriseClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.CheckDomainSunriseClaimResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CheckDomainSunriseClaimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain_sunrise_claim(
        self,
        request: domain_intl_20171218_models.CheckDomainSunriseClaimRequest,
    ) -> domain_intl_20171218_models.CheckDomainSunriseClaimResponse:
        """
        @param request: CheckDomainSunriseClaimRequest
        @return: CheckDomainSunriseClaimResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_domain_sunrise_claim_with_options(request, runtime)

    async def check_domain_sunrise_claim_async(
        self,
        request: domain_intl_20171218_models.CheckDomainSunriseClaimRequest,
    ) -> domain_intl_20171218_models.CheckDomainSunriseClaimResponse:
        """
        @param request: CheckDomainSunriseClaimRequest
        @return: CheckDomainSunriseClaimResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_domain_sunrise_claim_with_options_async(request, runtime)

    def check_transfer_in_feasibility_with_options(
        self,
        request: domain_intl_20171218_models.CheckTransferInFeasibilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.CheckTransferInFeasibilityResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CheckTransferInFeasibilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_transfer_in_feasibility_with_options_async(
        self,
        request: domain_intl_20171218_models.CheckTransferInFeasibilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.CheckTransferInFeasibilityResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CheckTransferInFeasibilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_transfer_in_feasibility(
        self,
        request: domain_intl_20171218_models.CheckTransferInFeasibilityRequest,
    ) -> domain_intl_20171218_models.CheckTransferInFeasibilityResponse:
        """
        @param request: CheckTransferInFeasibilityRequest
        @return: CheckTransferInFeasibilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_transfer_in_feasibility_with_options(request, runtime)

    async def check_transfer_in_feasibility_async(
        self,
        request: domain_intl_20171218_models.CheckTransferInFeasibilityRequest,
    ) -> domain_intl_20171218_models.CheckTransferInFeasibilityResponse:
        """
        @param request: CheckTransferInFeasibilityRequest
        @return: CheckTransferInFeasibilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_transfer_in_feasibility_with_options_async(request, runtime)

    def confirm_transfer_in_email_with_options(
        self,
        request: domain_intl_20171218_models.ConfirmTransferInEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.ConfirmTransferInEmailResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.ConfirmTransferInEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_transfer_in_email_with_options_async(
        self,
        request: domain_intl_20171218_models.ConfirmTransferInEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.ConfirmTransferInEmailResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.ConfirmTransferInEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_transfer_in_email(
        self,
        request: domain_intl_20171218_models.ConfirmTransferInEmailRequest,
    ) -> domain_intl_20171218_models.ConfirmTransferInEmailResponse:
        """
        @param request: ConfirmTransferInEmailRequest
        @return: ConfirmTransferInEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.confirm_transfer_in_email_with_options(request, runtime)

    async def confirm_transfer_in_email_async(
        self,
        request: domain_intl_20171218_models.ConfirmTransferInEmailRequest,
    ) -> domain_intl_20171218_models.ConfirmTransferInEmailResponse:
        """
        @param request: ConfirmTransferInEmailRequest
        @return: ConfirmTransferInEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.confirm_transfer_in_email_with_options_async(request, runtime)

    def delete_email_verification_with_options(
        self,
        request: domain_intl_20171218_models.DeleteEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.DeleteEmailVerificationResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.DeleteEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_email_verification_with_options_async(
        self,
        request: domain_intl_20171218_models.DeleteEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.DeleteEmailVerificationResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.DeleteEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_email_verification(
        self,
        request: domain_intl_20171218_models.DeleteEmailVerificationRequest,
    ) -> domain_intl_20171218_models.DeleteEmailVerificationResponse:
        """
        @param request: DeleteEmailVerificationRequest
        @return: DeleteEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_email_verification_with_options(request, runtime)

    async def delete_email_verification_async(
        self,
        request: domain_intl_20171218_models.DeleteEmailVerificationRequest,
    ) -> domain_intl_20171218_models.DeleteEmailVerificationResponse:
        """
        @param request: DeleteEmailVerificationRequest
        @return: DeleteEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_email_verification_with_options_async(request, runtime)

    def delete_registrant_profile_with_options(
        self,
        request: domain_intl_20171218_models.DeleteRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.DeleteRegistrantProfileResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.DeleteRegistrantProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_registrant_profile_with_options_async(
        self,
        request: domain_intl_20171218_models.DeleteRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.DeleteRegistrantProfileResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.DeleteRegistrantProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_registrant_profile(
        self,
        request: domain_intl_20171218_models.DeleteRegistrantProfileRequest,
    ) -> domain_intl_20171218_models.DeleteRegistrantProfileResponse:
        """
        @param request: DeleteRegistrantProfileRequest
        @return: DeleteRegistrantProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_registrant_profile_with_options(request, runtime)

    async def delete_registrant_profile_async(
        self,
        request: domain_intl_20171218_models.DeleteRegistrantProfileRequest,
    ) -> domain_intl_20171218_models.DeleteRegistrantProfileResponse:
        """
        @param request: DeleteRegistrantProfileRequest
        @return: DeleteRegistrantProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_registrant_profile_with_options_async(request, runtime)

    def email_verified_with_options(
        self,
        request: domain_intl_20171218_models.EmailVerifiedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.EmailVerifiedResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.EmailVerifiedResponse(),
            self.call_api(params, req, runtime)
        )

    async def email_verified_with_options_async(
        self,
        request: domain_intl_20171218_models.EmailVerifiedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.EmailVerifiedResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.EmailVerifiedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def email_verified(
        self,
        request: domain_intl_20171218_models.EmailVerifiedRequest,
    ) -> domain_intl_20171218_models.EmailVerifiedResponse:
        """
        @param request: EmailVerifiedRequest
        @return: EmailVerifiedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.email_verified_with_options(request, runtime)

    async def email_verified_async(
        self,
        request: domain_intl_20171218_models.EmailVerifiedRequest,
    ) -> domain_intl_20171218_models.EmailVerifiedResponse:
        """
        @param request: EmailVerifiedRequest
        @return: EmailVerifiedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.email_verified_with_options_async(request, runtime)

    def fuzzy_match_domain_sensitive_word_with_options(
        self,
        request: domain_intl_20171218_models.FuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.FuzzyMatchDomainSensitiveWordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.FuzzyMatchDomainSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def fuzzy_match_domain_sensitive_word_with_options_async(
        self,
        request: domain_intl_20171218_models.FuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.FuzzyMatchDomainSensitiveWordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.FuzzyMatchDomainSensitiveWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fuzzy_match_domain_sensitive_word(
        self,
        request: domain_intl_20171218_models.FuzzyMatchDomainSensitiveWordRequest,
    ) -> domain_intl_20171218_models.FuzzyMatchDomainSensitiveWordResponse:
        """
        @param request: FuzzyMatchDomainSensitiveWordRequest
        @return: FuzzyMatchDomainSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fuzzy_match_domain_sensitive_word_with_options(request, runtime)

    async def fuzzy_match_domain_sensitive_word_async(
        self,
        request: domain_intl_20171218_models.FuzzyMatchDomainSensitiveWordRequest,
    ) -> domain_intl_20171218_models.FuzzyMatchDomainSensitiveWordResponse:
        """
        @param request: FuzzyMatchDomainSensitiveWordRequest
        @return: FuzzyMatchDomainSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fuzzy_match_domain_sensitive_word_with_options_async(request, runtime)

    def list_email_verification_with_options(
        self,
        request: domain_intl_20171218_models.ListEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.ListEmailVerificationResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.ListEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_email_verification_with_options_async(
        self,
        request: domain_intl_20171218_models.ListEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.ListEmailVerificationResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.ListEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_email_verification(
        self,
        request: domain_intl_20171218_models.ListEmailVerificationRequest,
    ) -> domain_intl_20171218_models.ListEmailVerificationResponse:
        """
        @param request: ListEmailVerificationRequest
        @return: ListEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_email_verification_with_options(request, runtime)

    async def list_email_verification_async(
        self,
        request: domain_intl_20171218_models.ListEmailVerificationRequest,
    ) -> domain_intl_20171218_models.ListEmailVerificationResponse:
        """
        @param request: ListEmailVerificationRequest
        @return: ListEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_email_verification_with_options_async(request, runtime)

    def lookup_tmch_notice_with_options(
        self,
        request: domain_intl_20171218_models.LookupTmchNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.LookupTmchNoticeResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.LookupTmchNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def lookup_tmch_notice_with_options_async(
        self,
        request: domain_intl_20171218_models.LookupTmchNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.LookupTmchNoticeResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.LookupTmchNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lookup_tmch_notice(
        self,
        request: domain_intl_20171218_models.LookupTmchNoticeRequest,
    ) -> domain_intl_20171218_models.LookupTmchNoticeResponse:
        """
        @param request: LookupTmchNoticeRequest
        @return: LookupTmchNoticeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lookup_tmch_notice_with_options(request, runtime)

    async def lookup_tmch_notice_async(
        self,
        request: domain_intl_20171218_models.LookupTmchNoticeRequest,
    ) -> domain_intl_20171218_models.LookupTmchNoticeResponse:
        """
        @param request: LookupTmchNoticeRequest
        @return: LookupTmchNoticeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.lookup_tmch_notice_with_options_async(request, runtime)

    def poll_task_result_with_options(
        self,
        request: domain_intl_20171218_models.PollTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.PollTaskResultResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.PollTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def poll_task_result_with_options_async(
        self,
        request: domain_intl_20171218_models.PollTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.PollTaskResultResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.PollTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poll_task_result(
        self,
        request: domain_intl_20171218_models.PollTaskResultRequest,
    ) -> domain_intl_20171218_models.PollTaskResultResponse:
        """
        @param request: PollTaskResultRequest
        @return: PollTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.poll_task_result_with_options(request, runtime)

    async def poll_task_result_async(
        self,
        request: domain_intl_20171218_models.PollTaskResultRequest,
    ) -> domain_intl_20171218_models.PollTaskResultResponse:
        """
        @param request: PollTaskResultRequest
        @return: PollTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.poll_task_result_with_options_async(request, runtime)

    def query_art_extension_with_options(
        self,
        request: domain_intl_20171218_models.QueryArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryArtExtensionResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryArtExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_art_extension_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryArtExtensionResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryArtExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_art_extension(
        self,
        request: domain_intl_20171218_models.QueryArtExtensionRequest,
    ) -> domain_intl_20171218_models.QueryArtExtensionResponse:
        """
        @param request: QueryArtExtensionRequest
        @return: QueryArtExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_art_extension_with_options(request, runtime)

    async def query_art_extension_async(
        self,
        request: domain_intl_20171218_models.QueryArtExtensionRequest,
    ) -> domain_intl_20171218_models.QueryArtExtensionResponse:
        """
        @param request: QueryArtExtensionRequest
        @return: QueryArtExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_art_extension_with_options_async(request, runtime)

    def query_change_log_list_with_options(
        self,
        request: domain_intl_20171218_models.QueryChangeLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryChangeLogListResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryChangeLogListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_change_log_list_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryChangeLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryChangeLogListResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryChangeLogListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_change_log_list(
        self,
        request: domain_intl_20171218_models.QueryChangeLogListRequest,
    ) -> domain_intl_20171218_models.QueryChangeLogListResponse:
        """
        @param request: QueryChangeLogListRequest
        @return: QueryChangeLogListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_change_log_list_with_options(request, runtime)

    async def query_change_log_list_async(
        self,
        request: domain_intl_20171218_models.QueryChangeLogListRequest,
    ) -> domain_intl_20171218_models.QueryChangeLogListResponse:
        """
        @param request: QueryChangeLogListRequest
        @return: QueryChangeLogListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_change_log_list_with_options_async(request, runtime)

    def query_contact_info_with_options(
        self,
        request: domain_intl_20171218_models.QueryContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryContactInfoResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryContactInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_contact_info_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryContactInfoResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryContactInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_contact_info(
        self,
        request: domain_intl_20171218_models.QueryContactInfoRequest,
    ) -> domain_intl_20171218_models.QueryContactInfoResponse:
        """
        @param request: QueryContactInfoRequest
        @return: QueryContactInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_contact_info_with_options(request, runtime)

    async def query_contact_info_async(
        self,
        request: domain_intl_20171218_models.QueryContactInfoRequest,
    ) -> domain_intl_20171218_models.QueryContactInfoResponse:
        """
        @param request: QueryContactInfoRequest
        @return: QueryContactInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_contact_info_with_options_async(request, runtime)

    def query_dsrecord_with_options(
        self,
        request: domain_intl_20171218_models.QueryDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDSRecordResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dsrecord_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDSRecordResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dsrecord(
        self,
        request: domain_intl_20171218_models.QueryDSRecordRequest,
    ) -> domain_intl_20171218_models.QueryDSRecordResponse:
        """
        @param request: QueryDSRecordRequest
        @return: QueryDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_dsrecord_with_options(request, runtime)

    async def query_dsrecord_async(
        self,
        request: domain_intl_20171218_models.QueryDSRecordRequest,
    ) -> domain_intl_20171218_models.QueryDSRecordResponse:
        """
        @param request: QueryDSRecordRequest
        @return: QueryDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_dsrecord_with_options_async(request, runtime)

    def query_dns_host_with_options(
        self,
        request: domain_intl_20171218_models.QueryDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDnsHostResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dns_host_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDnsHostResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dns_host(
        self,
        request: domain_intl_20171218_models.QueryDnsHostRequest,
    ) -> domain_intl_20171218_models.QueryDnsHostResponse:
        """
        @param request: QueryDnsHostRequest
        @return: QueryDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_dns_host_with_options(request, runtime)

    async def query_dns_host_async(
        self,
        request: domain_intl_20171218_models.QueryDnsHostRequest,
    ) -> domain_intl_20171218_models.QueryDnsHostResponse:
        """
        @param request: QueryDnsHostRequest
        @return: QueryDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_dns_host_with_options_async(request, runtime)

    def query_domain_by_domain_name_with_options(
        self,
        request: domain_intl_20171218_models.QueryDomainByDomainNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDomainByDomainNameResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainByDomainNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_by_domain_name_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryDomainByDomainNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDomainByDomainNameResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainByDomainNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_by_domain_name(
        self,
        request: domain_intl_20171218_models.QueryDomainByDomainNameRequest,
    ) -> domain_intl_20171218_models.QueryDomainByDomainNameResponse:
        """
        @param request: QueryDomainByDomainNameRequest
        @return: QueryDomainByDomainNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_by_domain_name_with_options(request, runtime)

    async def query_domain_by_domain_name_async(
        self,
        request: domain_intl_20171218_models.QueryDomainByDomainNameRequest,
    ) -> domain_intl_20171218_models.QueryDomainByDomainNameResponse:
        """
        @param request: QueryDomainByDomainNameRequest
        @return: QueryDomainByDomainNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_by_domain_name_with_options_async(request, runtime)

    def query_domain_by_instance_id_with_options(
        self,
        request: domain_intl_20171218_models.QueryDomainByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDomainByInstanceIdResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_by_instance_id_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryDomainByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDomainByInstanceIdResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_by_instance_id(
        self,
        request: domain_intl_20171218_models.QueryDomainByInstanceIdRequest,
    ) -> domain_intl_20171218_models.QueryDomainByInstanceIdResponse:
        """
        @param request: QueryDomainByInstanceIdRequest
        @return: QueryDomainByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_by_instance_id_with_options(request, runtime)

    async def query_domain_by_instance_id_async(
        self,
        request: domain_intl_20171218_models.QueryDomainByInstanceIdRequest,
    ) -> domain_intl_20171218_models.QueryDomainByInstanceIdResponse:
        """
        @param request: QueryDomainByInstanceIdRequest
        @return: QueryDomainByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_by_instance_id_with_options_async(request, runtime)

    def query_domain_list_with_options(
        self,
        request: domain_intl_20171218_models.QueryDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDomainListResponse:
        """
        @param request: QueryDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccompany):
            query['Ccompany'] = request.ccompany
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_list_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDomainListResponse:
        """
        @param request: QueryDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ccompany):
            query['Ccompany'] = request.ccompany
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_list(
        self,
        request: domain_intl_20171218_models.QueryDomainListRequest,
    ) -> domain_intl_20171218_models.QueryDomainListResponse:
        """
        @param request: QueryDomainListRequest
        @return: QueryDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_list_with_options(request, runtime)

    async def query_domain_list_async(
        self,
        request: domain_intl_20171218_models.QueryDomainListRequest,
    ) -> domain_intl_20171218_models.QueryDomainListResponse:
        """
        @param request: QueryDomainListRequest
        @return: QueryDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_list_with_options_async(request, runtime)

    def query_domain_real_name_verification_info_with_options(
        self,
        request: domain_intl_20171218_models.QueryDomainRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDomainRealNameVerificationInfoResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainRealNameVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_real_name_verification_info_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryDomainRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryDomainRealNameVerificationInfoResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainRealNameVerificationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_real_name_verification_info(
        self,
        request: domain_intl_20171218_models.QueryDomainRealNameVerificationInfoRequest,
    ) -> domain_intl_20171218_models.QueryDomainRealNameVerificationInfoResponse:
        """
        @param request: QueryDomainRealNameVerificationInfoRequest
        @return: QueryDomainRealNameVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_real_name_verification_info_with_options(request, runtime)

    async def query_domain_real_name_verification_info_async(
        self,
        request: domain_intl_20171218_models.QueryDomainRealNameVerificationInfoRequest,
    ) -> domain_intl_20171218_models.QueryDomainRealNameVerificationInfoResponse:
        """
        @param request: QueryDomainRealNameVerificationInfoRequest
        @return: QueryDomainRealNameVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_real_name_verification_info_with_options_async(request, runtime)

    def query_ens_association_with_options(
        self,
        request: domain_intl_20171218_models.QueryEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryEnsAssociationResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryEnsAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ens_association_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryEnsAssociationResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryEnsAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ens_association(
        self,
        request: domain_intl_20171218_models.QueryEnsAssociationRequest,
    ) -> domain_intl_20171218_models.QueryEnsAssociationResponse:
        """
        @param request: QueryEnsAssociationRequest
        @return: QueryEnsAssociationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_ens_association_with_options(request, runtime)

    async def query_ens_association_async(
        self,
        request: domain_intl_20171218_models.QueryEnsAssociationRequest,
    ) -> domain_intl_20171218_models.QueryEnsAssociationResponse:
        """
        @param request: QueryEnsAssociationRequest
        @return: QueryEnsAssociationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_ens_association_with_options_async(request, runtime)

    def query_fail_reason_for_domain_real_name_verification_with_options(
        self,
        request: domain_intl_20171218_models.QueryFailReasonForDomainRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryFailReasonForDomainRealNameVerificationResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryFailReasonForDomainRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fail_reason_for_domain_real_name_verification_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryFailReasonForDomainRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryFailReasonForDomainRealNameVerificationResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryFailReasonForDomainRealNameVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fail_reason_for_domain_real_name_verification(
        self,
        request: domain_intl_20171218_models.QueryFailReasonForDomainRealNameVerificationRequest,
    ) -> domain_intl_20171218_models.QueryFailReasonForDomainRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForDomainRealNameVerificationRequest
        @return: QueryFailReasonForDomainRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_fail_reason_for_domain_real_name_verification_with_options(request, runtime)

    async def query_fail_reason_for_domain_real_name_verification_async(
        self,
        request: domain_intl_20171218_models.QueryFailReasonForDomainRealNameVerificationRequest,
    ) -> domain_intl_20171218_models.QueryFailReasonForDomainRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForDomainRealNameVerificationRequest
        @return: QueryFailReasonForDomainRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_fail_reason_for_domain_real_name_verification_with_options_async(request, runtime)

    def query_fail_reason_for_registrant_profile_real_name_verification_with_options(
        self,
        request: domain_intl_20171218_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fail_reason_for_registrant_profile_real_name_verification_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fail_reason_for_registrant_profile_real_name_verification(
        self,
        request: domain_intl_20171218_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
    ) -> domain_intl_20171218_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForRegistrantProfileRealNameVerificationRequest
        @return: QueryFailReasonForRegistrantProfileRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_fail_reason_for_registrant_profile_real_name_verification_with_options(request, runtime)

    async def query_fail_reason_for_registrant_profile_real_name_verification_async(
        self,
        request: domain_intl_20171218_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
    ) -> domain_intl_20171218_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        """
        @param request: QueryFailReasonForRegistrantProfileRealNameVerificationRequest
        @return: QueryFailReasonForRegistrantProfileRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_fail_reason_for_registrant_profile_real_name_verification_with_options_async(request, runtime)

    def query_local_ens_association_with_options(
        self,
        request: domain_intl_20171218_models.QueryLocalEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryLocalEnsAssociationResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryLocalEnsAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_local_ens_association_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryLocalEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryLocalEnsAssociationResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryLocalEnsAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_local_ens_association(
        self,
        request: domain_intl_20171218_models.QueryLocalEnsAssociationRequest,
    ) -> domain_intl_20171218_models.QueryLocalEnsAssociationResponse:
        """
        @param request: QueryLocalEnsAssociationRequest
        @return: QueryLocalEnsAssociationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_local_ens_association_with_options(request, runtime)

    async def query_local_ens_association_async(
        self,
        request: domain_intl_20171218_models.QueryLocalEnsAssociationRequest,
    ) -> domain_intl_20171218_models.QueryLocalEnsAssociationResponse:
        """
        @param request: QueryLocalEnsAssociationRequest
        @return: QueryLocalEnsAssociationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_local_ens_association_with_options_async(request, runtime)

    def query_registrant_profile_real_name_verification_info_with_options(
        self,
        request: domain_intl_20171218_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryRegistrantProfileRealNameVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_registrant_profile_real_name_verification_info_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryRegistrantProfileRealNameVerificationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_registrant_profile_real_name_verification_info(
        self,
        request: domain_intl_20171218_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
    ) -> domain_intl_20171218_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        """
        @param request: QueryRegistrantProfileRealNameVerificationInfoRequest
        @return: QueryRegistrantProfileRealNameVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_registrant_profile_real_name_verification_info_with_options(request, runtime)

    async def query_registrant_profile_real_name_verification_info_async(
        self,
        request: domain_intl_20171218_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
    ) -> domain_intl_20171218_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        """
        @param request: QueryRegistrantProfileRealNameVerificationInfoRequest
        @return: QueryRegistrantProfileRealNameVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_registrant_profile_real_name_verification_info_with_options_async(request, runtime)

    def query_registrant_profiles_with_options(
        self,
        request: domain_intl_20171218_models.QueryRegistrantProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryRegistrantProfilesResponse:
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
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRegistrantProfiles',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryRegistrantProfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_registrant_profiles_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryRegistrantProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryRegistrantProfilesResponse:
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
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRegistrantProfiles',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryRegistrantProfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_registrant_profiles(
        self,
        request: domain_intl_20171218_models.QueryRegistrantProfilesRequest,
    ) -> domain_intl_20171218_models.QueryRegistrantProfilesResponse:
        """
        @param request: QueryRegistrantProfilesRequest
        @return: QueryRegistrantProfilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_registrant_profiles_with_options(request, runtime)

    async def query_registrant_profiles_async(
        self,
        request: domain_intl_20171218_models.QueryRegistrantProfilesRequest,
    ) -> domain_intl_20171218_models.QueryRegistrantProfilesResponse:
        """
        @param request: QueryRegistrantProfilesRequest
        @return: QueryRegistrantProfilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_registrant_profiles_with_options_async(request, runtime)

    def query_task_detail_history_with_options(
        self,
        request: domain_intl_20171218_models.QueryTaskDetailHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTaskDetailHistoryResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskDetailHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_detail_history_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryTaskDetailHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTaskDetailHistoryResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskDetailHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_detail_history(
        self,
        request: domain_intl_20171218_models.QueryTaskDetailHistoryRequest,
    ) -> domain_intl_20171218_models.QueryTaskDetailHistoryResponse:
        """
        @param request: QueryTaskDetailHistoryRequest
        @return: QueryTaskDetailHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_detail_history_with_options(request, runtime)

    async def query_task_detail_history_async(
        self,
        request: domain_intl_20171218_models.QueryTaskDetailHistoryRequest,
    ) -> domain_intl_20171218_models.QueryTaskDetailHistoryResponse:
        """
        @param request: QueryTaskDetailHistoryRequest
        @return: QueryTaskDetailHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_detail_history_with_options_async(request, runtime)

    def query_task_detail_list_with_options(
        self,
        request: domain_intl_20171218_models.QueryTaskDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTaskDetailListResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_detail_list_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryTaskDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTaskDetailListResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_detail_list(
        self,
        request: domain_intl_20171218_models.QueryTaskDetailListRequest,
    ) -> domain_intl_20171218_models.QueryTaskDetailListResponse:
        """
        @param request: QueryTaskDetailListRequest
        @return: QueryTaskDetailListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_detail_list_with_options(request, runtime)

    async def query_task_detail_list_async(
        self,
        request: domain_intl_20171218_models.QueryTaskDetailListRequest,
    ) -> domain_intl_20171218_models.QueryTaskDetailListResponse:
        """
        @param request: QueryTaskDetailListRequest
        @return: QueryTaskDetailListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_detail_list_with_options_async(request, runtime)

    def query_task_info_history_with_options(
        self,
        request: domain_intl_20171218_models.QueryTaskInfoHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTaskInfoHistoryResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskInfoHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_info_history_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryTaskInfoHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTaskInfoHistoryResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskInfoHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_info_history(
        self,
        request: domain_intl_20171218_models.QueryTaskInfoHistoryRequest,
    ) -> domain_intl_20171218_models.QueryTaskInfoHistoryResponse:
        """
        @param request: QueryTaskInfoHistoryRequest
        @return: QueryTaskInfoHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_info_history_with_options(request, runtime)

    async def query_task_info_history_async(
        self,
        request: domain_intl_20171218_models.QueryTaskInfoHistoryRequest,
    ) -> domain_intl_20171218_models.QueryTaskInfoHistoryResponse:
        """
        @param request: QueryTaskInfoHistoryRequest
        @return: QueryTaskInfoHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_info_history_with_options_async(request, runtime)

    def query_task_list_with_options(
        self,
        request: domain_intl_20171218_models.QueryTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTaskListResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_list_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTaskListResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_list(
        self,
        request: domain_intl_20171218_models.QueryTaskListRequest,
    ) -> domain_intl_20171218_models.QueryTaskListResponse:
        """
        @param request: QueryTaskListRequest
        @return: QueryTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_list_with_options(request, runtime)

    async def query_task_list_async(
        self,
        request: domain_intl_20171218_models.QueryTaskListRequest,
    ) -> domain_intl_20171218_models.QueryTaskListResponse:
        """
        @param request: QueryTaskListRequest
        @return: QueryTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_list_with_options_async(request, runtime)

    def query_transfer_in_by_instance_id_with_options(
        self,
        request: domain_intl_20171218_models.QueryTransferInByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTransferInByInstanceIdResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTransferInByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_in_by_instance_id_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryTransferInByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTransferInByInstanceIdResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTransferInByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_in_by_instance_id(
        self,
        request: domain_intl_20171218_models.QueryTransferInByInstanceIdRequest,
    ) -> domain_intl_20171218_models.QueryTransferInByInstanceIdResponse:
        """
        @param request: QueryTransferInByInstanceIdRequest
        @return: QueryTransferInByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_in_by_instance_id_with_options(request, runtime)

    async def query_transfer_in_by_instance_id_async(
        self,
        request: domain_intl_20171218_models.QueryTransferInByInstanceIdRequest,
    ) -> domain_intl_20171218_models.QueryTransferInByInstanceIdResponse:
        """
        @param request: QueryTransferInByInstanceIdRequest
        @return: QueryTransferInByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_in_by_instance_id_with_options_async(request, runtime)

    def query_transfer_in_list_with_options(
        self,
        request: domain_intl_20171218_models.QueryTransferInListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTransferInListResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTransferInListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_in_list_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryTransferInListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTransferInListResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTransferInListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_in_list(
        self,
        request: domain_intl_20171218_models.QueryTransferInListRequest,
    ) -> domain_intl_20171218_models.QueryTransferInListResponse:
        """
        @param request: QueryTransferInListRequest
        @return: QueryTransferInListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_in_list_with_options(request, runtime)

    async def query_transfer_in_list_async(
        self,
        request: domain_intl_20171218_models.QueryTransferInListRequest,
    ) -> domain_intl_20171218_models.QueryTransferInListResponse:
        """
        @param request: QueryTransferInListRequest
        @return: QueryTransferInListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_in_list_with_options_async(request, runtime)

    def query_transfer_out_info_with_options(
        self,
        request: domain_intl_20171218_models.QueryTransferOutInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTransferOutInfoResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTransferOutInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_out_info_with_options_async(
        self,
        request: domain_intl_20171218_models.QueryTransferOutInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.QueryTransferOutInfoResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTransferOutInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_out_info(
        self,
        request: domain_intl_20171218_models.QueryTransferOutInfoRequest,
    ) -> domain_intl_20171218_models.QueryTransferOutInfoResponse:
        """
        @param request: QueryTransferOutInfoRequest
        @return: QueryTransferOutInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_out_info_with_options(request, runtime)

    async def query_transfer_out_info_async(
        self,
        request: domain_intl_20171218_models.QueryTransferOutInfoRequest,
    ) -> domain_intl_20171218_models.QueryTransferOutInfoResponse:
        """
        @param request: QueryTransferOutInfoRequest
        @return: QueryTransferOutInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_out_info_with_options_async(request, runtime)

    def registrant_profile_real_name_verification_with_options(
        self,
        request: domain_intl_20171218_models.RegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.RegistrantProfileRealNameVerificationResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.RegistrantProfileRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def registrant_profile_real_name_verification_with_options_async(
        self,
        request: domain_intl_20171218_models.RegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.RegistrantProfileRealNameVerificationResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.RegistrantProfileRealNameVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def registrant_profile_real_name_verification(
        self,
        request: domain_intl_20171218_models.RegistrantProfileRealNameVerificationRequest,
    ) -> domain_intl_20171218_models.RegistrantProfileRealNameVerificationResponse:
        """
        @param request: RegistrantProfileRealNameVerificationRequest
        @return: RegistrantProfileRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.registrant_profile_real_name_verification_with_options(request, runtime)

    async def registrant_profile_real_name_verification_async(
        self,
        request: domain_intl_20171218_models.RegistrantProfileRealNameVerificationRequest,
    ) -> domain_intl_20171218_models.RegistrantProfileRealNameVerificationResponse:
        """
        @param request: RegistrantProfileRealNameVerificationRequest
        @return: RegistrantProfileRealNameVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.registrant_profile_real_name_verification_with_options_async(request, runtime)

    def resend_email_verification_with_options(
        self,
        request: domain_intl_20171218_models.ResendEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.ResendEmailVerificationResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.ResendEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_email_verification_with_options_async(
        self,
        request: domain_intl_20171218_models.ResendEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.ResendEmailVerificationResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.ResendEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_email_verification(
        self,
        request: domain_intl_20171218_models.ResendEmailVerificationRequest,
    ) -> domain_intl_20171218_models.ResendEmailVerificationResponse:
        """
        @param request: ResendEmailVerificationRequest
        @return: ResendEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resend_email_verification_with_options(request, runtime)

    async def resend_email_verification_async(
        self,
        request: domain_intl_20171218_models.ResendEmailVerificationRequest,
    ) -> domain_intl_20171218_models.ResendEmailVerificationResponse:
        """
        @param request: ResendEmailVerificationRequest
        @return: ResendEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resend_email_verification_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_activate_with_options(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderActivateResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderActivateResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_activate_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderActivateResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderActivateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_activate(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderActivateRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderActivateResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderActivateRequest
        @return: SaveBatchTaskForCreatingOrderActivateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_activate_with_options(request, runtime)

    async def save_batch_task_for_creating_order_activate_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderActivateRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderActivateResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderActivateRequest
        @return: SaveBatchTaskForCreatingOrderActivateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_activate_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_redeem_with_options(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRedeemResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRedeemResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_redeem_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRedeemResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRedeemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_redeem(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRedeemRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderRedeemRequest
        @return: SaveBatchTaskForCreatingOrderRedeemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_redeem_with_options(request, runtime)

    async def save_batch_task_for_creating_order_redeem_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRedeemRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderRedeemRequest
        @return: SaveBatchTaskForCreatingOrderRedeemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_redeem_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_renew_with_options(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRenewResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRenewResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_renew_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRenewResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRenewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_renew(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRenewRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRenewResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderRenewRequest
        @return: SaveBatchTaskForCreatingOrderRenewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_renew_with_options(request, runtime)

    async def save_batch_task_for_creating_order_renew_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRenewRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRenewResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderRenewRequest
        @return: SaveBatchTaskForCreatingOrderRenewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_renew_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_transfer_with_options(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderTransferResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_transfer_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderTransferResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_transfer(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderTransferRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderTransferRequest
        @return: SaveBatchTaskForCreatingOrderTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_transfer_with_options(request, runtime)

    async def save_batch_task_for_creating_order_transfer_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForCreatingOrderTransferRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveBatchTaskForCreatingOrderTransferRequest
        @return: SaveBatchTaskForCreatingOrderTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_creating_order_transfer_with_options_async(request, runtime)

    def save_batch_task_for_domain_name_proxy_service_with_options(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        """
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
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForDomainNameProxyService',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForDomainNameProxyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_domain_name_proxy_service_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        """
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
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForDomainNameProxyService',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForDomainNameProxyServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_domain_name_proxy_service(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForDomainNameProxyServiceRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        """
        @param request: SaveBatchTaskForDomainNameProxyServiceRequest
        @return: SaveBatchTaskForDomainNameProxyServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_domain_name_proxy_service_with_options(request, runtime)

    async def save_batch_task_for_domain_name_proxy_service_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForDomainNameProxyServiceRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        """
        @param request: SaveBatchTaskForDomainNameProxyServiceRequest
        @return: SaveBatchTaskForDomainNameProxyServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_domain_name_proxy_service_with_options_async(request, runtime)

    def save_batch_task_for_modifying_domain_dns_with_options(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForModifyingDomainDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForModifyingDomainDnsResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForModifyingDomainDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_modifying_domain_dns_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForModifyingDomainDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForModifyingDomainDnsResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForModifyingDomainDnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_modifying_domain_dns(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForModifyingDomainDnsRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForModifyingDomainDnsResponse:
        """
        @param request: SaveBatchTaskForModifyingDomainDnsRequest
        @return: SaveBatchTaskForModifyingDomainDnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_modifying_domain_dns_with_options(request, runtime)

    async def save_batch_task_for_modifying_domain_dns_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForModifyingDomainDnsRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForModifyingDomainDnsResponse:
        """
        @param request: SaveBatchTaskForModifyingDomainDnsRequest
        @return: SaveBatchTaskForModifyingDomainDnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_modifying_domain_dns_with_options_async(request, runtime)

    def save_batch_task_for_reserve_drop_list_domain_with_options(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForReserveDropListDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForReserveDropListDomainResponse:
        """
        @summary 国际站删除抢注批量接口
        
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForReserveDropListDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_reserve_drop_list_domain_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForReserveDropListDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForReserveDropListDomainResponse:
        """
        @summary 国际站删除抢注批量接口
        
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForReserveDropListDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_reserve_drop_list_domain(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForReserveDropListDomainRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForReserveDropListDomainResponse:
        """
        @summary 国际站删除抢注批量接口
        
        @param request: SaveBatchTaskForReserveDropListDomainRequest
        @return: SaveBatchTaskForReserveDropListDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_reserve_drop_list_domain_with_options(request, runtime)

    async def save_batch_task_for_reserve_drop_list_domain_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForReserveDropListDomainRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForReserveDropListDomainResponse:
        """
        @summary 国际站删除抢注批量接口
        
        @param request: SaveBatchTaskForReserveDropListDomainRequest
        @return: SaveBatchTaskForReserveDropListDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_reserve_drop_list_domain_with_options_async(request, runtime)

    def save_batch_task_for_transfer_prohibition_lock_with_options(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForTransferProhibitionLockResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForTransferProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_transfer_prohibition_lock_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForTransferProhibitionLockResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForTransferProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_transfer_prohibition_lock(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForTransferProhibitionLockRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForTransferProhibitionLockResponse:
        """
        @param request: SaveBatchTaskForTransferProhibitionLockRequest
        @return: SaveBatchTaskForTransferProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_transfer_prohibition_lock_with_options(request, runtime)

    async def save_batch_task_for_transfer_prohibition_lock_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForTransferProhibitionLockRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForTransferProhibitionLockResponse:
        """
        @param request: SaveBatchTaskForTransferProhibitionLockRequest
        @return: SaveBatchTaskForTransferProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_transfer_prohibition_lock_with_options_async(request, runtime)

    def save_batch_task_for_update_prohibition_lock_with_options(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdateProhibitionLockResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForUpdateProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_update_prohibition_lock_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdateProhibitionLockResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForUpdateProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_update_prohibition_lock(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdateProhibitionLockRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        """
        @param request: SaveBatchTaskForUpdateProhibitionLockRequest
        @return: SaveBatchTaskForUpdateProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_update_prohibition_lock_with_options(request, runtime)

    async def save_batch_task_for_update_prohibition_lock_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdateProhibitionLockRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        """
        @param request: SaveBatchTaskForUpdateProhibitionLockRequest
        @return: SaveBatchTaskForUpdateProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_update_prohibition_lock_with_options_async(request, runtime)

    def save_batch_task_for_updating_contact_info_with_options(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoResponse:
        """
        @param request: SaveBatchTaskForUpdatingContactInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForUpdatingContactInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
            action='SaveBatchTaskForUpdatingContactInfo',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_updating_contact_info_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoResponse:
        """
        @param request: SaveBatchTaskForUpdatingContactInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveBatchTaskForUpdatingContactInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
            action='SaveBatchTaskForUpdatingContactInfo',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_updating_contact_info(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoResponse:
        """
        @param request: SaveBatchTaskForUpdatingContactInfoRequest
        @return: SaveBatchTaskForUpdatingContactInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_updating_contact_info_with_options(request, runtime)

    async def save_batch_task_for_updating_contact_info_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoResponse:
        """
        @param request: SaveBatchTaskForUpdatingContactInfoRequest
        @return: SaveBatchTaskForUpdatingContactInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_updating_contact_info_with_options_async(request, runtime)

    def save_batch_task_for_updating_contact_info_by_new_contact_with_options(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForUpdatingContactInfoByNewContact',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_updating_contact_info_by_new_contact_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForUpdatingContactInfoByNewContact',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_updating_contact_info_by_new_contact(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        """
        @param request: SaveBatchTaskForUpdatingContactInfoByNewContactRequest
        @return: SaveBatchTaskForUpdatingContactInfoByNewContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_updating_contact_info_by_new_contact_with_options(request, runtime)

    async def save_batch_task_for_updating_contact_info_by_new_contact_async(
        self,
        request: domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
    ) -> domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        """
        @param request: SaveBatchTaskForUpdatingContactInfoByNewContactRequest
        @return: SaveBatchTaskForUpdatingContactInfoByNewContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_batch_task_for_updating_contact_info_by_new_contact_with_options_async(request, runtime)

    def save_registrant_profile_with_options(
        self,
        request: domain_intl_20171218_models.SaveRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveRegistrantProfileResponse:
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRegistrantProfile',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveRegistrantProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_registrant_profile_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveRegistrantProfileResponse:
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRegistrantProfile',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveRegistrantProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_registrant_profile(
        self,
        request: domain_intl_20171218_models.SaveRegistrantProfileRequest,
    ) -> domain_intl_20171218_models.SaveRegistrantProfileResponse:
        """
        @param request: SaveRegistrantProfileRequest
        @return: SaveRegistrantProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_registrant_profile_with_options(request, runtime)

    async def save_registrant_profile_async(
        self,
        request: domain_intl_20171218_models.SaveRegistrantProfileRequest,
    ) -> domain_intl_20171218_models.SaveRegistrantProfileResponse:
        """
        @param request: SaveRegistrantProfileRequest
        @return: SaveRegistrantProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_registrant_profile_with_options_async(request, runtime)

    def save_single_task_for_adding_dsrecord_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForAddingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForAddingDSRecordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForAddingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_adding_dsrecord_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForAddingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForAddingDSRecordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForAddingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_adding_dsrecord(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForAddingDSRecordRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForAddingDSRecordResponse:
        """
        @param request: SaveSingleTaskForAddingDSRecordRequest
        @return: SaveSingleTaskForAddingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_adding_dsrecord_with_options(request, runtime)

    async def save_single_task_for_adding_dsrecord_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForAddingDSRecordRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForAddingDSRecordResponse:
        """
        @param request: SaveSingleTaskForAddingDSRecordRequest
        @return: SaveSingleTaskForAddingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_adding_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_approving_transfer_out_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForApprovingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForApprovingTransferOutResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForApprovingTransferOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_approving_transfer_out_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForApprovingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForApprovingTransferOutResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForApprovingTransferOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_approving_transfer_out(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForApprovingTransferOutRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForApprovingTransferOutResponse:
        """
        @param request: SaveSingleTaskForApprovingTransferOutRequest
        @return: SaveSingleTaskForApprovingTransferOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_approving_transfer_out_with_options(request, runtime)

    async def save_single_task_for_approving_transfer_out_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForApprovingTransferOutRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForApprovingTransferOutResponse:
        """
        @param request: SaveSingleTaskForApprovingTransferOutRequest
        @return: SaveSingleTaskForApprovingTransferOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_approving_transfer_out_with_options_async(request, runtime)

    def save_single_task_for_associating_ens_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForAssociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForAssociatingEnsResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForAssociatingEnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_associating_ens_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForAssociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForAssociatingEnsResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForAssociatingEnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_associating_ens(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForAssociatingEnsRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForAssociatingEnsResponse:
        """
        @param request: SaveSingleTaskForAssociatingEnsRequest
        @return: SaveSingleTaskForAssociatingEnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_associating_ens_with_options(request, runtime)

    async def save_single_task_for_associating_ens_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForAssociatingEnsRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForAssociatingEnsResponse:
        """
        @param request: SaveSingleTaskForAssociatingEnsRequest
        @return: SaveSingleTaskForAssociatingEnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_associating_ens_with_options_async(request, runtime)

    def save_single_task_for_canceling_transfer_in_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCancelingTransferInRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCancelingTransferInResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCancelingTransferInResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_canceling_transfer_in_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCancelingTransferInRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCancelingTransferInResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCancelingTransferInResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_canceling_transfer_in(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCancelingTransferInRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCancelingTransferInResponse:
        """
        @param request: SaveSingleTaskForCancelingTransferInRequest
        @return: SaveSingleTaskForCancelingTransferInResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_canceling_transfer_in_with_options(request, runtime)

    async def save_single_task_for_canceling_transfer_in_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCancelingTransferInRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCancelingTransferInResponse:
        """
        @param request: SaveSingleTaskForCancelingTransferInRequest
        @return: SaveSingleTaskForCancelingTransferInResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_canceling_transfer_in_with_options_async(request, runtime)

    def save_single_task_for_canceling_transfer_out_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCancelingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCancelingTransferOutResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCancelingTransferOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_canceling_transfer_out_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCancelingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCancelingTransferOutResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCancelingTransferOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_canceling_transfer_out(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCancelingTransferOutRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCancelingTransferOutResponse:
        """
        @param request: SaveSingleTaskForCancelingTransferOutRequest
        @return: SaveSingleTaskForCancelingTransferOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_canceling_transfer_out_with_options(request, runtime)

    async def save_single_task_for_canceling_transfer_out_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCancelingTransferOutRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCancelingTransferOutResponse:
        """
        @param request: SaveSingleTaskForCancelingTransferOutRequest
        @return: SaveSingleTaskForCancelingTransferOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_canceling_transfer_out_with_options_async(request, runtime)

    def save_single_task_for_creating_dns_host_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingDnsHostResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_dns_host_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingDnsHostResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_dns_host(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingDnsHostRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingDnsHostResponse:
        """
        @param request: SaveSingleTaskForCreatingDnsHostRequest
        @return: SaveSingleTaskForCreatingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_dns_host_with_options(request, runtime)

    async def save_single_task_for_creating_dns_host_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingDnsHostRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingDnsHostResponse:
        """
        @param request: SaveSingleTaskForCreatingDnsHostRequest
        @return: SaveSingleTaskForCreatingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_dns_host_with_options_async(request, runtime)

    def save_single_task_for_creating_order_activate_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderActivateResponse:
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderActivate',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderActivateResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_activate_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderActivateResponse:
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderActivate',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderActivateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_activate(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderActivateRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderActivateResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderActivateRequest
        @return: SaveSingleTaskForCreatingOrderActivateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_activate_with_options(request, runtime)

    async def save_single_task_for_creating_order_activate_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderActivateRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderActivateResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderActivateRequest
        @return: SaveSingleTaskForCreatingOrderActivateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_activate_with_options_async(request, runtime)

    def save_single_task_for_creating_order_redeem_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRedeemResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRedeemResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_redeem_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRedeemResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRedeemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_redeem(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRedeemRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderRedeemRequest
        @return: SaveSingleTaskForCreatingOrderRedeemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_redeem_with_options(request, runtime)

    async def save_single_task_for_creating_order_redeem_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRedeemRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderRedeemRequest
        @return: SaveSingleTaskForCreatingOrderRedeemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_redeem_with_options_async(request, runtime)

    def save_single_task_for_creating_order_renew_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRenewResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRenewResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_renew_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRenewResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRenewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_renew(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRenewRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRenewResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderRenewRequest
        @return: SaveSingleTaskForCreatingOrderRenewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_renew_with_options(request, runtime)

    async def save_single_task_for_creating_order_renew_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRenewRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRenewResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderRenewRequest
        @return: SaveSingleTaskForCreatingOrderRenewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_renew_with_options_async(request, runtime)

    def save_single_task_for_creating_order_transfer_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderTransferResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_transfer_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderTransferResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_transfer(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderTransferRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderTransferRequest
        @return: SaveSingleTaskForCreatingOrderTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_transfer_with_options(request, runtime)

    async def save_single_task_for_creating_order_transfer_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForCreatingOrderTransferRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForCreatingOrderTransferResponse:
        """
        @param request: SaveSingleTaskForCreatingOrderTransferRequest
        @return: SaveSingleTaskForCreatingOrderTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_creating_order_transfer_with_options_async(request, runtime)

    def save_single_task_for_deleting_dsrecord_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDeletingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDeletingDSRecordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDeletingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_deleting_dsrecord_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDeletingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDeletingDSRecordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDeletingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_deleting_dsrecord(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDeletingDSRecordRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDeletingDSRecordResponse:
        """
        @param request: SaveSingleTaskForDeletingDSRecordRequest
        @return: SaveSingleTaskForDeletingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_deleting_dsrecord_with_options(request, runtime)

    async def save_single_task_for_deleting_dsrecord_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDeletingDSRecordRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDeletingDSRecordResponse:
        """
        @param request: SaveSingleTaskForDeletingDSRecordRequest
        @return: SaveSingleTaskForDeletingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_deleting_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_deleting_dns_host_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDeletingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDeletingDnsHostResponse:
        """
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
            action='SaveSingleTaskForDeletingDnsHost',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDeletingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_deleting_dns_host_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDeletingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDeletingDnsHostResponse:
        """
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
            action='SaveSingleTaskForDeletingDnsHost',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDeletingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_deleting_dns_host(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDeletingDnsHostRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDeletingDnsHostResponse:
        """
        @param request: SaveSingleTaskForDeletingDnsHostRequest
        @return: SaveSingleTaskForDeletingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_deleting_dns_host_with_options(request, runtime)

    async def save_single_task_for_deleting_dns_host_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDeletingDnsHostRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDeletingDnsHostResponse:
        """
        @param request: SaveSingleTaskForDeletingDnsHostRequest
        @return: SaveSingleTaskForDeletingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_deleting_dns_host_with_options_async(request, runtime)

    def save_single_task_for_disassociating_ens_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDisassociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDisassociatingEnsResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDisassociatingEnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_disassociating_ens_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDisassociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDisassociatingEnsResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDisassociatingEnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_disassociating_ens(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDisassociatingEnsRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDisassociatingEnsResponse:
        """
        @param request: SaveSingleTaskForDisassociatingEnsRequest
        @return: SaveSingleTaskForDisassociatingEnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_disassociating_ens_with_options(request, runtime)

    async def save_single_task_for_disassociating_ens_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDisassociatingEnsRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDisassociatingEnsResponse:
        """
        @param request: SaveSingleTaskForDisassociatingEnsRequest
        @return: SaveSingleTaskForDisassociatingEnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_disassociating_ens_with_options_async(request, runtime)

    def save_single_task_for_domain_name_proxy_service_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDomainNameProxyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_domain_name_proxy_service_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDomainNameProxyServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_domain_name_proxy_service(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDomainNameProxyServiceRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        """
        @param request: SaveSingleTaskForDomainNameProxyServiceRequest
        @return: SaveSingleTaskForDomainNameProxyServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_domain_name_proxy_service_with_options(request, runtime)

    async def save_single_task_for_domain_name_proxy_service_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForDomainNameProxyServiceRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        """
        @param request: SaveSingleTaskForDomainNameProxyServiceRequest
        @return: SaveSingleTaskForDomainNameProxyServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_domain_name_proxy_service_with_options_async(request, runtime)

    def save_single_task_for_modifying_dsrecord_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForModifyingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForModifyingDSRecordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForModifyingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_modifying_dsrecord_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForModifyingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForModifyingDSRecordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForModifyingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_modifying_dsrecord(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForModifyingDSRecordRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForModifyingDSRecordResponse:
        """
        @param request: SaveSingleTaskForModifyingDSRecordRequest
        @return: SaveSingleTaskForModifyingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_modifying_dsrecord_with_options(request, runtime)

    async def save_single_task_for_modifying_dsrecord_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForModifyingDSRecordRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForModifyingDSRecordResponse:
        """
        @param request: SaveSingleTaskForModifyingDSRecordRequest
        @return: SaveSingleTaskForModifyingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_modifying_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_modifying_dns_host_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForModifyingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForModifyingDnsHostResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForModifyingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_modifying_dns_host_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForModifyingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForModifyingDnsHostResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForModifyingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_modifying_dns_host(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForModifyingDnsHostRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForModifyingDnsHostResponse:
        """
        @param request: SaveSingleTaskForModifyingDnsHostRequest
        @return: SaveSingleTaskForModifyingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_modifying_dns_host_with_options(request, runtime)

    async def save_single_task_for_modifying_dns_host_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForModifyingDnsHostRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForModifyingDnsHostResponse:
        """
        @param request: SaveSingleTaskForModifyingDnsHostRequest
        @return: SaveSingleTaskForModifyingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_modifying_dns_host_with_options_async(request, runtime)

    def save_single_task_for_querying_transfer_authorization_code_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_querying_transfer_authorization_code_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_querying_transfer_authorization_code(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        """
        @param request: SaveSingleTaskForQueryingTransferAuthorizationCodeRequest
        @return: SaveSingleTaskForQueryingTransferAuthorizationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_querying_transfer_authorization_code_with_options(request, runtime)

    async def save_single_task_for_querying_transfer_authorization_code_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        """
        @param request: SaveSingleTaskForQueryingTransferAuthorizationCodeRequest
        @return: SaveSingleTaskForQueryingTransferAuthorizationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_querying_transfer_authorization_code_with_options_async(request, runtime)

    def save_single_task_for_save_art_extension_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSaveArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSaveArtExtensionResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForSaveArtExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_save_art_extension_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSaveArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSaveArtExtensionResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForSaveArtExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_save_art_extension(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSaveArtExtensionRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSaveArtExtensionResponse:
        """
        @param request: SaveSingleTaskForSaveArtExtensionRequest
        @return: SaveSingleTaskForSaveArtExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_save_art_extension_with_options(request, runtime)

    async def save_single_task_for_save_art_extension_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSaveArtExtensionRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSaveArtExtensionResponse:
        """
        @param request: SaveSingleTaskForSaveArtExtensionRequest
        @return: SaveSingleTaskForSaveArtExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_save_art_extension_with_options_async(request, runtime)

    def save_single_task_for_synchronizing_dsrecord_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSynchronizingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForSynchronizingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_synchronizing_dsrecord_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSynchronizingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForSynchronizingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_synchronizing_dsrecord(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSynchronizingDSRecordRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        """
        @param request: SaveSingleTaskForSynchronizingDSRecordRequest
        @return: SaveSingleTaskForSynchronizingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_synchronizing_dsrecord_with_options(request, runtime)

    async def save_single_task_for_synchronizing_dsrecord_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSynchronizingDSRecordRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        """
        @param request: SaveSingleTaskForSynchronizingDSRecordRequest
        @return: SaveSingleTaskForSynchronizingDSRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_synchronizing_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_synchronizing_dns_host_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSynchronizingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForSynchronizingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_synchronizing_dns_host_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSynchronizingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForSynchronizingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_synchronizing_dns_host(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSynchronizingDnsHostRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        """
        @param request: SaveSingleTaskForSynchronizingDnsHostRequest
        @return: SaveSingleTaskForSynchronizingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_synchronizing_dns_host_with_options(request, runtime)

    async def save_single_task_for_synchronizing_dns_host_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForSynchronizingDnsHostRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        """
        @param request: SaveSingleTaskForSynchronizingDnsHostRequest
        @return: SaveSingleTaskForSynchronizingDnsHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_synchronizing_dns_host_with_options_async(request, runtime)

    def save_single_task_for_transfer_prohibition_lock_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForTransferProhibitionLockResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForTransferProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_transfer_prohibition_lock_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForTransferProhibitionLockResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForTransferProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_transfer_prohibition_lock(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForTransferProhibitionLockRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForTransferProhibitionLockResponse:
        """
        @param request: SaveSingleTaskForTransferProhibitionLockRequest
        @return: SaveSingleTaskForTransferProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_transfer_prohibition_lock_with_options(request, runtime)

    async def save_single_task_for_transfer_prohibition_lock_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForTransferProhibitionLockRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForTransferProhibitionLockResponse:
        """
        @param request: SaveSingleTaskForTransferProhibitionLockRequest
        @return: SaveSingleTaskForTransferProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_transfer_prohibition_lock_with_options_async(request, runtime)

    def save_single_task_for_update_prohibition_lock_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForUpdateProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_update_prohibition_lock_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForUpdateProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_update_prohibition_lock(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForUpdateProhibitionLockRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        """
        @param request: SaveSingleTaskForUpdateProhibitionLockRequest
        @return: SaveSingleTaskForUpdateProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_update_prohibition_lock_with_options(request, runtime)

    async def save_single_task_for_update_prohibition_lock_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForUpdateProhibitionLockRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        """
        @param request: SaveSingleTaskForUpdateProhibitionLockRequest
        @return: SaveSingleTaskForUpdateProhibitionLockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_update_prohibition_lock_with_options_async(request, runtime)

    def save_single_task_for_updating_contact_info_with_options(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForUpdatingContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForUpdatingContactInfoResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForUpdatingContactInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_updating_contact_info_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForUpdatingContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveSingleTaskForUpdatingContactInfoResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForUpdatingContactInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_updating_contact_info(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForUpdatingContactInfoRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForUpdatingContactInfoResponse:
        """
        @param request: SaveSingleTaskForUpdatingContactInfoRequest
        @return: SaveSingleTaskForUpdatingContactInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_updating_contact_info_with_options(request, runtime)

    async def save_single_task_for_updating_contact_info_async(
        self,
        request: domain_intl_20171218_models.SaveSingleTaskForUpdatingContactInfoRequest,
    ) -> domain_intl_20171218_models.SaveSingleTaskForUpdatingContactInfoResponse:
        """
        @param request: SaveSingleTaskForUpdatingContactInfoRequest
        @return: SaveSingleTaskForUpdatingContactInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_single_task_for_updating_contact_info_with_options_async(request, runtime)

    def save_task_for_submitting_domain_delete_with_options(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainDeleteResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForSubmittingDomainDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_submitting_domain_delete_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainDeleteResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForSubmittingDomainDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_submitting_domain_delete(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainDeleteRequest,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainDeleteResponse:
        """
        @param request: SaveTaskForSubmittingDomainDeleteRequest
        @return: SaveTaskForSubmittingDomainDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_delete_with_options(request, runtime)

    async def save_task_for_submitting_domain_delete_async(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainDeleteRequest,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainDeleteResponse:
        """
        @param request: SaveTaskForSubmittingDomainDeleteRequest
        @return: SaveTaskForSubmittingDomainDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_submitting_domain_delete_with_options_async(request, runtime)

    def save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_submitting_domain_real_name_verification_by_identity_credential(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        """
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest
        @return: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options(request, runtime)

    async def save_task_for_submitting_domain_real_name_verification_by_identity_credential_async(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        """
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest
        @return: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options_async(request, runtime)

    def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options_async(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_id(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        """
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest
        @return: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options(request, runtime)

    async def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_id_async(
        self,
        request: domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
    ) -> domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        """
        @param request: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest
        @return: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options_async(request, runtime)

    def save_task_for_updating_registrant_info_by_identity_credential_with_options(
        self,
        request: domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        """
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
        body = {}
        if not UtilClient.is_unset(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveTaskForUpdatingRegistrantInfoByIdentityCredential',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_updating_registrant_info_by_identity_credential_with_options_async(
        self,
        request: domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        """
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
        body = {}
        if not UtilClient.is_unset(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveTaskForUpdatingRegistrantInfoByIdentityCredential',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_updating_registrant_info_by_identity_credential(
        self,
        request: domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
    ) -> domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        """
        @param request: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest
        @return: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_updating_registrant_info_by_identity_credential_with_options(request, runtime)

    async def save_task_for_updating_registrant_info_by_identity_credential_async(
        self,
        request: domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
    ) -> domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        """
        @param request: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest
        @return: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_updating_registrant_info_by_identity_credential_with_options_async(request, runtime)

    def save_task_for_updating_registrant_info_by_registrant_profile_idwith_options(
        self,
        request: domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_updating_registrant_info_by_registrant_profile_idwith_options_async(
        self,
        request: domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_updating_registrant_info_by_registrant_profile_id(
        self,
        request: domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
    ) -> domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        """
        @param request: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest
        @return: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_updating_registrant_info_by_registrant_profile_idwith_options(request, runtime)

    async def save_task_for_updating_registrant_info_by_registrant_profile_id_async(
        self,
        request: domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
    ) -> domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        """
        @param request: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest
        @return: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_updating_registrant_info_by_registrant_profile_idwith_options_async(request, runtime)

    def submit_email_verification_with_options(
        self,
        request: domain_intl_20171218_models.SubmitEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SubmitEmailVerificationResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SubmitEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_email_verification_with_options_async(
        self,
        request: domain_intl_20171218_models.SubmitEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.SubmitEmailVerificationResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SubmitEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_email_verification(
        self,
        request: domain_intl_20171218_models.SubmitEmailVerificationRequest,
    ) -> domain_intl_20171218_models.SubmitEmailVerificationResponse:
        """
        @param request: SubmitEmailVerificationRequest
        @return: SubmitEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_email_verification_with_options(request, runtime)

    async def submit_email_verification_async(
        self,
        request: domain_intl_20171218_models.SubmitEmailVerificationRequest,
    ) -> domain_intl_20171218_models.SubmitEmailVerificationResponse:
        """
        @param request: SubmitEmailVerificationRequest
        @return: SubmitEmailVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_email_verification_with_options_async(request, runtime)

    def transfer_in_check_mail_token_with_options(
        self,
        request: domain_intl_20171218_models.TransferInCheckMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.TransferInCheckMailTokenResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInCheckMailTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_check_mail_token_with_options_async(
        self,
        request: domain_intl_20171218_models.TransferInCheckMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.TransferInCheckMailTokenResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInCheckMailTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_check_mail_token(
        self,
        request: domain_intl_20171218_models.TransferInCheckMailTokenRequest,
    ) -> domain_intl_20171218_models.TransferInCheckMailTokenResponse:
        """
        @param request: TransferInCheckMailTokenRequest
        @return: TransferInCheckMailTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_check_mail_token_with_options(request, runtime)

    async def transfer_in_check_mail_token_async(
        self,
        request: domain_intl_20171218_models.TransferInCheckMailTokenRequest,
    ) -> domain_intl_20171218_models.TransferInCheckMailTokenResponse:
        """
        @param request: TransferInCheckMailTokenRequest
        @return: TransferInCheckMailTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_check_mail_token_with_options_async(request, runtime)

    def transfer_in_reenter_transfer_authorization_code_with_options(
        self,
        request: domain_intl_20171218_models.TransferInReenterTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.TransferInReenterTransferAuthorizationCodeResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInReenterTransferAuthorizationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_reenter_transfer_authorization_code_with_options_async(
        self,
        request: domain_intl_20171218_models.TransferInReenterTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.TransferInReenterTransferAuthorizationCodeResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInReenterTransferAuthorizationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_reenter_transfer_authorization_code(
        self,
        request: domain_intl_20171218_models.TransferInReenterTransferAuthorizationCodeRequest,
    ) -> domain_intl_20171218_models.TransferInReenterTransferAuthorizationCodeResponse:
        """
        @param request: TransferInReenterTransferAuthorizationCodeRequest
        @return: TransferInReenterTransferAuthorizationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_reenter_transfer_authorization_code_with_options(request, runtime)

    async def transfer_in_reenter_transfer_authorization_code_async(
        self,
        request: domain_intl_20171218_models.TransferInReenterTransferAuthorizationCodeRequest,
    ) -> domain_intl_20171218_models.TransferInReenterTransferAuthorizationCodeResponse:
        """
        @param request: TransferInReenterTransferAuthorizationCodeRequest
        @return: TransferInReenterTransferAuthorizationCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_reenter_transfer_authorization_code_with_options_async(request, runtime)

    def transfer_in_refetch_whois_email_with_options(
        self,
        request: domain_intl_20171218_models.TransferInRefetchWhoisEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.TransferInRefetchWhoisEmailResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInRefetchWhoisEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_refetch_whois_email_with_options_async(
        self,
        request: domain_intl_20171218_models.TransferInRefetchWhoisEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.TransferInRefetchWhoisEmailResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInRefetchWhoisEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_refetch_whois_email(
        self,
        request: domain_intl_20171218_models.TransferInRefetchWhoisEmailRequest,
    ) -> domain_intl_20171218_models.TransferInRefetchWhoisEmailResponse:
        """
        @param request: TransferInRefetchWhoisEmailRequest
        @return: TransferInRefetchWhoisEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_refetch_whois_email_with_options(request, runtime)

    async def transfer_in_refetch_whois_email_async(
        self,
        request: domain_intl_20171218_models.TransferInRefetchWhoisEmailRequest,
    ) -> domain_intl_20171218_models.TransferInRefetchWhoisEmailResponse:
        """
        @param request: TransferInRefetchWhoisEmailRequest
        @return: TransferInRefetchWhoisEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_refetch_whois_email_with_options_async(request, runtime)

    def transfer_in_resend_mail_token_with_options(
        self,
        request: domain_intl_20171218_models.TransferInResendMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.TransferInResendMailTokenResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInResendMailTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_resend_mail_token_with_options_async(
        self,
        request: domain_intl_20171218_models.TransferInResendMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.TransferInResendMailTokenResponse:
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInResendMailTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_resend_mail_token(
        self,
        request: domain_intl_20171218_models.TransferInResendMailTokenRequest,
    ) -> domain_intl_20171218_models.TransferInResendMailTokenResponse:
        """
        @param request: TransferInResendMailTokenRequest
        @return: TransferInResendMailTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_resend_mail_token_with_options(request, runtime)

    async def transfer_in_resend_mail_token_async(
        self,
        request: domain_intl_20171218_models.TransferInResendMailTokenRequest,
    ) -> domain_intl_20171218_models.TransferInResendMailTokenResponse:
        """
        @param request: TransferInResendMailTokenRequest
        @return: TransferInResendMailTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_in_resend_mail_token_with_options_async(request, runtime)

    def verify_contact_field_with_options(
        self,
        request: domain_intl_20171218_models.VerifyContactFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.VerifyContactFieldResponse:
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyContactField',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.VerifyContactFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_contact_field_with_options_async(
        self,
        request: domain_intl_20171218_models.VerifyContactFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.VerifyContactFieldResponse:
        """
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyContactField',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.VerifyContactFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_contact_field(
        self,
        request: domain_intl_20171218_models.VerifyContactFieldRequest,
    ) -> domain_intl_20171218_models.VerifyContactFieldResponse:
        """
        @param request: VerifyContactFieldRequest
        @return: VerifyContactFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_contact_field_with_options(request, runtime)

    async def verify_contact_field_async(
        self,
        request: domain_intl_20171218_models.VerifyContactFieldRequest,
    ) -> domain_intl_20171218_models.VerifyContactFieldResponse:
        """
        @param request: VerifyContactFieldRequest
        @return: VerifyContactFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_contact_field_with_options_async(request, runtime)

    def verify_email_with_options(
        self,
        request: domain_intl_20171218_models.VerifyEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.VerifyEmailResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.VerifyEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_email_with_options_async(
        self,
        request: domain_intl_20171218_models.VerifyEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_intl_20171218_models.VerifyEmailResponse:
        """
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
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.VerifyEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_email(
        self,
        request: domain_intl_20171218_models.VerifyEmailRequest,
    ) -> domain_intl_20171218_models.VerifyEmailResponse:
        """
        @param request: VerifyEmailRequest
        @return: VerifyEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_email_with_options(request, runtime)

    async def verify_email_async(
        self,
        request: domain_intl_20171218_models.VerifyEmailRequest,
    ) -> domain_intl_20171218_models.VerifyEmailResponse:
        """
        @param request: VerifyEmailRequest
        @return: VerifyEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_email_with_options_async(request, runtime)
