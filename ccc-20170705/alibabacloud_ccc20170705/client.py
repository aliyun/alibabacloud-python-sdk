# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ccc20170705 import models as ccc20170705_models
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
        self._endpoint_map = {
            'ap-northeast-1': 'ccc.aliyuncs.com',
            'ap-south-1': 'ccc.aliyuncs.com',
            'ap-southeast-1': 'ccc.aliyuncs.com',
            'ap-southeast-2': 'ccc.aliyuncs.com',
            'ap-southeast-3': 'ccc.aliyuncs.com',
            'ap-southeast-5': 'ccc.aliyuncs.com',
            'cn-beijing': 'ccc.aliyuncs.com',
            'cn-chengdu': 'ccc.aliyuncs.com',
            'cn-hongkong': 'ccc.aliyuncs.com',
            'cn-huhehaote': 'ccc.aliyuncs.com',
            'cn-qingdao': 'ccc.aliyuncs.com',
            'cn-shenzhen': 'ccc.aliyuncs.com',
            'cn-zhangjiakou': 'ccc.aliyuncs.com',
            'eu-central-1': 'ccc.aliyuncs.com',
            'eu-west-1': 'ccc.aliyuncs.com',
            'me-east-1': 'ccc.aliyuncs.com',
            'us-east-1': 'ccc.aliyuncs.com',
            'us-west-1': 'ccc.aliyuncs.com',
            'cn-hangzhou-finance': 'ccc.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ccc.aliyuncs.com',
            'cn-shanghai-finance-1': 'ccc.aliyuncs.com',
            'cn-north-2-gov-1': 'ccc.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ccc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abort_predictive_jobs_with_options(
        self,
        request: ccc20170705_models.AbortPredictiveJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AbortPredictiveJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AbortPredictiveJobsResponse(),
            self.do_rpcrequest('AbortPredictiveJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def abort_predictive_jobs_with_options_async(
        self,
        request: ccc20170705_models.AbortPredictiveJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AbortPredictiveJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AbortPredictiveJobsResponse(),
            await self.do_rpcrequest_async('AbortPredictiveJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def abort_predictive_jobs(
        self,
        request: ccc20170705_models.AbortPredictiveJobsRequest,
    ) -> ccc20170705_models.AbortPredictiveJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.abort_predictive_jobs_with_options(request, runtime)

    async def abort_predictive_jobs_async(
        self,
        request: ccc20170705_models.AbortPredictiveJobsRequest,
    ) -> ccc20170705_models.AbortPredictiveJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abort_predictive_jobs_with_options_async(request, runtime)

    def add_agent_device_with_options(
        self,
        request: ccc20170705_models.AddAgentDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AddAgentDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AddAgentDeviceResponse(),
            self.do_rpcrequest('AddAgentDevice', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_agent_device_with_options_async(
        self,
        request: ccc20170705_models.AddAgentDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AddAgentDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AddAgentDeviceResponse(),
            await self.do_rpcrequest_async('AddAgentDevice', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_agent_device(
        self,
        request: ccc20170705_models.AddAgentDeviceRequest,
    ) -> ccc20170705_models.AddAgentDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_agent_device_with_options(request, runtime)

    async def add_agent_device_async(
        self,
        request: ccc20170705_models.AddAgentDeviceRequest,
    ) -> ccc20170705_models.AddAgentDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_agent_device_with_options_async(request, runtime)

    def add_bulk_phone_numbers_with_options(
        self,
        request: ccc20170705_models.AddBulkPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AddBulkPhoneNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AddBulkPhoneNumbersResponse(),
            self.do_rpcrequest('AddBulkPhoneNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_bulk_phone_numbers_with_options_async(
        self,
        request: ccc20170705_models.AddBulkPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AddBulkPhoneNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AddBulkPhoneNumbersResponse(),
            await self.do_rpcrequest_async('AddBulkPhoneNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_bulk_phone_numbers(
        self,
        request: ccc20170705_models.AddBulkPhoneNumbersRequest,
    ) -> ccc20170705_models.AddBulkPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_bulk_phone_numbers_with_options(request, runtime)

    async def add_bulk_phone_numbers_async(
        self,
        request: ccc20170705_models.AddBulkPhoneNumbersRequest,
    ) -> ccc20170705_models.AddBulkPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_bulk_phone_numbers_with_options_async(request, runtime)

    def add_jobs_to_predictive_job_group_with_options(
        self,
        request: ccc20170705_models.AddJobsToPredictiveJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AddJobsToPredictiveJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AddJobsToPredictiveJobGroupResponse(),
            self.do_rpcrequest('AddJobsToPredictiveJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_jobs_to_predictive_job_group_with_options_async(
        self,
        request: ccc20170705_models.AddJobsToPredictiveJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AddJobsToPredictiveJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AddJobsToPredictiveJobGroupResponse(),
            await self.do_rpcrequest_async('AddJobsToPredictiveJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_jobs_to_predictive_job_group(
        self,
        request: ccc20170705_models.AddJobsToPredictiveJobGroupRequest,
    ) -> ccc20170705_models.AddJobsToPredictiveJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_jobs_to_predictive_job_group_with_options(request, runtime)

    async def add_jobs_to_predictive_job_group_async(
        self,
        request: ccc20170705_models.AddJobsToPredictiveJobGroupRequest,
    ) -> ccc20170705_models.AddJobsToPredictiveJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_jobs_to_predictive_job_group_with_options_async(request, runtime)

    def add_phone_number_with_options(
        self,
        request: ccc20170705_models.AddPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AddPhoneNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AddPhoneNumberResponse(),
            self.do_rpcrequest('AddPhoneNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_phone_number_with_options_async(
        self,
        request: ccc20170705_models.AddPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AddPhoneNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AddPhoneNumberResponse(),
            await self.do_rpcrequest_async('AddPhoneNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_phone_number(
        self,
        request: ccc20170705_models.AddPhoneNumberRequest,
    ) -> ccc20170705_models.AddPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_phone_number_with_options(request, runtime)

    async def add_phone_number_async(
        self,
        request: ccc20170705_models.AddPhoneNumberRequest,
    ) -> ccc20170705_models.AddPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_phone_number_with_options_async(request, runtime)

    def add_phone_tags_with_options(
        self,
        request: ccc20170705_models.AddPhoneTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AddPhoneTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AddPhoneTagsResponse(),
            self.do_rpcrequest('AddPhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_phone_tags_with_options_async(
        self,
        request: ccc20170705_models.AddPhoneTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AddPhoneTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AddPhoneTagsResponse(),
            await self.do_rpcrequest_async('AddPhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_phone_tags(
        self,
        request: ccc20170705_models.AddPhoneTagsRequest,
    ) -> ccc20170705_models.AddPhoneTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_phone_tags_with_options(request, runtime)

    async def add_phone_tags_async(
        self,
        request: ccc20170705_models.AddPhoneTagsRequest,
    ) -> ccc20170705_models.AddPhoneTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_phone_tags_with_options_async(request, runtime)

    def assign_jobs_with_options(
        self,
        request: ccc20170705_models.AssignJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AssignJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AssignJobsResponse(),
            self.do_rpcrequest('AssignJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assign_jobs_with_options_async(
        self,
        request: ccc20170705_models.AssignJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AssignJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AssignJobsResponse(),
            await self.do_rpcrequest_async('AssignJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_jobs(
        self,
        request: ccc20170705_models.AssignJobsRequest,
    ) -> ccc20170705_models.AssignJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.assign_jobs_with_options(request, runtime)

    async def assign_jobs_async(
        self,
        request: ccc20170705_models.AssignJobsRequest,
    ) -> ccc20170705_models.AssignJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_jobs_with_options_async(request, runtime)

    def assign_users_with_options(
        self,
        request: ccc20170705_models.AssignUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AssignUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AssignUsersResponse(),
            self.do_rpcrequest('AssignUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assign_users_with_options_async(
        self,
        request: ccc20170705_models.AssignUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.AssignUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.AssignUsersResponse(),
            await self.do_rpcrequest_async('AssignUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_users(
        self,
        request: ccc20170705_models.AssignUsersRequest,
    ) -> ccc20170705_models.AssignUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.assign_users_with_options(request, runtime)

    async def assign_users_async(
        self,
        request: ccc20170705_models.AssignUsersRequest,
    ) -> ccc20170705_models.AssignUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_users_with_options_async(request, runtime)

    def call_online_privacy_number_with_options(
        self,
        request: ccc20170705_models.CallOnlinePrivacyNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CallOnlinePrivacyNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CallOnlinePrivacyNumberResponse(),
            self.do_rpcrequest('CallOnlinePrivacyNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def call_online_privacy_number_with_options_async(
        self,
        request: ccc20170705_models.CallOnlinePrivacyNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CallOnlinePrivacyNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CallOnlinePrivacyNumberResponse(),
            await self.do_rpcrequest_async('CallOnlinePrivacyNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def call_online_privacy_number(
        self,
        request: ccc20170705_models.CallOnlinePrivacyNumberRequest,
    ) -> ccc20170705_models.CallOnlinePrivacyNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.call_online_privacy_number_with_options(request, runtime)

    async def call_online_privacy_number_async(
        self,
        request: ccc20170705_models.CallOnlinePrivacyNumberRequest,
    ) -> ccc20170705_models.CallOnlinePrivacyNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.call_online_privacy_number_with_options_async(request, runtime)

    def cancel_jobs_with_options(
        self,
        request: ccc20170705_models.CancelJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CancelJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CancelJobsResponse(),
            self.do_rpcrequest('CancelJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_jobs_with_options_async(
        self,
        request: ccc20170705_models.CancelJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CancelJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CancelJobsResponse(),
            await self.do_rpcrequest_async('CancelJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_jobs(
        self,
        request: ccc20170705_models.CancelJobsRequest,
    ) -> ccc20170705_models.CancelJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_jobs_with_options(request, runtime)

    async def cancel_jobs_async(
        self,
        request: ccc20170705_models.CancelJobsRequest,
    ) -> ccc20170705_models.CancelJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_jobs_with_options_async(request, runtime)

    def check_number_avaliable_with_options(
        self,
        request: ccc20170705_models.CheckNumberAvaliableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CheckNumberAvaliableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CheckNumberAvaliableResponse(),
            self.do_rpcrequest('CheckNumberAvaliable', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_number_avaliable_with_options_async(
        self,
        request: ccc20170705_models.CheckNumberAvaliableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CheckNumberAvaliableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CheckNumberAvaliableResponse(),
            await self.do_rpcrequest_async('CheckNumberAvaliable', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_number_avaliable(
        self,
        request: ccc20170705_models.CheckNumberAvaliableRequest,
    ) -> ccc20170705_models.CheckNumberAvaliableResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_number_avaliable_with_options(request, runtime)

    async def check_number_avaliable_async(
        self,
        request: ccc20170705_models.CheckNumberAvaliableRequest,
    ) -> ccc20170705_models.CheckNumberAvaliableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_number_avaliable_with_options_async(request, runtime)

    def commit_contact_flow_version_modification_with_options(
        self,
        request: ccc20170705_models.CommitContactFlowVersionModificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CommitContactFlowVersionModificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CommitContactFlowVersionModificationResponse(),
            self.do_rpcrequest('CommitContactFlowVersionModification', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def commit_contact_flow_version_modification_with_options_async(
        self,
        request: ccc20170705_models.CommitContactFlowVersionModificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CommitContactFlowVersionModificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CommitContactFlowVersionModificationResponse(),
            await self.do_rpcrequest_async('CommitContactFlowVersionModification', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def commit_contact_flow_version_modification(
        self,
        request: ccc20170705_models.CommitContactFlowVersionModificationRequest,
    ) -> ccc20170705_models.CommitContactFlowVersionModificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.commit_contact_flow_version_modification_with_options(request, runtime)

    async def commit_contact_flow_version_modification_async(
        self,
        request: ccc20170705_models.CommitContactFlowVersionModificationRequest,
    ) -> ccc20170705_models.CommitContactFlowVersionModificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.commit_contact_flow_version_modification_with_options_async(request, runtime)

    def create_batch_jobs_with_options(
        self,
        request: ccc20170705_models.CreateBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateBatchJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateBatchJobsResponse(),
            self.do_rpcrequest('CreateBatchJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_batch_jobs_with_options_async(
        self,
        request: ccc20170705_models.CreateBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateBatchJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateBatchJobsResponse(),
            await self.do_rpcrequest_async('CreateBatchJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_batch_jobs(
        self,
        request: ccc20170705_models.CreateBatchJobsRequest,
    ) -> ccc20170705_models.CreateBatchJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_batch_jobs_with_options(request, runtime)

    async def create_batch_jobs_async(
        self,
        request: ccc20170705_models.CreateBatchJobsRequest,
    ) -> ccc20170705_models.CreateBatchJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_batch_jobs_with_options_async(request, runtime)

    def create_cab_instance_with_options(
        self,
        request: ccc20170705_models.CreateCabInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateCabInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateCabInstanceResponse(),
            self.do_rpcrequest('CreateCabInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cab_instance_with_options_async(
        self,
        request: ccc20170705_models.CreateCabInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateCabInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateCabInstanceResponse(),
            await self.do_rpcrequest_async('CreateCabInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cab_instance(
        self,
        request: ccc20170705_models.CreateCabInstanceRequest,
    ) -> ccc20170705_models.CreateCabInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cab_instance_with_options(request, runtime)

    async def create_cab_instance_async(
        self,
        request: ccc20170705_models.CreateCabInstanceRequest,
    ) -> ccc20170705_models.CreateCabInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cab_instance_with_options_async(request, runtime)

    def create_contact_flow_with_options(
        self,
        request: ccc20170705_models.CreateContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateContactFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateContactFlowResponse(),
            self.do_rpcrequest('CreateContactFlow', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_contact_flow_with_options_async(
        self,
        request: ccc20170705_models.CreateContactFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateContactFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateContactFlowResponse(),
            await self.do_rpcrequest_async('CreateContactFlow', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_contact_flow(
        self,
        request: ccc20170705_models.CreateContactFlowRequest,
    ) -> ccc20170705_models.CreateContactFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_contact_flow_with_options(request, runtime)

    async def create_contact_flow_async(
        self,
        request: ccc20170705_models.CreateContactFlowRequest,
    ) -> ccc20170705_models.CreateContactFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_contact_flow_with_options_async(request, runtime)

    def create_fault_with_options(
        self,
        request: ccc20170705_models.CreateFaultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateFaultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateFaultResponse(),
            self.do_rpcrequest('CreateFault', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_fault_with_options_async(
        self,
        request: ccc20170705_models.CreateFaultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateFaultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateFaultResponse(),
            await self.do_rpcrequest_async('CreateFault', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_fault(
        self,
        request: ccc20170705_models.CreateFaultRequest,
    ) -> ccc20170705_models.CreateFaultResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fault_with_options(request, runtime)

    async def create_fault_async(
        self,
        request: ccc20170705_models.CreateFaultRequest,
    ) -> ccc20170705_models.CreateFaultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fault_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: ccc20170705_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateInstanceResponse(),
            self.do_rpcrequest('CreateInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: ccc20170705_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateInstanceResponse(),
            await self.do_rpcrequest_async('CreateInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(
        self,
        request: ccc20170705_models.CreateInstanceRequest,
    ) -> ccc20170705_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: ccc20170705_models.CreateInstanceRequest,
    ) -> ccc20170705_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_job_group_with_options(
        self,
        request: ccc20170705_models.CreateJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateJobGroupResponse(),
            self.do_rpcrequest('CreateJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_job_group_with_options_async(
        self,
        request: ccc20170705_models.CreateJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateJobGroupResponse(),
            await self.do_rpcrequest_async('CreateJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_job_group(
        self,
        request: ccc20170705_models.CreateJobGroupRequest,
    ) -> ccc20170705_models.CreateJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_group_with_options(request, runtime)

    async def create_job_group_async(
        self,
        request: ccc20170705_models.CreateJobGroupRequest,
    ) -> ccc20170705_models.CreateJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_group_with_options_async(request, runtime)

    def create_media_with_options(
        self,
        request: ccc20170705_models.CreateMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateMediaResponse(),
            self.do_rpcrequest('CreateMedia', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_media_with_options_async(
        self,
        request: ccc20170705_models.CreateMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateMediaResponse(),
            await self.do_rpcrequest_async('CreateMedia', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_media(
        self,
        request: ccc20170705_models.CreateMediaRequest,
    ) -> ccc20170705_models.CreateMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_media_with_options(request, runtime)

    async def create_media_async(
        self,
        request: ccc20170705_models.CreateMediaRequest,
    ) -> ccc20170705_models.CreateMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_media_with_options_async(request, runtime)

    def create_predictive_job_group_with_options(
        self,
        request: ccc20170705_models.CreatePredictiveJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreatePredictiveJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreatePredictiveJobGroupResponse(),
            self.do_rpcrequest('CreatePredictiveJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_predictive_job_group_with_options_async(
        self,
        request: ccc20170705_models.CreatePredictiveJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreatePredictiveJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreatePredictiveJobGroupResponse(),
            await self.do_rpcrequest_async('CreatePredictiveJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_predictive_job_group(
        self,
        request: ccc20170705_models.CreatePredictiveJobGroupRequest,
    ) -> ccc20170705_models.CreatePredictiveJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_predictive_job_group_with_options(request, runtime)

    async def create_predictive_job_group_async(
        self,
        request: ccc20170705_models.CreatePredictiveJobGroupRequest,
    ) -> ccc20170705_models.CreatePredictiveJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_predictive_job_group_with_options_async(request, runtime)

    def create_scenario_with_options(
        self,
        request: ccc20170705_models.CreateScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateScenarioResponse(),
            self.do_rpcrequest('CreateScenario', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scenario_with_options_async(
        self,
        request: ccc20170705_models.CreateScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateScenarioResponse(),
            await self.do_rpcrequest_async('CreateScenario', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scenario(
        self,
        request: ccc20170705_models.CreateScenarioRequest,
    ) -> ccc20170705_models.CreateScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scenario_with_options(request, runtime)

    async def create_scenario_async(
        self,
        request: ccc20170705_models.CreateScenarioRequest,
    ) -> ccc20170705_models.CreateScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scenario_with_options_async(request, runtime)

    def create_scenario_from_template_with_options(
        self,
        request: ccc20170705_models.CreateScenarioFromTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateScenarioFromTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateScenarioFromTemplateResponse(),
            self.do_rpcrequest('CreateScenarioFromTemplate', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scenario_from_template_with_options_async(
        self,
        request: ccc20170705_models.CreateScenarioFromTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateScenarioFromTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateScenarioFromTemplateResponse(),
            await self.do_rpcrequest_async('CreateScenarioFromTemplate', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scenario_from_template(
        self,
        request: ccc20170705_models.CreateScenarioFromTemplateRequest,
    ) -> ccc20170705_models.CreateScenarioFromTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scenario_from_template_with_options(request, runtime)

    async def create_scenario_from_template_async(
        self,
        request: ccc20170705_models.CreateScenarioFromTemplateRequest,
    ) -> ccc20170705_models.CreateScenarioFromTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scenario_from_template_with_options_async(request, runtime)

    def create_skill_group_with_options(
        self,
        request: ccc20170705_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateSkillGroupResponse(),
            self.do_rpcrequest('CreateSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_skill_group_with_options_async(
        self,
        request: ccc20170705_models.CreateSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateSkillGroupResponse(),
            await self.do_rpcrequest_async('CreateSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_skill_group(
        self,
        request: ccc20170705_models.CreateSkillGroupRequest,
    ) -> ccc20170705_models.CreateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    async def create_skill_group_async(
        self,
        request: ccc20170705_models.CreateSkillGroupRequest,
    ) -> ccc20170705_models.CreateSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_skill_group_with_options_async(request, runtime)

    def create_survey_with_options(
        self,
        request: ccc20170705_models.CreateSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateSurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateSurveyResponse(),
            self.do_rpcrequest('CreateSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_survey_with_options_async(
        self,
        request: ccc20170705_models.CreateSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateSurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateSurveyResponse(),
            await self.do_rpcrequest_async('CreateSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_survey(
        self,
        request: ccc20170705_models.CreateSurveyRequest,
    ) -> ccc20170705_models.CreateSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_survey_with_options(request, runtime)

    async def create_survey_async(
        self,
        request: ccc20170705_models.CreateSurveyRequest,
    ) -> ccc20170705_models.CreateSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_survey_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: ccc20170705_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateUserResponse(),
            self.do_rpcrequest('CreateUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: ccc20170705_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateUserResponse(),
            await self.do_rpcrequest_async('CreateUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user(
        self,
        request: ccc20170705_models.CreateUserRequest,
    ) -> ccc20170705_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: ccc20170705_models.CreateUserRequest,
    ) -> ccc20170705_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_voice_appraise_with_options(
        self,
        request: ccc20170705_models.CreateVoiceAppraiseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateVoiceAppraiseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateVoiceAppraiseResponse(),
            self.do_rpcrequest('CreateVoiceAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_voice_appraise_with_options_async(
        self,
        request: ccc20170705_models.CreateVoiceAppraiseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.CreateVoiceAppraiseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.CreateVoiceAppraiseResponse(),
            await self.do_rpcrequest_async('CreateVoiceAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_voice_appraise(
        self,
        request: ccc20170705_models.CreateVoiceAppraiseRequest,
    ) -> ccc20170705_models.CreateVoiceAppraiseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_voice_appraise_with_options(request, runtime)

    async def create_voice_appraise_async(
        self,
        request: ccc20170705_models.CreateVoiceAppraiseRequest,
    ) -> ccc20170705_models.CreateVoiceAppraiseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_voice_appraise_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: ccc20170705_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeleteInstanceResponse(),
            self.do_rpcrequest('DeleteInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: ccc20170705_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeleteInstanceResponse(),
            await self.do_rpcrequest_async('DeleteInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(
        self,
        request: ccc20170705_models.DeleteInstanceRequest,
    ) -> ccc20170705_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: ccc20170705_models.DeleteInstanceRequest,
    ) -> ccc20170705_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_job_group_with_options(
        self,
        request: ccc20170705_models.DeleteJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeleteJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeleteJobGroupResponse(),
            self.do_rpcrequest('DeleteJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_job_group_with_options_async(
        self,
        request: ccc20170705_models.DeleteJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeleteJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeleteJobGroupResponse(),
            await self.do_rpcrequest_async('DeleteJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_job_group(
        self,
        request: ccc20170705_models.DeleteJobGroupRequest,
    ) -> ccc20170705_models.DeleteJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_job_group_with_options(request, runtime)

    async def delete_job_group_async(
        self,
        request: ccc20170705_models.DeleteJobGroupRequest,
    ) -> ccc20170705_models.DeleteJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_group_with_options_async(request, runtime)

    def delete_media_with_options(
        self,
        request: ccc20170705_models.DeleteMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeleteMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeleteMediaResponse(),
            self.do_rpcrequest('DeleteMedia', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_media_with_options_async(
        self,
        request: ccc20170705_models.DeleteMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeleteMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeleteMediaResponse(),
            await self.do_rpcrequest_async('DeleteMedia', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_media(
        self,
        request: ccc20170705_models.DeleteMediaRequest,
    ) -> ccc20170705_models.DeleteMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_media_with_options(request, runtime)

    async def delete_media_async(
        self,
        request: ccc20170705_models.DeleteMediaRequest,
    ) -> ccc20170705_models.DeleteMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_media_with_options_async(request, runtime)

    def delete_phone_tags_with_options(
        self,
        request: ccc20170705_models.DeletePhoneTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeletePhoneTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeletePhoneTagsResponse(),
            self.do_rpcrequest('DeletePhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_phone_tags_with_options_async(
        self,
        request: ccc20170705_models.DeletePhoneTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeletePhoneTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeletePhoneTagsResponse(),
            await self.do_rpcrequest_async('DeletePhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_phone_tags(
        self,
        request: ccc20170705_models.DeletePhoneTagsRequest,
    ) -> ccc20170705_models.DeletePhoneTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_phone_tags_with_options(request, runtime)

    async def delete_phone_tags_async(
        self,
        request: ccc20170705_models.DeletePhoneTagsRequest,
    ) -> ccc20170705_models.DeletePhoneTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_phone_tags_with_options_async(request, runtime)

    def delete_skill_group_with_options(
        self,
        request: ccc20170705_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeleteSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeleteSkillGroupResponse(),
            self.do_rpcrequest('DeleteSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_skill_group_with_options_async(
        self,
        request: ccc20170705_models.DeleteSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeleteSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeleteSkillGroupResponse(),
            await self.do_rpcrequest_async('DeleteSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_skill_group(
        self,
        request: ccc20170705_models.DeleteSkillGroupRequest,
    ) -> ccc20170705_models.DeleteSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_with_options(request, runtime)

    async def delete_skill_group_async(
        self,
        request: ccc20170705_models.DeleteSkillGroupRequest,
    ) -> ccc20170705_models.DeleteSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_skill_group_with_options_async(request, runtime)

    def delete_survey_with_options(
        self,
        request: ccc20170705_models.DeleteSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeleteSurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeleteSurveyResponse(),
            self.do_rpcrequest('DeleteSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_survey_with_options_async(
        self,
        request: ccc20170705_models.DeleteSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DeleteSurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DeleteSurveyResponse(),
            await self.do_rpcrequest_async('DeleteSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_survey(
        self,
        request: ccc20170705_models.DeleteSurveyRequest,
    ) -> ccc20170705_models.DeleteSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_survey_with_options(request, runtime)

    async def delete_survey_async(
        self,
        request: ccc20170705_models.DeleteSurveyRequest,
    ) -> ccc20170705_models.DeleteSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_survey_with_options_async(request, runtime)

    def dial_ex_with_options(
        self,
        request: ccc20170705_models.DialExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DialExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DialExResponse(),
            self.do_rpcrequest('DialEx', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dial_ex_with_options_async(
        self,
        request: ccc20170705_models.DialExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DialExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DialExResponse(),
            await self.do_rpcrequest_async('DialEx', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dial_ex(
        self,
        request: ccc20170705_models.DialExRequest,
    ) -> ccc20170705_models.DialExResponse:
        runtime = util_models.RuntimeOptions()
        return self.dial_ex_with_options(request, runtime)

    async def dial_ex_async(
        self,
        request: ccc20170705_models.DialExRequest,
    ) -> ccc20170705_models.DialExResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dial_ex_with_options_async(request, runtime)

    def dialogue_with_options(
        self,
        request: ccc20170705_models.DialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DialogueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DialogueResponse(),
            self.do_rpcrequest('Dialogue', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dialogue_with_options_async(
        self,
        request: ccc20170705_models.DialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DialogueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DialogueResponse(),
            await self.do_rpcrequest_async('Dialogue', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dialogue(
        self,
        request: ccc20170705_models.DialogueRequest,
    ) -> ccc20170705_models.DialogueResponse:
        runtime = util_models.RuntimeOptions()
        return self.dialogue_with_options(request, runtime)

    async def dialogue_async(
        self,
        request: ccc20170705_models.DialogueRequest,
    ) -> ccc20170705_models.DialogueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dialogue_with_options_async(request, runtime)

    def disable_trunk_providers_with_options(
        self,
        request: ccc20170705_models.DisableTrunkProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DisableTrunkProvidersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DisableTrunkProvidersResponse(),
            self.do_rpcrequest('DisableTrunkProviders', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_trunk_providers_with_options_async(
        self,
        request: ccc20170705_models.DisableTrunkProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DisableTrunkProvidersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DisableTrunkProvidersResponse(),
            await self.do_rpcrequest_async('DisableTrunkProviders', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_trunk_providers(
        self,
        request: ccc20170705_models.DisableTrunkProvidersRequest,
    ) -> ccc20170705_models.DisableTrunkProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_trunk_providers_with_options(request, runtime)

    async def disable_trunk_providers_async(
        self,
        request: ccc20170705_models.DisableTrunkProvidersRequest,
    ) -> ccc20170705_models.DisableTrunkProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_trunk_providers_with_options_async(request, runtime)

    def download_all_type_recording_with_options(
        self,
        request: ccc20170705_models.DownloadAllTypeRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DownloadAllTypeRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DownloadAllTypeRecordingResponse(),
            self.do_rpcrequest('DownloadAllTypeRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_all_type_recording_with_options_async(
        self,
        request: ccc20170705_models.DownloadAllTypeRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DownloadAllTypeRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DownloadAllTypeRecordingResponse(),
            await self.do_rpcrequest_async('DownloadAllTypeRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_all_type_recording(
        self,
        request: ccc20170705_models.DownloadAllTypeRecordingRequest,
    ) -> ccc20170705_models.DownloadAllTypeRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_all_type_recording_with_options(request, runtime)

    async def download_all_type_recording_async(
        self,
        request: ccc20170705_models.DownloadAllTypeRecordingRequest,
    ) -> ccc20170705_models.DownloadAllTypeRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_all_type_recording_with_options_async(request, runtime)

    def download_cab_recording_with_options(
        self,
        request: ccc20170705_models.DownloadCabRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DownloadCabRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DownloadCabRecordingResponse(),
            self.do_rpcrequest('DownloadCabRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_cab_recording_with_options_async(
        self,
        request: ccc20170705_models.DownloadCabRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DownloadCabRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DownloadCabRecordingResponse(),
            await self.do_rpcrequest_async('DownloadCabRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_cab_recording(
        self,
        request: ccc20170705_models.DownloadCabRecordingRequest,
    ) -> ccc20170705_models.DownloadCabRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_cab_recording_with_options(request, runtime)

    async def download_cab_recording_async(
        self,
        request: ccc20170705_models.DownloadCabRecordingRequest,
    ) -> ccc20170705_models.DownloadCabRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_cab_recording_with_options_async(request, runtime)

    def download_original_statistics_report_with_options(
        self,
        request: ccc20170705_models.DownloadOriginalStatisticsReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DownloadOriginalStatisticsReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DownloadOriginalStatisticsReportResponse(),
            self.do_rpcrequest('DownloadOriginalStatisticsReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_original_statistics_report_with_options_async(
        self,
        request: ccc20170705_models.DownloadOriginalStatisticsReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DownloadOriginalStatisticsReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DownloadOriginalStatisticsReportResponse(),
            await self.do_rpcrequest_async('DownloadOriginalStatisticsReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_original_statistics_report(
        self,
        request: ccc20170705_models.DownloadOriginalStatisticsReportRequest,
    ) -> ccc20170705_models.DownloadOriginalStatisticsReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_original_statistics_report_with_options(request, runtime)

    async def download_original_statistics_report_async(
        self,
        request: ccc20170705_models.DownloadOriginalStatisticsReportRequest,
    ) -> ccc20170705_models.DownloadOriginalStatisticsReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_original_statistics_report_with_options_async(request, runtime)

    def download_recording_with_options(
        self,
        request: ccc20170705_models.DownloadRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DownloadRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DownloadRecordingResponse(),
            self.do_rpcrequest('DownloadRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_recording_with_options_async(
        self,
        request: ccc20170705_models.DownloadRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DownloadRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DownloadRecordingResponse(),
            await self.do_rpcrequest_async('DownloadRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_recording(
        self,
        request: ccc20170705_models.DownloadRecordingRequest,
    ) -> ccc20170705_models.DownloadRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_recording_with_options(request, runtime)

    async def download_recording_async(
        self,
        request: ccc20170705_models.DownloadRecordingRequest,
    ) -> ccc20170705_models.DownloadRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_recording_with_options_async(request, runtime)

    def download_unreachable_contacts_with_options(
        self,
        request: ccc20170705_models.DownloadUnreachableContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DownloadUnreachableContactsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DownloadUnreachableContactsResponse(),
            self.do_rpcrequest('DownloadUnreachableContacts', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_unreachable_contacts_with_options_async(
        self,
        request: ccc20170705_models.DownloadUnreachableContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.DownloadUnreachableContactsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.DownloadUnreachableContactsResponse(),
            await self.do_rpcrequest_async('DownloadUnreachableContacts', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_unreachable_contacts(
        self,
        request: ccc20170705_models.DownloadUnreachableContactsRequest,
    ) -> ccc20170705_models.DownloadUnreachableContactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_unreachable_contacts_with_options(request, runtime)

    async def download_unreachable_contacts_async(
        self,
        request: ccc20170705_models.DownloadUnreachableContactsRequest,
    ) -> ccc20170705_models.DownloadUnreachableContactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_unreachable_contacts_with_options_async(request, runtime)

    def find_users_with_options(
        self,
        request: ccc20170705_models.FindUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.FindUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.FindUsersResponse(),
            self.do_rpcrequest('FindUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_users_with_options_async(
        self,
        request: ccc20170705_models.FindUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.FindUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.FindUsersResponse(),
            await self.do_rpcrequest_async('FindUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_users(
        self,
        request: ccc20170705_models.FindUsersRequest,
    ) -> ccc20170705_models.FindUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_users_with_options(request, runtime)

    async def find_users_async(
        self,
        request: ccc20170705_models.FindUsersRequest,
    ) -> ccc20170705_models.FindUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_users_with_options_async(request, runtime)

    def generate_agent_statistic_report_with_options(
        self,
        request: ccc20170705_models.GenerateAgentStatisticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GenerateAgentStatisticReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GenerateAgentStatisticReportResponse(),
            self.do_rpcrequest('GenerateAgentStatisticReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_agent_statistic_report_with_options_async(
        self,
        request: ccc20170705_models.GenerateAgentStatisticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GenerateAgentStatisticReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GenerateAgentStatisticReportResponse(),
            await self.do_rpcrequest_async('GenerateAgentStatisticReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_agent_statistic_report(
        self,
        request: ccc20170705_models.GenerateAgentStatisticReportRequest,
    ) -> ccc20170705_models.GenerateAgentStatisticReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_agent_statistic_report_with_options(request, runtime)

    async def generate_agent_statistic_report_async(
        self,
        request: ccc20170705_models.GenerateAgentStatisticReportRequest,
    ) -> ccc20170705_models.GenerateAgentStatisticReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_agent_statistic_report_with_options_async(request, runtime)

    def get_agent_data_with_options(
        self,
        request: ccc20170705_models.GetAgentDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetAgentDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetAgentDataResponse(),
            self.do_rpcrequest('GetAgentData', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_agent_data_with_options_async(
        self,
        request: ccc20170705_models.GetAgentDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetAgentDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetAgentDataResponse(),
            await self.do_rpcrequest_async('GetAgentData', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_agent_data(
        self,
        request: ccc20170705_models.GetAgentDataRequest,
    ) -> ccc20170705_models.GetAgentDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_data_with_options(request, runtime)

    async def get_agent_data_async(
        self,
        request: ccc20170705_models.GetAgentDataRequest,
    ) -> ccc20170705_models.GetAgentDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_data_with_options_async(request, runtime)

    def get_call_measure_summary_report_with_options(
        self,
        request: ccc20170705_models.GetCallMeasureSummaryReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetCallMeasureSummaryReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetCallMeasureSummaryReportResponse(),
            self.do_rpcrequest('GetCallMeasureSummaryReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_call_measure_summary_report_with_options_async(
        self,
        request: ccc20170705_models.GetCallMeasureSummaryReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetCallMeasureSummaryReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetCallMeasureSummaryReportResponse(),
            await self.do_rpcrequest_async('GetCallMeasureSummaryReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_call_measure_summary_report(
        self,
        request: ccc20170705_models.GetCallMeasureSummaryReportRequest,
    ) -> ccc20170705_models.GetCallMeasureSummaryReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_call_measure_summary_report_with_options(request, runtime)

    async def get_call_measure_summary_report_async(
        self,
        request: ccc20170705_models.GetCallMeasureSummaryReportRequest,
    ) -> ccc20170705_models.GetCallMeasureSummaryReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_call_measure_summary_report_with_options_async(request, runtime)

    def get_config_with_options(
        self,
        request: ccc20170705_models.GetConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetConfigResponse(),
            self.do_rpcrequest('GetConfig', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_config_with_options_async(
        self,
        request: ccc20170705_models.GetConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetConfigResponse(),
            await self.do_rpcrequest_async('GetConfig', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_config(
        self,
        request: ccc20170705_models.GetConfigRequest,
    ) -> ccc20170705_models.GetConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_config_with_options(request, runtime)

    async def get_config_async(
        self,
        request: ccc20170705_models.GetConfigRequest,
    ) -> ccc20170705_models.GetConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_config_with_options_async(request, runtime)

    def get_contact_info_by_outbound_task_id_with_options(
        self,
        request: ccc20170705_models.GetContactInfoByOutboundTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetContactInfoByOutboundTaskIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetContactInfoByOutboundTaskIdResponse(),
            self.do_rpcrequest('GetContactInfoByOutboundTaskId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_contact_info_by_outbound_task_id_with_options_async(
        self,
        request: ccc20170705_models.GetContactInfoByOutboundTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetContactInfoByOutboundTaskIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetContactInfoByOutboundTaskIdResponse(),
            await self.do_rpcrequest_async('GetContactInfoByOutboundTaskId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_contact_info_by_outbound_task_id(
        self,
        request: ccc20170705_models.GetContactInfoByOutboundTaskIdRequest,
    ) -> ccc20170705_models.GetContactInfoByOutboundTaskIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_contact_info_by_outbound_task_id_with_options(request, runtime)

    async def get_contact_info_by_outbound_task_id_async(
        self,
        request: ccc20170705_models.GetContactInfoByOutboundTaskIdRequest,
    ) -> ccc20170705_models.GetContactInfoByOutboundTaskIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_contact_info_by_outbound_task_id_with_options_async(request, runtime)

    def get_conversation_detail_by_contact_id_with_options(
        self,
        request: ccc20170705_models.GetConversationDetailByContactIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetConversationDetailByContactIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetConversationDetailByContactIdResponse(),
            self.do_rpcrequest('GetConversationDetailByContactId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_conversation_detail_by_contact_id_with_options_async(
        self,
        request: ccc20170705_models.GetConversationDetailByContactIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetConversationDetailByContactIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetConversationDetailByContactIdResponse(),
            await self.do_rpcrequest_async('GetConversationDetailByContactId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_conversation_detail_by_contact_id(
        self,
        request: ccc20170705_models.GetConversationDetailByContactIdRequest,
    ) -> ccc20170705_models.GetConversationDetailByContactIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_conversation_detail_by_contact_id_with_options(request, runtime)

    async def get_conversation_detail_by_contact_id_async(
        self,
        request: ccc20170705_models.GetConversationDetailByContactIdRequest,
    ) -> ccc20170705_models.GetConversationDetailByContactIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_conversation_detail_by_contact_id_with_options_async(request, runtime)

    def get_conversation_list_with_options(
        self,
        request: ccc20170705_models.GetConversationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetConversationListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetConversationListResponse(),
            self.do_rpcrequest('GetConversationList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_conversation_list_with_options_async(
        self,
        request: ccc20170705_models.GetConversationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetConversationListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetConversationListResponse(),
            await self.do_rpcrequest_async('GetConversationList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_conversation_list(
        self,
        request: ccc20170705_models.GetConversationListRequest,
    ) -> ccc20170705_models.GetConversationListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_conversation_list_with_options(request, runtime)

    async def get_conversation_list_async(
        self,
        request: ccc20170705_models.GetConversationListRequest,
    ) -> ccc20170705_models.GetConversationListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_conversation_list_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: ccc20170705_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetInstanceResponse(),
            self.do_rpcrequest('GetInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: ccc20170705_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetInstanceResponse(),
            await self.do_rpcrequest_async('GetInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance(
        self,
        request: ccc20170705_models.GetInstanceRequest,
    ) -> ccc20170705_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: ccc20170705_models.GetInstanceRequest,
    ) -> ccc20170705_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_instance_state_with_options(
        self,
        request: ccc20170705_models.GetInstanceStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetInstanceStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetInstanceStateResponse(),
            self.do_rpcrequest('GetInstanceState', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_state_with_options_async(
        self,
        request: ccc20170705_models.GetInstanceStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetInstanceStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetInstanceStateResponse(),
            await self.do_rpcrequest_async('GetInstanceState', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_state(
        self,
        request: ccc20170705_models.GetInstanceStateRequest,
    ) -> ccc20170705_models.GetInstanceStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_state_with_options(request, runtime)

    async def get_instance_state_async(
        self,
        request: ccc20170705_models.GetInstanceStateRequest,
    ) -> ccc20170705_models.GetInstanceStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_state_with_options_async(request, runtime)

    def get_instance_summary_report_with_options(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetInstanceSummaryReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetInstanceSummaryReportResponse(),
            self.do_rpcrequest('GetInstanceSummaryReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_summary_report_with_options_async(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetInstanceSummaryReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetInstanceSummaryReportResponse(),
            await self.do_rpcrequest_async('GetInstanceSummaryReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_summary_report(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportRequest,
    ) -> ccc20170705_models.GetInstanceSummaryReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_summary_report_with_options(request, runtime)

    async def get_instance_summary_report_async(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportRequest,
    ) -> ccc20170705_models.GetInstanceSummaryReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_summary_report_with_options_async(request, runtime)

    def get_instance_summary_report_by_interval_with_options(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportByIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetInstanceSummaryReportByIntervalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetInstanceSummaryReportByIntervalResponse(),
            self.do_rpcrequest('GetInstanceSummaryReportByInterval', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_summary_report_by_interval_with_options_async(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportByIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetInstanceSummaryReportByIntervalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetInstanceSummaryReportByIntervalResponse(),
            await self.do_rpcrequest_async('GetInstanceSummaryReportByInterval', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_summary_report_by_interval(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportByIntervalRequest,
    ) -> ccc20170705_models.GetInstanceSummaryReportByIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_summary_report_by_interval_with_options(request, runtime)

    async def get_instance_summary_report_by_interval_async(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportByIntervalRequest,
    ) -> ccc20170705_models.GetInstanceSummaryReportByIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_summary_report_by_interval_with_options_async(request, runtime)

    def get_instance_summary_report_since_midnight_with_options(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportSinceMidnightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetInstanceSummaryReportSinceMidnightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetInstanceSummaryReportSinceMidnightResponse(),
            self.do_rpcrequest('GetInstanceSummaryReportSinceMidnight', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_summary_report_since_midnight_with_options_async(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportSinceMidnightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetInstanceSummaryReportSinceMidnightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetInstanceSummaryReportSinceMidnightResponse(),
            await self.do_rpcrequest_async('GetInstanceSummaryReportSinceMidnight', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_summary_report_since_midnight(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportSinceMidnightRequest,
    ) -> ccc20170705_models.GetInstanceSummaryReportSinceMidnightResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_summary_report_since_midnight_with_options(request, runtime)

    async def get_instance_summary_report_since_midnight_async(
        self,
        request: ccc20170705_models.GetInstanceSummaryReportSinceMidnightRequest,
    ) -> ccc20170705_models.GetInstanceSummaryReportSinceMidnightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_summary_report_since_midnight_with_options_async(request, runtime)

    def get_job_with_options(
        self,
        request: ccc20170705_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobResponse(),
            self.do_rpcrequest('GetJob', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_with_options_async(
        self,
        request: ccc20170705_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobResponse(),
            await self.do_rpcrequest_async('GetJob', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job(
        self,
        request: ccc20170705_models.GetJobRequest,
    ) -> ccc20170705_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_with_options(request, runtime)

    async def get_job_async(
        self,
        request: ccc20170705_models.GetJobRequest,
    ) -> ccc20170705_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_with_options_async(request, runtime)

    def get_job_data_upload_params_with_options(
        self,
        request: ccc20170705_models.GetJobDataUploadParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobDataUploadParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobDataUploadParamsResponse(),
            self.do_rpcrequest('GetJobDataUploadParams', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_data_upload_params_with_options_async(
        self,
        request: ccc20170705_models.GetJobDataUploadParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobDataUploadParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobDataUploadParamsResponse(),
            await self.do_rpcrequest_async('GetJobDataUploadParams', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_data_upload_params(
        self,
        request: ccc20170705_models.GetJobDataUploadParamsRequest,
    ) -> ccc20170705_models.GetJobDataUploadParamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_data_upload_params_with_options(request, runtime)

    async def get_job_data_upload_params_async(
        self,
        request: ccc20170705_models.GetJobDataUploadParamsRequest,
    ) -> ccc20170705_models.GetJobDataUploadParamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_data_upload_params_with_options_async(request, runtime)

    def get_job_file_upload_url_with_options(
        self,
        request: ccc20170705_models.GetJobFileUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobFileUploadUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobFileUploadUrlResponse(),
            self.do_rpcrequest('GetJobFileUploadUrl', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_file_upload_url_with_options_async(
        self,
        request: ccc20170705_models.GetJobFileUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobFileUploadUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobFileUploadUrlResponse(),
            await self.do_rpcrequest_async('GetJobFileUploadUrl', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_file_upload_url(
        self,
        request: ccc20170705_models.GetJobFileUploadUrlRequest,
    ) -> ccc20170705_models.GetJobFileUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_file_upload_url_with_options(request, runtime)

    async def get_job_file_upload_url_async(
        self,
        request: ccc20170705_models.GetJobFileUploadUrlRequest,
    ) -> ccc20170705_models.GetJobFileUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_file_upload_url_with_options_async(request, runtime)

    def get_job_group_with_options(
        self,
        request: ccc20170705_models.GetJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobGroupResponse(),
            self.do_rpcrequest('GetJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_group_with_options_async(
        self,
        request: ccc20170705_models.GetJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobGroupResponse(),
            await self.do_rpcrequest_async('GetJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_group(
        self,
        request: ccc20170705_models.GetJobGroupRequest,
    ) -> ccc20170705_models.GetJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_group_with_options(request, runtime)

    async def get_job_group_async(
        self,
        request: ccc20170705_models.GetJobGroupRequest,
    ) -> ccc20170705_models.GetJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_group_with_options_async(request, runtime)

    def get_job_list_with_options(
        self,
        request: ccc20170705_models.GetJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobListResponse(),
            self.do_rpcrequest('GetJobList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_list_with_options_async(
        self,
        request: ccc20170705_models.GetJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobListResponse(),
            await self.do_rpcrequest_async('GetJobList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_list(
        self,
        request: ccc20170705_models.GetJobListRequest,
    ) -> ccc20170705_models.GetJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_list_with_options(request, runtime)

    async def get_job_list_async(
        self,
        request: ccc20170705_models.GetJobListRequest,
    ) -> ccc20170705_models.GetJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_list_with_options_async(request, runtime)

    def get_job_status_by_call_id_with_options(
        self,
        request: ccc20170705_models.GetJobStatusByCallIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobStatusByCallIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobStatusByCallIdResponse(),
            self.do_rpcrequest('GetJobStatusByCallId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_status_by_call_id_with_options_async(
        self,
        request: ccc20170705_models.GetJobStatusByCallIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobStatusByCallIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobStatusByCallIdResponse(),
            await self.do_rpcrequest_async('GetJobStatusByCallId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_status_by_call_id(
        self,
        request: ccc20170705_models.GetJobStatusByCallIdRequest,
    ) -> ccc20170705_models.GetJobStatusByCallIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_status_by_call_id_with_options(request, runtime)

    async def get_job_status_by_call_id_async(
        self,
        request: ccc20170705_models.GetJobStatusByCallIdRequest,
    ) -> ccc20170705_models.GetJobStatusByCallIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_status_by_call_id_with_options_async(request, runtime)

    def get_job_template_download_params_with_options(
        self,
        request: ccc20170705_models.GetJobTemplateDownloadParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobTemplateDownloadParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobTemplateDownloadParamsResponse(),
            self.do_rpcrequest('GetJobTemplateDownloadParams', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_template_download_params_with_options_async(
        self,
        request: ccc20170705_models.GetJobTemplateDownloadParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetJobTemplateDownloadParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetJobTemplateDownloadParamsResponse(),
            await self.do_rpcrequest_async('GetJobTemplateDownloadParams', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_template_download_params(
        self,
        request: ccc20170705_models.GetJobTemplateDownloadParamsRequest,
    ) -> ccc20170705_models.GetJobTemplateDownloadParamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_template_download_params_with_options(request, runtime)

    async def get_job_template_download_params_async(
        self,
        request: ccc20170705_models.GetJobTemplateDownloadParamsRequest,
    ) -> ccc20170705_models.GetJobTemplateDownloadParamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_template_download_params_with_options_async(request, runtime)

    def get_number_region_info_with_options(
        self,
        request: ccc20170705_models.GetNumberRegionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetNumberRegionInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetNumberRegionInfoResponse(),
            self.do_rpcrequest('GetNumberRegionInfo', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_number_region_info_with_options_async(
        self,
        request: ccc20170705_models.GetNumberRegionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetNumberRegionInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetNumberRegionInfoResponse(),
            await self.do_rpcrequest_async('GetNumberRegionInfo', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_number_region_info(
        self,
        request: ccc20170705_models.GetNumberRegionInfoRequest,
    ) -> ccc20170705_models.GetNumberRegionInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_number_region_info_with_options(request, runtime)

    async def get_number_region_info_async(
        self,
        request: ccc20170705_models.GetNumberRegionInfoRequest,
    ) -> ccc20170705_models.GetNumberRegionInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_number_region_info_with_options_async(request, runtime)

    def get_predictive_job_group_with_options(
        self,
        request: ccc20170705_models.GetPredictiveJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetPredictiveJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetPredictiveJobGroupResponse(),
            self.do_rpcrequest('GetPredictiveJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_predictive_job_group_with_options_async(
        self,
        request: ccc20170705_models.GetPredictiveJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetPredictiveJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetPredictiveJobGroupResponse(),
            await self.do_rpcrequest_async('GetPredictiveJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_predictive_job_group(
        self,
        request: ccc20170705_models.GetPredictiveJobGroupRequest,
    ) -> ccc20170705_models.GetPredictiveJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_predictive_job_group_with_options(request, runtime)

    async def get_predictive_job_group_async(
        self,
        request: ccc20170705_models.GetPredictiveJobGroupRequest,
    ) -> ccc20170705_models.GetPredictiveJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_predictive_job_group_with_options_async(request, runtime)

    def get_predictive_task_data_with_options(
        self,
        request: ccc20170705_models.GetPredictiveTaskDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetPredictiveTaskDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ccc20170705_models.GetPredictiveTaskDataResponse(),
            self.do_rpcrequest('GetPredictiveTaskData', '2017-07-05', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_predictive_task_data_with_options_async(
        self,
        request: ccc20170705_models.GetPredictiveTaskDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetPredictiveTaskDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ccc20170705_models.GetPredictiveTaskDataResponse(),
            await self.do_rpcrequest_async('GetPredictiveTaskData', '2017-07-05', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_predictive_task_data(
        self,
        request: ccc20170705_models.GetPredictiveTaskDataRequest,
    ) -> ccc20170705_models.GetPredictiveTaskDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_predictive_task_data_with_options(request, runtime)

    async def get_predictive_task_data_async(
        self,
        request: ccc20170705_models.GetPredictiveTaskDataRequest,
    ) -> ccc20170705_models.GetPredictiveTaskDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_predictive_task_data_with_options_async(request, runtime)

    def get_record_oss_upload_param_with_options(
        self,
        request: ccc20170705_models.GetRecordOssUploadParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetRecordOssUploadParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetRecordOssUploadParamResponse(),
            self.do_rpcrequest('GetRecordOssUploadParam', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_record_oss_upload_param_with_options_async(
        self,
        request: ccc20170705_models.GetRecordOssUploadParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetRecordOssUploadParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetRecordOssUploadParamResponse(),
            await self.do_rpcrequest_async('GetRecordOssUploadParam', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_record_oss_upload_param(
        self,
        request: ccc20170705_models.GetRecordOssUploadParamRequest,
    ) -> ccc20170705_models.GetRecordOssUploadParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_record_oss_upload_param_with_options(request, runtime)

    async def get_record_oss_upload_param_async(
        self,
        request: ccc20170705_models.GetRecordOssUploadParamRequest,
    ) -> ccc20170705_models.GetRecordOssUploadParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_record_oss_upload_param_with_options_async(request, runtime)

    def get_route_point_with_options(
        self,
        request: ccc20170705_models.GetRoutePointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetRoutePointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetRoutePointResponse(),
            self.do_rpcrequest('GetRoutePoint', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_route_point_with_options_async(
        self,
        request: ccc20170705_models.GetRoutePointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetRoutePointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetRoutePointResponse(),
            await self.do_rpcrequest_async('GetRoutePoint', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_route_point(
        self,
        request: ccc20170705_models.GetRoutePointRequest,
    ) -> ccc20170705_models.GetRoutePointResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_route_point_with_options(request, runtime)

    async def get_route_point_async(
        self,
        request: ccc20170705_models.GetRoutePointRequest,
    ) -> ccc20170705_models.GetRoutePointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_route_point_with_options_async(request, runtime)

    def get_scenario_with_options(
        self,
        request: ccc20170705_models.GetScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetScenarioResponse(),
            self.do_rpcrequest('GetScenario', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_scenario_with_options_async(
        self,
        request: ccc20170705_models.GetScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetScenarioResponse(),
            await self.do_rpcrequest_async('GetScenario', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_scenario(
        self,
        request: ccc20170705_models.GetScenarioRequest,
    ) -> ccc20170705_models.GetScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scenario_with_options(request, runtime)

    async def get_scenario_async(
        self,
        request: ccc20170705_models.GetScenarioRequest,
    ) -> ccc20170705_models.GetScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scenario_with_options_async(request, runtime)

    def get_service_extensions_with_options(
        self,
        request: ccc20170705_models.GetServiceExtensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetServiceExtensionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetServiceExtensionsResponse(),
            self.do_rpcrequest('GetServiceExtensions', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_service_extensions_with_options_async(
        self,
        request: ccc20170705_models.GetServiceExtensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetServiceExtensionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetServiceExtensionsResponse(),
            await self.do_rpcrequest_async('GetServiceExtensions', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_extensions(
        self,
        request: ccc20170705_models.GetServiceExtensionsRequest,
    ) -> ccc20170705_models.GetServiceExtensionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_extensions_with_options(request, runtime)

    async def get_service_extensions_async(
        self,
        request: ccc20170705_models.GetServiceExtensionsRequest,
    ) -> ccc20170705_models.GetServiceExtensionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_extensions_with_options_async(request, runtime)

    def get_sms_config_with_options(
        self,
        request: ccc20170705_models.GetSmsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetSmsConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetSmsConfigResponse(),
            self.do_rpcrequest('GetSmsConfig', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sms_config_with_options_async(
        self,
        request: ccc20170705_models.GetSmsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetSmsConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetSmsConfigResponse(),
            await self.do_rpcrequest_async('GetSmsConfig', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sms_config(
        self,
        request: ccc20170705_models.GetSmsConfigRequest,
    ) -> ccc20170705_models.GetSmsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sms_config_with_options(request, runtime)

    async def get_sms_config_async(
        self,
        request: ccc20170705_models.GetSmsConfigRequest,
    ) -> ccc20170705_models.GetSmsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sms_config_with_options_async(request, runtime)

    def get_survey_with_options(
        self,
        request: ccc20170705_models.GetSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetSurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetSurveyResponse(),
            self.do_rpcrequest('GetSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_survey_with_options_async(
        self,
        request: ccc20170705_models.GetSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetSurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetSurveyResponse(),
            await self.do_rpcrequest_async('GetSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_survey(
        self,
        request: ccc20170705_models.GetSurveyRequest,
    ) -> ccc20170705_models.GetSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_survey_with_options(request, runtime)

    async def get_survey_async(
        self,
        request: ccc20170705_models.GetSurveyRequest,
    ) -> ccc20170705_models.GetSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_survey_with_options_async(request, runtime)

    def get_turncredentials_with_options(
        self,
        request: ccc20170705_models.GetTURNCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetTURNCredentialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetTURNCredentialsResponse(),
            self.do_rpcrequest('GetTURNCredentials', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_turncredentials_with_options_async(
        self,
        request: ccc20170705_models.GetTURNCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetTURNCredentialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetTURNCredentialsResponse(),
            await self.do_rpcrequest_async('GetTURNCredentials', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_turncredentials(
        self,
        request: ccc20170705_models.GetTURNCredentialsRequest,
    ) -> ccc20170705_models.GetTURNCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_turncredentials_with_options(request, runtime)

    async def get_turncredentials_async(
        self,
        request: ccc20170705_models.GetTURNCredentialsRequest,
    ) -> ccc20170705_models.GetTURNCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_turncredentials_with_options_async(request, runtime)

    def get_turnserver_list_with_options(
        self,
        request: ccc20170705_models.GetTURNServerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetTURNServerListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetTURNServerListResponse(),
            self.do_rpcrequest('GetTURNServerList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_turnserver_list_with_options_async(
        self,
        request: ccc20170705_models.GetTURNServerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetTURNServerListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetTURNServerListResponse(),
            await self.do_rpcrequest_async('GetTURNServerList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_turnserver_list(
        self,
        request: ccc20170705_models.GetTURNServerListRequest,
    ) -> ccc20170705_models.GetTURNServerListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_turnserver_list_with_options(request, runtime)

    async def get_turnserver_list_async(
        self,
        request: ccc20170705_models.GetTURNServerListRequest,
    ) -> ccc20170705_models.GetTURNServerListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_turnserver_list_with_options_async(request, runtime)

    def get_task_list_with_options(
        self,
        request: ccc20170705_models.GetTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetTaskListResponse(),
            self.do_rpcrequest('GetTaskList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_task_list_with_options_async(
        self,
        request: ccc20170705_models.GetTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetTaskListResponse(),
            await self.do_rpcrequest_async('GetTaskList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_list(
        self,
        request: ccc20170705_models.GetTaskListRequest,
    ) -> ccc20170705_models.GetTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_list_with_options(request, runtime)

    async def get_task_list_async(
        self,
        request: ccc20170705_models.GetTaskListRequest,
    ) -> ccc20170705_models.GetTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_list_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: ccc20170705_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetUserResponse(),
            self.do_rpcrequest('GetUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: ccc20170705_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetUserResponse(),
            await self.do_rpcrequest_async('GetUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user(
        self,
        request: ccc20170705_models.GetUserRequest,
    ) -> ccc20170705_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: ccc20170705_models.GetUserRequest,
    ) -> ccc20170705_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_user_by_extension_with_options(
        self,
        request: ccc20170705_models.GetUserByExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetUserByExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetUserByExtensionResponse(),
            self.do_rpcrequest('GetUserByExtension', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_by_extension_with_options_async(
        self,
        request: ccc20170705_models.GetUserByExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.GetUserByExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.GetUserByExtensionResponse(),
            await self.do_rpcrequest_async('GetUserByExtension', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_by_extension(
        self,
        request: ccc20170705_models.GetUserByExtensionRequest,
    ) -> ccc20170705_models.GetUserByExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_by_extension_with_options(request, runtime)

    async def get_user_by_extension_async(
        self,
        request: ccc20170705_models.GetUserByExtensionRequest,
    ) -> ccc20170705_models.GetUserByExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_by_extension_with_options_async(request, runtime)

    def inflight_task_timeout_with_options(
        self,
        request: ccc20170705_models.InflightTaskTimeoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.InflightTaskTimeoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.InflightTaskTimeoutResponse(),
            self.do_rpcrequest('InflightTaskTimeout', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def inflight_task_timeout_with_options_async(
        self,
        request: ccc20170705_models.InflightTaskTimeoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.InflightTaskTimeoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.InflightTaskTimeoutResponse(),
            await self.do_rpcrequest_async('InflightTaskTimeout', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def inflight_task_timeout(
        self,
        request: ccc20170705_models.InflightTaskTimeoutRequest,
    ) -> ccc20170705_models.InflightTaskTimeoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.inflight_task_timeout_with_options(request, runtime)

    async def inflight_task_timeout_async(
        self,
        request: ccc20170705_models.InflightTaskTimeoutRequest,
    ) -> ccc20170705_models.InflightTaskTimeoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.inflight_task_timeout_with_options_async(request, runtime)

    def launch_appraise_with_options(
        self,
        request: ccc20170705_models.LaunchAppraiseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.LaunchAppraiseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.LaunchAppraiseResponse(),
            self.do_rpcrequest('LaunchAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def launch_appraise_with_options_async(
        self,
        request: ccc20170705_models.LaunchAppraiseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.LaunchAppraiseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.LaunchAppraiseResponse(),
            await self.do_rpcrequest_async('LaunchAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def launch_appraise(
        self,
        request: ccc20170705_models.LaunchAppraiseRequest,
    ) -> ccc20170705_models.LaunchAppraiseResponse:
        runtime = util_models.RuntimeOptions()
        return self.launch_appraise_with_options(request, runtime)

    async def launch_appraise_async(
        self,
        request: ccc20170705_models.LaunchAppraiseRequest,
    ) -> ccc20170705_models.LaunchAppraiseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.launch_appraise_with_options_async(request, runtime)

    def launch_short_message_appraise_with_options(
        self,
        request: ccc20170705_models.LaunchShortMessageAppraiseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.LaunchShortMessageAppraiseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.LaunchShortMessageAppraiseResponse(),
            self.do_rpcrequest('LaunchShortMessageAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def launch_short_message_appraise_with_options_async(
        self,
        request: ccc20170705_models.LaunchShortMessageAppraiseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.LaunchShortMessageAppraiseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.LaunchShortMessageAppraiseResponse(),
            await self.do_rpcrequest_async('LaunchShortMessageAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def launch_short_message_appraise(
        self,
        request: ccc20170705_models.LaunchShortMessageAppraiseRequest,
    ) -> ccc20170705_models.LaunchShortMessageAppraiseResponse:
        runtime = util_models.RuntimeOptions()
        return self.launch_short_message_appraise_with_options(request, runtime)

    async def launch_short_message_appraise_async(
        self,
        request: ccc20170705_models.LaunchShortMessageAppraiseRequest,
    ) -> ccc20170705_models.LaunchShortMessageAppraiseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.launch_short_message_appraise_with_options_async(request, runtime)

    def list_agent_devices_with_options(
        self,
        request: ccc20170705_models.ListAgentDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentDevicesResponse(),
            self.do_rpcrequest('ListAgentDevices', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_agent_devices_with_options_async(
        self,
        request: ccc20170705_models.ListAgentDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentDevicesResponse(),
            await self.do_rpcrequest_async('ListAgentDevices', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_devices(
        self,
        request: ccc20170705_models.ListAgentDevicesRequest,
    ) -> ccc20170705_models.ListAgentDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_devices_with_options(request, runtime)

    async def list_agent_devices_async(
        self,
        request: ccc20170705_models.ListAgentDevicesRequest,
    ) -> ccc20170705_models.ListAgentDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_devices_with_options_async(request, runtime)

    def list_agent_events_with_options(
        self,
        request: ccc20170705_models.ListAgentEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentEventsResponse(),
            self.do_rpcrequest('ListAgentEvents', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_agent_events_with_options_async(
        self,
        request: ccc20170705_models.ListAgentEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentEventsResponse(),
            await self.do_rpcrequest_async('ListAgentEvents', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_events(
        self,
        request: ccc20170705_models.ListAgentEventsRequest,
    ) -> ccc20170705_models.ListAgentEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_events_with_options(request, runtime)

    async def list_agent_events_async(
        self,
        request: ccc20170705_models.ListAgentEventsRequest,
    ) -> ccc20170705_models.ListAgentEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_events_with_options_async(request, runtime)

    def list_agent_state_logs_with_options(
        self,
        request: ccc20170705_models.ListAgentStateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentStateLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentStateLogsResponse(),
            self.do_rpcrequest('ListAgentStateLogs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_agent_state_logs_with_options_async(
        self,
        request: ccc20170705_models.ListAgentStateLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentStateLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentStateLogsResponse(),
            await self.do_rpcrequest_async('ListAgentStateLogs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_state_logs(
        self,
        request: ccc20170705_models.ListAgentStateLogsRequest,
    ) -> ccc20170705_models.ListAgentStateLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_state_logs_with_options(request, runtime)

    async def list_agent_state_logs_async(
        self,
        request: ccc20170705_models.ListAgentStateLogsRequest,
    ) -> ccc20170705_models.ListAgentStateLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_state_logs_with_options_async(request, runtime)

    def list_agent_states_with_options(
        self,
        request: ccc20170705_models.ListAgentStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentStatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentStatesResponse(),
            self.do_rpcrequest('ListAgentStates', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_agent_states_with_options_async(
        self,
        request: ccc20170705_models.ListAgentStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentStatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentStatesResponse(),
            await self.do_rpcrequest_async('ListAgentStates', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_states(
        self,
        request: ccc20170705_models.ListAgentStatesRequest,
    ) -> ccc20170705_models.ListAgentStatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_states_with_options(request, runtime)

    async def list_agent_states_async(
        self,
        request: ccc20170705_models.ListAgentStatesRequest,
    ) -> ccc20170705_models.ListAgentStatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_states_with_options_async(request, runtime)

    def list_agent_summary_reports_with_options(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentSummaryReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentSummaryReportsResponse(),
            self.do_rpcrequest('ListAgentSummaryReports', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_agent_summary_reports_with_options_async(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentSummaryReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentSummaryReportsResponse(),
            await self.do_rpcrequest_async('ListAgentSummaryReports', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_summary_reports(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsRequest,
    ) -> ccc20170705_models.ListAgentSummaryReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_summary_reports_with_options(request, runtime)

    async def list_agent_summary_reports_async(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsRequest,
    ) -> ccc20170705_models.ListAgentSummaryReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_summary_reports_with_options_async(request, runtime)

    def list_agent_summary_reports_by_interval_with_options(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsByIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentSummaryReportsByIntervalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentSummaryReportsByIntervalResponse(),
            self.do_rpcrequest('ListAgentSummaryReportsByInterval', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_agent_summary_reports_by_interval_with_options_async(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsByIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentSummaryReportsByIntervalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentSummaryReportsByIntervalResponse(),
            await self.do_rpcrequest_async('ListAgentSummaryReportsByInterval', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_summary_reports_by_interval(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsByIntervalRequest,
    ) -> ccc20170705_models.ListAgentSummaryReportsByIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_summary_reports_by_interval_with_options(request, runtime)

    async def list_agent_summary_reports_by_interval_async(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsByIntervalRequest,
    ) -> ccc20170705_models.ListAgentSummaryReportsByIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_summary_reports_by_interval_with_options_async(request, runtime)

    def list_agent_summary_reports_since_midnight_with_options(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsSinceMidnightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentSummaryReportsSinceMidnightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentSummaryReportsSinceMidnightResponse(),
            self.do_rpcrequest('ListAgentSummaryReportsSinceMidnight', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_agent_summary_reports_since_midnight_with_options_async(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsSinceMidnightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListAgentSummaryReportsSinceMidnightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListAgentSummaryReportsSinceMidnightResponse(),
            await self.do_rpcrequest_async('ListAgentSummaryReportsSinceMidnight', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_summary_reports_since_midnight(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsSinceMidnightRequest,
    ) -> ccc20170705_models.ListAgentSummaryReportsSinceMidnightResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_summary_reports_since_midnight_with_options(request, runtime)

    async def list_agent_summary_reports_since_midnight_async(
        self,
        request: ccc20170705_models.ListAgentSummaryReportsSinceMidnightRequest,
    ) -> ccc20170705_models.ListAgentSummaryReportsSinceMidnightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_summary_reports_since_midnight_with_options_async(request, runtime)

    def list_basic_statistics_report_sub_items_with_options(
        self,
        request: ccc20170705_models.ListBasicStatisticsReportSubItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListBasicStatisticsReportSubItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListBasicStatisticsReportSubItemsResponse(),
            self.do_rpcrequest('ListBasicStatisticsReportSubItems', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_basic_statistics_report_sub_items_with_options_async(
        self,
        request: ccc20170705_models.ListBasicStatisticsReportSubItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListBasicStatisticsReportSubItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListBasicStatisticsReportSubItemsResponse(),
            await self.do_rpcrequest_async('ListBasicStatisticsReportSubItems', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_basic_statistics_report_sub_items(
        self,
        request: ccc20170705_models.ListBasicStatisticsReportSubItemsRequest,
    ) -> ccc20170705_models.ListBasicStatisticsReportSubItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_basic_statistics_report_sub_items_with_options(request, runtime)

    async def list_basic_statistics_report_sub_items_async(
        self,
        request: ccc20170705_models.ListBasicStatisticsReportSubItemsRequest,
    ) -> ccc20170705_models.ListBasicStatisticsReportSubItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_basic_statistics_report_sub_items_with_options_async(request, runtime)

    def list_call_detail_records_with_options(
        self,
        request: ccc20170705_models.ListCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListCallDetailRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListCallDetailRecordsResponse(),
            self.do_rpcrequest('ListCallDetailRecords', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_call_detail_records_with_options_async(
        self,
        request: ccc20170705_models.ListCallDetailRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListCallDetailRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListCallDetailRecordsResponse(),
            await self.do_rpcrequest_async('ListCallDetailRecords', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_detail_records(
        self,
        request: ccc20170705_models.ListCallDetailRecordsRequest,
    ) -> ccc20170705_models.ListCallDetailRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_call_detail_records_with_options(request, runtime)

    async def list_call_detail_records_async(
        self,
        request: ccc20170705_models.ListCallDetailRecordsRequest,
    ) -> ccc20170705_models.ListCallDetailRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_call_detail_records_with_options_async(request, runtime)

    def list_call_event_detail_by_contact_id_with_options(
        self,
        request: ccc20170705_models.ListCallEventDetailByContactIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListCallEventDetailByContactIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListCallEventDetailByContactIdResponse(),
            self.do_rpcrequest('ListCallEventDetailByContactId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_call_event_detail_by_contact_id_with_options_async(
        self,
        request: ccc20170705_models.ListCallEventDetailByContactIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListCallEventDetailByContactIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListCallEventDetailByContactIdResponse(),
            await self.do_rpcrequest_async('ListCallEventDetailByContactId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_event_detail_by_contact_id(
        self,
        request: ccc20170705_models.ListCallEventDetailByContactIdRequest,
    ) -> ccc20170705_models.ListCallEventDetailByContactIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_call_event_detail_by_contact_id_with_options(request, runtime)

    async def list_call_event_detail_by_contact_id_async(
        self,
        request: ccc20170705_models.ListCallEventDetailByContactIdRequest,
    ) -> ccc20170705_models.ListCallEventDetailByContactIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_call_event_detail_by_contact_id_with_options_async(request, runtime)

    def list_call_measure_summary_reports_with_options(
        self,
        request: ccc20170705_models.ListCallMeasureSummaryReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListCallMeasureSummaryReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListCallMeasureSummaryReportsResponse(),
            self.do_rpcrequest('ListCallMeasureSummaryReports', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_call_measure_summary_reports_with_options_async(
        self,
        request: ccc20170705_models.ListCallMeasureSummaryReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListCallMeasureSummaryReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListCallMeasureSummaryReportsResponse(),
            await self.do_rpcrequest_async('ListCallMeasureSummaryReports', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_measure_summary_reports(
        self,
        request: ccc20170705_models.ListCallMeasureSummaryReportsRequest,
    ) -> ccc20170705_models.ListCallMeasureSummaryReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_call_measure_summary_reports_with_options(request, runtime)

    async def list_call_measure_summary_reports_async(
        self,
        request: ccc20170705_models.ListCallMeasureSummaryReportsRequest,
    ) -> ccc20170705_models.ListCallMeasureSummaryReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_call_measure_summary_reports_with_options_async(request, runtime)

    def list_config_with_options(
        self,
        request: ccc20170705_models.ListConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListConfigResponse(),
            self.do_rpcrequest('ListConfig', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_config_with_options_async(
        self,
        request: ccc20170705_models.ListConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListConfigResponse(),
            await self.do_rpcrequest_async('ListConfig', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_config(
        self,
        request: ccc20170705_models.ListConfigRequest,
    ) -> ccc20170705_models.ListConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_config_with_options(request, runtime)

    async def list_config_async(
        self,
        request: ccc20170705_models.ListConfigRequest,
    ) -> ccc20170705_models.ListConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_config_with_options_async(request, runtime)

    def list_contact_flows_with_options(
        self,
        request: ccc20170705_models.ListContactFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListContactFlowsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListContactFlowsResponse(),
            self.do_rpcrequest('ListContactFlows', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_contact_flows_with_options_async(
        self,
        request: ccc20170705_models.ListContactFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListContactFlowsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListContactFlowsResponse(),
            await self.do_rpcrequest_async('ListContactFlows', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_contact_flows(
        self,
        request: ccc20170705_models.ListContactFlowsRequest,
    ) -> ccc20170705_models.ListContactFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_contact_flows_with_options(request, runtime)

    async def list_contact_flows_async(
        self,
        request: ccc20170705_models.ListContactFlowsRequest,
    ) -> ccc20170705_models.ListContactFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_contact_flows_with_options_async(request, runtime)

    def list_instances_of_user_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListInstancesOfUserResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ccc20170705_models.ListInstancesOfUserResponse(),
            self.do_rpcrequest('ListInstancesOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instances_of_user_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListInstancesOfUserResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ccc20170705_models.ListInstancesOfUserResponse(),
            await self.do_rpcrequest_async('ListInstancesOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances_of_user(self) -> ccc20170705_models.ListInstancesOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_of_user_with_options(runtime)

    async def list_instances_of_user_async(self) -> ccc20170705_models.ListInstancesOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_of_user_with_options_async(runtime)

    def list_ivr_tracking_detail_with_options(
        self,
        request: ccc20170705_models.ListIvrTrackingDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListIvrTrackingDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListIvrTrackingDetailResponse(),
            self.do_rpcrequest('ListIvrTrackingDetail', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ivr_tracking_detail_with_options_async(
        self,
        request: ccc20170705_models.ListIvrTrackingDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListIvrTrackingDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListIvrTrackingDetailResponse(),
            await self.do_rpcrequest_async('ListIvrTrackingDetail', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ivr_tracking_detail(
        self,
        request: ccc20170705_models.ListIvrTrackingDetailRequest,
    ) -> ccc20170705_models.ListIvrTrackingDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ivr_tracking_detail_with_options(request, runtime)

    async def list_ivr_tracking_detail_async(
        self,
        request: ccc20170705_models.ListIvrTrackingDetailRequest,
    ) -> ccc20170705_models.ListIvrTrackingDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ivr_tracking_detail_with_options_async(request, runtime)

    def list_job_groups_with_options(
        self,
        request: ccc20170705_models.ListJobGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListJobGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListJobGroupsResponse(),
            self.do_rpcrequest('ListJobGroups', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_job_groups_with_options_async(
        self,
        request: ccc20170705_models.ListJobGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListJobGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListJobGroupsResponse(),
            await self.do_rpcrequest_async('ListJobGroups', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_job_groups(
        self,
        request: ccc20170705_models.ListJobGroupsRequest,
    ) -> ccc20170705_models.ListJobGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_groups_with_options(request, runtime)

    async def list_job_groups_async(
        self,
        request: ccc20170705_models.ListJobGroupsRequest,
    ) -> ccc20170705_models.ListJobGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_groups_with_options_async(request, runtime)

    def list_job_status_with_options(
        self,
        request: ccc20170705_models.ListJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListJobStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListJobStatusResponse(),
            self.do_rpcrequest('ListJobStatus', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_job_status_with_options_async(
        self,
        request: ccc20170705_models.ListJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListJobStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListJobStatusResponse(),
            await self.do_rpcrequest_async('ListJobStatus', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_job_status(
        self,
        request: ccc20170705_models.ListJobStatusRequest,
    ) -> ccc20170705_models.ListJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_status_with_options(request, runtime)

    async def list_job_status_async(
        self,
        request: ccc20170705_models.ListJobStatusRequest,
    ) -> ccc20170705_models.ListJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_status_with_options_async(request, runtime)

    def list_jobs_by_group_with_options(
        self,
        request: ccc20170705_models.ListJobsByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListJobsByGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListJobsByGroupResponse(),
            self.do_rpcrequest('ListJobsByGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_jobs_by_group_with_options_async(
        self,
        request: ccc20170705_models.ListJobsByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListJobsByGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListJobsByGroupResponse(),
            await self.do_rpcrequest_async('ListJobsByGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_jobs_by_group(
        self,
        request: ccc20170705_models.ListJobsByGroupRequest,
    ) -> ccc20170705_models.ListJobsByGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_by_group_with_options(request, runtime)

    async def list_jobs_by_group_async(
        self,
        request: ccc20170705_models.ListJobsByGroupRequest,
    ) -> ccc20170705_models.ListJobsByGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_by_group_with_options_async(request, runtime)

    def list_medias_with_options(
        self,
        request: ccc20170705_models.ListMediasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListMediasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListMediasResponse(),
            self.do_rpcrequest('ListMedias', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_medias_with_options_async(
        self,
        request: ccc20170705_models.ListMediasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListMediasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListMediasResponse(),
            await self.do_rpcrequest_async('ListMedias', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_medias(
        self,
        request: ccc20170705_models.ListMediasRequest,
    ) -> ccc20170705_models.ListMediasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_medias_with_options(request, runtime)

    async def list_medias_async(
        self,
        request: ccc20170705_models.ListMediasRequest,
    ) -> ccc20170705_models.ListMediasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_medias_with_options_async(request, runtime)

    def list_outbound_phone_number_of_user_with_options(
        self,
        request: ccc20170705_models.ListOutboundPhoneNumberOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListOutboundPhoneNumberOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListOutboundPhoneNumberOfUserResponse(),
            self.do_rpcrequest('ListOutboundPhoneNumberOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_outbound_phone_number_of_user_with_options_async(
        self,
        request: ccc20170705_models.ListOutboundPhoneNumberOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListOutboundPhoneNumberOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListOutboundPhoneNumberOfUserResponse(),
            await self.do_rpcrequest_async('ListOutboundPhoneNumberOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_outbound_phone_number_of_user(
        self,
        request: ccc20170705_models.ListOutboundPhoneNumberOfUserRequest,
    ) -> ccc20170705_models.ListOutboundPhoneNumberOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_phone_number_of_user_with_options(request, runtime)

    async def list_outbound_phone_number_of_user_async(
        self,
        request: ccc20170705_models.ListOutboundPhoneNumberOfUserRequest,
    ) -> ccc20170705_models.ListOutboundPhoneNumberOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_outbound_phone_number_of_user_with_options_async(request, runtime)

    def list_phone_numbers_with_options(
        self,
        request: ccc20170705_models.ListPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListPhoneNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListPhoneNumbersResponse(),
            self.do_rpcrequest('ListPhoneNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_phone_numbers_with_options_async(
        self,
        request: ccc20170705_models.ListPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListPhoneNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListPhoneNumbersResponse(),
            await self.do_rpcrequest_async('ListPhoneNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_phone_numbers(
        self,
        request: ccc20170705_models.ListPhoneNumbersRequest,
    ) -> ccc20170705_models.ListPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_phone_numbers_with_options(request, runtime)

    async def list_phone_numbers_async(
        self,
        request: ccc20170705_models.ListPhoneNumbersRequest,
    ) -> ccc20170705_models.ListPhoneNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_phone_numbers_with_options_async(request, runtime)

    def list_phone_tags_with_options(
        self,
        request: ccc20170705_models.ListPhoneTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListPhoneTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListPhoneTagsResponse(),
            self.do_rpcrequest('ListPhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_phone_tags_with_options_async(
        self,
        request: ccc20170705_models.ListPhoneTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListPhoneTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListPhoneTagsResponse(),
            await self.do_rpcrequest_async('ListPhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_phone_tags(
        self,
        request: ccc20170705_models.ListPhoneTagsRequest,
    ) -> ccc20170705_models.ListPhoneTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_phone_tags_with_options(request, runtime)

    async def list_phone_tags_async(
        self,
        request: ccc20170705_models.ListPhoneTagsRequest,
    ) -> ccc20170705_models.ListPhoneTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_phone_tags_with_options_async(request, runtime)

    def list_real_time_agent_with_options(
        self,
        request: ccc20170705_models.ListRealTimeAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRealTimeAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRealTimeAgentResponse(),
            self.do_rpcrequest('ListRealTimeAgent', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_real_time_agent_with_options_async(
        self,
        request: ccc20170705_models.ListRealTimeAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRealTimeAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRealTimeAgentResponse(),
            await self.do_rpcrequest_async('ListRealTimeAgent', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_real_time_agent(
        self,
        request: ccc20170705_models.ListRealTimeAgentRequest,
    ) -> ccc20170705_models.ListRealTimeAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_real_time_agent_with_options(request, runtime)

    async def list_real_time_agent_async(
        self,
        request: ccc20170705_models.ListRealTimeAgentRequest,
    ) -> ccc20170705_models.ListRealTimeAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_real_time_agent_with_options_async(request, runtime)

    def list_recent_call_records_with_options(
        self,
        request: ccc20170705_models.ListRecentCallRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRecentCallRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRecentCallRecordsResponse(),
            self.do_rpcrequest('ListRecentCallRecords', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_recent_call_records_with_options_async(
        self,
        request: ccc20170705_models.ListRecentCallRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRecentCallRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRecentCallRecordsResponse(),
            await self.do_rpcrequest_async('ListRecentCallRecords', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_recent_call_records(
        self,
        request: ccc20170705_models.ListRecentCallRecordsRequest,
    ) -> ccc20170705_models.ListRecentCallRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_recent_call_records_with_options(request, runtime)

    async def list_recent_call_records_async(
        self,
        request: ccc20170705_models.ListRecentCallRecordsRequest,
    ) -> ccc20170705_models.ListRecentCallRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_recent_call_records_with_options_async(request, runtime)

    def list_recording_of_dual_track_with_options(
        self,
        request: ccc20170705_models.ListRecordingOfDualTrackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRecordingOfDualTrackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRecordingOfDualTrackResponse(),
            self.do_rpcrequest('ListRecordingOfDualTrack', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_recording_of_dual_track_with_options_async(
        self,
        request: ccc20170705_models.ListRecordingOfDualTrackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRecordingOfDualTrackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRecordingOfDualTrackResponse(),
            await self.do_rpcrequest_async('ListRecordingOfDualTrack', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_recording_of_dual_track(
        self,
        request: ccc20170705_models.ListRecordingOfDualTrackRequest,
    ) -> ccc20170705_models.ListRecordingOfDualTrackResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_recording_of_dual_track_with_options(request, runtime)

    async def list_recording_of_dual_track_async(
        self,
        request: ccc20170705_models.ListRecordingOfDualTrackRequest,
    ) -> ccc20170705_models.ListRecordingOfDualTrackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_recording_of_dual_track_with_options_async(request, runtime)

    def list_recordings_with_options(
        self,
        request: ccc20170705_models.ListRecordingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRecordingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRecordingsResponse(),
            self.do_rpcrequest('ListRecordings', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_recordings_with_options_async(
        self,
        request: ccc20170705_models.ListRecordingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRecordingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRecordingsResponse(),
            await self.do_rpcrequest_async('ListRecordings', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_recordings(
        self,
        request: ccc20170705_models.ListRecordingsRequest,
    ) -> ccc20170705_models.ListRecordingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_recordings_with_options(request, runtime)

    async def list_recordings_async(
        self,
        request: ccc20170705_models.ListRecordingsRequest,
    ) -> ccc20170705_models.ListRecordingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_recordings_with_options_async(request, runtime)

    def list_recordings_by_contact_id_with_options(
        self,
        request: ccc20170705_models.ListRecordingsByContactIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRecordingsByContactIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRecordingsByContactIdResponse(),
            self.do_rpcrequest('ListRecordingsByContactId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_recordings_by_contact_id_with_options_async(
        self,
        request: ccc20170705_models.ListRecordingsByContactIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRecordingsByContactIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRecordingsByContactIdResponse(),
            await self.do_rpcrequest_async('ListRecordingsByContactId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_recordings_by_contact_id(
        self,
        request: ccc20170705_models.ListRecordingsByContactIdRequest,
    ) -> ccc20170705_models.ListRecordingsByContactIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_recordings_by_contact_id_with_options(request, runtime)

    async def list_recordings_by_contact_id_async(
        self,
        request: ccc20170705_models.ListRecordingsByContactIdRequest,
    ) -> ccc20170705_models.ListRecordingsByContactIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_recordings_by_contact_id_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: ccc20170705_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRolesResponse(),
            self.do_rpcrequest('ListRoles', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: ccc20170705_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListRolesResponse(),
            await self.do_rpcrequest_async('ListRoles', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_roles(
        self,
        request: ccc20170705_models.ListRolesRequest,
    ) -> ccc20170705_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: ccc20170705_models.ListRolesRequest,
    ) -> ccc20170705_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_scenario_templates_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListScenarioTemplatesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ccc20170705_models.ListScenarioTemplatesResponse(),
            self.do_rpcrequest('ListScenarioTemplates', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scenario_templates_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListScenarioTemplatesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ccc20170705_models.ListScenarioTemplatesResponse(),
            await self.do_rpcrequest_async('ListScenarioTemplates', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scenario_templates(self) -> ccc20170705_models.ListScenarioTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scenario_templates_with_options(runtime)

    async def list_scenario_templates_async(self) -> ccc20170705_models.ListScenarioTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scenario_templates_with_options_async(runtime)

    def list_scenarios_with_options(
        self,
        request: ccc20170705_models.ListScenariosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListScenariosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListScenariosResponse(),
            self.do_rpcrequest('ListScenarios', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scenarios_with_options_async(
        self,
        request: ccc20170705_models.ListScenariosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListScenariosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListScenariosResponse(),
            await self.do_rpcrequest_async('ListScenarios', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scenarios(
        self,
        request: ccc20170705_models.ListScenariosRequest,
    ) -> ccc20170705_models.ListScenariosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scenarios_with_options(request, runtime)

    async def list_scenarios_async(
        self,
        request: ccc20170705_models.ListScenariosRequest,
    ) -> ccc20170705_models.ListScenariosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scenarios_with_options_async(request, runtime)

    def list_skill_group_states_with_options(
        self,
        request: ccc20170705_models.ListSkillGroupStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupStatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupStatesResponse(),
            self.do_rpcrequest('ListSkillGroupStates', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_skill_group_states_with_options_async(
        self,
        request: ccc20170705_models.ListSkillGroupStatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupStatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupStatesResponse(),
            await self.do_rpcrequest_async('ListSkillGroupStates', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_group_states(
        self,
        request: ccc20170705_models.ListSkillGroupStatesRequest,
    ) -> ccc20170705_models.ListSkillGroupStatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_states_with_options(request, runtime)

    async def list_skill_group_states_async(
        self,
        request: ccc20170705_models.ListSkillGroupStatesRequest,
    ) -> ccc20170705_models.ListSkillGroupStatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_group_states_with_options_async(request, runtime)

    def list_skill_group_summary_reports_with_options(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupSummaryReportsResponse(),
            self.do_rpcrequest('ListSkillGroupSummaryReports', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_skill_group_summary_reports_with_options_async(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupSummaryReportsResponse(),
            await self.do_rpcrequest_async('ListSkillGroupSummaryReports', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_group_summary_reports(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsRequest,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_summary_reports_with_options(request, runtime)

    async def list_skill_group_summary_reports_async(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsRequest,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_group_summary_reports_with_options_async(request, runtime)

    def list_skill_group_summary_reports_by_interval_with_options(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsByIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsByIntervalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupSummaryReportsByIntervalResponse(),
            self.do_rpcrequest('ListSkillGroupSummaryReportsByInterval', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_skill_group_summary_reports_by_interval_with_options_async(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsByIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsByIntervalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupSummaryReportsByIntervalResponse(),
            await self.do_rpcrequest_async('ListSkillGroupSummaryReportsByInterval', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_group_summary_reports_by_interval(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsByIntervalRequest,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsByIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_summary_reports_by_interval_with_options(request, runtime)

    async def list_skill_group_summary_reports_by_interval_async(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsByIntervalRequest,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsByIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_group_summary_reports_by_interval_with_options_async(request, runtime)

    def list_skill_group_summary_reports_since_midnight_with_options(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupSummaryReportsSinceMidnightResponse(),
            self.do_rpcrequest('ListSkillGroupSummaryReportsSinceMidnight', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_skill_group_summary_reports_since_midnight_with_options_async(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupSummaryReportsSinceMidnightResponse(),
            await self.do_rpcrequest_async('ListSkillGroupSummaryReportsSinceMidnight', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_group_summary_reports_since_midnight(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_summary_reports_since_midnight_with_options(request, runtime)

    async def list_skill_group_summary_reports_since_midnight_async(
        self,
        request: ccc20170705_models.ListSkillGroupSummaryReportsSinceMidnightRequest,
    ) -> ccc20170705_models.ListSkillGroupSummaryReportsSinceMidnightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_group_summary_reports_since_midnight_with_options_async(request, runtime)

    def list_skill_groups_with_options(
        self,
        request: ccc20170705_models.ListSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupsResponse(),
            self.do_rpcrequest('ListSkillGroups', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_skill_groups_with_options_async(
        self,
        request: ccc20170705_models.ListSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupsResponse(),
            await self.do_rpcrequest_async('ListSkillGroups', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_groups(
        self,
        request: ccc20170705_models.ListSkillGroupsRequest,
    ) -> ccc20170705_models.ListSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_groups_with_options(request, runtime)

    async def list_skill_groups_async(
        self,
        request: ccc20170705_models.ListSkillGroupsRequest,
    ) -> ccc20170705_models.ListSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_groups_with_options_async(request, runtime)

    def list_skill_groups_of_user_with_options(
        self,
        request: ccc20170705_models.ListSkillGroupsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupsOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupsOfUserResponse(),
            self.do_rpcrequest('ListSkillGroupsOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_skill_groups_of_user_with_options_async(
        self,
        request: ccc20170705_models.ListSkillGroupsOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSkillGroupsOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSkillGroupsOfUserResponse(),
            await self.do_rpcrequest_async('ListSkillGroupsOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_groups_of_user(
        self,
        request: ccc20170705_models.ListSkillGroupsOfUserRequest,
    ) -> ccc20170705_models.ListSkillGroupsOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_skill_groups_of_user_with_options(request, runtime)

    async def list_skill_groups_of_user_async(
        self,
        request: ccc20170705_models.ListSkillGroupsOfUserRequest,
    ) -> ccc20170705_models.ListSkillGroupsOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_groups_of_user_with_options_async(request, runtime)

    def list_surveys_with_options(
        self,
        request: ccc20170705_models.ListSurveysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSurveysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSurveysResponse(),
            self.do_rpcrequest('ListSurveys', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_surveys_with_options_async(
        self,
        request: ccc20170705_models.ListSurveysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListSurveysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListSurveysResponse(),
            await self.do_rpcrequest_async('ListSurveys', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_surveys(
        self,
        request: ccc20170705_models.ListSurveysRequest,
    ) -> ccc20170705_models.ListSurveysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_surveys_with_options(request, runtime)

    async def list_surveys_async(
        self,
        request: ccc20170705_models.ListSurveysRequest,
    ) -> ccc20170705_models.ListSurveysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_surveys_with_options_async(request, runtime)

    def list_transferable_skill_groups_with_options(
        self,
        request: ccc20170705_models.ListTransferableSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListTransferableSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListTransferableSkillGroupsResponse(),
            self.do_rpcrequest('ListTransferableSkillGroups', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_transferable_skill_groups_with_options_async(
        self,
        request: ccc20170705_models.ListTransferableSkillGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListTransferableSkillGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListTransferableSkillGroupsResponse(),
            await self.do_rpcrequest_async('ListTransferableSkillGroups', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_transferable_skill_groups(
        self,
        request: ccc20170705_models.ListTransferableSkillGroupsRequest,
    ) -> ccc20170705_models.ListTransferableSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transferable_skill_groups_with_options(request, runtime)

    async def list_transferable_skill_groups_async(
        self,
        request: ccc20170705_models.ListTransferableSkillGroupsRequest,
    ) -> ccc20170705_models.ListTransferableSkillGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transferable_skill_groups_with_options_async(request, runtime)

    def list_trunk_providers_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListTrunkProvidersResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ccc20170705_models.ListTrunkProvidersResponse(),
            self.do_rpcrequest('ListTrunkProviders', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_trunk_providers_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListTrunkProvidersResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ccc20170705_models.ListTrunkProvidersResponse(),
            await self.do_rpcrequest_async('ListTrunkProviders', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_trunk_providers(self) -> ccc20170705_models.ListTrunkProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_trunk_providers_with_options(runtime)

    async def list_trunk_providers_async(self) -> ccc20170705_models.ListTrunkProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_trunk_providers_with_options_async(runtime)

    def list_trunks_of_skill_group_with_options(
        self,
        request: ccc20170705_models.ListTrunksOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListTrunksOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListTrunksOfSkillGroupResponse(),
            self.do_rpcrequest('ListTrunksOfSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_trunks_of_skill_group_with_options_async(
        self,
        request: ccc20170705_models.ListTrunksOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListTrunksOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListTrunksOfSkillGroupResponse(),
            await self.do_rpcrequest_async('ListTrunksOfSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_trunks_of_skill_group(
        self,
        request: ccc20170705_models.ListTrunksOfSkillGroupRequest,
    ) -> ccc20170705_models.ListTrunksOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_trunks_of_skill_group_with_options(request, runtime)

    async def list_trunks_of_skill_group_async(
        self,
        request: ccc20170705_models.ListTrunksOfSkillGroupRequest,
    ) -> ccc20170705_models.ListTrunksOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_trunks_of_skill_group_with_options_async(request, runtime)

    def list_unreachable_contacts_with_options(
        self,
        request: ccc20170705_models.ListUnreachableContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListUnreachableContactsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListUnreachableContactsResponse(),
            self.do_rpcrequest('ListUnreachableContacts', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_unreachable_contacts_with_options_async(
        self,
        request: ccc20170705_models.ListUnreachableContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListUnreachableContactsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListUnreachableContactsResponse(),
            await self.do_rpcrequest_async('ListUnreachableContacts', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_unreachable_contacts(
        self,
        request: ccc20170705_models.ListUnreachableContactsRequest,
    ) -> ccc20170705_models.ListUnreachableContactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_unreachable_contacts_with_options(request, runtime)

    async def list_unreachable_contacts_async(
        self,
        request: ccc20170705_models.ListUnreachableContactsRequest,
    ) -> ccc20170705_models.ListUnreachableContactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_unreachable_contacts_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ccc20170705_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListUsersResponse(),
            self.do_rpcrequest('ListUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ccc20170705_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListUsersResponse(),
            await self.do_rpcrequest_async('ListUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(
        self,
        request: ccc20170705_models.ListUsersRequest,
    ) -> ccc20170705_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ccc20170705_models.ListUsersRequest,
    ) -> ccc20170705_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_users_of_skill_group_with_options(
        self,
        request: ccc20170705_models.ListUsersOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListUsersOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListUsersOfSkillGroupResponse(),
            self.do_rpcrequest('ListUsersOfSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_of_skill_group_with_options_async(
        self,
        request: ccc20170705_models.ListUsersOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListUsersOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListUsersOfSkillGroupResponse(),
            await self.do_rpcrequest_async('ListUsersOfSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users_of_skill_group(
        self,
        request: ccc20170705_models.ListUsersOfSkillGroupRequest,
    ) -> ccc20170705_models.ListUsersOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_of_skill_group_with_options(request, runtime)

    async def list_users_of_skill_group_async(
        self,
        request: ccc20170705_models.ListUsersOfSkillGroupRequest,
    ) -> ccc20170705_models.ListUsersOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_of_skill_group_with_options_async(request, runtime)

    def list_voice_appraise_with_options(
        self,
        request: ccc20170705_models.ListVoiceAppraiseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListVoiceAppraiseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListVoiceAppraiseResponse(),
            self.do_rpcrequest('ListVoiceAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_voice_appraise_with_options_async(
        self,
        request: ccc20170705_models.ListVoiceAppraiseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ListVoiceAppraiseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ListVoiceAppraiseResponse(),
            await self.do_rpcrequest_async('ListVoiceAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_voice_appraise(
        self,
        request: ccc20170705_models.ListVoiceAppraiseRequest,
    ) -> ccc20170705_models.ListVoiceAppraiseResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_voice_appraise_with_options(request, runtime)

    async def list_voice_appraise_async(
        self,
        request: ccc20170705_models.ListVoiceAppraiseRequest,
    ) -> ccc20170705_models.ListVoiceAppraiseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_voice_appraise_with_options_async(request, runtime)

    def modify_agent_device_with_options(
        self,
        request: ccc20170705_models.ModifyAgentDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyAgentDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyAgentDeviceResponse(),
            self.do_rpcrequest('ModifyAgentDevice', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_agent_device_with_options_async(
        self,
        request: ccc20170705_models.ModifyAgentDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyAgentDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyAgentDeviceResponse(),
            await self.do_rpcrequest_async('ModifyAgentDevice', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_agent_device(
        self,
        request: ccc20170705_models.ModifyAgentDeviceRequest,
    ) -> ccc20170705_models.ModifyAgentDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_agent_device_with_options(request, runtime)

    async def modify_agent_device_async(
        self,
        request: ccc20170705_models.ModifyAgentDeviceRequest,
    ) -> ccc20170705_models.ModifyAgentDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_agent_device_with_options_async(request, runtime)

    def modify_cab_instance_with_options(
        self,
        request: ccc20170705_models.ModifyCabInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyCabInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyCabInstanceResponse(),
            self.do_rpcrequest('ModifyCabInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cab_instance_with_options_async(
        self,
        request: ccc20170705_models.ModifyCabInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyCabInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyCabInstanceResponse(),
            await self.do_rpcrequest_async('ModifyCabInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cab_instance(
        self,
        request: ccc20170705_models.ModifyCabInstanceRequest,
    ) -> ccc20170705_models.ModifyCabInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cab_instance_with_options(request, runtime)

    async def modify_cab_instance_async(
        self,
        request: ccc20170705_models.ModifyCabInstanceRequest,
    ) -> ccc20170705_models.ModifyCabInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cab_instance_with_options_async(request, runtime)

    def modify_call_ratio_with_options(
        self,
        request: ccc20170705_models.ModifyCallRatioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyCallRatioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyCallRatioResponse(),
            self.do_rpcrequest('ModifyCallRatio', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_call_ratio_with_options_async(
        self,
        request: ccc20170705_models.ModifyCallRatioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyCallRatioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyCallRatioResponse(),
            await self.do_rpcrequest_async('ModifyCallRatio', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_call_ratio(
        self,
        request: ccc20170705_models.ModifyCallRatioRequest,
    ) -> ccc20170705_models.ModifyCallRatioResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_call_ratio_with_options(request, runtime)

    async def modify_call_ratio_async(
        self,
        request: ccc20170705_models.ModifyCallRatioRequest,
    ) -> ccc20170705_models.ModifyCallRatioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_call_ratio_with_options_async(request, runtime)

    def modify_phone_number_with_options(
        self,
        request: ccc20170705_models.ModifyPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyPhoneNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyPhoneNumberResponse(),
            self.do_rpcrequest('ModifyPhoneNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_phone_number_with_options_async(
        self,
        request: ccc20170705_models.ModifyPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyPhoneNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyPhoneNumberResponse(),
            await self.do_rpcrequest_async('ModifyPhoneNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_phone_number(
        self,
        request: ccc20170705_models.ModifyPhoneNumberRequest,
    ) -> ccc20170705_models.ModifyPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_phone_number_with_options(request, runtime)

    async def modify_phone_number_async(
        self,
        request: ccc20170705_models.ModifyPhoneNumberRequest,
    ) -> ccc20170705_models.ModifyPhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_phone_number_with_options_async(request, runtime)

    def modify_phone_tags_with_options(
        self,
        request: ccc20170705_models.ModifyPhoneTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyPhoneTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyPhoneTagsResponse(),
            self.do_rpcrequest('ModifyPhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_phone_tags_with_options_async(
        self,
        request: ccc20170705_models.ModifyPhoneTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyPhoneTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyPhoneTagsResponse(),
            await self.do_rpcrequest_async('ModifyPhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_phone_tags(
        self,
        request: ccc20170705_models.ModifyPhoneTagsRequest,
    ) -> ccc20170705_models.ModifyPhoneTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_phone_tags_with_options(request, runtime)

    async def modify_phone_tags_async(
        self,
        request: ccc20170705_models.ModifyPhoneTagsRequest,
    ) -> ccc20170705_models.ModifyPhoneTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_phone_tags_with_options_async(request, runtime)

    def modify_primary_trunks_of_skill_group_with_options(
        self,
        request: ccc20170705_models.ModifyPrimaryTrunksOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyPrimaryTrunksOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyPrimaryTrunksOfSkillGroupResponse(),
            self.do_rpcrequest('ModifyPrimaryTrunksOfSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_primary_trunks_of_skill_group_with_options_async(
        self,
        request: ccc20170705_models.ModifyPrimaryTrunksOfSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyPrimaryTrunksOfSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyPrimaryTrunksOfSkillGroupResponse(),
            await self.do_rpcrequest_async('ModifyPrimaryTrunksOfSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_primary_trunks_of_skill_group(
        self,
        request: ccc20170705_models.ModifyPrimaryTrunksOfSkillGroupRequest,
    ) -> ccc20170705_models.ModifyPrimaryTrunksOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_primary_trunks_of_skill_group_with_options(request, runtime)

    async def modify_primary_trunks_of_skill_group_async(
        self,
        request: ccc20170705_models.ModifyPrimaryTrunksOfSkillGroupRequest,
    ) -> ccc20170705_models.ModifyPrimaryTrunksOfSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_primary_trunks_of_skill_group_with_options_async(request, runtime)

    def modify_privacy_number_call_detail_with_options(
        self,
        request: ccc20170705_models.ModifyPrivacyNumberCallDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyPrivacyNumberCallDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyPrivacyNumberCallDetailResponse(),
            self.do_rpcrequest('ModifyPrivacyNumberCallDetail', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_privacy_number_call_detail_with_options_async(
        self,
        request: ccc20170705_models.ModifyPrivacyNumberCallDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyPrivacyNumberCallDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyPrivacyNumberCallDetailResponse(),
            await self.do_rpcrequest_async('ModifyPrivacyNumberCallDetail', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_privacy_number_call_detail(
        self,
        request: ccc20170705_models.ModifyPrivacyNumberCallDetailRequest,
    ) -> ccc20170705_models.ModifyPrivacyNumberCallDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_privacy_number_call_detail_with_options(request, runtime)

    async def modify_privacy_number_call_detail_async(
        self,
        request: ccc20170705_models.ModifyPrivacyNumberCallDetailRequest,
    ) -> ccc20170705_models.ModifyPrivacyNumberCallDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_privacy_number_call_detail_with_options_async(request, runtime)

    def modify_scenario_with_options(
        self,
        request: ccc20170705_models.ModifyScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyScenarioResponse(),
            self.do_rpcrequest('ModifyScenario', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scenario_with_options_async(
        self,
        request: ccc20170705_models.ModifyScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyScenarioResponse(),
            await self.do_rpcrequest_async('ModifyScenario', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scenario(
        self,
        request: ccc20170705_models.ModifyScenarioRequest,
    ) -> ccc20170705_models.ModifyScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scenario_with_options(request, runtime)

    async def modify_scenario_async(
        self,
        request: ccc20170705_models.ModifyScenarioRequest,
    ) -> ccc20170705_models.ModifyScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scenario_with_options_async(request, runtime)

    def modify_skill_group_with_options(
        self,
        request: ccc20170705_models.ModifySkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifySkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifySkillGroupResponse(),
            self.do_rpcrequest('ModifySkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_skill_group_with_options_async(
        self,
        request: ccc20170705_models.ModifySkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifySkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifySkillGroupResponse(),
            await self.do_rpcrequest_async('ModifySkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_skill_group(
        self,
        request: ccc20170705_models.ModifySkillGroupRequest,
    ) -> ccc20170705_models.ModifySkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_group_with_options(request, runtime)

    async def modify_skill_group_async(
        self,
        request: ccc20170705_models.ModifySkillGroupRequest,
    ) -> ccc20170705_models.ModifySkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_skill_group_with_options_async(request, runtime)

    def modify_skill_group_of_user_with_options(
        self,
        request: ccc20170705_models.ModifySkillGroupOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifySkillGroupOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifySkillGroupOfUserResponse(),
            self.do_rpcrequest('ModifySkillGroupOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_skill_group_of_user_with_options_async(
        self,
        request: ccc20170705_models.ModifySkillGroupOfUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifySkillGroupOfUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifySkillGroupOfUserResponse(),
            await self.do_rpcrequest_async('ModifySkillGroupOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_skill_group_of_user(
        self,
        request: ccc20170705_models.ModifySkillGroupOfUserRequest,
    ) -> ccc20170705_models.ModifySkillGroupOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_group_of_user_with_options(request, runtime)

    async def modify_skill_group_of_user_async(
        self,
        request: ccc20170705_models.ModifySkillGroupOfUserRequest,
    ) -> ccc20170705_models.ModifySkillGroupOfUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_skill_group_of_user_with_options_async(request, runtime)

    def modify_skill_group_outbound_numbers_with_options(
        self,
        request: ccc20170705_models.ModifySkillGroupOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifySkillGroupOutboundNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifySkillGroupOutboundNumbersResponse(),
            self.do_rpcrequest('ModifySkillGroupOutboundNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_skill_group_outbound_numbers_with_options_async(
        self,
        request: ccc20170705_models.ModifySkillGroupOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifySkillGroupOutboundNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifySkillGroupOutboundNumbersResponse(),
            await self.do_rpcrequest_async('ModifySkillGroupOutboundNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_skill_group_outbound_numbers(
        self,
        request: ccc20170705_models.ModifySkillGroupOutboundNumbersRequest,
    ) -> ccc20170705_models.ModifySkillGroupOutboundNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_group_outbound_numbers_with_options(request, runtime)

    async def modify_skill_group_outbound_numbers_async(
        self,
        request: ccc20170705_models.ModifySkillGroupOutboundNumbersRequest,
    ) -> ccc20170705_models.ModifySkillGroupOutboundNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_skill_group_outbound_numbers_with_options_async(request, runtime)

    def modify_survey_with_options(
        self,
        request: ccc20170705_models.ModifySurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifySurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifySurveyResponse(),
            self.do_rpcrequest('ModifySurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_survey_with_options_async(
        self,
        request: ccc20170705_models.ModifySurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifySurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifySurveyResponse(),
            await self.do_rpcrequest_async('ModifySurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_survey(
        self,
        request: ccc20170705_models.ModifySurveyRequest,
    ) -> ccc20170705_models.ModifySurveyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_survey_with_options(request, runtime)

    async def modify_survey_async(
        self,
        request: ccc20170705_models.ModifySurveyRequest,
    ) -> ccc20170705_models.ModifySurveyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_survey_with_options_async(request, runtime)

    def modify_user_with_options(
        self,
        request: ccc20170705_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyUserResponse(),
            self.do_rpcrequest('ModifyUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_user_with_options_async(
        self,
        request: ccc20170705_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ModifyUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ModifyUserResponse(),
            await self.do_rpcrequest_async('ModifyUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user(
        self,
        request: ccc20170705_models.ModifyUserRequest,
    ) -> ccc20170705_models.ModifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    async def modify_user_async(
        self,
        request: ccc20170705_models.ModifyUserRequest,
    ) -> ccc20170705_models.ModifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_with_options_async(request, runtime)

    def pick_global_outbound_numbers_with_options(
        self,
        request: ccc20170705_models.PickGlobalOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PickGlobalOutboundNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PickGlobalOutboundNumbersResponse(),
            self.do_rpcrequest('PickGlobalOutboundNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pick_global_outbound_numbers_with_options_async(
        self,
        request: ccc20170705_models.PickGlobalOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PickGlobalOutboundNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PickGlobalOutboundNumbersResponse(),
            await self.do_rpcrequest_async('PickGlobalOutboundNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pick_global_outbound_numbers(
        self,
        request: ccc20170705_models.PickGlobalOutboundNumbersRequest,
    ) -> ccc20170705_models.PickGlobalOutboundNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.pick_global_outbound_numbers_with_options(request, runtime)

    async def pick_global_outbound_numbers_async(
        self,
        request: ccc20170705_models.PickGlobalOutboundNumbersRequest,
    ) -> ccc20170705_models.PickGlobalOutboundNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pick_global_outbound_numbers_with_options_async(request, runtime)

    def pick_local_number_with_options(
        self,
        request: ccc20170705_models.PickLocalNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PickLocalNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PickLocalNumberResponse(),
            self.do_rpcrequest('PickLocalNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pick_local_number_with_options_async(
        self,
        request: ccc20170705_models.PickLocalNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PickLocalNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PickLocalNumberResponse(),
            await self.do_rpcrequest_async('PickLocalNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pick_local_number(
        self,
        request: ccc20170705_models.PickLocalNumberRequest,
    ) -> ccc20170705_models.PickLocalNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.pick_local_number_with_options(request, runtime)

    async def pick_local_number_async(
        self,
        request: ccc20170705_models.PickLocalNumberRequest,
    ) -> ccc20170705_models.PickLocalNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pick_local_number_with_options_async(request, runtime)

    def pick_outbound_numbers_with_options(
        self,
        request: ccc20170705_models.PickOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PickOutboundNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PickOutboundNumbersResponse(),
            self.do_rpcrequest('PickOutboundNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pick_outbound_numbers_with_options_async(
        self,
        request: ccc20170705_models.PickOutboundNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PickOutboundNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PickOutboundNumbersResponse(),
            await self.do_rpcrequest_async('PickOutboundNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pick_outbound_numbers(
        self,
        request: ccc20170705_models.PickOutboundNumbersRequest,
    ) -> ccc20170705_models.PickOutboundNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.pick_outbound_numbers_with_options(request, runtime)

    async def pick_outbound_numbers_async(
        self,
        request: ccc20170705_models.PickOutboundNumbersRequest,
    ) -> ccc20170705_models.PickOutboundNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pick_outbound_numbers_with_options_async(request, runtime)

    def publish_contact_flow_version_with_options(
        self,
        request: ccc20170705_models.PublishContactFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PublishContactFlowVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PublishContactFlowVersionResponse(),
            self.do_rpcrequest('PublishContactFlowVersion', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_contact_flow_version_with_options_async(
        self,
        request: ccc20170705_models.PublishContactFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PublishContactFlowVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PublishContactFlowVersionResponse(),
            await self.do_rpcrequest_async('PublishContactFlowVersion', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_contact_flow_version(
        self,
        request: ccc20170705_models.PublishContactFlowVersionRequest,
    ) -> ccc20170705_models.PublishContactFlowVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_contact_flow_version_with_options(request, runtime)

    async def publish_contact_flow_version_async(
        self,
        request: ccc20170705_models.PublishContactFlowVersionRequest,
    ) -> ccc20170705_models.PublishContactFlowVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_contact_flow_version_with_options_async(request, runtime)

    def publish_predictive_job_group_with_options(
        self,
        request: ccc20170705_models.PublishPredictiveJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PublishPredictiveJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PublishPredictiveJobGroupResponse(),
            self.do_rpcrequest('PublishPredictiveJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_predictive_job_group_with_options_async(
        self,
        request: ccc20170705_models.PublishPredictiveJobGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PublishPredictiveJobGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PublishPredictiveJobGroupResponse(),
            await self.do_rpcrequest_async('PublishPredictiveJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_predictive_job_group(
        self,
        request: ccc20170705_models.PublishPredictiveJobGroupRequest,
    ) -> ccc20170705_models.PublishPredictiveJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_predictive_job_group_with_options(request, runtime)

    async def publish_predictive_job_group_async(
        self,
        request: ccc20170705_models.PublishPredictiveJobGroupRequest,
    ) -> ccc20170705_models.PublishPredictiveJobGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_predictive_job_group_with_options_async(request, runtime)

    def publish_survey_with_options(
        self,
        request: ccc20170705_models.PublishSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PublishSurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PublishSurveyResponse(),
            self.do_rpcrequest('PublishSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_survey_with_options_async(
        self,
        request: ccc20170705_models.PublishSurveyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.PublishSurveyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.PublishSurveyResponse(),
            await self.do_rpcrequest_async('PublishSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_survey(
        self,
        request: ccc20170705_models.PublishSurveyRequest,
    ) -> ccc20170705_models.PublishSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_survey_with_options(request, runtime)

    async def publish_survey_async(
        self,
        request: ccc20170705_models.PublishSurveyRequest,
    ) -> ccc20170705_models.PublishSurveyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_survey_with_options_async(request, runtime)

    def refresh_token_with_options(
        self,
        request: ccc20170705_models.RefreshTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.RefreshTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.RefreshTokenResponse(),
            self.do_rpcrequest('RefreshToken', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_token_with_options_async(
        self,
        request: ccc20170705_models.RefreshTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.RefreshTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.RefreshTokenResponse(),
            await self.do_rpcrequest_async('RefreshToken', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_token(
        self,
        request: ccc20170705_models.RefreshTokenRequest,
    ) -> ccc20170705_models.RefreshTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_token_with_options(request, runtime)

    async def refresh_token_async(
        self,
        request: ccc20170705_models.RefreshTokenRequest,
    ) -> ccc20170705_models.RefreshTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_token_with_options_async(request, runtime)

    def remove_phone_number_with_options(
        self,
        request: ccc20170705_models.RemovePhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.RemovePhoneNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.RemovePhoneNumberResponse(),
            self.do_rpcrequest('RemovePhoneNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_phone_number_with_options_async(
        self,
        request: ccc20170705_models.RemovePhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.RemovePhoneNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.RemovePhoneNumberResponse(),
            await self.do_rpcrequest_async('RemovePhoneNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_phone_number(
        self,
        request: ccc20170705_models.RemovePhoneNumberRequest,
    ) -> ccc20170705_models.RemovePhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_number_with_options(request, runtime)

    async def remove_phone_number_async(
        self,
        request: ccc20170705_models.RemovePhoneNumberRequest,
    ) -> ccc20170705_models.RemovePhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_phone_number_with_options_async(request, runtime)

    def remove_users_with_options(
        self,
        request: ccc20170705_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.RemoveUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.RemoveUsersResponse(),
            self.do_rpcrequest('RemoveUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_users_with_options_async(
        self,
        request: ccc20170705_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.RemoveUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.RemoveUsersResponse(),
            await self.do_rpcrequest_async('RemoveUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_users(
        self,
        request: ccc20170705_models.RemoveUsersRequest,
    ) -> ccc20170705_models.RemoveUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    async def remove_users_async(
        self,
        request: ccc20170705_models.RemoveUsersRequest,
    ) -> ccc20170705_models.RemoveUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_with_options_async(request, runtime)

    def remove_users_from_skill_group_with_options(
        self,
        request: ccc20170705_models.RemoveUsersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.RemoveUsersFromSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.RemoveUsersFromSkillGroupResponse(),
            self.do_rpcrequest('RemoveUsersFromSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_users_from_skill_group_with_options_async(
        self,
        request: ccc20170705_models.RemoveUsersFromSkillGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.RemoveUsersFromSkillGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.RemoveUsersFromSkillGroupResponse(),
            await self.do_rpcrequest_async('RemoveUsersFromSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_users_from_skill_group(
        self,
        request: ccc20170705_models.RemoveUsersFromSkillGroupRequest,
    ) -> ccc20170705_models.RemoveUsersFromSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_users_from_skill_group_with_options(request, runtime)

    async def remove_users_from_skill_group_async(
        self,
        request: ccc20170705_models.RemoveUsersFromSkillGroupRequest,
    ) -> ccc20170705_models.RemoveUsersFromSkillGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_from_skill_group_with_options_async(request, runtime)

    def request_login_info_with_options(
        self,
        request: ccc20170705_models.RequestLoginInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.RequestLoginInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.RequestLoginInfoResponse(),
            self.do_rpcrequest('RequestLoginInfo', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def request_login_info_with_options_async(
        self,
        request: ccc20170705_models.RequestLoginInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.RequestLoginInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.RequestLoginInfoResponse(),
            await self.do_rpcrequest_async('RequestLoginInfo', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def request_login_info(
        self,
        request: ccc20170705_models.RequestLoginInfoRequest,
    ) -> ccc20170705_models.RequestLoginInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.request_login_info_with_options(request, runtime)

    async def request_login_info_async(
        self,
        request: ccc20170705_models.RequestLoginInfoRequest,
    ) -> ccc20170705_models.RequestLoginInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.request_login_info_with_options_async(request, runtime)

    def reset_user_status_with_options(
        self,
        request: ccc20170705_models.ResetUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ResetUserStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ResetUserStatusResponse(),
            self.do_rpcrequest('ResetUserStatus', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_user_status_with_options_async(
        self,
        request: ccc20170705_models.ResetUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ResetUserStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ResetUserStatusResponse(),
            await self.do_rpcrequest_async('ResetUserStatus', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_user_status(
        self,
        request: ccc20170705_models.ResetUserStatusRequest,
    ) -> ccc20170705_models.ResetUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_user_status_with_options(request, runtime)

    async def reset_user_status_async(
        self,
        request: ccc20170705_models.ResetUserStatusRequest,
    ) -> ccc20170705_models.ResetUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_user_status_with_options_async(request, runtime)

    def resume_jobs_with_options(
        self,
        request: ccc20170705_models.ResumeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ResumeJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ResumeJobsResponse(),
            self.do_rpcrequest('ResumeJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_jobs_with_options_async(
        self,
        request: ccc20170705_models.ResumeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ResumeJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ResumeJobsResponse(),
            await self.do_rpcrequest_async('ResumeJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_jobs(
        self,
        request: ccc20170705_models.ResumeJobsRequest,
    ) -> ccc20170705_models.ResumeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_jobs_with_options(request, runtime)

    async def resume_jobs_async(
        self,
        request: ccc20170705_models.ResumeJobsRequest,
    ) -> ccc20170705_models.ResumeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_jobs_with_options_async(request, runtime)

    def resume_predictive_jobs_with_options(
        self,
        request: ccc20170705_models.ResumePredictiveJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ResumePredictiveJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ResumePredictiveJobsResponse(),
            self.do_rpcrequest('ResumePredictiveJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_predictive_jobs_with_options_async(
        self,
        request: ccc20170705_models.ResumePredictiveJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.ResumePredictiveJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.ResumePredictiveJobsResponse(),
            await self.do_rpcrequest_async('ResumePredictiveJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_predictive_jobs(
        self,
        request: ccc20170705_models.ResumePredictiveJobsRequest,
    ) -> ccc20170705_models.ResumePredictiveJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_predictive_jobs_with_options(request, runtime)

    async def resume_predictive_jobs_async(
        self,
        request: ccc20170705_models.ResumePredictiveJobsRequest,
    ) -> ccc20170705_models.ResumePredictiveJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_predictive_jobs_with_options_async(request, runtime)

    def save_stats_with_options(
        self,
        request: ccc20170705_models.SaveStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SaveStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SaveStatsResponse(),
            self.do_rpcrequest('SaveStats', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_stats_with_options_async(
        self,
        request: ccc20170705_models.SaveStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SaveStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SaveStatsResponse(),
            await self.do_rpcrequest_async('SaveStats', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_stats(
        self,
        request: ccc20170705_models.SaveStatsRequest,
    ) -> ccc20170705_models.SaveStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_stats_with_options(request, runtime)

    async def save_stats_async(
        self,
        request: ccc20170705_models.SaveStatsRequest,
    ) -> ccc20170705_models.SaveStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_stats_with_options_async(request, runtime)

    def save_terminal_log_with_options(
        self,
        request: ccc20170705_models.SaveTerminalLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SaveTerminalLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SaveTerminalLogResponse(),
            self.do_rpcrequest('SaveTerminalLog', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_terminal_log_with_options_async(
        self,
        request: ccc20170705_models.SaveTerminalLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SaveTerminalLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SaveTerminalLogResponse(),
            await self.do_rpcrequest_async('SaveTerminalLog', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_terminal_log(
        self,
        request: ccc20170705_models.SaveTerminalLogRequest,
    ) -> ccc20170705_models.SaveTerminalLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_terminal_log_with_options(request, runtime)

    async def save_terminal_log_async(
        self,
        request: ccc20170705_models.SaveTerminalLogRequest,
    ) -> ccc20170705_models.SaveTerminalLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_terminal_log_with_options_async(request, runtime)

    def save_web_rtcstats_with_options(
        self,
        request: ccc20170705_models.SaveWebRTCStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SaveWebRTCStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SaveWebRTCStatsResponse(),
            self.do_rpcrequest('SaveWebRTCStats', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_web_rtcstats_with_options_async(
        self,
        request: ccc20170705_models.SaveWebRTCStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SaveWebRTCStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SaveWebRTCStatsResponse(),
            await self.do_rpcrequest_async('SaveWebRTCStats', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_web_rtcstats(
        self,
        request: ccc20170705_models.SaveWebRTCStatsRequest,
    ) -> ccc20170705_models.SaveWebRTCStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_web_rtcstats_with_options(request, runtime)

    async def save_web_rtcstats_async(
        self,
        request: ccc20170705_models.SaveWebRTCStatsRequest,
    ) -> ccc20170705_models.SaveWebRTCStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_web_rtcstats_with_options_async(request, runtime)

    def send_predefined_short_message_with_options(
        self,
        request: ccc20170705_models.SendPredefinedShortMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SendPredefinedShortMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SendPredefinedShortMessageResponse(),
            self.do_rpcrequest('SendPredefinedShortMessage', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_predefined_short_message_with_options_async(
        self,
        request: ccc20170705_models.SendPredefinedShortMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SendPredefinedShortMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SendPredefinedShortMessageResponse(),
            await self.do_rpcrequest_async('SendPredefinedShortMessage', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_predefined_short_message(
        self,
        request: ccc20170705_models.SendPredefinedShortMessageRequest,
    ) -> ccc20170705_models.SendPredefinedShortMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_predefined_short_message_with_options(request, runtime)

    async def send_predefined_short_message_async(
        self,
        request: ccc20170705_models.SendPredefinedShortMessageRequest,
    ) -> ccc20170705_models.SendPredefinedShortMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_predefined_short_message_with_options_async(request, runtime)

    def start_back_2back_call_with_options(
        self,
        request: ccc20170705_models.StartBack2BackCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.StartBack2BackCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.StartBack2BackCallResponse(),
            self.do_rpcrequest('StartBack2BackCall', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_back_2back_call_with_options_async(
        self,
        request: ccc20170705_models.StartBack2BackCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.StartBack2BackCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.StartBack2BackCallResponse(),
            await self.do_rpcrequest_async('StartBack2BackCall', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_back_2back_call(
        self,
        request: ccc20170705_models.StartBack2BackCallRequest,
    ) -> ccc20170705_models.StartBack2BackCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_back_2back_call_with_options(request, runtime)

    async def start_back_2back_call_async(
        self,
        request: ccc20170705_models.StartBack2BackCallRequest,
    ) -> ccc20170705_models.StartBack2BackCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_back_2back_call_with_options_async(request, runtime)

    def start_job_with_options(
        self,
        request: ccc20170705_models.StartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.StartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.StartJobResponse(),
            self.do_rpcrequest('StartJob', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_job_with_options_async(
        self,
        request: ccc20170705_models.StartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.StartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.StartJobResponse(),
            await self.do_rpcrequest_async('StartJob', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_job(
        self,
        request: ccc20170705_models.StartJobRequest,
    ) -> ccc20170705_models.StartJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_job_with_options(request, runtime)

    async def start_job_async(
        self,
        request: ccc20170705_models.StartJobRequest,
    ) -> ccc20170705_models.StartJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_job_with_options_async(request, runtime)

    def submit_batch_jobs_with_options(
        self,
        request: ccc20170705_models.SubmitBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SubmitBatchJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SubmitBatchJobsResponse(),
            self.do_rpcrequest('SubmitBatchJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_batch_jobs_with_options_async(
        self,
        request: ccc20170705_models.SubmitBatchJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SubmitBatchJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SubmitBatchJobsResponse(),
            await self.do_rpcrequest_async('SubmitBatchJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_batch_jobs(
        self,
        request: ccc20170705_models.SubmitBatchJobsRequest,
    ) -> ccc20170705_models.SubmitBatchJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_batch_jobs_with_options(request, runtime)

    async def submit_batch_jobs_async(
        self,
        request: ccc20170705_models.SubmitBatchJobsRequest,
    ) -> ccc20170705_models.SubmitBatchJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_batch_jobs_with_options_async(request, runtime)

    def submit_cab_recording_with_options(
        self,
        request: ccc20170705_models.SubmitCabRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SubmitCabRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SubmitCabRecordingResponse(),
            self.do_rpcrequest('SubmitCabRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_cab_recording_with_options_async(
        self,
        request: ccc20170705_models.SubmitCabRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SubmitCabRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SubmitCabRecordingResponse(),
            await self.do_rpcrequest_async('SubmitCabRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_cab_recording(
        self,
        request: ccc20170705_models.SubmitCabRecordingRequest,
    ) -> ccc20170705_models.SubmitCabRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_cab_recording_with_options(request, runtime)

    async def submit_cab_recording_async(
        self,
        request: ccc20170705_models.SubmitCabRecordingRequest,
    ) -> ccc20170705_models.SubmitCabRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_cab_recording_with_options_async(request, runtime)

    def suspend_jobs_with_options(
        self,
        request: ccc20170705_models.SuspendJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SuspendJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SuspendJobsResponse(),
            self.do_rpcrequest('SuspendJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_jobs_with_options_async(
        self,
        request: ccc20170705_models.SuspendJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SuspendJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SuspendJobsResponse(),
            await self.do_rpcrequest_async('SuspendJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_jobs(
        self,
        request: ccc20170705_models.SuspendJobsRequest,
    ) -> ccc20170705_models.SuspendJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_jobs_with_options(request, runtime)

    async def suspend_jobs_async(
        self,
        request: ccc20170705_models.SuspendJobsRequest,
    ) -> ccc20170705_models.SuspendJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_jobs_with_options_async(request, runtime)

    def suspend_predictive_jobs_with_options(
        self,
        request: ccc20170705_models.SuspendPredictiveJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SuspendPredictiveJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SuspendPredictiveJobsResponse(),
            self.do_rpcrequest('SuspendPredictiveJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_predictive_jobs_with_options_async(
        self,
        request: ccc20170705_models.SuspendPredictiveJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.SuspendPredictiveJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.SuspendPredictiveJobsResponse(),
            await self.do_rpcrequest_async('SuspendPredictiveJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_predictive_jobs(
        self,
        request: ccc20170705_models.SuspendPredictiveJobsRequest,
    ) -> ccc20170705_models.SuspendPredictiveJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_predictive_jobs_with_options(request, runtime)

    async def suspend_predictive_jobs_async(
        self,
        request: ccc20170705_models.SuspendPredictiveJobsRequest,
    ) -> ccc20170705_models.SuspendPredictiveJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_predictive_jobs_with_options_async(request, runtime)

    def task_preparing_with_options(
        self,
        request: ccc20170705_models.TaskPreparingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.TaskPreparingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.TaskPreparingResponse(),
            self.do_rpcrequest('TaskPreparing', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def task_preparing_with_options_async(
        self,
        request: ccc20170705_models.TaskPreparingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ccc20170705_models.TaskPreparingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20170705_models.TaskPreparingResponse(),
            await self.do_rpcrequest_async('TaskPreparing', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def task_preparing(
        self,
        request: ccc20170705_models.TaskPreparingRequest,
    ) -> ccc20170705_models.TaskPreparingResponse:
        runtime = util_models.RuntimeOptions()
        return self.task_preparing_with_options(request, runtime)

    async def task_preparing_async(
        self,
        request: ccc20170705_models.TaskPreparingRequest,
    ) -> ccc20170705_models.TaskPreparingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.task_preparing_with_options_async(request, runtime)
