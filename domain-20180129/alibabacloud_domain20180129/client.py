# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_domain20180129 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def acknowledge_task_result_with_options(
        self,
        request: main_models.AcknowledgeTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcknowledgeTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_detail_no):
            query['TaskDetailNo'] = request.task_detail_no
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcknowledgeTaskResult',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcknowledgeTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def acknowledge_task_result_with_options_async(
        self,
        request: main_models.AcknowledgeTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcknowledgeTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_detail_no):
            query['TaskDetailNo'] = request.task_detail_no
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcknowledgeTaskResult',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcknowledgeTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def acknowledge_task_result(
        self,
        request: main_models.AcknowledgeTaskResultRequest,
    ) -> main_models.AcknowledgeTaskResultResponse:
        runtime = RuntimeOptions()
        return self.acknowledge_task_result_with_options(request, runtime)

    async def acknowledge_task_result_async(
        self,
        request: main_models.AcknowledgeTaskResultRequest,
    ) -> main_models.AcknowledgeTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.acknowledge_task_result_with_options_async(request, runtime)

    def batch_fuzzy_match_domain_sensitive_word_with_options(
        self,
        request: main_models.BatchFuzzyMatchDomainSensitiveWordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchFuzzyMatchDomainSensitiveWord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchFuzzyMatchDomainSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_fuzzy_match_domain_sensitive_word_with_options_async(
        self,
        request: main_models.BatchFuzzyMatchDomainSensitiveWordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchFuzzyMatchDomainSensitiveWord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchFuzzyMatchDomainSensitiveWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_fuzzy_match_domain_sensitive_word(
        self,
        request: main_models.BatchFuzzyMatchDomainSensitiveWordRequest,
    ) -> main_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        runtime = RuntimeOptions()
        return self.batch_fuzzy_match_domain_sensitive_word_with_options(request, runtime)

    async def batch_fuzzy_match_domain_sensitive_word_async(
        self,
        request: main_models.BatchFuzzyMatchDomainSensitiveWordRequest,
    ) -> main_models.BatchFuzzyMatchDomainSensitiveWordResponse:
        runtime = RuntimeOptions()
        return await self.batch_fuzzy_match_domain_sensitive_word_with_options_async(request, runtime)

    def cancel_domain_verification_with_options(
        self,
        request: main_models.CancelDomainVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDomainVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDomainVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDomainVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_domain_verification_with_options_async(
        self,
        request: main_models.CancelDomainVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDomainVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDomainVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDomainVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_domain_verification(
        self,
        request: main_models.CancelDomainVerificationRequest,
    ) -> main_models.CancelDomainVerificationResponse:
        runtime = RuntimeOptions()
        return self.cancel_domain_verification_with_options(request, runtime)

    async def cancel_domain_verification_async(
        self,
        request: main_models.CancelDomainVerificationRequest,
    ) -> main_models.CancelDomainVerificationResponse:
        runtime = RuntimeOptions()
        return await self.cancel_domain_verification_with_options_async(request, runtime)

    def cancel_operation_audit_with_options(
        self,
        request: main_models.CancelOperationAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelOperationAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelOperationAudit',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOperationAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_operation_audit_with_options_async(
        self,
        request: main_models.CancelOperationAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelOperationAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelOperationAudit',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOperationAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_operation_audit(
        self,
        request: main_models.CancelOperationAuditRequest,
    ) -> main_models.CancelOperationAuditResponse:
        runtime = RuntimeOptions()
        return self.cancel_operation_audit_with_options(request, runtime)

    async def cancel_operation_audit_async(
        self,
        request: main_models.CancelOperationAuditRequest,
    ) -> main_models.CancelOperationAuditResponse:
        runtime = RuntimeOptions()
        return await self.cancel_operation_audit_with_options_async(request, runtime)

    def cancel_qualification_verification_with_options(
        self,
        request: main_models.CancelQualificationVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelQualificationVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelQualificationVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelQualificationVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_qualification_verification_with_options_async(
        self,
        request: main_models.CancelQualificationVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelQualificationVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelQualificationVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelQualificationVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_qualification_verification(
        self,
        request: main_models.CancelQualificationVerificationRequest,
    ) -> main_models.CancelQualificationVerificationResponse:
        runtime = RuntimeOptions()
        return self.cancel_qualification_verification_with_options(request, runtime)

    async def cancel_qualification_verification_async(
        self,
        request: main_models.CancelQualificationVerificationRequest,
    ) -> main_models.CancelQualificationVerificationResponse:
        runtime = RuntimeOptions()
        return await self.cancel_qualification_verification_with_options_async(request, runtime)

    def cancel_task_with_options(
        self,
        request: main_models.CancelTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_no):
            query['TaskNo'] = request.task_no
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        request: main_models.CancelTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_no):
            query['TaskNo'] = request.task_no
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        request: main_models.CancelTaskRequest,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    async def cancel_task_async(
        self,
        request: main_models.CancelTaskRequest,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_task_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_domain_with_options(
        self,
        request: main_models.CheckDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.fee_command):
            query['FeeCommand'] = request.fee_command
        if not DaraCore.is_null(request.fee_currency):
            query['FeeCurrency'] = request.fee_currency
        if not DaraCore.is_null(request.fee_period):
            query['FeePeriod'] = request.fee_period
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDomain',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_with_options_async(
        self,
        request: main_models.CheckDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.fee_command):
            query['FeeCommand'] = request.fee_command
        if not DaraCore.is_null(request.fee_currency):
            query['FeeCurrency'] = request.fee_currency
        if not DaraCore.is_null(request.fee_period):
            query['FeePeriod'] = request.fee_period
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDomain',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain(
        self,
        request: main_models.CheckDomainRequest,
    ) -> main_models.CheckDomainResponse:
        runtime = RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    async def check_domain_async(
        self,
        request: main_models.CheckDomainRequest,
    ) -> main_models.CheckDomainResponse:
        runtime = RuntimeOptions()
        return await self.check_domain_with_options_async(request, runtime)

    def check_domain_sunrise_claim_with_options(
        self,
        request: main_models.CheckDomainSunriseClaimRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDomainSunriseClaimResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDomainSunriseClaim',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDomainSunriseClaimResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_sunrise_claim_with_options_async(
        self,
        request: main_models.CheckDomainSunriseClaimRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDomainSunriseClaimResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDomainSunriseClaim',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDomainSunriseClaimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain_sunrise_claim(
        self,
        request: main_models.CheckDomainSunriseClaimRequest,
    ) -> main_models.CheckDomainSunriseClaimResponse:
        runtime = RuntimeOptions()
        return self.check_domain_sunrise_claim_with_options(request, runtime)

    async def check_domain_sunrise_claim_async(
        self,
        request: main_models.CheckDomainSunriseClaimRequest,
    ) -> main_models.CheckDomainSunriseClaimResponse:
        runtime = RuntimeOptions()
        return await self.check_domain_sunrise_claim_with_options_async(request, runtime)

    def check_intl_fix_price_domain_status_with_options(
        self,
        request: main_models.CheckIntlFixPriceDomainStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckIntlFixPriceDomainStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckIntlFixPriceDomainStatus',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckIntlFixPriceDomainStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_intl_fix_price_domain_status_with_options_async(
        self,
        request: main_models.CheckIntlFixPriceDomainStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckIntlFixPriceDomainStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckIntlFixPriceDomainStatus',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckIntlFixPriceDomainStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_intl_fix_price_domain_status(
        self,
        request: main_models.CheckIntlFixPriceDomainStatusRequest,
    ) -> main_models.CheckIntlFixPriceDomainStatusResponse:
        runtime = RuntimeOptions()
        return self.check_intl_fix_price_domain_status_with_options(request, runtime)

    async def check_intl_fix_price_domain_status_async(
        self,
        request: main_models.CheckIntlFixPriceDomainStatusRequest,
    ) -> main_models.CheckIntlFixPriceDomainStatusResponse:
        runtime = RuntimeOptions()
        return await self.check_intl_fix_price_domain_status_with_options_async(request, runtime)

    def check_max_year_of_server_lock_with_options(
        self,
        request: main_models.CheckMaxYearOfServerLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckMaxYearOfServerLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_action):
            query['CheckAction'] = request.check_action
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckMaxYearOfServerLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckMaxYearOfServerLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_max_year_of_server_lock_with_options_async(
        self,
        request: main_models.CheckMaxYearOfServerLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckMaxYearOfServerLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_action):
            query['CheckAction'] = request.check_action
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckMaxYearOfServerLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckMaxYearOfServerLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_max_year_of_server_lock(
        self,
        request: main_models.CheckMaxYearOfServerLockRequest,
    ) -> main_models.CheckMaxYearOfServerLockResponse:
        runtime = RuntimeOptions()
        return self.check_max_year_of_server_lock_with_options(request, runtime)

    async def check_max_year_of_server_lock_async(
        self,
        request: main_models.CheckMaxYearOfServerLockRequest,
    ) -> main_models.CheckMaxYearOfServerLockResponse:
        runtime = RuntimeOptions()
        return await self.check_max_year_of_server_lock_with_options_async(request, runtime)

    def check_processing_server_lock_apply_with_options(
        self,
        request: main_models.CheckProcessingServerLockApplyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckProcessingServerLockApplyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.fee_period):
            query['FeePeriod'] = request.fee_period
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckProcessingServerLockApply',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckProcessingServerLockApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_processing_server_lock_apply_with_options_async(
        self,
        request: main_models.CheckProcessingServerLockApplyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckProcessingServerLockApplyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.fee_period):
            query['FeePeriod'] = request.fee_period
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckProcessingServerLockApply',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckProcessingServerLockApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_processing_server_lock_apply(
        self,
        request: main_models.CheckProcessingServerLockApplyRequest,
    ) -> main_models.CheckProcessingServerLockApplyResponse:
        runtime = RuntimeOptions()
        return self.check_processing_server_lock_apply_with_options(request, runtime)

    async def check_processing_server_lock_apply_async(
        self,
        request: main_models.CheckProcessingServerLockApplyRequest,
    ) -> main_models.CheckProcessingServerLockApplyResponse:
        runtime = RuntimeOptions()
        return await self.check_processing_server_lock_apply_with_options_async(request, runtime)

    def check_transfer_in_feasibility_with_options(
        self,
        request: main_models.CheckTransferInFeasibilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckTransferInFeasibilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.transfer_authorization_code):
            query['TransferAuthorizationCode'] = request.transfer_authorization_code
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckTransferInFeasibility',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckTransferInFeasibilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_transfer_in_feasibility_with_options_async(
        self,
        request: main_models.CheckTransferInFeasibilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckTransferInFeasibilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.transfer_authorization_code):
            query['TransferAuthorizationCode'] = request.transfer_authorization_code
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckTransferInFeasibility',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckTransferInFeasibilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_transfer_in_feasibility(
        self,
        request: main_models.CheckTransferInFeasibilityRequest,
    ) -> main_models.CheckTransferInFeasibilityResponse:
        runtime = RuntimeOptions()
        return self.check_transfer_in_feasibility_with_options(request, runtime)

    async def check_transfer_in_feasibility_async(
        self,
        request: main_models.CheckTransferInFeasibilityRequest,
    ) -> main_models.CheckTransferInFeasibilityResponse:
        runtime = RuntimeOptions()
        return await self.check_transfer_in_feasibility_with_options_async(request, runtime)

    def confirm_transfer_in_email_with_options(
        self,
        request: main_models.ConfirmTransferInEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmTransferInEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmTransferInEmail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmTransferInEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_transfer_in_email_with_options_async(
        self,
        request: main_models.ConfirmTransferInEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmTransferInEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmTransferInEmail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmTransferInEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_transfer_in_email(
        self,
        request: main_models.ConfirmTransferInEmailRequest,
    ) -> main_models.ConfirmTransferInEmailResponse:
        runtime = RuntimeOptions()
        return self.confirm_transfer_in_email_with_options(request, runtime)

    async def confirm_transfer_in_email_async(
        self,
        request: main_models.ConfirmTransferInEmailRequest,
    ) -> main_models.ConfirmTransferInEmailResponse:
        runtime = RuntimeOptions()
        return await self.confirm_transfer_in_email_with_options_async(request, runtime)

    def create_intl_fixed_price_domain_order_with_options(
        self,
        request: main_models.CreateIntlFixedPriceDomainOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntlFixedPriceDomainOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.expected_price):
            query['ExpectedPrice'] = request.expected_price
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntlFixedPriceDomainOrder',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntlFixedPriceDomainOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_intl_fixed_price_domain_order_with_options_async(
        self,
        request: main_models.CreateIntlFixedPriceDomainOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntlFixedPriceDomainOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.expected_price):
            query['ExpectedPrice'] = request.expected_price
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntlFixedPriceDomainOrder',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntlFixedPriceDomainOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_intl_fixed_price_domain_order(
        self,
        request: main_models.CreateIntlFixedPriceDomainOrderRequest,
    ) -> main_models.CreateIntlFixedPriceDomainOrderResponse:
        runtime = RuntimeOptions()
        return self.create_intl_fixed_price_domain_order_with_options(request, runtime)

    async def create_intl_fixed_price_domain_order_async(
        self,
        request: main_models.CreateIntlFixedPriceDomainOrderRequest,
    ) -> main_models.CreateIntlFixedPriceDomainOrderResponse:
        runtime = RuntimeOptions()
        return await self.create_intl_fixed_price_domain_order_with_options_async(request, runtime)

    def delete_contact_templates_with_options(
        self,
        request: main_models.DeleteContactTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.registrant_profile_ids):
            query['RegistrantProfileIds'] = request.registrant_profile_ids
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactTemplates',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_templates_with_options_async(
        self,
        request: main_models.DeleteContactTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.registrant_profile_ids):
            query['RegistrantProfileIds'] = request.registrant_profile_ids
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactTemplates',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_templates(
        self,
        request: main_models.DeleteContactTemplatesRequest,
    ) -> main_models.DeleteContactTemplatesResponse:
        runtime = RuntimeOptions()
        return self.delete_contact_templates_with_options(request, runtime)

    async def delete_contact_templates_async(
        self,
        request: main_models.DeleteContactTemplatesRequest,
    ) -> main_models.DeleteContactTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.delete_contact_templates_with_options_async(request, runtime)

    def delete_domain_group_with_options(
        self,
        request: main_models.DeleteDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainGroup',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_group_with_options_async(
        self,
        request: main_models.DeleteDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainGroup',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_group(
        self,
        request: main_models.DeleteDomainGroupRequest,
    ) -> main_models.DeleteDomainGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_group_with_options(request, runtime)

    async def delete_domain_group_async(
        self,
        request: main_models.DeleteDomainGroupRequest,
    ) -> main_models.DeleteDomainGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_group_with_options_async(request, runtime)

    def delete_email_verification_with_options(
        self,
        request: main_models.DeleteEmailVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEmailVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEmailVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_email_verification_with_options_async(
        self,
        request: main_models.DeleteEmailVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEmailVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEmailVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_email_verification(
        self,
        request: main_models.DeleteEmailVerificationRequest,
    ) -> main_models.DeleteEmailVerificationResponse:
        runtime = RuntimeOptions()
        return self.delete_email_verification_with_options(request, runtime)

    async def delete_email_verification_async(
        self,
        request: main_models.DeleteEmailVerificationRequest,
    ) -> main_models.DeleteEmailVerificationResponse:
        runtime = RuntimeOptions()
        return await self.delete_email_verification_with_options_async(request, runtime)

    def delete_registrant_profile_with_options(
        self,
        request: main_models.DeleteRegistrantProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegistrantProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegistrantProfile',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegistrantProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_registrant_profile_with_options_async(
        self,
        request: main_models.DeleteRegistrantProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegistrantProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegistrantProfile',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegistrantProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_registrant_profile(
        self,
        request: main_models.DeleteRegistrantProfileRequest,
    ) -> main_models.DeleteRegistrantProfileResponse:
        runtime = RuntimeOptions()
        return self.delete_registrant_profile_with_options(request, runtime)

    async def delete_registrant_profile_async(
        self,
        request: main_models.DeleteRegistrantProfileRequest,
    ) -> main_models.DeleteRegistrantProfileResponse:
        runtime = RuntimeOptions()
        return await self.delete_registrant_profile_with_options_async(request, runtime)

    def domain_special_biz_cancel_with_options(
        self,
        request: main_models.DomainSpecialBizCancelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DomainSpecialBizCancelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DomainSpecialBizCancel',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DomainSpecialBizCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def domain_special_biz_cancel_with_options_async(
        self,
        request: main_models.DomainSpecialBizCancelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DomainSpecialBizCancelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DomainSpecialBizCancel',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DomainSpecialBizCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def domain_special_biz_cancel(
        self,
        request: main_models.DomainSpecialBizCancelRequest,
    ) -> main_models.DomainSpecialBizCancelResponse:
        runtime = RuntimeOptions()
        return self.domain_special_biz_cancel_with_options(request, runtime)

    async def domain_special_biz_cancel_async(
        self,
        request: main_models.DomainSpecialBizCancelRequest,
    ) -> main_models.DomainSpecialBizCancelResponse:
        runtime = RuntimeOptions()
        return await self.domain_special_biz_cancel_with_options_async(request, runtime)

    def email_verified_with_options(
        self,
        request: main_models.EmailVerifiedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EmailVerifiedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EmailVerified',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EmailVerifiedResponse(),
            self.call_api(params, req, runtime)
        )

    async def email_verified_with_options_async(
        self,
        request: main_models.EmailVerifiedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EmailVerifiedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EmailVerified',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EmailVerifiedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def email_verified(
        self,
        request: main_models.EmailVerifiedRequest,
    ) -> main_models.EmailVerifiedResponse:
        runtime = RuntimeOptions()
        return self.email_verified_with_options(request, runtime)

    async def email_verified_async(
        self,
        request: main_models.EmailVerifiedRequest,
    ) -> main_models.EmailVerifiedResponse:
        runtime = RuntimeOptions()
        return await self.email_verified_with_options_async(request, runtime)

    def fuzzy_match_domain_sensitive_word_with_options(
        self,
        request: main_models.FuzzyMatchDomainSensitiveWordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FuzzyMatchDomainSensitiveWordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FuzzyMatchDomainSensitiveWord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FuzzyMatchDomainSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def fuzzy_match_domain_sensitive_word_with_options_async(
        self,
        request: main_models.FuzzyMatchDomainSensitiveWordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FuzzyMatchDomainSensitiveWordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FuzzyMatchDomainSensitiveWord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FuzzyMatchDomainSensitiveWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fuzzy_match_domain_sensitive_word(
        self,
        request: main_models.FuzzyMatchDomainSensitiveWordRequest,
    ) -> main_models.FuzzyMatchDomainSensitiveWordResponse:
        runtime = RuntimeOptions()
        return self.fuzzy_match_domain_sensitive_word_with_options(request, runtime)

    async def fuzzy_match_domain_sensitive_word_async(
        self,
        request: main_models.FuzzyMatchDomainSensitiveWordRequest,
    ) -> main_models.FuzzyMatchDomainSensitiveWordResponse:
        runtime = RuntimeOptions()
        return await self.fuzzy_match_domain_sensitive_word_with_options_async(request, runtime)

    def get_intl_fix_price_domain_list_url_with_options(
        self,
        request: main_models.GetIntlFixPriceDomainListUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntlFixPriceDomainListUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.list_date):
            query['ListDate'] = request.list_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIntlFixPriceDomainListUrl',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntlFixPriceDomainListUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intl_fix_price_domain_list_url_with_options_async(
        self,
        request: main_models.GetIntlFixPriceDomainListUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntlFixPriceDomainListUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.list_date):
            query['ListDate'] = request.list_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIntlFixPriceDomainListUrl',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntlFixPriceDomainListUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intl_fix_price_domain_list_url(
        self,
        request: main_models.GetIntlFixPriceDomainListUrlRequest,
    ) -> main_models.GetIntlFixPriceDomainListUrlResponse:
        runtime = RuntimeOptions()
        return self.get_intl_fix_price_domain_list_url_with_options(request, runtime)

    async def get_intl_fix_price_domain_list_url_async(
        self,
        request: main_models.GetIntlFixPriceDomainListUrlRequest,
    ) -> main_models.GetIntlFixPriceDomainListUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_intl_fix_price_domain_list_url_with_options_async(request, runtime)

    def get_operation_oss_upload_policy_with_options(
        self,
        request: main_models.GetOperationOssUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOperationOssUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_type):
            query['AuditType'] = request.audit_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOperationOssUploadPolicy',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOperationOssUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_operation_oss_upload_policy_with_options_async(
        self,
        request: main_models.GetOperationOssUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOperationOssUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_type):
            query['AuditType'] = request.audit_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOperationOssUploadPolicy',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOperationOssUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_operation_oss_upload_policy(
        self,
        request: main_models.GetOperationOssUploadPolicyRequest,
    ) -> main_models.GetOperationOssUploadPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_operation_oss_upload_policy_with_options(request, runtime)

    async def get_operation_oss_upload_policy_async(
        self,
        request: main_models.GetOperationOssUploadPolicyRequest,
    ) -> main_models.GetOperationOssUploadPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_operation_oss_upload_policy_with_options_async(request, runtime)

    def get_qualification_upload_policy_with_options(
        self,
        request: main_models.GetQualificationUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualificationUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualificationUploadPolicy',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualificationUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qualification_upload_policy_with_options_async(
        self,
        request: main_models.GetQualificationUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualificationUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualificationUploadPolicy',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualificationUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qualification_upload_policy(
        self,
        request: main_models.GetQualificationUploadPolicyRequest,
    ) -> main_models.GetQualificationUploadPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_qualification_upload_policy_with_options(request, runtime)

    async def get_qualification_upload_policy_async(
        self,
        request: main_models.GetQualificationUploadPolicyRequest,
    ) -> main_models.GetQualificationUploadPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_qualification_upload_policy_with_options_async(request, runtime)

    def list_email_verification_with_options(
        self,
        request: main_models.ListEmailVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEmailVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.verification_status):
            query['VerificationStatus'] = request.verification_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEmailVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_email_verification_with_options_async(
        self,
        request: main_models.ListEmailVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEmailVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.verification_status):
            query['VerificationStatus'] = request.verification_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEmailVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_email_verification(
        self,
        request: main_models.ListEmailVerificationRequest,
    ) -> main_models.ListEmailVerificationResponse:
        runtime = RuntimeOptions()
        return self.list_email_verification_with_options(request, runtime)

    async def list_email_verification_async(
        self,
        request: main_models.ListEmailVerificationRequest,
    ) -> main_models.ListEmailVerificationResponse:
        runtime = RuntimeOptions()
        return await self.list_email_verification_with_options_async(request, runtime)

    def list_server_lock_with_options(
        self,
        request: main_models.ListServerLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServerLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_start_date):
            query['BeginStartDate'] = request.begin_start_date
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_expire_date):
            query['EndExpireDate'] = request.end_expire_date
        if not DaraCore.is_null(request.end_start_date):
            query['EndStartDate'] = request.end_start_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lock_product_id):
            query['LockProductId'] = request.lock_product_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.server_lock_status):
            query['ServerLockStatus'] = request.server_lock_status
        if not DaraCore.is_null(request.start_expire_date):
            query['StartExpireDate'] = request.start_expire_date
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServerLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServerLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_lock_with_options_async(
        self,
        request: main_models.ListServerLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServerLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_start_date):
            query['BeginStartDate'] = request.begin_start_date
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_expire_date):
            query['EndExpireDate'] = request.end_expire_date
        if not DaraCore.is_null(request.end_start_date):
            query['EndStartDate'] = request.end_start_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lock_product_id):
            query['LockProductId'] = request.lock_product_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.server_lock_status):
            query['ServerLockStatus'] = request.server_lock_status
        if not DaraCore.is_null(request.start_expire_date):
            query['StartExpireDate'] = request.start_expire_date
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServerLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServerLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_lock(
        self,
        request: main_models.ListServerLockRequest,
    ) -> main_models.ListServerLockResponse:
        runtime = RuntimeOptions()
        return self.list_server_lock_with_options(request, runtime)

    async def list_server_lock_async(
        self,
        request: main_models.ListServerLockRequest,
    ) -> main_models.ListServerLockResponse:
        runtime = RuntimeOptions()
        return await self.list_server_lock_with_options_async(request, runtime)

    def lookup_tmch_notice_with_options(
        self,
        request: main_models.LookupTmchNoticeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LookupTmchNoticeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.claim_key):
            query['ClaimKey'] = request.claim_key
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LookupTmchNotice',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LookupTmchNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def lookup_tmch_notice_with_options_async(
        self,
        request: main_models.LookupTmchNoticeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LookupTmchNoticeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.claim_key):
            query['ClaimKey'] = request.claim_key
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LookupTmchNotice',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LookupTmchNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lookup_tmch_notice(
        self,
        request: main_models.LookupTmchNoticeRequest,
    ) -> main_models.LookupTmchNoticeResponse:
        runtime = RuntimeOptions()
        return self.lookup_tmch_notice_with_options(request, runtime)

    async def lookup_tmch_notice_async(
        self,
        request: main_models.LookupTmchNoticeRequest,
    ) -> main_models.LookupTmchNoticeResponse:
        runtime = RuntimeOptions()
        return await self.lookup_tmch_notice_with_options_async(request, runtime)

    def poll_task_result_with_options(
        self,
        request: main_models.PollTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PollTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_no):
            query['TaskNo'] = request.task_no
        if not DaraCore.is_null(request.task_result_status):
            query['TaskResultStatus'] = request.task_result_status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PollTaskResult',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PollTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def poll_task_result_with_options_async(
        self,
        request: main_models.PollTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PollTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_no):
            query['TaskNo'] = request.task_no
        if not DaraCore.is_null(request.task_result_status):
            query['TaskResultStatus'] = request.task_result_status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PollTaskResult',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PollTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poll_task_result(
        self,
        request: main_models.PollTaskResultRequest,
    ) -> main_models.PollTaskResultResponse:
        runtime = RuntimeOptions()
        return self.poll_task_result_with_options(request, runtime)

    async def poll_task_result_async(
        self,
        request: main_models.PollTaskResultRequest,
    ) -> main_models.PollTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.poll_task_result_with_options_async(request, runtime)

    def query_advanced_domain_list_with_options(
        self,
        request: main_models.QueryAdvancedDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAdvancedDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.domain_name_sort):
            query['DomainNameSort'] = request.domain_name_sort
        if not DaraCore.is_null(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not DaraCore.is_null(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not DaraCore.is_null(request.end_length):
            query['EndLength'] = request.end_length
        if not DaraCore.is_null(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not DaraCore.is_null(request.excluded):
            query['Excluded'] = request.excluded
        if not DaraCore.is_null(request.excluded_prefix):
            query['ExcludedPrefix'] = request.excluded_prefix
        if not DaraCore.is_null(request.excluded_suffix):
            query['ExcludedSuffix'] = request.excluded_suffix
        if not DaraCore.is_null(request.expiration_date_sort):
            query['ExpirationDateSort'] = request.expiration_date_sort
        if not DaraCore.is_null(request.form):
            query['Form'] = request.form
        if not DaraCore.is_null(request.is_premium_domain):
            query['IsPremiumDomain'] = request.is_premium_domain
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.key_word_prefix):
            query['KeyWordPrefix'] = request.key_word_prefix
        if not DaraCore.is_null(request.key_word_suffix):
            query['KeyWordSuffix'] = request.key_word_suffix
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not DaraCore.is_null(request.product_domain_type_sort):
            query['ProductDomainTypeSort'] = request.product_domain_type_sort
        if not DaraCore.is_null(request.registration_date_sort):
            query['RegistrationDateSort'] = request.registration_date_sort
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not DaraCore.is_null(request.start_length):
            query['StartLength'] = request.start_length
        if not DaraCore.is_null(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not DaraCore.is_null(request.suffixs):
            query['Suffixs'] = request.suffixs
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.trade_type):
            query['TradeType'] = request.trade_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAdvancedDomainList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAdvancedDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_advanced_domain_list_with_options_async(
        self,
        request: main_models.QueryAdvancedDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAdvancedDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.domain_name_sort):
            query['DomainNameSort'] = request.domain_name_sort
        if not DaraCore.is_null(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not DaraCore.is_null(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not DaraCore.is_null(request.end_length):
            query['EndLength'] = request.end_length
        if not DaraCore.is_null(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not DaraCore.is_null(request.excluded):
            query['Excluded'] = request.excluded
        if not DaraCore.is_null(request.excluded_prefix):
            query['ExcludedPrefix'] = request.excluded_prefix
        if not DaraCore.is_null(request.excluded_suffix):
            query['ExcludedSuffix'] = request.excluded_suffix
        if not DaraCore.is_null(request.expiration_date_sort):
            query['ExpirationDateSort'] = request.expiration_date_sort
        if not DaraCore.is_null(request.form):
            query['Form'] = request.form
        if not DaraCore.is_null(request.is_premium_domain):
            query['IsPremiumDomain'] = request.is_premium_domain
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.key_word_prefix):
            query['KeyWordPrefix'] = request.key_word_prefix
        if not DaraCore.is_null(request.key_word_suffix):
            query['KeyWordSuffix'] = request.key_word_suffix
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not DaraCore.is_null(request.product_domain_type_sort):
            query['ProductDomainTypeSort'] = request.product_domain_type_sort
        if not DaraCore.is_null(request.registration_date_sort):
            query['RegistrationDateSort'] = request.registration_date_sort
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not DaraCore.is_null(request.start_length):
            query['StartLength'] = request.start_length
        if not DaraCore.is_null(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not DaraCore.is_null(request.suffixs):
            query['Suffixs'] = request.suffixs
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.trade_type):
            query['TradeType'] = request.trade_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAdvancedDomainList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAdvancedDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_advanced_domain_list(
        self,
        request: main_models.QueryAdvancedDomainListRequest,
    ) -> main_models.QueryAdvancedDomainListResponse:
        runtime = RuntimeOptions()
        return self.query_advanced_domain_list_with_options(request, runtime)

    async def query_advanced_domain_list_async(
        self,
        request: main_models.QueryAdvancedDomainListRequest,
    ) -> main_models.QueryAdvancedDomainListResponse:
        runtime = RuntimeOptions()
        return await self.query_advanced_domain_list_with_options_async(request, runtime)

    def query_art_extension_with_options(
        self,
        request: main_models.QueryArtExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryArtExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryArtExtension',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryArtExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_art_extension_with_options_async(
        self,
        request: main_models.QueryArtExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryArtExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryArtExtension',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryArtExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_art_extension(
        self,
        request: main_models.QueryArtExtensionRequest,
    ) -> main_models.QueryArtExtensionResponse:
        runtime = RuntimeOptions()
        return self.query_art_extension_with_options(request, runtime)

    async def query_art_extension_async(
        self,
        request: main_models.QueryArtExtensionRequest,
    ) -> main_models.QueryArtExtensionResponse:
        runtime = RuntimeOptions()
        return await self.query_art_extension_with_options_async(request, runtime)

    def query_change_log_list_with_options(
        self,
        request: main_models.QueryChangeLogListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryChangeLogListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryChangeLogList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryChangeLogListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_change_log_list_with_options_async(
        self,
        request: main_models.QueryChangeLogListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryChangeLogListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryChangeLogList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryChangeLogListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_change_log_list(
        self,
        request: main_models.QueryChangeLogListRequest,
    ) -> main_models.QueryChangeLogListResponse:
        runtime = RuntimeOptions()
        return self.query_change_log_list_with_options(request, runtime)

    async def query_change_log_list_async(
        self,
        request: main_models.QueryChangeLogListRequest,
    ) -> main_models.QueryChangeLogListResponse:
        runtime = RuntimeOptions()
        return await self.query_change_log_list_with_options_async(request, runtime)

    def query_contact_info_with_options(
        self,
        request: main_models.QueryContactInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContactInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryContactInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryContactInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_contact_info_with_options_async(
        self,
        request: main_models.QueryContactInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContactInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryContactInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryContactInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_contact_info(
        self,
        request: main_models.QueryContactInfoRequest,
    ) -> main_models.QueryContactInfoResponse:
        runtime = RuntimeOptions()
        return self.query_contact_info_with_options(request, runtime)

    async def query_contact_info_async(
        self,
        request: main_models.QueryContactInfoRequest,
    ) -> main_models.QueryContactInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_contact_info_with_options_async(request, runtime)

    def query_dsrecord_with_options(
        self,
        request: main_models.QueryDSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDSRecord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dsrecord_with_options_async(
        self,
        request: main_models.QueryDSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDSRecord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dsrecord(
        self,
        request: main_models.QueryDSRecordRequest,
    ) -> main_models.QueryDSRecordResponse:
        runtime = RuntimeOptions()
        return self.query_dsrecord_with_options(request, runtime)

    async def query_dsrecord_async(
        self,
        request: main_models.QueryDSRecordRequest,
    ) -> main_models.QueryDSRecordResponse:
        runtime = RuntimeOptions()
        return await self.query_dsrecord_with_options_async(request, runtime)

    def query_dns_host_with_options(
        self,
        request: main_models.QueryDnsHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDnsHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDnsHost',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dns_host_with_options_async(
        self,
        request: main_models.QueryDnsHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDnsHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDnsHost',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dns_host(
        self,
        request: main_models.QueryDnsHostRequest,
    ) -> main_models.QueryDnsHostResponse:
        runtime = RuntimeOptions()
        return self.query_dns_host_with_options(request, runtime)

    async def query_dns_host_async(
        self,
        request: main_models.QueryDnsHostRequest,
    ) -> main_models.QueryDnsHostResponse:
        runtime = RuntimeOptions()
        return await self.query_dns_host_with_options_async(request, runtime)

    def query_domain_admin_division_with_options(
        self,
        request: main_models.QueryDomainAdminDivisionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainAdminDivisionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainAdminDivision',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainAdminDivisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_admin_division_with_options_async(
        self,
        request: main_models.QueryDomainAdminDivisionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainAdminDivisionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainAdminDivision',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainAdminDivisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_admin_division(
        self,
        request: main_models.QueryDomainAdminDivisionRequest,
    ) -> main_models.QueryDomainAdminDivisionResponse:
        runtime = RuntimeOptions()
        return self.query_domain_admin_division_with_options(request, runtime)

    async def query_domain_admin_division_async(
        self,
        request: main_models.QueryDomainAdminDivisionRequest,
    ) -> main_models.QueryDomainAdminDivisionResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_admin_division_with_options_async(request, runtime)

    def query_domain_by_domain_name_with_options(
        self,
        request: main_models.QueryDomainByDomainNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainByDomainNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainByDomainName',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainByDomainNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_by_domain_name_with_options_async(
        self,
        request: main_models.QueryDomainByDomainNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainByDomainNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainByDomainName',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainByDomainNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_by_domain_name(
        self,
        request: main_models.QueryDomainByDomainNameRequest,
    ) -> main_models.QueryDomainByDomainNameResponse:
        runtime = RuntimeOptions()
        return self.query_domain_by_domain_name_with_options(request, runtime)

    async def query_domain_by_domain_name_async(
        self,
        request: main_models.QueryDomainByDomainNameRequest,
    ) -> main_models.QueryDomainByDomainNameResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_by_domain_name_with_options_async(request, runtime)

    def query_domain_by_instance_id_with_options(
        self,
        request: main_models.QueryDomainByInstanceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainByInstanceId',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_by_instance_id_with_options_async(
        self,
        request: main_models.QueryDomainByInstanceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainByInstanceId',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_by_instance_id(
        self,
        request: main_models.QueryDomainByInstanceIdRequest,
    ) -> main_models.QueryDomainByInstanceIdResponse:
        runtime = RuntimeOptions()
        return self.query_domain_by_instance_id_with_options(request, runtime)

    async def query_domain_by_instance_id_async(
        self,
        request: main_models.QueryDomainByInstanceIdRequest,
    ) -> main_models.QueryDomainByInstanceIdResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_by_instance_id_with_options_async(request, runtime)

    def query_domain_group_list_with_options(
        self,
        request: main_models.QueryDomainGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainGroupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_group_name):
            query['DomainGroupName'] = request.domain_group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not DaraCore.is_null(request.order_key_type):
            query['OrderKeyType'] = request.order_key_type
        if not DaraCore.is_null(request.show_deleting_group):
            query['ShowDeletingGroup'] = request.show_deleting_group
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainGroupList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_group_list_with_options_async(
        self,
        request: main_models.QueryDomainGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainGroupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_group_name):
            query['DomainGroupName'] = request.domain_group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not DaraCore.is_null(request.order_key_type):
            query['OrderKeyType'] = request.order_key_type
        if not DaraCore.is_null(request.show_deleting_group):
            query['ShowDeletingGroup'] = request.show_deleting_group
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainGroupList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_group_list(
        self,
        request: main_models.QueryDomainGroupListRequest,
    ) -> main_models.QueryDomainGroupListResponse:
        runtime = RuntimeOptions()
        return self.query_domain_group_list_with_options(request, runtime)

    async def query_domain_group_list_async(
        self,
        request: main_models.QueryDomainGroupListRequest,
    ) -> main_models.QueryDomainGroupListResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_group_list_with_options_async(request, runtime)

    def query_domain_list_with_options(
        self,
        request: main_models.QueryDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccompany):
            query['Ccompany'] = request.ccompany
        if not DaraCore.is_null(request.dns):
            query['Dns'] = request.dns
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not DaraCore.is_null(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not DaraCore.is_null(request.order_key_type):
            query['OrderKeyType'] = request.order_key_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.registrar):
            query['Registrar'] = request.registrar
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not DaraCore.is_null(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_list_with_options_async(
        self,
        request: main_models.QueryDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccompany):
            query['Ccompany'] = request.ccompany
        if not DaraCore.is_null(request.dns):
            query['Dns'] = request.dns
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not DaraCore.is_null(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not DaraCore.is_null(request.order_key_type):
            query['OrderKeyType'] = request.order_key_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.registrar):
            query['Registrar'] = request.registrar
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not DaraCore.is_null(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_list(
        self,
        request: main_models.QueryDomainListRequest,
    ) -> main_models.QueryDomainListResponse:
        runtime = RuntimeOptions()
        return self.query_domain_list_with_options(request, runtime)

    async def query_domain_list_async(
        self,
        request: main_models.QueryDomainListRequest,
    ) -> main_models.QueryDomainListResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_list_with_options_async(request, runtime)

    def query_domain_real_name_verification_info_with_options(
        self,
        request: main_models.QueryDomainRealNameVerificationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainRealNameVerificationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.fetch_image):
            query['FetchImage'] = request.fetch_image
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainRealNameVerificationInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainRealNameVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_real_name_verification_info_with_options_async(
        self,
        request: main_models.QueryDomainRealNameVerificationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainRealNameVerificationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.fetch_image):
            query['FetchImage'] = request.fetch_image
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainRealNameVerificationInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainRealNameVerificationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_real_name_verification_info(
        self,
        request: main_models.QueryDomainRealNameVerificationInfoRequest,
    ) -> main_models.QueryDomainRealNameVerificationInfoResponse:
        runtime = RuntimeOptions()
        return self.query_domain_real_name_verification_info_with_options(request, runtime)

    async def query_domain_real_name_verification_info_async(
        self,
        request: main_models.QueryDomainRealNameVerificationInfoRequest,
    ) -> main_models.QueryDomainRealNameVerificationInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_real_name_verification_info_with_options_async(request, runtime)

    def query_domain_real_time_price_with_options(
        self,
        tmp_req: main_models.QueryDomainRealTimePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainRealTimePriceResponse:
        tmp_req.validate()
        request = main_models.QueryDomainRealTimePriceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.domain_item):
            request.domain_item_shrink = Utils.array_to_string_with_specified_style(tmp_req.domain_item, 'DomainItem', 'json')
        query = {}
        if not DaraCore.is_null(request.currency):
            query['Currency'] = request.currency
        if not DaraCore.is_null(request.domain_item_shrink):
            query['DomainItem'] = request.domain_item_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainRealTimePrice',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainRealTimePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_real_time_price_with_options_async(
        self,
        tmp_req: main_models.QueryDomainRealTimePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainRealTimePriceResponse:
        tmp_req.validate()
        request = main_models.QueryDomainRealTimePriceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.domain_item):
            request.domain_item_shrink = Utils.array_to_string_with_specified_style(tmp_req.domain_item, 'DomainItem', 'json')
        query = {}
        if not DaraCore.is_null(request.currency):
            query['Currency'] = request.currency
        if not DaraCore.is_null(request.domain_item_shrink):
            query['DomainItem'] = request.domain_item_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainRealTimePrice',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainRealTimePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_real_time_price(
        self,
        request: main_models.QueryDomainRealTimePriceRequest,
    ) -> main_models.QueryDomainRealTimePriceResponse:
        runtime = RuntimeOptions()
        return self.query_domain_real_time_price_with_options(request, runtime)

    async def query_domain_real_time_price_async(
        self,
        request: main_models.QueryDomainRealTimePriceRequest,
    ) -> main_models.QueryDomainRealTimePriceResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_real_time_price_with_options_async(request, runtime)

    def query_domain_special_biz_detail_with_options(
        self,
        request: main_models.QueryDomainSpecialBizDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainSpecialBizDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainSpecialBizDetail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainSpecialBizDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_special_biz_detail_with_options_async(
        self,
        request: main_models.QueryDomainSpecialBizDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainSpecialBizDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainSpecialBizDetail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainSpecialBizDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_special_biz_detail(
        self,
        request: main_models.QueryDomainSpecialBizDetailRequest,
    ) -> main_models.QueryDomainSpecialBizDetailResponse:
        runtime = RuntimeOptions()
        return self.query_domain_special_biz_detail_with_options(request, runtime)

    async def query_domain_special_biz_detail_async(
        self,
        request: main_models.QueryDomainSpecialBizDetailRequest,
    ) -> main_models.QueryDomainSpecialBizDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_special_biz_detail_with_options_async(request, runtime)

    def query_domain_special_biz_info_by_domain_with_options(
        self,
        request: main_models.QueryDomainSpecialBizInfoByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainSpecialBizInfoByDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainSpecialBizInfoByDomain',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainSpecialBizInfoByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_special_biz_info_by_domain_with_options_async(
        self,
        request: main_models.QueryDomainSpecialBizInfoByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainSpecialBizInfoByDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainSpecialBizInfoByDomain',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainSpecialBizInfoByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_special_biz_info_by_domain(
        self,
        request: main_models.QueryDomainSpecialBizInfoByDomainRequest,
    ) -> main_models.QueryDomainSpecialBizInfoByDomainResponse:
        runtime = RuntimeOptions()
        return self.query_domain_special_biz_info_by_domain_with_options(request, runtime)

    async def query_domain_special_biz_info_by_domain_async(
        self,
        request: main_models.QueryDomainSpecialBizInfoByDomainRequest,
    ) -> main_models.QueryDomainSpecialBizInfoByDomainResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_special_biz_info_by_domain_with_options_async(request, runtime)

    def query_domain_suffix_with_options(
        self,
        request: main_models.QueryDomainSuffixRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainSuffixResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainSuffix',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainSuffixResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_suffix_with_options_async(
        self,
        request: main_models.QueryDomainSuffixRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainSuffixResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainSuffix',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainSuffixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_suffix(
        self,
        request: main_models.QueryDomainSuffixRequest,
    ) -> main_models.QueryDomainSuffixResponse:
        runtime = RuntimeOptions()
        return self.query_domain_suffix_with_options(request, runtime)

    async def query_domain_suffix_async(
        self,
        request: main_models.QueryDomainSuffixRequest,
    ) -> main_models.QueryDomainSuffixResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_suffix_with_options_async(request, runtime)

    def query_email_verification_with_options(
        self,
        request: main_models.QueryEmailVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEmailVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEmailVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_email_verification_with_options_async(
        self,
        request: main_models.QueryEmailVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEmailVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEmailVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_email_verification(
        self,
        request: main_models.QueryEmailVerificationRequest,
    ) -> main_models.QueryEmailVerificationResponse:
        runtime = RuntimeOptions()
        return self.query_email_verification_with_options(request, runtime)

    async def query_email_verification_async(
        self,
        request: main_models.QueryEmailVerificationRequest,
    ) -> main_models.QueryEmailVerificationResponse:
        runtime = RuntimeOptions()
        return await self.query_email_verification_with_options_async(request, runtime)

    def query_ens_association_with_options(
        self,
        request: main_models.QueryEnsAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEnsAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEnsAssociation',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEnsAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ens_association_with_options_async(
        self,
        request: main_models.QueryEnsAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEnsAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEnsAssociation',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEnsAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ens_association(
        self,
        request: main_models.QueryEnsAssociationRequest,
    ) -> main_models.QueryEnsAssociationResponse:
        runtime = RuntimeOptions()
        return self.query_ens_association_with_options(request, runtime)

    async def query_ens_association_async(
        self,
        request: main_models.QueryEnsAssociationRequest,
    ) -> main_models.QueryEnsAssociationResponse:
        runtime = RuntimeOptions()
        return await self.query_ens_association_with_options_async(request, runtime)

    def query_fail_reason_for_domain_real_name_verification_with_options(
        self,
        request: main_models.QueryFailReasonForDomainRealNameVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFailReasonForDomainRealNameVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.real_name_verification_action):
            query['RealNameVerificationAction'] = request.real_name_verification_action
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFailReasonForDomainRealNameVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFailReasonForDomainRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fail_reason_for_domain_real_name_verification_with_options_async(
        self,
        request: main_models.QueryFailReasonForDomainRealNameVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFailReasonForDomainRealNameVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.real_name_verification_action):
            query['RealNameVerificationAction'] = request.real_name_verification_action
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFailReasonForDomainRealNameVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFailReasonForDomainRealNameVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fail_reason_for_domain_real_name_verification(
        self,
        request: main_models.QueryFailReasonForDomainRealNameVerificationRequest,
    ) -> main_models.QueryFailReasonForDomainRealNameVerificationResponse:
        runtime = RuntimeOptions()
        return self.query_fail_reason_for_domain_real_name_verification_with_options(request, runtime)

    async def query_fail_reason_for_domain_real_name_verification_async(
        self,
        request: main_models.QueryFailReasonForDomainRealNameVerificationRequest,
    ) -> main_models.QueryFailReasonForDomainRealNameVerificationResponse:
        runtime = RuntimeOptions()
        return await self.query_fail_reason_for_domain_real_name_verification_with_options_async(request, runtime)

    def query_fail_reason_for_registrant_profile_real_name_verification_with_options(
        self,
        request: main_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileID'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFailReasonForRegistrantProfileRealNameVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fail_reason_for_registrant_profile_real_name_verification_with_options_async(
        self,
        request: main_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileID'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFailReasonForRegistrantProfileRealNameVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fail_reason_for_registrant_profile_real_name_verification(
        self,
        request: main_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
    ) -> main_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        runtime = RuntimeOptions()
        return self.query_fail_reason_for_registrant_profile_real_name_verification_with_options(request, runtime)

    async def query_fail_reason_for_registrant_profile_real_name_verification_async(
        self,
        request: main_models.QueryFailReasonForRegistrantProfileRealNameVerificationRequest,
    ) -> main_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse:
        runtime = RuntimeOptions()
        return await self.query_fail_reason_for_registrant_profile_real_name_verification_with_options_async(request, runtime)

    def query_failing_reason_list_for_qualification_with_options(
        self,
        request: main_models.QueryFailingReasonListForQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFailingReasonListForQualificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFailingReasonListForQualification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFailingReasonListForQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_failing_reason_list_for_qualification_with_options_async(
        self,
        request: main_models.QueryFailingReasonListForQualificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFailingReasonListForQualificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFailingReasonListForQualification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFailingReasonListForQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_failing_reason_list_for_qualification(
        self,
        request: main_models.QueryFailingReasonListForQualificationRequest,
    ) -> main_models.QueryFailingReasonListForQualificationResponse:
        runtime = RuntimeOptions()
        return self.query_failing_reason_list_for_qualification_with_options(request, runtime)

    async def query_failing_reason_list_for_qualification_async(
        self,
        request: main_models.QueryFailingReasonListForQualificationRequest,
    ) -> main_models.QueryFailingReasonListForQualificationResponse:
        runtime = RuntimeOptions()
        return await self.query_failing_reason_list_for_qualification_with_options_async(request, runtime)

    def query_intl_fixed_price_order_list_with_options(
        self,
        request: main_models.QueryIntlFixedPriceOrderListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryIntlFixedPriceOrderListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryIntlFixedPriceOrderList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryIntlFixedPriceOrderListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_intl_fixed_price_order_list_with_options_async(
        self,
        request: main_models.QueryIntlFixedPriceOrderListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryIntlFixedPriceOrderListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryIntlFixedPriceOrderList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryIntlFixedPriceOrderListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_intl_fixed_price_order_list(
        self,
        request: main_models.QueryIntlFixedPriceOrderListRequest,
    ) -> main_models.QueryIntlFixedPriceOrderListResponse:
        runtime = RuntimeOptions()
        return self.query_intl_fixed_price_order_list_with_options(request, runtime)

    async def query_intl_fixed_price_order_list_async(
        self,
        request: main_models.QueryIntlFixedPriceOrderListRequest,
    ) -> main_models.QueryIntlFixedPriceOrderListResponse:
        runtime = RuntimeOptions()
        return await self.query_intl_fixed_price_order_list_with_options_async(request, runtime)

    def query_local_ens_association_with_options(
        self,
        request: main_models.QueryLocalEnsAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLocalEnsAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLocalEnsAssociation',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLocalEnsAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_local_ens_association_with_options_async(
        self,
        request: main_models.QueryLocalEnsAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLocalEnsAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLocalEnsAssociation',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLocalEnsAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_local_ens_association(
        self,
        request: main_models.QueryLocalEnsAssociationRequest,
    ) -> main_models.QueryLocalEnsAssociationResponse:
        runtime = RuntimeOptions()
        return self.query_local_ens_association_with_options(request, runtime)

    async def query_local_ens_association_async(
        self,
        request: main_models.QueryLocalEnsAssociationRequest,
    ) -> main_models.QueryLocalEnsAssociationResponse:
        runtime = RuntimeOptions()
        return await self.query_local_ens_association_with_options_async(request, runtime)

    def query_operation_audit_info_detail_with_options(
        self,
        request: main_models.QueryOperationAuditInfoDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOperationAuditInfoDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOperationAuditInfoDetail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOperationAuditInfoDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_operation_audit_info_detail_with_options_async(
        self,
        request: main_models.QueryOperationAuditInfoDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOperationAuditInfoDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOperationAuditInfoDetail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOperationAuditInfoDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_operation_audit_info_detail(
        self,
        request: main_models.QueryOperationAuditInfoDetailRequest,
    ) -> main_models.QueryOperationAuditInfoDetailResponse:
        runtime = RuntimeOptions()
        return self.query_operation_audit_info_detail_with_options(request, runtime)

    async def query_operation_audit_info_detail_async(
        self,
        request: main_models.QueryOperationAuditInfoDetailRequest,
    ) -> main_models.QueryOperationAuditInfoDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_operation_audit_info_detail_with_options_async(request, runtime)

    def query_operation_audit_info_list_with_options(
        self,
        request: main_models.QueryOperationAuditInfoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOperationAuditInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.audit_type):
            query['AuditType'] = request.audit_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOperationAuditInfoList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOperationAuditInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_operation_audit_info_list_with_options_async(
        self,
        request: main_models.QueryOperationAuditInfoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOperationAuditInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.audit_type):
            query['AuditType'] = request.audit_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOperationAuditInfoList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOperationAuditInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_operation_audit_info_list(
        self,
        request: main_models.QueryOperationAuditInfoListRequest,
    ) -> main_models.QueryOperationAuditInfoListResponse:
        runtime = RuntimeOptions()
        return self.query_operation_audit_info_list_with_options(request, runtime)

    async def query_operation_audit_info_list_async(
        self,
        request: main_models.QueryOperationAuditInfoListRequest,
    ) -> main_models.QueryOperationAuditInfoListResponse:
        runtime = RuntimeOptions()
        return await self.query_operation_audit_info_list_with_options_async(request, runtime)

    def query_qualification_detail_with_options(
        self,
        request: main_models.QueryQualificationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryQualificationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryQualificationDetail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryQualificationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_qualification_detail_with_options_async(
        self,
        request: main_models.QueryQualificationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryQualificationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryQualificationDetail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryQualificationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_qualification_detail(
        self,
        request: main_models.QueryQualificationDetailRequest,
    ) -> main_models.QueryQualificationDetailResponse:
        runtime = RuntimeOptions()
        return self.query_qualification_detail_with_options(request, runtime)

    async def query_qualification_detail_async(
        self,
        request: main_models.QueryQualificationDetailRequest,
    ) -> main_models.QueryQualificationDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_qualification_detail_with_options_async(request, runtime)

    def query_registrant_profile_real_name_verification_info_with_options(
        self,
        request: main_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fetch_image):
            query['FetchImage'] = request.fetch_image
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRegistrantProfileRealNameVerificationInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRegistrantProfileRealNameVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_registrant_profile_real_name_verification_info_with_options_async(
        self,
        request: main_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fetch_image):
            query['FetchImage'] = request.fetch_image
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRegistrantProfileRealNameVerificationInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRegistrantProfileRealNameVerificationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_registrant_profile_real_name_verification_info(
        self,
        request: main_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
    ) -> main_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        runtime = RuntimeOptions()
        return self.query_registrant_profile_real_name_verification_info_with_options(request, runtime)

    async def query_registrant_profile_real_name_verification_info_async(
        self,
        request: main_models.QueryRegistrantProfileRealNameVerificationInfoRequest,
    ) -> main_models.QueryRegistrantProfileRealNameVerificationInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_registrant_profile_real_name_verification_info_with_options_async(request, runtime)

    def query_registrant_profiles_with_options(
        self,
        request: main_models.QueryRegistrantProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRegistrantProfilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_registrant_profile):
            query['DefaultRegistrantProfile'] = request.default_registrant_profile
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.real_name_status):
            query['RealNameStatus'] = request.real_name_status
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRegistrantProfiles',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRegistrantProfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_registrant_profiles_with_options_async(
        self,
        request: main_models.QueryRegistrantProfilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRegistrantProfilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_registrant_profile):
            query['DefaultRegistrantProfile'] = request.default_registrant_profile
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.real_name_status):
            query['RealNameStatus'] = request.real_name_status
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRegistrantProfiles',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRegistrantProfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_registrant_profiles(
        self,
        request: main_models.QueryRegistrantProfilesRequest,
    ) -> main_models.QueryRegistrantProfilesResponse:
        runtime = RuntimeOptions()
        return self.query_registrant_profiles_with_options(request, runtime)

    async def query_registrant_profiles_async(
        self,
        request: main_models.QueryRegistrantProfilesRequest,
    ) -> main_models.QueryRegistrantProfilesResponse:
        runtime = RuntimeOptions()
        return await self.query_registrant_profiles_with_options_async(request, runtime)

    def query_server_lock_with_options(
        self,
        request: main_models.QueryServerLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryServerLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryServerLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryServerLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_server_lock_with_options_async(
        self,
        request: main_models.QueryServerLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryServerLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryServerLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryServerLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_server_lock(
        self,
        request: main_models.QueryServerLockRequest,
    ) -> main_models.QueryServerLockResponse:
        runtime = RuntimeOptions()
        return self.query_server_lock_with_options(request, runtime)

    async def query_server_lock_async(
        self,
        request: main_models.QueryServerLockRequest,
    ) -> main_models.QueryServerLockResponse:
        runtime = RuntimeOptions()
        return await self.query_server_lock_with_options_async(request, runtime)

    def query_task_detail_history_with_options(
        self,
        request: main_models.QueryTaskDetailHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskDetailHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_name_cursor):
            query['DomainNameCursor'] = request.domain_name_cursor
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_detail_no_cursor):
            query['TaskDetailNoCursor'] = request.task_detail_no_cursor
        if not DaraCore.is_null(request.task_no):
            query['TaskNo'] = request.task_no
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskDetailHistory',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskDetailHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_detail_history_with_options_async(
        self,
        request: main_models.QueryTaskDetailHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskDetailHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_name_cursor):
            query['DomainNameCursor'] = request.domain_name_cursor
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_detail_no_cursor):
            query['TaskDetailNoCursor'] = request.task_detail_no_cursor
        if not DaraCore.is_null(request.task_no):
            query['TaskNo'] = request.task_no
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskDetailHistory',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskDetailHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_detail_history(
        self,
        request: main_models.QueryTaskDetailHistoryRequest,
    ) -> main_models.QueryTaskDetailHistoryResponse:
        runtime = RuntimeOptions()
        return self.query_task_detail_history_with_options(request, runtime)

    async def query_task_detail_history_async(
        self,
        request: main_models.QueryTaskDetailHistoryRequest,
    ) -> main_models.QueryTaskDetailHistoryResponse:
        runtime = RuntimeOptions()
        return await self.query_task_detail_history_with_options_async(request, runtime)

    def query_task_detail_list_with_options(
        self,
        request: main_models.QueryTaskDetailListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskDetailListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_no):
            query['TaskNo'] = request.task_no
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskDetailList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_detail_list_with_options_async(
        self,
        request: main_models.QueryTaskDetailListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskDetailListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_no):
            query['TaskNo'] = request.task_no
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskDetailList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_detail_list(
        self,
        request: main_models.QueryTaskDetailListRequest,
    ) -> main_models.QueryTaskDetailListResponse:
        runtime = RuntimeOptions()
        return self.query_task_detail_list_with_options(request, runtime)

    async def query_task_detail_list_async(
        self,
        request: main_models.QueryTaskDetailListRequest,
    ) -> main_models.QueryTaskDetailListResponse:
        runtime = RuntimeOptions()
        return await self.query_task_detail_list_with_options_async(request, runtime)

    def query_task_info_history_with_options(
        self,
        request: main_models.QueryTaskInfoHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskInfoHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not DaraCore.is_null(request.create_time_cursor):
            query['CreateTimeCursor'] = request.create_time_cursor
        if not DaraCore.is_null(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_no_cursor):
            query['TaskNoCursor'] = request.task_no_cursor
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskInfoHistory',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskInfoHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_info_history_with_options_async(
        self,
        request: main_models.QueryTaskInfoHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskInfoHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not DaraCore.is_null(request.create_time_cursor):
            query['CreateTimeCursor'] = request.create_time_cursor
        if not DaraCore.is_null(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_no_cursor):
            query['TaskNoCursor'] = request.task_no_cursor
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskInfoHistory',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskInfoHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_info_history(
        self,
        request: main_models.QueryTaskInfoHistoryRequest,
    ) -> main_models.QueryTaskInfoHistoryResponse:
        runtime = RuntimeOptions()
        return self.query_task_info_history_with_options(request, runtime)

    async def query_task_info_history_async(
        self,
        request: main_models.QueryTaskInfoHistoryRequest,
    ) -> main_models.QueryTaskInfoHistoryResponse:
        runtime = RuntimeOptions()
        return await self.query_task_info_history_with_options_async(request, runtime)

    def query_task_list_with_options(
        self,
        request: main_models.QueryTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not DaraCore.is_null(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_list_with_options_async(
        self,
        request: main_models.QueryTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not DaraCore.is_null(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_list(
        self,
        request: main_models.QueryTaskListRequest,
    ) -> main_models.QueryTaskListResponse:
        runtime = RuntimeOptions()
        return self.query_task_list_with_options(request, runtime)

    async def query_task_list_async(
        self,
        request: main_models.QueryTaskListRequest,
    ) -> main_models.QueryTaskListResponse:
        runtime = RuntimeOptions()
        return await self.query_task_list_with_options_async(request, runtime)

    def query_transfer_in_by_instance_id_with_options(
        self,
        request: main_models.QueryTransferInByInstanceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTransferInByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTransferInByInstanceId',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTransferInByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_in_by_instance_id_with_options_async(
        self,
        request: main_models.QueryTransferInByInstanceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTransferInByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTransferInByInstanceId',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTransferInByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_in_by_instance_id(
        self,
        request: main_models.QueryTransferInByInstanceIdRequest,
    ) -> main_models.QueryTransferInByInstanceIdResponse:
        runtime = RuntimeOptions()
        return self.query_transfer_in_by_instance_id_with_options(request, runtime)

    async def query_transfer_in_by_instance_id_async(
        self,
        request: main_models.QueryTransferInByInstanceIdRequest,
    ) -> main_models.QueryTransferInByInstanceIdResponse:
        runtime = RuntimeOptions()
        return await self.query_transfer_in_by_instance_id_with_options_async(request, runtime)

    def query_transfer_in_list_with_options(
        self,
        request: main_models.QueryTransferInListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTransferInListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.simple_transfer_in_status):
            query['SimpleTransferInStatus'] = request.simple_transfer_in_status
        if not DaraCore.is_null(request.submission_end_date):
            query['SubmissionEndDate'] = request.submission_end_date
        if not DaraCore.is_null(request.submission_start_date):
            query['SubmissionStartDate'] = request.submission_start_date
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTransferInList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTransferInListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_in_list_with_options_async(
        self,
        request: main_models.QueryTransferInListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTransferInListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.simple_transfer_in_status):
            query['SimpleTransferInStatus'] = request.simple_transfer_in_status
        if not DaraCore.is_null(request.submission_end_date):
            query['SubmissionEndDate'] = request.submission_end_date
        if not DaraCore.is_null(request.submission_start_date):
            query['SubmissionStartDate'] = request.submission_start_date
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTransferInList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTransferInListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_in_list(
        self,
        request: main_models.QueryTransferInListRequest,
    ) -> main_models.QueryTransferInListResponse:
        runtime = RuntimeOptions()
        return self.query_transfer_in_list_with_options(request, runtime)

    async def query_transfer_in_list_async(
        self,
        request: main_models.QueryTransferInListRequest,
    ) -> main_models.QueryTransferInListResponse:
        runtime = RuntimeOptions()
        return await self.query_transfer_in_list_with_options_async(request, runtime)

    def query_transfer_out_info_with_options(
        self,
        request: main_models.QueryTransferOutInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTransferOutInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTransferOutInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTransferOutInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_out_info_with_options_async(
        self,
        request: main_models.QueryTransferOutInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTransferOutInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTransferOutInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTransferOutInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_out_info(
        self,
        request: main_models.QueryTransferOutInfoRequest,
    ) -> main_models.QueryTransferOutInfoResponse:
        runtime = RuntimeOptions()
        return self.query_transfer_out_info_with_options(request, runtime)

    async def query_transfer_out_info_async(
        self,
        request: main_models.QueryTransferOutInfoRequest,
    ) -> main_models.QueryTransferOutInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_transfer_out_info_with_options_async(request, runtime)

    def registrant_profile_real_name_verification_with_options(
        self,
        request: main_models.RegistrantProfileRealNameVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegistrantProfileRealNameVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not DaraCore.is_null(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileID'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RegistrantProfileRealNameVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegistrantProfileRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def registrant_profile_real_name_verification_with_options_async(
        self,
        request: main_models.RegistrantProfileRealNameVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegistrantProfileRealNameVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not DaraCore.is_null(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileID'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RegistrantProfileRealNameVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegistrantProfileRealNameVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def registrant_profile_real_name_verification(
        self,
        request: main_models.RegistrantProfileRealNameVerificationRequest,
    ) -> main_models.RegistrantProfileRealNameVerificationResponse:
        runtime = RuntimeOptions()
        return self.registrant_profile_real_name_verification_with_options(request, runtime)

    async def registrant_profile_real_name_verification_async(
        self,
        request: main_models.RegistrantProfileRealNameVerificationRequest,
    ) -> main_models.RegistrantProfileRealNameVerificationResponse:
        runtime = RuntimeOptions()
        return await self.registrant_profile_real_name_verification_with_options_async(request, runtime)

    def resend_email_verification_with_options(
        self,
        request: main_models.ResendEmailVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendEmailVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendEmailVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_email_verification_with_options_async(
        self,
        request: main_models.ResendEmailVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendEmailVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendEmailVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_email_verification(
        self,
        request: main_models.ResendEmailVerificationRequest,
    ) -> main_models.ResendEmailVerificationResponse:
        runtime = RuntimeOptions()
        return self.resend_email_verification_with_options(request, runtime)

    async def resend_email_verification_async(
        self,
        request: main_models.ResendEmailVerificationRequest,
    ) -> main_models.ResendEmailVerificationResponse:
        runtime = RuntimeOptions()
        return await self.resend_email_verification_with_options_async(request, runtime)

    def reset_qualification_verification_with_options(
        self,
        request: main_models.ResetQualificationVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetQualificationVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetQualificationVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetQualificationVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_qualification_verification_with_options_async(
        self,
        request: main_models.ResetQualificationVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetQualificationVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetQualificationVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetQualificationVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_qualification_verification(
        self,
        request: main_models.ResetQualificationVerificationRequest,
    ) -> main_models.ResetQualificationVerificationResponse:
        runtime = RuntimeOptions()
        return self.reset_qualification_verification_with_options(request, runtime)

    async def reset_qualification_verification_async(
        self,
        request: main_models.ResetQualificationVerificationRequest,
    ) -> main_models.ResetQualificationVerificationResponse:
        runtime = RuntimeOptions()
        return await self.reset_qualification_verification_with_options_async(request, runtime)

    def save_batch_domain_remark_with_options(
        self,
        request: main_models.SaveBatchDomainRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchDomainRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchDomainRemark',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchDomainRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_domain_remark_with_options_async(
        self,
        request: main_models.SaveBatchDomainRemarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchDomainRemarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchDomainRemark',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchDomainRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_domain_remark(
        self,
        request: main_models.SaveBatchDomainRemarkRequest,
    ) -> main_models.SaveBatchDomainRemarkResponse:
        runtime = RuntimeOptions()
        return self.save_batch_domain_remark_with_options(request, runtime)

    async def save_batch_domain_remark_async(
        self,
        request: main_models.SaveBatchDomainRemarkRequest,
    ) -> main_models.SaveBatchDomainRemarkResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_domain_remark_with_options_async(request, runtime)

    def save_batch_task_for_apply_quick_transfer_out_openly_with_options(
        self,
        request: main_models.SaveBatchTaskForApplyQuickTransferOutOpenlyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForApplyQuickTransferOutOpenly',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_apply_quick_transfer_out_openly_with_options_async(
        self,
        request: main_models.SaveBatchTaskForApplyQuickTransferOutOpenlyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForApplyQuickTransferOutOpenly',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_apply_quick_transfer_out_openly(
        self,
        request: main_models.SaveBatchTaskForApplyQuickTransferOutOpenlyRequest,
    ) -> main_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_apply_quick_transfer_out_openly_with_options(request, runtime)

    async def save_batch_task_for_apply_quick_transfer_out_openly_async(
        self,
        request: main_models.SaveBatchTaskForApplyQuickTransferOutOpenlyRequest,
    ) -> main_models.SaveBatchTaskForApplyQuickTransferOutOpenlyResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_apply_quick_transfer_out_openly_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_activate_with_options(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderActivateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForCreatingOrderActivateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_activate_param):
            query['OrderActivateParam'] = request.order_activate_param
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForCreatingOrderActivate',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForCreatingOrderActivateResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_activate_with_options_async(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderActivateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForCreatingOrderActivateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_activate_param):
            query['OrderActivateParam'] = request.order_activate_param
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForCreatingOrderActivate',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForCreatingOrderActivateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_activate(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderActivateRequest,
    ) -> main_models.SaveBatchTaskForCreatingOrderActivateResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_creating_order_activate_with_options(request, runtime)

    async def save_batch_task_for_creating_order_activate_async(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderActivateRequest,
    ) -> main_models.SaveBatchTaskForCreatingOrderActivateResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_creating_order_activate_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_redeem_with_options(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderRedeemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_redeem_param):
            query['OrderRedeemParam'] = request.order_redeem_param
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForCreatingOrderRedeem',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForCreatingOrderRedeemResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_redeem_with_options_async(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderRedeemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_redeem_param):
            query['OrderRedeemParam'] = request.order_redeem_param
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForCreatingOrderRedeem',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForCreatingOrderRedeemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_redeem(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderRedeemRequest,
    ) -> main_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_creating_order_redeem_with_options(request, runtime)

    async def save_batch_task_for_creating_order_redeem_async(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderRedeemRequest,
    ) -> main_models.SaveBatchTaskForCreatingOrderRedeemResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_creating_order_redeem_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_renew_with_options(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderRenewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForCreatingOrderRenewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_renew_param):
            query['OrderRenewParam'] = request.order_renew_param
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForCreatingOrderRenew',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForCreatingOrderRenewResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_renew_with_options_async(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderRenewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForCreatingOrderRenewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_renew_param):
            query['OrderRenewParam'] = request.order_renew_param
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForCreatingOrderRenew',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForCreatingOrderRenewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_renew(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderRenewRequest,
    ) -> main_models.SaveBatchTaskForCreatingOrderRenewResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_creating_order_renew_with_options(request, runtime)

    async def save_batch_task_for_creating_order_renew_async(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderRenewRequest,
    ) -> main_models.SaveBatchTaskForCreatingOrderRenewResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_creating_order_renew_with_options_async(request, runtime)

    def save_batch_task_for_creating_order_transfer_with_options(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForCreatingOrderTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_transfer_param):
            query['OrderTransferParam'] = request.order_transfer_param
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForCreatingOrderTransfer',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForCreatingOrderTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_creating_order_transfer_with_options_async(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForCreatingOrderTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_transfer_param):
            query['OrderTransferParam'] = request.order_transfer_param
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForCreatingOrderTransfer',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForCreatingOrderTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_creating_order_transfer(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderTransferRequest,
    ) -> main_models.SaveBatchTaskForCreatingOrderTransferResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_creating_order_transfer_with_options(request, runtime)

    async def save_batch_task_for_creating_order_transfer_async(
        self,
        request: main_models.SaveBatchTaskForCreatingOrderTransferRequest,
    ) -> main_models.SaveBatchTaskForCreatingOrderTransferResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_creating_order_transfer_with_options_async(request, runtime)

    def save_batch_task_for_domain_name_proxy_service_with_options(
        self,
        request: main_models.SaveBatchTaskForDomainNameProxyServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForDomainNameProxyService',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForDomainNameProxyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_domain_name_proxy_service_with_options_async(
        self,
        request: main_models.SaveBatchTaskForDomainNameProxyServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForDomainNameProxyService',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForDomainNameProxyServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_domain_name_proxy_service(
        self,
        request: main_models.SaveBatchTaskForDomainNameProxyServiceRequest,
    ) -> main_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_domain_name_proxy_service_with_options(request, runtime)

    async def save_batch_task_for_domain_name_proxy_service_async(
        self,
        request: main_models.SaveBatchTaskForDomainNameProxyServiceRequest,
    ) -> main_models.SaveBatchTaskForDomainNameProxyServiceResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_domain_name_proxy_service_with_options_async(request, runtime)

    def save_batch_task_for_generate_domain_certificate_with_options(
        self,
        tmp_req: main_models.SaveBatchTaskForGenerateDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForGenerateDomainCertificateResponse:
        tmp_req.validate()
        request = main_models.SaveBatchTaskForGenerateDomainCertificateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.domain_names):
            request.domain_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.domain_names, 'DomainNames', 'json')
        query = {}
        if not DaraCore.is_null(request.domain_names_shrink):
            query['DomainNames'] = request.domain_names_shrink
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForGenerateDomainCertificate',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForGenerateDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_generate_domain_certificate_with_options_async(
        self,
        tmp_req: main_models.SaveBatchTaskForGenerateDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForGenerateDomainCertificateResponse:
        tmp_req.validate()
        request = main_models.SaveBatchTaskForGenerateDomainCertificateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.domain_names):
            request.domain_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.domain_names, 'DomainNames', 'json')
        query = {}
        if not DaraCore.is_null(request.domain_names_shrink):
            query['DomainNames'] = request.domain_names_shrink
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForGenerateDomainCertificate',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForGenerateDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_generate_domain_certificate(
        self,
        request: main_models.SaveBatchTaskForGenerateDomainCertificateRequest,
    ) -> main_models.SaveBatchTaskForGenerateDomainCertificateResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_generate_domain_certificate_with_options(request, runtime)

    async def save_batch_task_for_generate_domain_certificate_async(
        self,
        request: main_models.SaveBatchTaskForGenerateDomainCertificateRequest,
    ) -> main_models.SaveBatchTaskForGenerateDomainCertificateResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_generate_domain_certificate_with_options_async(request, runtime)

    def save_batch_task_for_modifying_domain_dns_with_options(
        self,
        request: main_models.SaveBatchTaskForModifyingDomainDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForModifyingDomainDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_name_server):
            query['DomainNameServer'] = request.domain_name_server
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForModifyingDomainDns',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForModifyingDomainDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_modifying_domain_dns_with_options_async(
        self,
        request: main_models.SaveBatchTaskForModifyingDomainDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForModifyingDomainDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_name_server):
            query['DomainNameServer'] = request.domain_name_server
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForModifyingDomainDns',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForModifyingDomainDnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_modifying_domain_dns(
        self,
        request: main_models.SaveBatchTaskForModifyingDomainDnsRequest,
    ) -> main_models.SaveBatchTaskForModifyingDomainDnsResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_modifying_domain_dns_with_options(request, runtime)

    async def save_batch_task_for_modifying_domain_dns_async(
        self,
        request: main_models.SaveBatchTaskForModifyingDomainDnsRequest,
    ) -> main_models.SaveBatchTaskForModifyingDomainDnsResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_modifying_domain_dns_with_options_async(request, runtime)

    def save_batch_task_for_reserve_drop_list_domain_with_options(
        self,
        request: main_models.SaveBatchTaskForReserveDropListDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForReserveDropListDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForReserveDropListDomain',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForReserveDropListDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_reserve_drop_list_domain_with_options_async(
        self,
        request: main_models.SaveBatchTaskForReserveDropListDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForReserveDropListDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForReserveDropListDomain',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForReserveDropListDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_reserve_drop_list_domain(
        self,
        request: main_models.SaveBatchTaskForReserveDropListDomainRequest,
    ) -> main_models.SaveBatchTaskForReserveDropListDomainResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_reserve_drop_list_domain_with_options(request, runtime)

    async def save_batch_task_for_reserve_drop_list_domain_async(
        self,
        request: main_models.SaveBatchTaskForReserveDropListDomainRequest,
    ) -> main_models.SaveBatchTaskForReserveDropListDomainResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_reserve_drop_list_domain_with_options_async(request, runtime)

    def save_batch_task_for_transfer_out_by_authorization_code_with_options(
        self,
        request: main_models.SaveBatchTaskForTransferOutByAuthorizationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForTransferOutByAuthorizationCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.transfer_out_param_list):
            query['TransferOutParamList'] = request.transfer_out_param_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForTransferOutByAuthorizationCode',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForTransferOutByAuthorizationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_transfer_out_by_authorization_code_with_options_async(
        self,
        request: main_models.SaveBatchTaskForTransferOutByAuthorizationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForTransferOutByAuthorizationCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.transfer_out_param_list):
            query['TransferOutParamList'] = request.transfer_out_param_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForTransferOutByAuthorizationCode',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForTransferOutByAuthorizationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_transfer_out_by_authorization_code(
        self,
        request: main_models.SaveBatchTaskForTransferOutByAuthorizationCodeRequest,
    ) -> main_models.SaveBatchTaskForTransferOutByAuthorizationCodeResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_transfer_out_by_authorization_code_with_options(request, runtime)

    async def save_batch_task_for_transfer_out_by_authorization_code_async(
        self,
        request: main_models.SaveBatchTaskForTransferOutByAuthorizationCodeRequest,
    ) -> main_models.SaveBatchTaskForTransferOutByAuthorizationCodeResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_transfer_out_by_authorization_code_with_options_async(request, runtime)

    def save_batch_task_for_transfer_prohibition_lock_with_options(
        self,
        request: main_models.SaveBatchTaskForTransferProhibitionLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForTransferProhibitionLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForTransferProhibitionLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForTransferProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_transfer_prohibition_lock_with_options_async(
        self,
        request: main_models.SaveBatchTaskForTransferProhibitionLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForTransferProhibitionLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForTransferProhibitionLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForTransferProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_transfer_prohibition_lock(
        self,
        request: main_models.SaveBatchTaskForTransferProhibitionLockRequest,
    ) -> main_models.SaveBatchTaskForTransferProhibitionLockResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_transfer_prohibition_lock_with_options(request, runtime)

    async def save_batch_task_for_transfer_prohibition_lock_async(
        self,
        request: main_models.SaveBatchTaskForTransferProhibitionLockRequest,
    ) -> main_models.SaveBatchTaskForTransferProhibitionLockResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_transfer_prohibition_lock_with_options_async(request, runtime)

    def save_batch_task_for_update_prohibition_lock_with_options(
        self,
        request: main_models.SaveBatchTaskForUpdateProhibitionLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForUpdateProhibitionLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForUpdateProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_update_prohibition_lock_with_options_async(
        self,
        request: main_models.SaveBatchTaskForUpdateProhibitionLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForUpdateProhibitionLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForUpdateProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_update_prohibition_lock(
        self,
        request: main_models.SaveBatchTaskForUpdateProhibitionLockRequest,
    ) -> main_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_update_prohibition_lock_with_options(request, runtime)

    async def save_batch_task_for_update_prohibition_lock_async(
        self,
        request: main_models.SaveBatchTaskForUpdateProhibitionLockRequest,
    ) -> main_models.SaveBatchTaskForUpdateProhibitionLockResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_update_prohibition_lock_with_options_async(request, runtime)

    def save_batch_task_for_updating_contact_info_by_new_contact_with_options(
        self,
        request: main_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForUpdatingContactInfoByNewContact',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_updating_contact_info_by_new_contact_with_options_async(
        self,
        request: main_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForUpdatingContactInfoByNewContact',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_updating_contact_info_by_new_contact(
        self,
        request: main_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
    ) -> main_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_updating_contact_info_by_new_contact_with_options(request, runtime)

    async def save_batch_task_for_updating_contact_info_by_new_contact_async(
        self,
        request: main_models.SaveBatchTaskForUpdatingContactInfoByNewContactRequest,
    ) -> main_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_updating_contact_info_by_new_contact_with_options_async(request, runtime)

    def save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options(
        self,
        request: main_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForUpdatingContactInfoByRegistrantProfileId',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options_async(
        self,
        request: main_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveBatchTaskForUpdatingContactInfoByRegistrantProfileId',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_batch_task_for_updating_contact_info_by_registrant_profile_id(
        self,
        request: main_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest,
    ) -> main_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse:
        runtime = RuntimeOptions()
        return self.save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options(request, runtime)

    async def save_batch_task_for_updating_contact_info_by_registrant_profile_id_async(
        self,
        request: main_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdRequest,
    ) -> main_models.SaveBatchTaskForUpdatingContactInfoByRegistrantProfileIdResponse:
        runtime = RuntimeOptions()
        return await self.save_batch_task_for_updating_contact_info_by_registrant_profile_id_with_options_async(request, runtime)

    def save_domain_group_with_options(
        self,
        request: main_models.SaveDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.domain_group_name):
            query['DomainGroupName'] = request.domain_group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveDomainGroup',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_domain_group_with_options_async(
        self,
        request: main_models.SaveDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.domain_group_name):
            query['DomainGroupName'] = request.domain_group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveDomainGroup',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_domain_group(
        self,
        request: main_models.SaveDomainGroupRequest,
    ) -> main_models.SaveDomainGroupResponse:
        runtime = RuntimeOptions()
        return self.save_domain_group_with_options(request, runtime)

    async def save_domain_group_async(
        self,
        request: main_models.SaveDomainGroupRequest,
    ) -> main_models.SaveDomainGroupResponse:
        runtime = RuntimeOptions()
        return await self.save_domain_group_with_options_async(request, runtime)

    def save_registrant_profile_with_options(
        self,
        request: main_models.SaveRegistrantProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveRegistrantProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.default_registrant_profile):
            query['DefaultRegistrantProfile'] = request.default_registrant_profile
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveRegistrantProfile',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveRegistrantProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_registrant_profile_with_options_async(
        self,
        request: main_models.SaveRegistrantProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveRegistrantProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.default_registrant_profile):
            query['DefaultRegistrantProfile'] = request.default_registrant_profile
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveRegistrantProfile',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveRegistrantProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_registrant_profile(
        self,
        request: main_models.SaveRegistrantProfileRequest,
    ) -> main_models.SaveRegistrantProfileResponse:
        runtime = RuntimeOptions()
        return self.save_registrant_profile_with_options(request, runtime)

    async def save_registrant_profile_async(
        self,
        request: main_models.SaveRegistrantProfileRequest,
    ) -> main_models.SaveRegistrantProfileResponse:
        runtime = RuntimeOptions()
        return await self.save_registrant_profile_with_options_async(request, runtime)

    def save_registrant_profile_real_name_verification_with_options(
        self,
        request: main_models.SaveRegistrantProfileRealNameVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveRegistrantProfileRealNameVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.identity_credential):
            query['IdentityCredential'] = request.identity_credential
        if not DaraCore.is_null(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not DaraCore.is_null(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveRegistrantProfileRealNameVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveRegistrantProfileRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_registrant_profile_real_name_verification_with_options_async(
        self,
        request: main_models.SaveRegistrantProfileRealNameVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveRegistrantProfileRealNameVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.identity_credential):
            query['IdentityCredential'] = request.identity_credential
        if not DaraCore.is_null(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not DaraCore.is_null(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveRegistrantProfileRealNameVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveRegistrantProfileRealNameVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_registrant_profile_real_name_verification(
        self,
        request: main_models.SaveRegistrantProfileRealNameVerificationRequest,
    ) -> main_models.SaveRegistrantProfileRealNameVerificationResponse:
        runtime = RuntimeOptions()
        return self.save_registrant_profile_real_name_verification_with_options(request, runtime)

    async def save_registrant_profile_real_name_verification_async(
        self,
        request: main_models.SaveRegistrantProfileRealNameVerificationRequest,
    ) -> main_models.SaveRegistrantProfileRealNameVerificationResponse:
        runtime = RuntimeOptions()
        return await self.save_registrant_profile_real_name_verification_with_options_async(request, runtime)

    def save_single_task_for_adding_dsrecord_with_options(
        self,
        request: main_models.SaveSingleTaskForAddingDSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForAddingDSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.digest_type):
            query['DigestType'] = request.digest_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForAddingDSRecord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForAddingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_adding_dsrecord_with_options_async(
        self,
        request: main_models.SaveSingleTaskForAddingDSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForAddingDSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.digest_type):
            query['DigestType'] = request.digest_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForAddingDSRecord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForAddingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_adding_dsrecord(
        self,
        request: main_models.SaveSingleTaskForAddingDSRecordRequest,
    ) -> main_models.SaveSingleTaskForAddingDSRecordResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_adding_dsrecord_with_options(request, runtime)

    async def save_single_task_for_adding_dsrecord_async(
        self,
        request: main_models.SaveSingleTaskForAddingDSRecordRequest,
    ) -> main_models.SaveSingleTaskForAddingDSRecordResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_adding_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_apply_quick_transfer_out_openly_with_options(
        self,
        request: main_models.SaveSingleTaskForApplyQuickTransferOutOpenlyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForApplyQuickTransferOutOpenly',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_apply_quick_transfer_out_openly_with_options_async(
        self,
        request: main_models.SaveSingleTaskForApplyQuickTransferOutOpenlyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForApplyQuickTransferOutOpenly',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_apply_quick_transfer_out_openly(
        self,
        request: main_models.SaveSingleTaskForApplyQuickTransferOutOpenlyRequest,
    ) -> main_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_apply_quick_transfer_out_openly_with_options(request, runtime)

    async def save_single_task_for_apply_quick_transfer_out_openly_async(
        self,
        request: main_models.SaveSingleTaskForApplyQuickTransferOutOpenlyRequest,
    ) -> main_models.SaveSingleTaskForApplyQuickTransferOutOpenlyResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_apply_quick_transfer_out_openly_with_options_async(request, runtime)

    def save_single_task_for_approving_transfer_out_with_options(
        self,
        request: main_models.SaveSingleTaskForApprovingTransferOutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForApprovingTransferOutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForApprovingTransferOut',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForApprovingTransferOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_approving_transfer_out_with_options_async(
        self,
        request: main_models.SaveSingleTaskForApprovingTransferOutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForApprovingTransferOutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForApprovingTransferOut',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForApprovingTransferOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_approving_transfer_out(
        self,
        request: main_models.SaveSingleTaskForApprovingTransferOutRequest,
    ) -> main_models.SaveSingleTaskForApprovingTransferOutResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_approving_transfer_out_with_options(request, runtime)

    async def save_single_task_for_approving_transfer_out_async(
        self,
        request: main_models.SaveSingleTaskForApprovingTransferOutRequest,
    ) -> main_models.SaveSingleTaskForApprovingTransferOutResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_approving_transfer_out_with_options_async(request, runtime)

    def save_single_task_for_associating_ens_with_options(
        self,
        request: main_models.SaveSingleTaskForAssociatingEnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForAssociatingEnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForAssociatingEns',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForAssociatingEnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_associating_ens_with_options_async(
        self,
        request: main_models.SaveSingleTaskForAssociatingEnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForAssociatingEnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForAssociatingEns',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForAssociatingEnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_associating_ens(
        self,
        request: main_models.SaveSingleTaskForAssociatingEnsRequest,
    ) -> main_models.SaveSingleTaskForAssociatingEnsResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_associating_ens_with_options(request, runtime)

    async def save_single_task_for_associating_ens_async(
        self,
        request: main_models.SaveSingleTaskForAssociatingEnsRequest,
    ) -> main_models.SaveSingleTaskForAssociatingEnsResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_associating_ens_with_options_async(request, runtime)

    def save_single_task_for_canceling_transfer_in_with_options(
        self,
        request: main_models.SaveSingleTaskForCancelingTransferInRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCancelingTransferInResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCancelingTransferIn',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCancelingTransferInResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_canceling_transfer_in_with_options_async(
        self,
        request: main_models.SaveSingleTaskForCancelingTransferInRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCancelingTransferInResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCancelingTransferIn',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCancelingTransferInResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_canceling_transfer_in(
        self,
        request: main_models.SaveSingleTaskForCancelingTransferInRequest,
    ) -> main_models.SaveSingleTaskForCancelingTransferInResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_canceling_transfer_in_with_options(request, runtime)

    async def save_single_task_for_canceling_transfer_in_async(
        self,
        request: main_models.SaveSingleTaskForCancelingTransferInRequest,
    ) -> main_models.SaveSingleTaskForCancelingTransferInResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_canceling_transfer_in_with_options_async(request, runtime)

    def save_single_task_for_canceling_transfer_out_with_options(
        self,
        request: main_models.SaveSingleTaskForCancelingTransferOutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCancelingTransferOutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCancelingTransferOut',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCancelingTransferOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_canceling_transfer_out_with_options_async(
        self,
        request: main_models.SaveSingleTaskForCancelingTransferOutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCancelingTransferOutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCancelingTransferOut',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCancelingTransferOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_canceling_transfer_out(
        self,
        request: main_models.SaveSingleTaskForCancelingTransferOutRequest,
    ) -> main_models.SaveSingleTaskForCancelingTransferOutResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_canceling_transfer_out_with_options(request, runtime)

    async def save_single_task_for_canceling_transfer_out_async(
        self,
        request: main_models.SaveSingleTaskForCancelingTransferOutRequest,
    ) -> main_models.SaveSingleTaskForCancelingTransferOutResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_canceling_transfer_out_with_options_async(request, runtime)

    def save_single_task_for_creating_dns_host_with_options(
        self,
        request: main_models.SaveSingleTaskForCreatingDnsHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCreatingDnsHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dns_name):
            query['DnsName'] = request.dns_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCreatingDnsHost',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCreatingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_dns_host_with_options_async(
        self,
        request: main_models.SaveSingleTaskForCreatingDnsHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCreatingDnsHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dns_name):
            query['DnsName'] = request.dns_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCreatingDnsHost',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCreatingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_dns_host(
        self,
        request: main_models.SaveSingleTaskForCreatingDnsHostRequest,
    ) -> main_models.SaveSingleTaskForCreatingDnsHostResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_creating_dns_host_with_options(request, runtime)

    async def save_single_task_for_creating_dns_host_async(
        self,
        request: main_models.SaveSingleTaskForCreatingDnsHostRequest,
    ) -> main_models.SaveSingleTaskForCreatingDnsHostResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_creating_dns_host_with_options_async(request, runtime)

    def save_single_task_for_creating_order_activate_with_options(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderActivateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCreatingOrderActivateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dns_1):
            query['Dns1'] = request.dns_1
        if not DaraCore.is_null(request.dns_2):
            query['Dns2'] = request.dns_2
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.enable_domain_proxy):
            query['EnableDomainProxy'] = request.enable_domain_proxy
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.permit_premium_activation):
            query['PermitPremiumActivation'] = request.permit_premium_activation
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_duration):
            query['SubscriptionDuration'] = request.subscription_duration
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.trademark_domain_activation):
            query['TrademarkDomainActivation'] = request.trademark_domain_activation
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCreatingOrderActivate',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCreatingOrderActivateResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_activate_with_options_async(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderActivateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCreatingOrderActivateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dns_1):
            query['Dns1'] = request.dns_1
        if not DaraCore.is_null(request.dns_2):
            query['Dns2'] = request.dns_2
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.enable_domain_proxy):
            query['EnableDomainProxy'] = request.enable_domain_proxy
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.permit_premium_activation):
            query['PermitPremiumActivation'] = request.permit_premium_activation
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.subscription_duration):
            query['SubscriptionDuration'] = request.subscription_duration
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.trademark_domain_activation):
            query['TrademarkDomainActivation'] = request.trademark_domain_activation
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCreatingOrderActivate',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCreatingOrderActivateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_activate(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderActivateRequest,
    ) -> main_models.SaveSingleTaskForCreatingOrderActivateResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_creating_order_activate_with_options(request, runtime)

    async def save_single_task_for_creating_order_activate_async(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderActivateRequest,
    ) -> main_models.SaveSingleTaskForCreatingOrderActivateResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_creating_order_activate_with_options_async(request, runtime)

    def save_single_task_for_creating_order_redeem_with_options(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderRedeemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.current_expiration_date):
            query['CurrentExpirationDate'] = request.current_expiration_date
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCreatingOrderRedeem',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCreatingOrderRedeemResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_redeem_with_options_async(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderRedeemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.current_expiration_date):
            query['CurrentExpirationDate'] = request.current_expiration_date
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCreatingOrderRedeem',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCreatingOrderRedeemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_redeem(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderRedeemRequest,
    ) -> main_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_creating_order_redeem_with_options(request, runtime)

    async def save_single_task_for_creating_order_redeem_async(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderRedeemRequest,
    ) -> main_models.SaveSingleTaskForCreatingOrderRedeemResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_creating_order_redeem_with_options_async(request, runtime)

    def save_single_task_for_creating_order_renew_with_options(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderRenewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCreatingOrderRenewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.current_expiration_date):
            query['CurrentExpirationDate'] = request.current_expiration_date
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.subscription_duration):
            query['SubscriptionDuration'] = request.subscription_duration
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCreatingOrderRenew',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCreatingOrderRenewResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_renew_with_options_async(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderRenewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCreatingOrderRenewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.current_expiration_date):
            query['CurrentExpirationDate'] = request.current_expiration_date
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.subscription_duration):
            query['SubscriptionDuration'] = request.subscription_duration
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCreatingOrderRenew',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCreatingOrderRenewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_renew(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderRenewRequest,
    ) -> main_models.SaveSingleTaskForCreatingOrderRenewResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_creating_order_renew_with_options(request, runtime)

    async def save_single_task_for_creating_order_renew_async(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderRenewRequest,
    ) -> main_models.SaveSingleTaskForCreatingOrderRenewResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_creating_order_renew_with_options_async(request, runtime)

    def save_single_task_for_creating_order_transfer_with_options(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCreatingOrderTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorization_code):
            query['AuthorizationCode'] = request.authorization_code
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.permit_premium_transfer):
            query['PermitPremiumTransfer'] = request.permit_premium_transfer
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCreatingOrderTransfer',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCreatingOrderTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_creating_order_transfer_with_options_async(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForCreatingOrderTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorization_code):
            query['AuthorizationCode'] = request.authorization_code
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.permit_premium_transfer):
            query['PermitPremiumTransfer'] = request.permit_premium_transfer
        if not DaraCore.is_null(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not DaraCore.is_null(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForCreatingOrderTransfer',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForCreatingOrderTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_creating_order_transfer(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderTransferRequest,
    ) -> main_models.SaveSingleTaskForCreatingOrderTransferResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_creating_order_transfer_with_options(request, runtime)

    async def save_single_task_for_creating_order_transfer_async(
        self,
        request: main_models.SaveSingleTaskForCreatingOrderTransferRequest,
    ) -> main_models.SaveSingleTaskForCreatingOrderTransferResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_creating_order_transfer_with_options_async(request, runtime)

    def save_single_task_for_deleting_dsrecord_with_options(
        self,
        request: main_models.SaveSingleTaskForDeletingDSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForDeletingDSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForDeletingDSRecord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForDeletingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_deleting_dsrecord_with_options_async(
        self,
        request: main_models.SaveSingleTaskForDeletingDSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForDeletingDSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForDeletingDSRecord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForDeletingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_deleting_dsrecord(
        self,
        request: main_models.SaveSingleTaskForDeletingDSRecordRequest,
    ) -> main_models.SaveSingleTaskForDeletingDSRecordResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_deleting_dsrecord_with_options(request, runtime)

    async def save_single_task_for_deleting_dsrecord_async(
        self,
        request: main_models.SaveSingleTaskForDeletingDSRecordRequest,
    ) -> main_models.SaveSingleTaskForDeletingDSRecordResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_deleting_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_deleting_dns_host_with_options(
        self,
        request: main_models.SaveSingleTaskForDeletingDnsHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForDeletingDnsHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dns_name):
            query['DnsName'] = request.dns_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForDeletingDnsHost',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForDeletingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_deleting_dns_host_with_options_async(
        self,
        request: main_models.SaveSingleTaskForDeletingDnsHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForDeletingDnsHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dns_name):
            query['DnsName'] = request.dns_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForDeletingDnsHost',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForDeletingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_deleting_dns_host(
        self,
        request: main_models.SaveSingleTaskForDeletingDnsHostRequest,
    ) -> main_models.SaveSingleTaskForDeletingDnsHostResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_deleting_dns_host_with_options(request, runtime)

    async def save_single_task_for_deleting_dns_host_async(
        self,
        request: main_models.SaveSingleTaskForDeletingDnsHostRequest,
    ) -> main_models.SaveSingleTaskForDeletingDnsHostResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_deleting_dns_host_with_options_async(request, runtime)

    def save_single_task_for_disassociating_ens_with_options(
        self,
        request: main_models.SaveSingleTaskForDisassociatingEnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForDisassociatingEnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForDisassociatingEns',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForDisassociatingEnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_disassociating_ens_with_options_async(
        self,
        request: main_models.SaveSingleTaskForDisassociatingEnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForDisassociatingEnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForDisassociatingEns',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForDisassociatingEnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_disassociating_ens(
        self,
        request: main_models.SaveSingleTaskForDisassociatingEnsRequest,
    ) -> main_models.SaveSingleTaskForDisassociatingEnsResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_disassociating_ens_with_options(request, runtime)

    async def save_single_task_for_disassociating_ens_async(
        self,
        request: main_models.SaveSingleTaskForDisassociatingEnsRequest,
    ) -> main_models.SaveSingleTaskForDisassociatingEnsResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_disassociating_ens_with_options_async(request, runtime)

    def save_single_task_for_domain_name_proxy_service_with_options(
        self,
        request: main_models.SaveSingleTaskForDomainNameProxyServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForDomainNameProxyService',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForDomainNameProxyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_domain_name_proxy_service_with_options_async(
        self,
        request: main_models.SaveSingleTaskForDomainNameProxyServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForDomainNameProxyService',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForDomainNameProxyServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_domain_name_proxy_service(
        self,
        request: main_models.SaveSingleTaskForDomainNameProxyServiceRequest,
    ) -> main_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_domain_name_proxy_service_with_options(request, runtime)

    async def save_single_task_for_domain_name_proxy_service_async(
        self,
        request: main_models.SaveSingleTaskForDomainNameProxyServiceRequest,
    ) -> main_models.SaveSingleTaskForDomainNameProxyServiceResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_domain_name_proxy_service_with_options_async(request, runtime)

    def save_single_task_for_generate_domain_certificate_with_options(
        self,
        request: main_models.SaveSingleTaskForGenerateDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForGenerateDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForGenerateDomainCertificate',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForGenerateDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_generate_domain_certificate_with_options_async(
        self,
        request: main_models.SaveSingleTaskForGenerateDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForGenerateDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForGenerateDomainCertificate',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForGenerateDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_generate_domain_certificate(
        self,
        request: main_models.SaveSingleTaskForGenerateDomainCertificateRequest,
    ) -> main_models.SaveSingleTaskForGenerateDomainCertificateResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_generate_domain_certificate_with_options(request, runtime)

    async def save_single_task_for_generate_domain_certificate_async(
        self,
        request: main_models.SaveSingleTaskForGenerateDomainCertificateRequest,
    ) -> main_models.SaveSingleTaskForGenerateDomainCertificateResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_generate_domain_certificate_with_options_async(request, runtime)

    def save_single_task_for_modifying_dsrecord_with_options(
        self,
        request: main_models.SaveSingleTaskForModifyingDSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForModifyingDSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.digest_type):
            query['DigestType'] = request.digest_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForModifyingDSRecord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForModifyingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_modifying_dsrecord_with_options_async(
        self,
        request: main_models.SaveSingleTaskForModifyingDSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForModifyingDSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.digest_type):
            query['DigestType'] = request.digest_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForModifyingDSRecord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForModifyingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_modifying_dsrecord(
        self,
        request: main_models.SaveSingleTaskForModifyingDSRecordRequest,
    ) -> main_models.SaveSingleTaskForModifyingDSRecordResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_modifying_dsrecord_with_options(request, runtime)

    async def save_single_task_for_modifying_dsrecord_async(
        self,
        request: main_models.SaveSingleTaskForModifyingDSRecordRequest,
    ) -> main_models.SaveSingleTaskForModifyingDSRecordResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_modifying_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_modifying_dns_host_with_options(
        self,
        request: main_models.SaveSingleTaskForModifyingDnsHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForModifyingDnsHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dns_name):
            query['DnsName'] = request.dns_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForModifyingDnsHost',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForModifyingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_modifying_dns_host_with_options_async(
        self,
        request: main_models.SaveSingleTaskForModifyingDnsHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForModifyingDnsHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dns_name):
            query['DnsName'] = request.dns_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForModifyingDnsHost',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForModifyingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_modifying_dns_host(
        self,
        request: main_models.SaveSingleTaskForModifyingDnsHostRequest,
    ) -> main_models.SaveSingleTaskForModifyingDnsHostResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_modifying_dns_host_with_options(request, runtime)

    async def save_single_task_for_modifying_dns_host_async(
        self,
        request: main_models.SaveSingleTaskForModifyingDnsHostRequest,
    ) -> main_models.SaveSingleTaskForModifyingDnsHostResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_modifying_dns_host_with_options_async(request, runtime)

    def save_single_task_for_querying_transfer_authorization_code_with_options(
        self,
        request: main_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForQueryingTransferAuthorizationCode',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_querying_transfer_authorization_code_with_options_async(
        self,
        request: main_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForQueryingTransferAuthorizationCode',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_querying_transfer_authorization_code(
        self,
        request: main_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
    ) -> main_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_querying_transfer_authorization_code_with_options(request, runtime)

    async def save_single_task_for_querying_transfer_authorization_code_async(
        self,
        request: main_models.SaveSingleTaskForQueryingTransferAuthorizationCodeRequest,
    ) -> main_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_querying_transfer_authorization_code_with_options_async(request, runtime)

    def save_single_task_for_reserve_drop_list_domain_with_options(
        self,
        request: main_models.SaveSingleTaskForReserveDropListDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForReserveDropListDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.dns_1):
            query['Dns1'] = request.dns_1
        if not DaraCore.is_null(request.dns_2):
            query['Dns2'] = request.dns_2
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForReserveDropListDomain',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForReserveDropListDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_reserve_drop_list_domain_with_options_async(
        self,
        request: main_models.SaveSingleTaskForReserveDropListDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForReserveDropListDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.dns_1):
            query['Dns1'] = request.dns_1
        if not DaraCore.is_null(request.dns_2):
            query['Dns2'] = request.dns_2
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForReserveDropListDomain',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForReserveDropListDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_reserve_drop_list_domain(
        self,
        request: main_models.SaveSingleTaskForReserveDropListDomainRequest,
    ) -> main_models.SaveSingleTaskForReserveDropListDomainResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_reserve_drop_list_domain_with_options(request, runtime)

    async def save_single_task_for_reserve_drop_list_domain_async(
        self,
        request: main_models.SaveSingleTaskForReserveDropListDomainRequest,
    ) -> main_models.SaveSingleTaskForReserveDropListDomainResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_reserve_drop_list_domain_with_options_async(request, runtime)

    def save_single_task_for_save_art_extension_with_options(
        self,
        request: main_models.SaveSingleTaskForSaveArtExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForSaveArtExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date_or_period):
            query['DateOrPeriod'] = request.date_or_period
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.features):
            query['Features'] = request.features
        if not DaraCore.is_null(request.inscriptions_and_markings):
            query['InscriptionsAndMarkings'] = request.inscriptions_and_markings
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.maker):
            query['Maker'] = request.maker
        if not DaraCore.is_null(request.materials_and_techniques):
            query['MaterialsAndTechniques'] = request.materials_and_techniques
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.reference):
            query['Reference'] = request.reference
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForSaveArtExtension',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForSaveArtExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_save_art_extension_with_options_async(
        self,
        request: main_models.SaveSingleTaskForSaveArtExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForSaveArtExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date_or_period):
            query['DateOrPeriod'] = request.date_or_period
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.features):
            query['Features'] = request.features
        if not DaraCore.is_null(request.inscriptions_and_markings):
            query['InscriptionsAndMarkings'] = request.inscriptions_and_markings
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.maker):
            query['Maker'] = request.maker
        if not DaraCore.is_null(request.materials_and_techniques):
            query['MaterialsAndTechniques'] = request.materials_and_techniques
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.reference):
            query['Reference'] = request.reference
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForSaveArtExtension',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForSaveArtExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_save_art_extension(
        self,
        request: main_models.SaveSingleTaskForSaveArtExtensionRequest,
    ) -> main_models.SaveSingleTaskForSaveArtExtensionResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_save_art_extension_with_options(request, runtime)

    async def save_single_task_for_save_art_extension_async(
        self,
        request: main_models.SaveSingleTaskForSaveArtExtensionRequest,
    ) -> main_models.SaveSingleTaskForSaveArtExtensionResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_save_art_extension_with_options_async(request, runtime)

    def save_single_task_for_synchronizing_dsrecord_with_options(
        self,
        request: main_models.SaveSingleTaskForSynchronizingDSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForSynchronizingDSRecord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForSynchronizingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_synchronizing_dsrecord_with_options_async(
        self,
        request: main_models.SaveSingleTaskForSynchronizingDSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForSynchronizingDSRecord',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForSynchronizingDSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_synchronizing_dsrecord(
        self,
        request: main_models.SaveSingleTaskForSynchronizingDSRecordRequest,
    ) -> main_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_synchronizing_dsrecord_with_options(request, runtime)

    async def save_single_task_for_synchronizing_dsrecord_async(
        self,
        request: main_models.SaveSingleTaskForSynchronizingDSRecordRequest,
    ) -> main_models.SaveSingleTaskForSynchronizingDSRecordResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_synchronizing_dsrecord_with_options_async(request, runtime)

    def save_single_task_for_synchronizing_dns_host_with_options(
        self,
        request: main_models.SaveSingleTaskForSynchronizingDnsHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForSynchronizingDnsHost',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForSynchronizingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_synchronizing_dns_host_with_options_async(
        self,
        request: main_models.SaveSingleTaskForSynchronizingDnsHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForSynchronizingDnsHost',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForSynchronizingDnsHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_synchronizing_dns_host(
        self,
        request: main_models.SaveSingleTaskForSynchronizingDnsHostRequest,
    ) -> main_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_synchronizing_dns_host_with_options(request, runtime)

    async def save_single_task_for_synchronizing_dns_host_async(
        self,
        request: main_models.SaveSingleTaskForSynchronizingDnsHostRequest,
    ) -> main_models.SaveSingleTaskForSynchronizingDnsHostResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_synchronizing_dns_host_with_options_async(request, runtime)

    def save_single_task_for_transfer_out_by_authorization_code_with_options(
        self,
        request: main_models.SaveSingleTaskForTransferOutByAuthorizationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForTransferOutByAuthorizationCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorization_code):
            query['AuthorizationCode'] = request.authorization_code
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForTransferOutByAuthorizationCode',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForTransferOutByAuthorizationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_transfer_out_by_authorization_code_with_options_async(
        self,
        request: main_models.SaveSingleTaskForTransferOutByAuthorizationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForTransferOutByAuthorizationCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorization_code):
            query['AuthorizationCode'] = request.authorization_code
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForTransferOutByAuthorizationCode',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForTransferOutByAuthorizationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_transfer_out_by_authorization_code(
        self,
        request: main_models.SaveSingleTaskForTransferOutByAuthorizationCodeRequest,
    ) -> main_models.SaveSingleTaskForTransferOutByAuthorizationCodeResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_transfer_out_by_authorization_code_with_options(request, runtime)

    async def save_single_task_for_transfer_out_by_authorization_code_async(
        self,
        request: main_models.SaveSingleTaskForTransferOutByAuthorizationCodeRequest,
    ) -> main_models.SaveSingleTaskForTransferOutByAuthorizationCodeResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_transfer_out_by_authorization_code_with_options_async(request, runtime)

    def save_single_task_for_transfer_prohibition_lock_with_options(
        self,
        request: main_models.SaveSingleTaskForTransferProhibitionLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForTransferProhibitionLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForTransferProhibitionLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForTransferProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_transfer_prohibition_lock_with_options_async(
        self,
        request: main_models.SaveSingleTaskForTransferProhibitionLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForTransferProhibitionLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForTransferProhibitionLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForTransferProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_transfer_prohibition_lock(
        self,
        request: main_models.SaveSingleTaskForTransferProhibitionLockRequest,
    ) -> main_models.SaveSingleTaskForTransferProhibitionLockResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_transfer_prohibition_lock_with_options(request, runtime)

    async def save_single_task_for_transfer_prohibition_lock_async(
        self,
        request: main_models.SaveSingleTaskForTransferProhibitionLockRequest,
    ) -> main_models.SaveSingleTaskForTransferProhibitionLockResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_transfer_prohibition_lock_with_options_async(request, runtime)

    def save_single_task_for_update_prohibition_lock_with_options(
        self,
        request: main_models.SaveSingleTaskForUpdateProhibitionLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForUpdateProhibitionLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForUpdateProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_update_prohibition_lock_with_options_async(
        self,
        request: main_models.SaveSingleTaskForUpdateProhibitionLockRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForUpdateProhibitionLock',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForUpdateProhibitionLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_update_prohibition_lock(
        self,
        request: main_models.SaveSingleTaskForUpdateProhibitionLockRequest,
    ) -> main_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_update_prohibition_lock_with_options(request, runtime)

    async def save_single_task_for_update_prohibition_lock_async(
        self,
        request: main_models.SaveSingleTaskForUpdateProhibitionLockRequest,
    ) -> main_models.SaveSingleTaskForUpdateProhibitionLockResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_update_prohibition_lock_with_options_async(request, runtime)

    def save_single_task_for_updating_contact_info_with_options(
        self,
        request: main_models.SaveSingleTaskForUpdatingContactInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForUpdatingContactInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForUpdatingContactInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForUpdatingContactInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_single_task_for_updating_contact_info_with_options_async(
        self,
        request: main_models.SaveSingleTaskForUpdatingContactInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveSingleTaskForUpdatingContactInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveSingleTaskForUpdatingContactInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSingleTaskForUpdatingContactInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_single_task_for_updating_contact_info(
        self,
        request: main_models.SaveSingleTaskForUpdatingContactInfoRequest,
    ) -> main_models.SaveSingleTaskForUpdatingContactInfoResponse:
        runtime = RuntimeOptions()
        return self.save_single_task_for_updating_contact_info_with_options(request, runtime)

    async def save_single_task_for_updating_contact_info_async(
        self,
        request: main_models.SaveSingleTaskForUpdatingContactInfoRequest,
    ) -> main_models.SaveSingleTaskForUpdatingContactInfoResponse:
        runtime = RuntimeOptions()
        return await self.save_single_task_for_updating_contact_info_with_options_async(request, runtime)

    def save_task_for_submitting_domain_delete_with_options(
        self,
        request: main_models.SaveTaskForSubmittingDomainDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForSubmittingDomainDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForSubmittingDomainDelete',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForSubmittingDomainDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_submitting_domain_delete_with_options_async(
        self,
        request: main_models.SaveTaskForSubmittingDomainDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForSubmittingDomainDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForSubmittingDomainDelete',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForSubmittingDomainDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_submitting_domain_delete(
        self,
        request: main_models.SaveTaskForSubmittingDomainDeleteRequest,
    ) -> main_models.SaveTaskForSubmittingDomainDeleteResponse:
        runtime = RuntimeOptions()
        return self.save_task_for_submitting_domain_delete_with_options(request, runtime)

    async def save_task_for_submitting_domain_delete_async(
        self,
        request: main_models.SaveTaskForSubmittingDomainDeleteRequest,
    ) -> main_models.SaveTaskForSubmittingDomainDeleteResponse:
        runtime = RuntimeOptions()
        return await self.save_task_for_submitting_domain_delete_with_options_async(request, runtime)

    def save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options(
        self,
        request: main_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not DaraCore.is_null(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredential',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options_async(
        self,
        request: main_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not DaraCore.is_null(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredential',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_submitting_domain_real_name_verification_by_identity_credential(
        self,
        request: main_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
    ) -> main_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        runtime = RuntimeOptions()
        return self.save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options(request, runtime)

    async def save_task_for_submitting_domain_real_name_verification_by_identity_credential_async(
        self,
        request: main_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest,
    ) -> main_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse:
        runtime = RuntimeOptions()
        return await self.save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options_async(request, runtime)

    def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options(
        self,
        request: main_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileID',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options_async(
        self,
        request: main_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileID',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_id(
        self,
        request: main_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
    ) -> main_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        runtime = RuntimeOptions()
        return self.save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options(request, runtime)

    async def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_id_async(
        self,
        request: main_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest,
    ) -> main_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse:
        runtime = RuntimeOptions()
        return await self.save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options_async(request, runtime)

    def save_task_for_updating_registrant_info_by_identity_credential_with_options(
        self,
        request: main_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not DaraCore.is_null(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        body = {}
        if not DaraCore.is_null(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForUpdatingRegistrantInfoByIdentityCredential',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_updating_registrant_info_by_identity_credential_with_options_async(
        self,
        request: main_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not DaraCore.is_null(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        body = {}
        if not DaraCore.is_null(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForUpdatingRegistrantInfoByIdentityCredential',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_updating_registrant_info_by_identity_credential(
        self,
        request: main_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
    ) -> main_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        runtime = RuntimeOptions()
        return self.save_task_for_updating_registrant_info_by_identity_credential_with_options(request, runtime)

    async def save_task_for_updating_registrant_info_by_identity_credential_async(
        self,
        request: main_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest,
    ) -> main_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse:
        runtime = RuntimeOptions()
        return await self.save_task_for_updating_registrant_info_by_identity_credential_with_options_async(request, runtime)

    def save_task_for_updating_registrant_info_by_registrant_profile_idwith_options(
        self,
        request: main_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForUpdatingRegistrantInfoByRegistrantProfileID',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_updating_registrant_info_by_registrant_profile_idwith_options_async(
        self,
        request: main_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForUpdatingRegistrantInfoByRegistrantProfileID',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_updating_registrant_info_by_registrant_profile_id(
        self,
        request: main_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
    ) -> main_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        runtime = RuntimeOptions()
        return self.save_task_for_updating_registrant_info_by_registrant_profile_idwith_options(request, runtime)

    async def save_task_for_updating_registrant_info_by_registrant_profile_id_async(
        self,
        request: main_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest,
    ) -> main_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse:
        runtime = RuntimeOptions()
        return await self.save_task_for_updating_registrant_info_by_registrant_profile_idwith_options_async(request, runtime)

    def scroll_domain_list_with_options(
        self,
        request: main_models.ScrollDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ScrollDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not DaraCore.is_null(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not DaraCore.is_null(request.end_length):
            query['EndLength'] = request.end_length
        if not DaraCore.is_null(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not DaraCore.is_null(request.excluded):
            query['Excluded'] = request.excluded
        if not DaraCore.is_null(request.excluded_prefix):
            query['ExcludedPrefix'] = request.excluded_prefix
        if not DaraCore.is_null(request.excluded_suffix):
            query['ExcludedSuffix'] = request.excluded_suffix
        if not DaraCore.is_null(request.form):
            query['Form'] = request.form
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.key_word_prefix):
            query['KeyWordPrefix'] = request.key_word_prefix
        if not DaraCore.is_null(request.key_word_suffix):
            query['KeyWordSuffix'] = request.key_word_suffix
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scroll_id):
            query['ScrollId'] = request.scroll_id
        if not DaraCore.is_null(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not DaraCore.is_null(request.start_length):
            query['StartLength'] = request.start_length
        if not DaraCore.is_null(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not DaraCore.is_null(request.suffixs):
            query['Suffixs'] = request.suffixs
        if not DaraCore.is_null(request.trade_type):
            query['TradeType'] = request.trade_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScrollDomainList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScrollDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def scroll_domain_list_with_options_async(
        self,
        request: main_models.ScrollDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ScrollDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not DaraCore.is_null(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not DaraCore.is_null(request.end_length):
            query['EndLength'] = request.end_length
        if not DaraCore.is_null(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not DaraCore.is_null(request.excluded):
            query['Excluded'] = request.excluded
        if not DaraCore.is_null(request.excluded_prefix):
            query['ExcludedPrefix'] = request.excluded_prefix
        if not DaraCore.is_null(request.excluded_suffix):
            query['ExcludedSuffix'] = request.excluded_suffix
        if not DaraCore.is_null(request.form):
            query['Form'] = request.form
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.key_word_prefix):
            query['KeyWordPrefix'] = request.key_word_prefix
        if not DaraCore.is_null(request.key_word_suffix):
            query['KeyWordSuffix'] = request.key_word_suffix
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scroll_id):
            query['ScrollId'] = request.scroll_id
        if not DaraCore.is_null(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not DaraCore.is_null(request.start_length):
            query['StartLength'] = request.start_length
        if not DaraCore.is_null(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not DaraCore.is_null(request.suffixs):
            query['Suffixs'] = request.suffixs
        if not DaraCore.is_null(request.trade_type):
            query['TradeType'] = request.trade_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScrollDomainList',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScrollDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scroll_domain_list(
        self,
        request: main_models.ScrollDomainListRequest,
    ) -> main_models.ScrollDomainListResponse:
        runtime = RuntimeOptions()
        return self.scroll_domain_list_with_options(request, runtime)

    async def scroll_domain_list_async(
        self,
        request: main_models.ScrollDomainListRequest,
    ) -> main_models.ScrollDomainListResponse:
        runtime = RuntimeOptions()
        return await self.scroll_domain_list_with_options_async(request, runtime)

    def set_default_registrant_profile_with_options(
        self,
        request: main_models.SetDefaultRegistrantProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultRegistrantProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultRegistrantProfile',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultRegistrantProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_registrant_profile_with_options_async(
        self,
        request: main_models.SetDefaultRegistrantProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultRegistrantProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultRegistrantProfile',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultRegistrantProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_registrant_profile(
        self,
        request: main_models.SetDefaultRegistrantProfileRequest,
    ) -> main_models.SetDefaultRegistrantProfileResponse:
        runtime = RuntimeOptions()
        return self.set_default_registrant_profile_with_options(request, runtime)

    async def set_default_registrant_profile_async(
        self,
        request: main_models.SetDefaultRegistrantProfileRequest,
    ) -> main_models.SetDefaultRegistrantProfileResponse:
        runtime = RuntimeOptions()
        return await self.set_default_registrant_profile_with_options_async(request, runtime)

    def setup_domain_auto_renew_with_options(
        self,
        request: main_models.SetupDomainAutoRenewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetupDomainAutoRenewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetupDomainAutoRenew',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetupDomainAutoRenewResponse(),
            self.call_api(params, req, runtime)
        )

    async def setup_domain_auto_renew_with_options_async(
        self,
        request: main_models.SetupDomainAutoRenewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetupDomainAutoRenewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetupDomainAutoRenew',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetupDomainAutoRenewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def setup_domain_auto_renew(
        self,
        request: main_models.SetupDomainAutoRenewRequest,
    ) -> main_models.SetupDomainAutoRenewResponse:
        runtime = RuntimeOptions()
        return self.setup_domain_auto_renew_with_options(request, runtime)

    async def setup_domain_auto_renew_async(
        self,
        request: main_models.SetupDomainAutoRenewRequest,
    ) -> main_models.SetupDomainAutoRenewResponse:
        runtime = RuntimeOptions()
        return await self.setup_domain_auto_renew_with_options_async(request, runtime)

    def submit_domain_special_biz_credentials_with_options(
        self,
        request: main_models.SubmitDomainSpecialBizCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDomainSpecialBizCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.credentials):
            body['Credentials'] = request.credentials
        if not DaraCore.is_null(request.extend):
            body['Extend'] = request.extend
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDomainSpecialBizCredentials',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDomainSpecialBizCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_domain_special_biz_credentials_with_options_async(
        self,
        request: main_models.SubmitDomainSpecialBizCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDomainSpecialBizCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.biz_id):
            body['BizId'] = request.biz_id
        if not DaraCore.is_null(request.credentials):
            body['Credentials'] = request.credentials
        if not DaraCore.is_null(request.extend):
            body['Extend'] = request.extend
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDomainSpecialBizCredentials',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDomainSpecialBizCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_domain_special_biz_credentials(
        self,
        request: main_models.SubmitDomainSpecialBizCredentialsRequest,
    ) -> main_models.SubmitDomainSpecialBizCredentialsResponse:
        runtime = RuntimeOptions()
        return self.submit_domain_special_biz_credentials_with_options(request, runtime)

    async def submit_domain_special_biz_credentials_async(
        self,
        request: main_models.SubmitDomainSpecialBizCredentialsRequest,
    ) -> main_models.SubmitDomainSpecialBizCredentialsResponse:
        runtime = RuntimeOptions()
        return await self.submit_domain_special_biz_credentials_with_options_async(request, runtime)

    def submit_email_verification_with_options(
        self,
        request: main_models.SubmitEmailVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitEmailVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.send_if_exist):
            query['SendIfExist'] = request.send_if_exist
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitEmailVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_email_verification_with_options_async(
        self,
        request: main_models.SubmitEmailVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitEmailVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.send_if_exist):
            query['SendIfExist'] = request.send_if_exist
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitEmailVerification',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitEmailVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_email_verification(
        self,
        request: main_models.SubmitEmailVerificationRequest,
    ) -> main_models.SubmitEmailVerificationResponse:
        runtime = RuntimeOptions()
        return self.submit_email_verification_with_options(request, runtime)

    async def submit_email_verification_async(
        self,
        request: main_models.SubmitEmailVerificationRequest,
    ) -> main_models.SubmitEmailVerificationResponse:
        runtime = RuntimeOptions()
        return await self.submit_email_verification_with_options_async(request, runtime)

    def submit_operation_audit_info_with_options(
        self,
        request: main_models.SubmitOperationAuditInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitOperationAuditInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_info):
            query['AuditInfo'] = request.audit_info
        if not DaraCore.is_null(request.audit_type):
            query['AuditType'] = request.audit_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitOperationAuditInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitOperationAuditInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_operation_audit_info_with_options_async(
        self,
        request: main_models.SubmitOperationAuditInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitOperationAuditInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_info):
            query['AuditInfo'] = request.audit_info
        if not DaraCore.is_null(request.audit_type):
            query['AuditType'] = request.audit_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitOperationAuditInfo',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitOperationAuditInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_operation_audit_info(
        self,
        request: main_models.SubmitOperationAuditInfoRequest,
    ) -> main_models.SubmitOperationAuditInfoResponse:
        runtime = RuntimeOptions()
        return self.submit_operation_audit_info_with_options(request, runtime)

    async def submit_operation_audit_info_async(
        self,
        request: main_models.SubmitOperationAuditInfoRequest,
    ) -> main_models.SubmitOperationAuditInfoResponse:
        runtime = RuntimeOptions()
        return await self.submit_operation_audit_info_with_options_async(request, runtime)

    def submit_operation_credentials_with_options(
        self,
        request: main_models.SubmitOperationCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitOperationCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not DaraCore.is_null(request.audit_type):
            query['AuditType'] = request.audit_type
        if not DaraCore.is_null(request.credentials):
            query['Credentials'] = request.credentials
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_type):
            query['RegType'] = request.reg_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitOperationCredentials',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitOperationCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_operation_credentials_with_options_async(
        self,
        request: main_models.SubmitOperationCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitOperationCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_record_id):
            query['AuditRecordId'] = request.audit_record_id
        if not DaraCore.is_null(request.audit_type):
            query['AuditType'] = request.audit_type
        if not DaraCore.is_null(request.credentials):
            query['Credentials'] = request.credentials
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.reg_type):
            query['RegType'] = request.reg_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitOperationCredentials',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitOperationCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_operation_credentials(
        self,
        request: main_models.SubmitOperationCredentialsRequest,
    ) -> main_models.SubmitOperationCredentialsResponse:
        runtime = RuntimeOptions()
        return self.submit_operation_credentials_with_options(request, runtime)

    async def submit_operation_credentials_async(
        self,
        request: main_models.SubmitOperationCredentialsRequest,
    ) -> main_models.SubmitOperationCredentialsResponse:
        runtime = RuntimeOptions()
        return await self.submit_operation_credentials_with_options_async(request, runtime)

    def transfer_in_check_mail_token_with_options(
        self,
        request: main_models.TransferInCheckMailTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferInCheckMailTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferInCheckMailToken',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferInCheckMailTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_check_mail_token_with_options_async(
        self,
        request: main_models.TransferInCheckMailTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferInCheckMailTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferInCheckMailToken',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferInCheckMailTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_check_mail_token(
        self,
        request: main_models.TransferInCheckMailTokenRequest,
    ) -> main_models.TransferInCheckMailTokenResponse:
        runtime = RuntimeOptions()
        return self.transfer_in_check_mail_token_with_options(request, runtime)

    async def transfer_in_check_mail_token_async(
        self,
        request: main_models.TransferInCheckMailTokenRequest,
    ) -> main_models.TransferInCheckMailTokenResponse:
        runtime = RuntimeOptions()
        return await self.transfer_in_check_mail_token_with_options_async(request, runtime)

    def transfer_in_reenter_transfer_authorization_code_with_options(
        self,
        request: main_models.TransferInReenterTransferAuthorizationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferInReenterTransferAuthorizationCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.transfer_authorization_code):
            query['TransferAuthorizationCode'] = request.transfer_authorization_code
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferInReenterTransferAuthorizationCode',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferInReenterTransferAuthorizationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_reenter_transfer_authorization_code_with_options_async(
        self,
        request: main_models.TransferInReenterTransferAuthorizationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferInReenterTransferAuthorizationCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.transfer_authorization_code):
            query['TransferAuthorizationCode'] = request.transfer_authorization_code
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferInReenterTransferAuthorizationCode',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferInReenterTransferAuthorizationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_reenter_transfer_authorization_code(
        self,
        request: main_models.TransferInReenterTransferAuthorizationCodeRequest,
    ) -> main_models.TransferInReenterTransferAuthorizationCodeResponse:
        runtime = RuntimeOptions()
        return self.transfer_in_reenter_transfer_authorization_code_with_options(request, runtime)

    async def transfer_in_reenter_transfer_authorization_code_async(
        self,
        request: main_models.TransferInReenterTransferAuthorizationCodeRequest,
    ) -> main_models.TransferInReenterTransferAuthorizationCodeResponse:
        runtime = RuntimeOptions()
        return await self.transfer_in_reenter_transfer_authorization_code_with_options_async(request, runtime)

    def transfer_in_refetch_whois_email_with_options(
        self,
        request: main_models.TransferInRefetchWhoisEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferInRefetchWhoisEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferInRefetchWhoisEmail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferInRefetchWhoisEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_refetch_whois_email_with_options_async(
        self,
        request: main_models.TransferInRefetchWhoisEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferInRefetchWhoisEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferInRefetchWhoisEmail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferInRefetchWhoisEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_refetch_whois_email(
        self,
        request: main_models.TransferInRefetchWhoisEmailRequest,
    ) -> main_models.TransferInRefetchWhoisEmailResponse:
        runtime = RuntimeOptions()
        return self.transfer_in_refetch_whois_email_with_options(request, runtime)

    async def transfer_in_refetch_whois_email_async(
        self,
        request: main_models.TransferInRefetchWhoisEmailRequest,
    ) -> main_models.TransferInRefetchWhoisEmailResponse:
        runtime = RuntimeOptions()
        return await self.transfer_in_refetch_whois_email_with_options_async(request, runtime)

    def transfer_in_resend_mail_token_with_options(
        self,
        request: main_models.TransferInResendMailTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferInResendMailTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferInResendMailToken',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferInResendMailTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_in_resend_mail_token_with_options_async(
        self,
        request: main_models.TransferInResendMailTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferInResendMailTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferInResendMailToken',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferInResendMailTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_in_resend_mail_token(
        self,
        request: main_models.TransferInResendMailTokenRequest,
    ) -> main_models.TransferInResendMailTokenResponse:
        runtime = RuntimeOptions()
        return self.transfer_in_resend_mail_token_with_options(request, runtime)

    async def transfer_in_resend_mail_token_async(
        self,
        request: main_models.TransferInResendMailTokenRequest,
    ) -> main_models.TransferInResendMailTokenResponse:
        runtime = RuntimeOptions()
        return await self.transfer_in_resend_mail_token_with_options_async(request, runtime)

    def update_domain_to_domain_group_with_options(
        self,
        request: main_models.UpdateDomainToDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainToDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source):
            query['DataSource'] = request.data_source
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.replace):
            query['Replace'] = request.replace
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.file_to_upload):
            body['FileToUpload'] = request.file_to_upload
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainToDomainGroup',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainToDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_to_domain_group_with_options_async(
        self,
        request: main_models.UpdateDomainToDomainGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainToDomainGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source):
            query['DataSource'] = request.data_source
        if not DaraCore.is_null(request.domain_group_id):
            query['DomainGroupId'] = request.domain_group_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.replace):
            query['Replace'] = request.replace
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not DaraCore.is_null(request.file_to_upload):
            body['FileToUpload'] = request.file_to_upload
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainToDomainGroup',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainToDomainGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_to_domain_group(
        self,
        request: main_models.UpdateDomainToDomainGroupRequest,
    ) -> main_models.UpdateDomainToDomainGroupResponse:
        runtime = RuntimeOptions()
        return self.update_domain_to_domain_group_with_options(request, runtime)

    async def update_domain_to_domain_group_async(
        self,
        request: main_models.UpdateDomainToDomainGroupRequest,
    ) -> main_models.UpdateDomainToDomainGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_domain_to_domain_group_with_options_async(request, runtime)

    def verify_contact_field_with_options(
        self,
        request: main_models.VerifyContactFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyContactFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyContactField',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyContactFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_contact_field_with_options_async(
        self,
        request: main_models.VerifyContactFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyContactFieldResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not DaraCore.is_null(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not DaraCore.is_null(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.zh_address):
            query['ZhAddress'] = request.zh_address
        if not DaraCore.is_null(request.zh_city):
            query['ZhCity'] = request.zh_city
        if not DaraCore.is_null(request.zh_province):
            query['ZhProvince'] = request.zh_province
        if not DaraCore.is_null(request.zh_registrant_name):
            query['ZhRegistrantName'] = request.zh_registrant_name
        if not DaraCore.is_null(request.zh_registrant_organization):
            query['ZhRegistrantOrganization'] = request.zh_registrant_organization
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyContactField',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyContactFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_contact_field(
        self,
        request: main_models.VerifyContactFieldRequest,
    ) -> main_models.VerifyContactFieldResponse:
        runtime = RuntimeOptions()
        return self.verify_contact_field_with_options(request, runtime)

    async def verify_contact_field_async(
        self,
        request: main_models.VerifyContactFieldRequest,
    ) -> main_models.VerifyContactFieldResponse:
        runtime = RuntimeOptions()
        return await self.verify_contact_field_with_options_async(request, runtime)

    def verify_email_with_options(
        self,
        request: main_models.VerifyEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyEmail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_email_with_options_async(
        self,
        request: main_models.VerifyEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyEmail',
            version = '2018-01-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_email(
        self,
        request: main_models.VerifyEmailRequest,
    ) -> main_models.VerifyEmailResponse:
        runtime = RuntimeOptions()
        return self.verify_email_with_options(request, runtime)

    async def verify_email_async(
        self,
        request: main_models.VerifyEmailRequest,
    ) -> main_models.VerifyEmailResponse:
        runtime = RuntimeOptions()
        return await self.verify_email_with_options_async(request, runtime)
