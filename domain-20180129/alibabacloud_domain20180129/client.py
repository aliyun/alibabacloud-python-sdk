# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_domain20180129 import models as domain_20180129_models
from alibabacloud_tea_util import models as util_models


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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.AcknowledgeTaskResultResponse().from_map(
            self.do_rpcrequest('AcknowledgeTaskResult', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def acknowledge_task_result_with_options_async(
        self,
        request: domain_20180129_models.AcknowledgeTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.AcknowledgeTaskResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.AcknowledgeTaskResultResponse().from_map(
            await self.do_rpcrequest_async('AcknowledgeTaskResult', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordResponse().from_map(
            self.do_rpcrequest('BatchFuzzyMatchDomainSensitiveWord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_fuzzy_match_domain_sensitive_word_with_options_async(
        self,
        request: domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.BatchFuzzyMatchDomainSensitiveWordResponse().from_map(
            await self.do_rpcrequest_async('BatchFuzzyMatchDomainSensitiveWord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CancelDomainVerificationResponse().from_map(
            self.do_rpcrequest('CancelDomainVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_domain_verification_with_options_async(
        self,
        request: domain_20180129_models.CancelDomainVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelDomainVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CancelDomainVerificationResponse().from_map(
            await self.do_rpcrequest_async('CancelDomainVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CancelOperationAuditResponse().from_map(
            self.do_rpcrequest('CancelOperationAudit', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_operation_audit_with_options_async(
        self,
        request: domain_20180129_models.CancelOperationAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelOperationAuditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CancelOperationAuditResponse().from_map(
            await self.do_rpcrequest_async('CancelOperationAudit', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CancelQualificationVerificationResponse().from_map(
            self.do_rpcrequest('CancelQualificationVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_qualification_verification_with_options_async(
        self,
        request: domain_20180129_models.CancelQualificationVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelQualificationVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CancelQualificationVerificationResponse().from_map(
            await self.do_rpcrequest_async('CancelQualificationVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CancelTaskResponse().from_map(
            self.do_rpcrequest('CancelTask', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        request: domain_20180129_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CancelTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CancelTaskResponse().from_map(
            await self.do_rpcrequest_async('CancelTask', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CheckDomainResponse().from_map(
            self.do_rpcrequest('CheckDomain', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_domain_with_options_async(
        self,
        request: domain_20180129_models.CheckDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CheckDomainResponse().from_map(
            await self.do_rpcrequest_async('CheckDomain', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CheckDomainSunriseClaimResponse().from_map(
            self.do_rpcrequest('CheckDomainSunriseClaim', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_domain_sunrise_claim_with_options_async(
        self,
        request: domain_20180129_models.CheckDomainSunriseClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckDomainSunriseClaimResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CheckDomainSunriseClaimResponse().from_map(
            await self.do_rpcrequest_async('CheckDomainSunriseClaim', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CheckMaxYearOfServerLockResponse().from_map(
            self.do_rpcrequest('CheckMaxYearOfServerLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_max_year_of_server_lock_with_options_async(
        self,
        request: domain_20180129_models.CheckMaxYearOfServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckMaxYearOfServerLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CheckMaxYearOfServerLockResponse().from_map(
            await self.do_rpcrequest_async('CheckMaxYearOfServerLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CheckProcessingServerLockApplyResponse().from_map(
            self.do_rpcrequest('CheckProcessingServerLockApply', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_processing_server_lock_apply_with_options_async(
        self,
        request: domain_20180129_models.CheckProcessingServerLockApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckProcessingServerLockApplyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CheckProcessingServerLockApplyResponse().from_map(
            await self.do_rpcrequest_async('CheckProcessingServerLockApply', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CheckTransferInFeasibilityResponse().from_map(
            self.do_rpcrequest('CheckTransferInFeasibility', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_transfer_in_feasibility_with_options_async(
        self,
        request: domain_20180129_models.CheckTransferInFeasibilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.CheckTransferInFeasibilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.CheckTransferInFeasibilityResponse().from_map(
            await self.do_rpcrequest_async('CheckTransferInFeasibility', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ConfirmTransferInEmailResponse().from_map(
            self.do_rpcrequest('ConfirmTransferInEmail', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def confirm_transfer_in_email_with_options_async(
        self,
        request: domain_20180129_models.ConfirmTransferInEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ConfirmTransferInEmailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ConfirmTransferInEmailResponse().from_map(
            await self.do_rpcrequest_async('ConfirmTransferInEmail', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_domain_group_with_options(
        self,
        request: domain_20180129_models.DeleteDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteDomainGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.DeleteDomainGroupResponse().from_map(
            self.do_rpcrequest('DeleteDomainGroup', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_domain_group_with_options_async(
        self,
        request: domain_20180129_models.DeleteDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteDomainGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.DeleteDomainGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteDomainGroup', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.DeleteEmailVerificationResponse().from_map(
            self.do_rpcrequest('DeleteEmailVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_email_verification_with_options_async(
        self,
        request: domain_20180129_models.DeleteEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteEmailVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.DeleteEmailVerificationResponse().from_map(
            await self.do_rpcrequest_async('DeleteEmailVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.DeleteRegistrantProfileResponse().from_map(
            self.do_rpcrequest('DeleteRegistrantProfile', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_registrant_profile_with_options_async(
        self,
        request: domain_20180129_models.DeleteRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.DeleteRegistrantProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.DeleteRegistrantProfileResponse().from_map(
            await self.do_rpcrequest_async('DeleteRegistrantProfile', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.EmailVerifiedResponse().from_map(
            self.do_rpcrequest('EmailVerified', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def email_verified_with_options_async(
        self,
        request: domain_20180129_models.EmailVerifiedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.EmailVerifiedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.EmailVerifiedResponse().from_map(
            await self.do_rpcrequest_async('EmailVerified', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.FuzzyMatchDomainSensitiveWordResponse().from_map(
            self.do_rpcrequest('FuzzyMatchDomainSensitiveWord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def fuzzy_match_domain_sensitive_word_with_options_async(
        self,
        request: domain_20180129_models.FuzzyMatchDomainSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.FuzzyMatchDomainSensitiveWordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.FuzzyMatchDomainSensitiveWordResponse().from_map(
            await self.do_rpcrequest_async('FuzzyMatchDomainSensitiveWord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.GetOperationOssUploadPolicyResponse().from_map(
            self.do_rpcrequest('GetOperationOssUploadPolicy', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_operation_oss_upload_policy_with_options_async(
        self,
        request: domain_20180129_models.GetOperationOssUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.GetOperationOssUploadPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.GetOperationOssUploadPolicyResponse().from_map(
            await self.do_rpcrequest_async('GetOperationOssUploadPolicy', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.GetQualificationUploadPolicyResponse().from_map(
            self.do_rpcrequest('GetQualificationUploadPolicy', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_qualification_upload_policy_with_options_async(
        self,
        request: domain_20180129_models.GetQualificationUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.GetQualificationUploadPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.GetQualificationUploadPolicyResponse().from_map(
            await self.do_rpcrequest_async('GetQualificationUploadPolicy', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ListEmailVerificationResponse().from_map(
            self.do_rpcrequest('ListEmailVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_email_verification_with_options_async(
        self,
        request: domain_20180129_models.ListEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ListEmailVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ListEmailVerificationResponse().from_map(
            await self.do_rpcrequest_async('ListEmailVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ListServerLockResponse().from_map(
            self.do_rpcrequest('ListServerLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_server_lock_with_options_async(
        self,
        request: domain_20180129_models.ListServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ListServerLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ListServerLockResponse().from_map(
            await self.do_rpcrequest_async('ListServerLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.LookupTmchNoticeResponse().from_map(
            self.do_rpcrequest('LookupTmchNotice', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def lookup_tmch_notice_with_options_async(
        self,
        request: domain_20180129_models.LookupTmchNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.LookupTmchNoticeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.LookupTmchNoticeResponse().from_map(
            await self.do_rpcrequest_async('LookupTmchNotice', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.PollTaskResultResponse().from_map(
            self.do_rpcrequest('PollTaskResult', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def poll_task_result_with_options_async(
        self,
        request: domain_20180129_models.PollTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.PollTaskResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.PollTaskResultResponse().from_map(
            await self.do_rpcrequest_async('PollTaskResult', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryAdvancedDomainListResponse().from_map(
            self.do_rpcrequest('QueryAdvancedDomainList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_advanced_domain_list_with_options_async(
        self,
        request: domain_20180129_models.QueryAdvancedDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryAdvancedDomainListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryAdvancedDomainListResponse().from_map(
            await self.do_rpcrequest_async('QueryAdvancedDomainList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryArtExtensionResponse().from_map(
            self.do_rpcrequest('QueryArtExtension', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_art_extension_with_options_async(
        self,
        request: domain_20180129_models.QueryArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryArtExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryArtExtensionResponse().from_map(
            await self.do_rpcrequest_async('QueryArtExtension', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryChangeLogListResponse().from_map(
            self.do_rpcrequest('QueryChangeLogList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_change_log_list_with_options_async(
        self,
        request: domain_20180129_models.QueryChangeLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryChangeLogListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryChangeLogListResponse().from_map(
            await self.do_rpcrequest_async('QueryChangeLogList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryContactInfoResponse().from_map(
            self.do_rpcrequest('QueryContactInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_contact_info_with_options_async(
        self,
        request: domain_20180129_models.QueryContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryContactInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryContactInfoResponse().from_map(
            await self.do_rpcrequest_async('QueryContactInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_dns_host_with_options(
        self,
        request: domain_20180129_models.QueryDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDnsHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDnsHostResponse().from_map(
            self.do_rpcrequest('QueryDnsHost', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_dns_host_with_options_async(
        self,
        request: domain_20180129_models.QueryDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDnsHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDnsHostResponse().from_map(
            await self.do_rpcrequest_async('QueryDnsHost', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainAdminDivisionResponse().from_map(
            self.do_rpcrequest('QueryDomainAdminDivision', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_domain_admin_division_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainAdminDivisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainAdminDivisionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainAdminDivisionResponse().from_map(
            await self.do_rpcrequest_async('QueryDomainAdminDivision', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainByDomainNameResponse().from_map(
            self.do_rpcrequest('QueryDomainByDomainName', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_domain_by_domain_name_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainByDomainNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainByDomainNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainByDomainNameResponse().from_map(
            await self.do_rpcrequest_async('QueryDomainByDomainName', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainByInstanceIdResponse().from_map(
            self.do_rpcrequest('QueryDomainByInstanceId', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_domain_by_instance_id_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainByInstanceIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainByInstanceIdResponse().from_map(
            await self.do_rpcrequest_async('QueryDomainByInstanceId', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainGroupListResponse().from_map(
            self.do_rpcrequest('QueryDomainGroupList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_domain_group_list_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainGroupListResponse().from_map(
            await self.do_rpcrequest_async('QueryDomainGroupList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainListResponse().from_map(
            self.do_rpcrequest('QueryDomainList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_domain_list_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainListResponse().from_map(
            await self.do_rpcrequest_async('QueryDomainList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainRealNameVerificationInfoResponse().from_map(
            self.do_rpcrequest('QueryDomainRealNameVerificationInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_domain_real_name_verification_info_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainRealNameVerificationInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainRealNameVerificationInfoResponse().from_map(
            await self.do_rpcrequest_async('QueryDomainRealNameVerificationInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainSuffixResponse().from_map(
            self.do_rpcrequest('QueryDomainSuffix', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_domain_suffix_with_options_async(
        self,
        request: domain_20180129_models.QueryDomainSuffixRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDomainSuffixResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDomainSuffixResponse().from_map(
            await self.do_rpcrequest_async('QueryDomainSuffix', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_dsrecord_with_options(
        self,
        request: domain_20180129_models.QueryDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDSRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDSRecordResponse().from_map(
            self.do_rpcrequest('QueryDSRecord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_dsrecord_with_options_async(
        self,
        request: domain_20180129_models.QueryDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryDSRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryDSRecordResponse().from_map(
            await self.do_rpcrequest_async('QueryDSRecord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_email_verification_with_options(
        self,
        request: domain_20180129_models.QueryEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryEmailVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryEmailVerificationResponse().from_map(
            self.do_rpcrequest('QueryEmailVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_email_verification_with_options_async(
        self,
        request: domain_20180129_models.QueryEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryEmailVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryEmailVerificationResponse().from_map(
            await self.do_rpcrequest_async('QueryEmailVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryEnsAssociationResponse().from_map(
            self.do_rpcrequest('QueryEnsAssociation', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_ens_association_with_options_async(
        self,
        request: domain_20180129_models.QueryEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryEnsAssociationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryEnsAssociationResponse().from_map(
            await self.do_rpcrequest_async('QueryEnsAssociation', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_failing_reason_list_for_qualification_with_options(
        self,
        request: domain_20180129_models.QueryFailingReasonListForQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailingReasonListForQualificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryFailingReasonListForQualificationResponse().from_map(
            self.do_rpcrequest('QueryFailingReasonListForQualification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_failing_reason_list_for_qualification_with_options_async(
        self,
        request: domain_20180129_models.QueryFailingReasonListForQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailingReasonListForQualificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryFailingReasonListForQualificationResponse().from_map(
            await self.do_rpcrequest_async('QueryFailingReasonListForQualification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_fail_reason_for_domain_real_name_verification_with_options(
        self,
        request: domain_20180129_models.QueryFailReasonForDomainRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse().from_map(
            self.do_rpcrequest('QueryFailReasonForDomainRealNameVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_fail_reason_for_domain_real_name_verification_with_options_async(
        self,
        request: domain_20180129_models.QueryFailReasonForDomainRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryFailReasonForDomainRealNameVerificationResponse().from_map(
            await self.do_rpcrequest_async('QueryFailReasonForDomainRealNameVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse().from_map(
            self.do_rpcrequest('QueryFailReasonForRegistrantProfileRealNameVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_fail_reason_for_registrant_profile_real_name_verification_with_options_async(
        self,
        request: domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse().from_map(
            await self.do_rpcrequest_async('QueryFailReasonForRegistrantProfileRealNameVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_local_ens_association_with_options(
        self,
        request: domain_20180129_models.QueryLocalEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryLocalEnsAssociationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryLocalEnsAssociationResponse().from_map(
            self.do_rpcrequest('QueryLocalEnsAssociation', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_local_ens_association_with_options_async(
        self,
        request: domain_20180129_models.QueryLocalEnsAssociationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryLocalEnsAssociationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryLocalEnsAssociationResponse().from_map(
            await self.do_rpcrequest_async('QueryLocalEnsAssociation', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryOperationAuditInfoDetailResponse().from_map(
            self.do_rpcrequest('QueryOperationAuditInfoDetail', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_operation_audit_info_detail_with_options_async(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryOperationAuditInfoDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryOperationAuditInfoDetailResponse().from_map(
            await self.do_rpcrequest_async('QueryOperationAuditInfoDetail', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryOperationAuditInfoListResponse().from_map(
            self.do_rpcrequest('QueryOperationAuditInfoList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_operation_audit_info_list_with_options_async(
        self,
        request: domain_20180129_models.QueryOperationAuditInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryOperationAuditInfoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryOperationAuditInfoListResponse().from_map(
            await self.do_rpcrequest_async('QueryOperationAuditInfoList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryQualificationDetailResponse().from_map(
            self.do_rpcrequest('QueryQualificationDetail', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_qualification_detail_with_options_async(
        self,
        request: domain_20180129_models.QueryQualificationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryQualificationDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryQualificationDetailResponse().from_map(
            await self.do_rpcrequest_async('QueryQualificationDetail', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoResponse().from_map(
            self.do_rpcrequest('QueryRegistrantProfileRealNameVerificationInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_registrant_profile_real_name_verification_info_with_options_async(
        self,
        request: domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryRegistrantProfileRealNameVerificationInfoResponse().from_map(
            await self.do_rpcrequest_async('QueryRegistrantProfileRealNameVerificationInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryRegistrantProfilesResponse().from_map(
            self.do_rpcrequest('QueryRegistrantProfiles', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_registrant_profiles_with_options_async(
        self,
        request: domain_20180129_models.QueryRegistrantProfilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryRegistrantProfilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryRegistrantProfilesResponse().from_map(
            await self.do_rpcrequest_async('QueryRegistrantProfiles', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryServerLockResponse().from_map(
            self.do_rpcrequest('QueryServerLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_server_lock_with_options_async(
        self,
        request: domain_20180129_models.QueryServerLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryServerLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryServerLockResponse().from_map(
            await self.do_rpcrequest_async('QueryServerLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTaskDetailHistoryResponse().from_map(
            self.do_rpcrequest('QueryTaskDetailHistory', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_task_detail_history_with_options_async(
        self,
        request: domain_20180129_models.QueryTaskDetailHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskDetailHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTaskDetailHistoryResponse().from_map(
            await self.do_rpcrequest_async('QueryTaskDetailHistory', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTaskDetailListResponse().from_map(
            self.do_rpcrequest('QueryTaskDetailList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_task_detail_list_with_options_async(
        self,
        request: domain_20180129_models.QueryTaskDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskDetailListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTaskDetailListResponse().from_map(
            await self.do_rpcrequest_async('QueryTaskDetailList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTaskInfoHistoryResponse().from_map(
            self.do_rpcrequest('QueryTaskInfoHistory', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_task_info_history_with_options_async(
        self,
        request: domain_20180129_models.QueryTaskInfoHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskInfoHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTaskInfoHistoryResponse().from_map(
            await self.do_rpcrequest_async('QueryTaskInfoHistory', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTaskListResponse().from_map(
            self.do_rpcrequest('QueryTaskList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_task_list_with_options_async(
        self,
        request: domain_20180129_models.QueryTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTaskListResponse().from_map(
            await self.do_rpcrequest_async('QueryTaskList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTransferInByInstanceIdResponse().from_map(
            self.do_rpcrequest('QueryTransferInByInstanceId', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_transfer_in_by_instance_id_with_options_async(
        self,
        request: domain_20180129_models.QueryTransferInByInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferInByInstanceIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTransferInByInstanceIdResponse().from_map(
            await self.do_rpcrequest_async('QueryTransferInByInstanceId', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTransferInListResponse().from_map(
            self.do_rpcrequest('QueryTransferInList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_transfer_in_list_with_options_async(
        self,
        request: domain_20180129_models.QueryTransferInListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferInListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTransferInListResponse().from_map(
            await self.do_rpcrequest_async('QueryTransferInList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTransferOutInfoResponse().from_map(
            self.do_rpcrequest('QueryTransferOutInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_transfer_out_info_with_options_async(
        self,
        request: domain_20180129_models.QueryTransferOutInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.QueryTransferOutInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.QueryTransferOutInfoResponse().from_map(
            await self.do_rpcrequest_async('QueryTransferOutInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.RegistrantProfileRealNameVerificationResponse().from_map(
            self.do_rpcrequest('RegistrantProfileRealNameVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def registrant_profile_real_name_verification_with_options_async(
        self,
        request: domain_20180129_models.RegistrantProfileRealNameVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.RegistrantProfileRealNameVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.RegistrantProfileRealNameVerificationResponse().from_map(
            await self.do_rpcrequest_async('RegistrantProfileRealNameVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ResendEmailVerificationResponse().from_map(
            self.do_rpcrequest('ResendEmailVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resend_email_verification_with_options_async(
        self,
        request: domain_20180129_models.ResendEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ResendEmailVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ResendEmailVerificationResponse().from_map(
            await self.do_rpcrequest_async('ResendEmailVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ResetQualificationVerificationResponse().from_map(
            self.do_rpcrequest('ResetQualificationVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_qualification_verification_with_options_async(
        self,
        request: domain_20180129_models.ResetQualificationVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ResetQualificationVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ResetQualificationVerificationResponse().from_map(
            await self.do_rpcrequest_async('ResetQualificationVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchDomainRemarkResponse().from_map(
            self.do_rpcrequest('SaveBatchDomainRemark', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_batch_domain_remark_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchDomainRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchDomainRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchDomainRemarkResponse().from_map(
            await self.do_rpcrequest_async('SaveBatchDomainRemark', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForCreatingOrderActivateResponse().from_map(
            self.do_rpcrequest('SaveBatchTaskForCreatingOrderActivate', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_batch_task_for_creating_order_activate_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderActivateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForCreatingOrderActivateResponse().from_map(
            await self.do_rpcrequest_async('SaveBatchTaskForCreatingOrderActivate', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemResponse().from_map(
            self.do_rpcrequest('SaveBatchTaskForCreatingOrderRedeem', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_batch_task_for_creating_order_redeem_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForCreatingOrderRedeemResponse().from_map(
            await self.do_rpcrequest_async('SaveBatchTaskForCreatingOrderRedeem', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForCreatingOrderRenewResponse().from_map(
            self.do_rpcrequest('SaveBatchTaskForCreatingOrderRenew', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_batch_task_for_creating_order_renew_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderRenewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForCreatingOrderRenewResponse().from_map(
            await self.do_rpcrequest_async('SaveBatchTaskForCreatingOrderRenew', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForCreatingOrderTransferResponse().from_map(
            self.do_rpcrequest('SaveBatchTaskForCreatingOrderTransfer', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_batch_task_for_creating_order_transfer_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForCreatingOrderTransferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForCreatingOrderTransferResponse().from_map(
            await self.do_rpcrequest_async('SaveBatchTaskForCreatingOrderTransfer', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceResponse().from_map(
            self.do_rpcrequest('SaveBatchTaskForDomainNameProxyService', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_batch_task_for_domain_name_proxy_service_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForDomainNameProxyServiceResponse().from_map(
            await self.do_rpcrequest_async('SaveBatchTaskForDomainNameProxyService', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForModifyingDomainDnsResponse().from_map(
            self.do_rpcrequest('SaveBatchTaskForModifyingDomainDns', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_batch_task_for_modifying_domain_dns_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForModifyingDomainDnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForModifyingDomainDnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForModifyingDomainDnsResponse().from_map(
            await self.do_rpcrequest_async('SaveBatchTaskForModifyingDomainDns', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def save_batch_task_for_transfer_prohibition_lock_with_options(
        self,
        request: domain_20180129_models.SaveBatchTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse().from_map(
            self.do_rpcrequest('SaveBatchTaskForTransferProhibitionLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_batch_task_for_transfer_prohibition_lock_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForTransferProhibitionLockResponse().from_map(
            await self.do_rpcrequest_async('SaveBatchTaskForTransferProhibitionLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockResponse().from_map(
            self.do_rpcrequest('SaveBatchTaskForUpdateProhibitionLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_batch_task_for_update_prohibition_lock_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForUpdateProhibitionLockResponse().from_map(
            await self.do_rpcrequest_async('SaveBatchTaskForUpdateProhibitionLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse().from_map(
            self.do_rpcrequest('SaveBatchTaskForUpdatingContactInfoByNewContact', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_batch_task_for_updating_contact_info_by_new_contact_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse().from_map(
            await self.do_rpcrequest_async('SaveBatchTaskForUpdatingContactInfoByNewContact', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse().from_map(
            self.do_rpcrequest('SaveBatchTaskForUpdatingContactInfoByRegistrantProfileId', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options_async(
        self,
        request: domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse().from_map(
            await self.do_rpcrequest_async('SaveBatchTaskForUpdatingContactInfoByRegistrantProfileId', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveDomainGroupResponse().from_map(
            self.do_rpcrequest('SaveDomainGroup', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_domain_group_with_options_async(
        self,
        request: domain_20180129_models.SaveDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveDomainGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveDomainGroupResponse().from_map(
            await self.do_rpcrequest_async('SaveDomainGroup', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveRegistrantProfileResponse().from_map(
            self.do_rpcrequest('SaveRegistrantProfile', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_registrant_profile_with_options_async(
        self,
        request: domain_20180129_models.SaveRegistrantProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveRegistrantProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveRegistrantProfileResponse().from_map(
            await self.do_rpcrequest_async('SaveRegistrantProfile', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def save_single_task_for_adding_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForAddingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForAddingDSRecord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_adding_dsrecord_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForAddingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForAddingDSRecordResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForAddingDSRecord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForApprovingTransferOutResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForApprovingTransferOut', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_approving_transfer_out_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForApprovingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForApprovingTransferOutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForApprovingTransferOutResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForApprovingTransferOut', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForAssociatingEnsResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForAssociatingEns', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_associating_ens_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForAssociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForAssociatingEnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForAssociatingEnsResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForAssociatingEns', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCancelingTransferInResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForCancelingTransferIn', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_canceling_transfer_in_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferInRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferInResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCancelingTransferInResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForCancelingTransferIn', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCancelingTransferOutResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForCancelingTransferOut', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_canceling_transfer_out_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCancelingTransferOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCancelingTransferOutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCancelingTransferOutResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForCancelingTransferOut', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCreatingDnsHostResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForCreatingDnsHost', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_creating_dns_host_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingDnsHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCreatingDnsHostResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForCreatingDnsHost', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCreatingOrderActivateResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForCreatingOrderActivate', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_creating_order_activate_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderActivateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderActivateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCreatingOrderActivateResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForCreatingOrderActivate', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForCreatingOrderRedeem', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_creating_order_redeem_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCreatingOrderRedeemResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForCreatingOrderRedeem', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCreatingOrderRenewResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForCreatingOrderRenew', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_creating_order_renew_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderRenewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCreatingOrderRenewResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForCreatingOrderRenew', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCreatingOrderTransferResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForCreatingOrderTransfer', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_creating_order_transfer_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForCreatingOrderTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForCreatingOrderTransferResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForCreatingOrderTransferResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForCreatingOrderTransfer', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def save_single_task_for_deleting_dns_host_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForDeletingDnsHost', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_deleting_dns_host_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForDeletingDnsHostResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForDeletingDnsHost', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def save_single_task_for_deleting_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForDeletingDSRecord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_deleting_dsrecord_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDeletingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForDeletingDSRecordResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForDeletingDSRecord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def save_single_task_for_disassociating_ens_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForDisassociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForDisassociatingEns', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_disassociating_ens_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDisassociatingEnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForDisassociatingEnsResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForDisassociatingEns', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForDomainNameProxyService', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_domain_name_proxy_service_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForDomainNameProxyServiceResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForDomainNameProxyService', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def save_single_task_for_modifying_dns_host_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForModifyingDnsHost', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_modifying_dns_host_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForModifyingDnsHostResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForModifyingDnsHost', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def save_single_task_for_modifying_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForModifyingDSRecord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_modifying_dsrecord_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForModifyingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForModifyingDSRecordResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForModifyingDSRecord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def save_single_task_for_querying_transfer_authorization_code_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForQueryingTransferAuthorizationCode', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_querying_transfer_authorization_code_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForQueryingTransferAuthorizationCode', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForSaveArtExtensionResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForSaveArtExtension', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_save_art_extension_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSaveArtExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSaveArtExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForSaveArtExtensionResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForSaveArtExtension', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def save_single_task_for_synchronizing_dns_host_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForSynchronizingDnsHost', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_synchronizing_dns_host_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForSynchronizingDnsHostResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForSynchronizingDnsHost', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def save_single_task_for_synchronizing_dsrecord_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForSynchronizingDSRecord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_synchronizing_dsrecord_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForSynchronizingDSRecordResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForSynchronizingDSRecord', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def save_single_task_for_transfer_prohibition_lock_with_options(
        self,
        request: domain_20180129_models.SaveSingleTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForTransferProhibitionLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_transfer_prohibition_lock_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForTransferProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForTransferProhibitionLockResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForTransferProhibitionLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForUpdateProhibitionLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_update_prohibition_lock_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForUpdateProhibitionLockResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForUpdateProhibitionLock', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForUpdatingContactInfoResponse().from_map(
            self.do_rpcrequest('SaveSingleTaskForUpdatingContactInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_single_task_for_updating_contact_info_with_options_async(
        self,
        request: domain_20180129_models.SaveSingleTaskForUpdatingContactInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveSingleTaskForUpdatingContactInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveSingleTaskForUpdatingContactInfoResponse().from_map(
            await self.do_rpcrequest_async('SaveSingleTaskForUpdatingContactInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveTaskForSubmittingDomainDeleteResponse().from_map(
            self.do_rpcrequest('SaveTaskForSubmittingDomainDelete', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_task_for_submitting_domain_delete_with_options_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainDeleteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveTaskForSubmittingDomainDeleteResponse().from_map(
            await self.do_rpcrequest_async('SaveTaskForSubmittingDomainDelete', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse().from_map(
            self.do_rpcrequest('SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredential', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse().from_map(
            await self.do_rpcrequest_async('SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredential', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse().from_map(
            self.do_rpcrequest('SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileID', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options_async(
        self,
        request: domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse().from_map(
            await self.do_rpcrequest_async('SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileID', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse().from_map(
            self.do_rpcrequest('SaveTaskForUpdatingRegistrantInfoByIdentityCredential', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_task_for_updating_registrant_info_by_identity_credential_with_options_async(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse().from_map(
            await self.do_rpcrequest_async('SaveTaskForUpdatingRegistrantInfoByIdentityCredential', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse().from_map(
            self.do_rpcrequest('SaveTaskForUpdatingRegistrantInfoByRegistrantProfileID', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_task_for_updating_registrant_info_by_registrant_profile_idwith_options_async(
        self,
        request: domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse().from_map(
            await self.do_rpcrequest_async('SaveTaskForUpdatingRegistrantInfoByRegistrantProfileID', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ScrollDomainListResponse().from_map(
            self.do_rpcrequest('ScrollDomainList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def scroll_domain_list_with_options_async(
        self,
        request: domain_20180129_models.ScrollDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.ScrollDomainListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.ScrollDomainListResponse().from_map(
            await self.do_rpcrequest_async('ScrollDomainList', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def submit_email_verification_with_options(
        self,
        request: domain_20180129_models.SubmitEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitEmailVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SubmitEmailVerificationResponse().from_map(
            self.do_rpcrequest('SubmitEmailVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_email_verification_with_options_async(
        self,
        request: domain_20180129_models.SubmitEmailVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitEmailVerificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SubmitEmailVerificationResponse().from_map(
            await self.do_rpcrequest_async('SubmitEmailVerification', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SubmitOperationAuditInfoResponse().from_map(
            self.do_rpcrequest('SubmitOperationAuditInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_operation_audit_info_with_options_async(
        self,
        request: domain_20180129_models.SubmitOperationAuditInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitOperationAuditInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SubmitOperationAuditInfoResponse().from_map(
            await self.do_rpcrequest_async('SubmitOperationAuditInfo', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SubmitOperationCredentialsResponse().from_map(
            self.do_rpcrequest('SubmitOperationCredentials', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_operation_credentials_with_options_async(
        self,
        request: domain_20180129_models.SubmitOperationCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.SubmitOperationCredentialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.SubmitOperationCredentialsResponse().from_map(
            await self.do_rpcrequest_async('SubmitOperationCredentials', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.TransferInCheckMailTokenResponse().from_map(
            self.do_rpcrequest('TransferInCheckMailToken', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_in_check_mail_token_with_options_async(
        self,
        request: domain_20180129_models.TransferInCheckMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInCheckMailTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.TransferInCheckMailTokenResponse().from_map(
            await self.do_rpcrequest_async('TransferInCheckMailToken', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.TransferInReenterTransferAuthorizationCodeResponse().from_map(
            self.do_rpcrequest('TransferInReenterTransferAuthorizationCode', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_in_reenter_transfer_authorization_code_with_options_async(
        self,
        request: domain_20180129_models.TransferInReenterTransferAuthorizationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInReenterTransferAuthorizationCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.TransferInReenterTransferAuthorizationCodeResponse().from_map(
            await self.do_rpcrequest_async('TransferInReenterTransferAuthorizationCode', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.TransferInRefetchWhoisEmailResponse().from_map(
            self.do_rpcrequest('TransferInRefetchWhoisEmail', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_in_refetch_whois_email_with_options_async(
        self,
        request: domain_20180129_models.TransferInRefetchWhoisEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInRefetchWhoisEmailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.TransferInRefetchWhoisEmailResponse().from_map(
            await self.do_rpcrequest_async('TransferInRefetchWhoisEmail', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.TransferInResendMailTokenResponse().from_map(
            self.do_rpcrequest('TransferInResendMailToken', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_in_resend_mail_token_with_options_async(
        self,
        request: domain_20180129_models.TransferInResendMailTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.TransferInResendMailTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.TransferInResendMailTokenResponse().from_map(
            await self.do_rpcrequest_async('TransferInResendMailToken', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.UpdateDomainToDomainGroupResponse().from_map(
            self.do_rpcrequest('UpdateDomainToDomainGroup', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_domain_to_domain_group_with_options_async(
        self,
        request: domain_20180129_models.UpdateDomainToDomainGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.UpdateDomainToDomainGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.UpdateDomainToDomainGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateDomainToDomainGroup', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.VerifyContactFieldResponse().from_map(
            self.do_rpcrequest('VerifyContactField', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_contact_field_with_options_async(
        self,
        request: domain_20180129_models.VerifyContactFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.VerifyContactFieldResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.VerifyContactFieldResponse().from_map(
            await self.do_rpcrequest_async('VerifyContactField', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.VerifyEmailResponse().from_map(
            self.do_rpcrequest('VerifyEmail', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_email_with_options_async(
        self,
        request: domain_20180129_models.VerifyEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> domain_20180129_models.VerifyEmailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return domain_20180129_models.VerifyEmailResponse().from_map(
            await self.do_rpcrequest_async('VerifyEmail', '2018-01-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
