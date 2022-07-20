# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cgcs20211111 import models as cgcs20211111_models
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
        self._endpoint = self.get_endpoint('cgcs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_reserve_task_with_options(
        self,
        request: cgcs20211111_models.CancelReserveTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CancelReserveTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelReserveTask',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CancelReserveTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_reserve_task_with_options_async(
        self,
        request: cgcs20211111_models.CancelReserveTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CancelReserveTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelReserveTask',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CancelReserveTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_reserve_task(
        self,
        request: cgcs20211111_models.CancelReserveTaskRequest,
    ) -> cgcs20211111_models.CancelReserveTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_reserve_task_with_options(request, runtime)

    async def cancel_reserve_task_async(
        self,
        request: cgcs20211111_models.CancelReserveTaskRequest,
    ) -> cgcs20211111_models.CancelReserveTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_reserve_task_with_options_async(request, runtime)

    def create_adaptation_with_options(
        self,
        tmp_req: cgcs20211111_models.CreateAdaptationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAdaptationResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAdaptationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.adapt_target):
            request.adapt_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.adapt_target), 'AdaptTarget', 'json')
        body = {}
        if not UtilClient.is_unset(request.adapt_target_shrink):
            body['AdaptTarget'] = request.adapt_target_shrink
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAdaptation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAdaptationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_adaptation_with_options_async(
        self,
        tmp_req: cgcs20211111_models.CreateAdaptationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAdaptationResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAdaptationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.adapt_target):
            request.adapt_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.adapt_target), 'AdaptTarget', 'json')
        body = {}
        if not UtilClient.is_unset(request.adapt_target_shrink):
            body['AdaptTarget'] = request.adapt_target_shrink
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAdaptation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAdaptationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_adaptation(
        self,
        request: cgcs20211111_models.CreateAdaptationRequest,
    ) -> cgcs20211111_models.CreateAdaptationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_adaptation_with_options(request, runtime)

    async def create_adaptation_async(
        self,
        request: cgcs20211111_models.CreateAdaptationRequest,
    ) -> cgcs20211111_models.CreateAdaptationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_adaptation_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: cgcs20211111_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: cgcs20211111_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: cgcs20211111_models.CreateAppRequest,
    ) -> cgcs20211111_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: cgcs20211111_models.CreateAppRequest,
    ) -> cgcs20211111_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_app_session_with_options(
        self,
        request: cgcs20211111_models.CreateAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.enable_postpaid):
            query['EnablePostpaid'] = request.enable_postpaid
        if not UtilClient.is_unset(request.start_parameters):
            query['StartParameters'] = request.start_parameters
        if not UtilClient.is_unset(request.system_info):
            query['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_session_with_options_async(
        self,
        request: cgcs20211111_models.CreateAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.enable_postpaid):
            query['EnablePostpaid'] = request.enable_postpaid
        if not UtilClient.is_unset(request.start_parameters):
            query['StartParameters'] = request.start_parameters
        if not UtilClient.is_unset(request.system_info):
            query['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_session(
        self,
        request: cgcs20211111_models.CreateAppSessionRequest,
    ) -> cgcs20211111_models.CreateAppSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_session_with_options(request, runtime)

    async def create_app_session_async(
        self,
        request: cgcs20211111_models.CreateAppSessionRequest,
    ) -> cgcs20211111_models.CreateAppSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_session_with_options_async(request, runtime)

    def create_app_session_batch_sync_with_options(
        self,
        tmp_req: cgcs20211111_models.CreateAppSessionBatchSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionBatchSyncResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAppSessionBatchSyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app_infos):
            request.app_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app_infos, 'AppInfos', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_infos_shrink):
            query['AppInfos'] = request.app_infos_shrink
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSessionBatchSync',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionBatchSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_session_batch_sync_with_options_async(
        self,
        tmp_req: cgcs20211111_models.CreateAppSessionBatchSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionBatchSyncResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAppSessionBatchSyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app_infos):
            request.app_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app_infos, 'AppInfos', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_infos_shrink):
            query['AppInfos'] = request.app_infos_shrink
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSessionBatchSync',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionBatchSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_session_batch_sync(
        self,
        request: cgcs20211111_models.CreateAppSessionBatchSyncRequest,
    ) -> cgcs20211111_models.CreateAppSessionBatchSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_session_batch_sync_with_options(request, runtime)

    async def create_app_session_batch_sync_async(
        self,
        request: cgcs20211111_models.CreateAppSessionBatchSyncRequest,
    ) -> cgcs20211111_models.CreateAppSessionBatchSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_session_batch_sync_with_options_async(request, runtime)

    def create_app_session_sync_with_options(
        self,
        request: cgcs20211111_models.CreateAppSessionSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.district_id):
            query['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.start_parameters):
            query['StartParameters'] = request.start_parameters
        if not UtilClient.is_unset(request.system_info):
            query['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSessionSync',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_session_sync_with_options_async(
        self,
        request: cgcs20211111_models.CreateAppSessionSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.district_id):
            query['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.start_parameters):
            query['StartParameters'] = request.start_parameters
        if not UtilClient.is_unset(request.system_info):
            query['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSessionSync',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_session_sync(
        self,
        request: cgcs20211111_models.CreateAppSessionSyncRequest,
    ) -> cgcs20211111_models.CreateAppSessionSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_session_sync_with_options(request, runtime)

    async def create_app_session_sync_async(
        self,
        request: cgcs20211111_models.CreateAppSessionSyncRequest,
    ) -> cgcs20211111_models.CreateAppSessionSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_session_sync_with_options_async(request, runtime)

    def create_app_version_with_options(
        self,
        request: cgcs20211111_models.CreateAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_version_with_options_async(
        self,
        request: cgcs20211111_models.CreateAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_version(
        self,
        request: cgcs20211111_models.CreateAppVersionRequest,
    ) -> cgcs20211111_models.CreateAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_version_with_options(request, runtime)

    async def create_app_version_async(
        self,
        request: cgcs20211111_models.CreateAppVersionRequest,
    ) -> cgcs20211111_models.CreateAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_version_with_options_async(request, runtime)

    def create_capacity_reservation_with_options(
        self,
        request: cgcs20211111_models.CreateCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateCapacityReservationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.expect_resource_ready_time):
            body['ExpectResourceReadyTime'] = request.expect_resource_ready_time
        if not UtilClient.is_unset(request.expect_session_capacity):
            body['ExpectSessionCapacity'] = request.expect_session_capacity
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCapacityReservation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateCapacityReservationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_capacity_reservation_with_options_async(
        self,
        request: cgcs20211111_models.CreateCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateCapacityReservationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.expect_resource_ready_time):
            body['ExpectResourceReadyTime'] = request.expect_resource_ready_time
        if not UtilClient.is_unset(request.expect_session_capacity):
            body['ExpectSessionCapacity'] = request.expect_session_capacity
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCapacityReservation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateCapacityReservationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_capacity_reservation(
        self,
        request: cgcs20211111_models.CreateCapacityReservationRequest,
    ) -> cgcs20211111_models.CreateCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_capacity_reservation_with_options(request, runtime)

    async def create_capacity_reservation_async(
        self,
        request: cgcs20211111_models.CreateCapacityReservationRequest,
    ) -> cgcs20211111_models.CreateCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_capacity_reservation_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        tmp_req: cgcs20211111_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.bound_app_id_list):
            request.bound_app_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bound_app_id_list, 'BoundAppIdList', 'json')
        if not UtilClient.is_unset(tmp_req.project_quota_limit):
            request.project_quota_limit_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.project_quota_limit), 'ProjectQuotaLimit', 'json')
        body = {}
        if not UtilClient.is_unset(request.bound_app_id_list_shrink):
            body['BoundAppIdList'] = request.bound_app_id_list_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.project_memo):
            body['ProjectMemo'] = request.project_memo
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_quota_limit_shrink):
            body['ProjectQuotaLimit'] = request.project_quota_limit_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        tmp_req: cgcs20211111_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.bound_app_id_list):
            request.bound_app_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bound_app_id_list, 'BoundAppIdList', 'json')
        if not UtilClient.is_unset(tmp_req.project_quota_limit):
            request.project_quota_limit_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.project_quota_limit), 'ProjectQuotaLimit', 'json')
        body = {}
        if not UtilClient.is_unset(request.bound_app_id_list_shrink):
            body['BoundAppIdList'] = request.bound_app_id_list_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.project_memo):
            body['ProjectMemo'] = request.project_memo
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_quota_limit_shrink):
            body['ProjectQuotaLimit'] = request.project_quota_limit_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: cgcs20211111_models.CreateProjectRequest,
    ) -> cgcs20211111_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: cgcs20211111_models.CreateProjectRequest,
    ) -> cgcs20211111_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: cgcs20211111_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: cgcs20211111_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: cgcs20211111_models.DeleteAppRequest,
    ) -> cgcs20211111_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: cgcs20211111_models.DeleteAppRequest,
    ) -> cgcs20211111_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_app_version_with_options(
        self,
        request: cgcs20211111_models.DeleteAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.DeleteAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.DeleteAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_version_with_options_async(
        self,
        request: cgcs20211111_models.DeleteAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.DeleteAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.DeleteAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_version(
        self,
        request: cgcs20211111_models.DeleteAppVersionRequest,
    ) -> cgcs20211111_models.DeleteAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_version_with_options(request, runtime)

    async def delete_app_version_async(
        self,
        request: cgcs20211111_models.DeleteAppVersionRequest,
    ) -> cgcs20211111_models.DeleteAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_version_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: cgcs20211111_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: cgcs20211111_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        request: cgcs20211111_models.DeleteProjectRequest,
    ) -> cgcs20211111_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: cgcs20211111_models.DeleteProjectRequest,
    ) -> cgcs20211111_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def get_adaptation_with_options(
        self,
        request: cgcs20211111_models.GetAdaptationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAdaptationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.adapt_apply_id):
            body['AdaptApplyId'] = request.adapt_apply_id
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAdaptation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAdaptationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_adaptation_with_options_async(
        self,
        request: cgcs20211111_models.GetAdaptationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAdaptationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.adapt_apply_id):
            body['AdaptApplyId'] = request.adapt_apply_id
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAdaptation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAdaptationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_adaptation(
        self,
        request: cgcs20211111_models.GetAdaptationRequest,
    ) -> cgcs20211111_models.GetAdaptationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_adaptation_with_options(request, runtime)

    async def get_adaptation_async(
        self,
        request: cgcs20211111_models.GetAdaptationRequest,
    ) -> cgcs20211111_models.GetAdaptationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_adaptation_with_options_async(request, runtime)

    def get_app_with_options(
        self,
        request: cgcs20211111_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_with_options_async(
        self,
        request: cgcs20211111_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app(
        self,
        request: cgcs20211111_models.GetAppRequest,
    ) -> cgcs20211111_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    async def get_app_async(
        self,
        request: cgcs20211111_models.GetAppRequest,
    ) -> cgcs20211111_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_with_options_async(request, runtime)

    def get_app_ccu_with_options(
        self,
        request: cgcs20211111_models.GetAppCcuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppCcuResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppCcu',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppCcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_ccu_with_options_async(
        self,
        request: cgcs20211111_models.GetAppCcuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppCcuResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppCcu',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppCcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_ccu(
        self,
        request: cgcs20211111_models.GetAppCcuRequest,
    ) -> cgcs20211111_models.GetAppCcuResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_ccu_with_options(request, runtime)

    async def get_app_ccu_async(
        self,
        request: cgcs20211111_models.GetAppCcuRequest,
    ) -> cgcs20211111_models.GetAppCcuResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_ccu_with_options_async(request, runtime)

    def get_app_session_with_options(
        self,
        request: cgcs20211111_models.GetAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_session_with_options_async(
        self,
        request: cgcs20211111_models.GetAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_session(
        self,
        request: cgcs20211111_models.GetAppSessionRequest,
    ) -> cgcs20211111_models.GetAppSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_session_with_options(request, runtime)

    async def get_app_session_async(
        self,
        request: cgcs20211111_models.GetAppSessionRequest,
    ) -> cgcs20211111_models.GetAppSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_session_with_options_async(request, runtime)

    def get_app_version_with_options(
        self,
        request: cgcs20211111_models.GetAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_version_with_options_async(
        self,
        request: cgcs20211111_models.GetAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_version(
        self,
        request: cgcs20211111_models.GetAppVersionRequest,
    ) -> cgcs20211111_models.GetAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_version_with_options(request, runtime)

    async def get_app_version_async(
        self,
        request: cgcs20211111_models.GetAppVersionRequest,
    ) -> cgcs20211111_models.GetAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_version_with_options_async(request, runtime)

    def get_capacity_with_options(
        self,
        request: cgcs20211111_models.GetCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetCapacityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCapacity',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_capacity_with_options_async(
        self,
        request: cgcs20211111_models.GetCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetCapacityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCapacity',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_capacity(
        self,
        request: cgcs20211111_models.GetCapacityRequest,
    ) -> cgcs20211111_models.GetCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_capacity_with_options(request, runtime)

    async def get_capacity_async(
        self,
        request: cgcs20211111_models.GetCapacityRequest,
    ) -> cgcs20211111_models.GetCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_capacity_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: cgcs20211111_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: cgcs20211111_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        request: cgcs20211111_models.GetProjectRequest,
    ) -> cgcs20211111_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: cgcs20211111_models.GetProjectRequest,
    ) -> cgcs20211111_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_reserve_task_detail_with_options(
        self,
        request: cgcs20211111_models.GetReserveTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetReserveTaskDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReserveTaskDetail',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetReserveTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_reserve_task_detail_with_options_async(
        self,
        request: cgcs20211111_models.GetReserveTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetReserveTaskDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReserveTaskDetail',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetReserveTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_reserve_task_detail(
        self,
        request: cgcs20211111_models.GetReserveTaskDetailRequest,
    ) -> cgcs20211111_models.GetReserveTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_reserve_task_detail_with_options(request, runtime)

    async def get_reserve_task_detail_async(
        self,
        request: cgcs20211111_models.GetReserveTaskDetailRequest,
    ) -> cgcs20211111_models.GetReserveTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_reserve_task_detail_with_options_async(request, runtime)

    def get_resource_public_ips_with_options(
        self,
        request: cgcs20211111_models.GetResourcePublicIPsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetResourcePublicIPsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetResourcePublicIPs',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetResourcePublicIPsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_public_ips_with_options_async(
        self,
        request: cgcs20211111_models.GetResourcePublicIPsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetResourcePublicIPsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetResourcePublicIPs',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetResourcePublicIPsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_public_ips(
        self,
        request: cgcs20211111_models.GetResourcePublicIPsRequest,
    ) -> cgcs20211111_models.GetResourcePublicIPsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_public_ips_with_options(request, runtime)

    async def get_resource_public_ips_async(
        self,
        request: cgcs20211111_models.GetResourcePublicIPsRequest,
    ) -> cgcs20211111_models.GetResourcePublicIPsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_public_ips_with_options_async(request, runtime)

    def get_tenant_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetTenantResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetTenant',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetTenantResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tenant_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetTenantResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetTenant',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetTenantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tenant(self) -> cgcs20211111_models.GetTenantResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_tenant_with_options(runtime)

    async def get_tenant_async(self) -> cgcs20211111_models.GetTenantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_tenant_with_options_async(runtime)

    def list_app_with_options(
        self,
        request: cgcs20211111_models.ListAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key_search):
            body['KeySearch'] = request.key_search
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_with_options_async(
        self,
        request: cgcs20211111_models.ListAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key_search):
            body['KeySearch'] = request.key_search
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app(
        self,
        request: cgcs20211111_models.ListAppRequest,
    ) -> cgcs20211111_models.ListAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_with_options(request, runtime)

    async def list_app_async(
        self,
        request: cgcs20211111_models.ListAppRequest,
    ) -> cgcs20211111_models.ListAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_with_options_async(request, runtime)

    def list_app_sessions_with_options(
        self,
        request: cgcs20211111_models.ListAppSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppSessionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.custom_session_ids):
            query['CustomSessionIds'] = request.custom_session_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform_session_ids):
            query['PlatformSessionIds'] = request.platform_session_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppSessions',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_sessions_with_options_async(
        self,
        request: cgcs20211111_models.ListAppSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppSessionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.custom_session_ids):
            query['CustomSessionIds'] = request.custom_session_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform_session_ids):
            query['PlatformSessionIds'] = request.platform_session_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppSessions',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_sessions(
        self,
        request: cgcs20211111_models.ListAppSessionsRequest,
    ) -> cgcs20211111_models.ListAppSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_sessions_with_options(request, runtime)

    async def list_app_sessions_async(
        self,
        request: cgcs20211111_models.ListAppSessionsRequest,
    ) -> cgcs20211111_models.ListAppSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_sessions_with_options_async(request, runtime)

    def list_app_version_with_options(
        self,
        request: cgcs20211111_models.ListAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_version_with_options_async(
        self,
        request: cgcs20211111_models.ListAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_version(
        self,
        request: cgcs20211111_models.ListAppVersionRequest,
    ) -> cgcs20211111_models.ListAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_version_with_options(request, runtime)

    async def list_app_version_async(
        self,
        request: cgcs20211111_models.ListAppVersionRequest,
    ) -> cgcs20211111_models.ListAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_version_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: cgcs20211111_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ModifyAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: cgcs20211111_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ModifyAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        request: cgcs20211111_models.ModifyAppRequest,
    ) -> cgcs20211111_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: cgcs20211111_models.ModifyAppRequest,
    ) -> cgcs20211111_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_app_version_with_options(
        self,
        request: cgcs20211111_models.ModifyAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ModifyAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ModifyAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_version_with_options_async(
        self,
        request: cgcs20211111_models.ModifyAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ModifyAppVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ModifyAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_version(
        self,
        request: cgcs20211111_models.ModifyAppVersionRequest,
    ) -> cgcs20211111_models.ModifyAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_app_version_with_options(request, runtime)

    async def modify_app_version_async(
        self,
        request: cgcs20211111_models.ModifyAppVersionRequest,
    ) -> cgcs20211111_models.ModifyAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_version_with_options_async(request, runtime)

    def modify_project_with_options(
        self,
        tmp_req: cgcs20211111_models.ModifyProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ModifyProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.ModifyProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.bound_app_id_list):
            request.bound_app_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bound_app_id_list, 'BoundAppIdList', 'json')
        if not UtilClient.is_unset(tmp_req.project_quota_limit):
            request.project_quota_limit_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.project_quota_limit), 'ProjectQuotaLimit', 'json')
        body = {}
        if not UtilClient.is_unset(request.bound_app_id_list_shrink):
            body['BoundAppIdList'] = request.bound_app_id_list_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_memo):
            body['ProjectMemo'] = request.project_memo
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_quota_limit_shrink):
            body['ProjectQuotaLimit'] = request.project_quota_limit_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyProject',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ModifyProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_project_with_options_async(
        self,
        tmp_req: cgcs20211111_models.ModifyProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ModifyProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.ModifyProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.bound_app_id_list):
            request.bound_app_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.bound_app_id_list, 'BoundAppIdList', 'json')
        if not UtilClient.is_unset(tmp_req.project_quota_limit):
            request.project_quota_limit_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.project_quota_limit), 'ProjectQuotaLimit', 'json')
        body = {}
        if not UtilClient.is_unset(request.bound_app_id_list_shrink):
            body['BoundAppIdList'] = request.bound_app_id_list_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_memo):
            body['ProjectMemo'] = request.project_memo
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_quota_limit_shrink):
            body['ProjectQuotaLimit'] = request.project_quota_limit_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyProject',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ModifyProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_project(
        self,
        request: cgcs20211111_models.ModifyProjectRequest,
    ) -> cgcs20211111_models.ModifyProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_project_with_options(request, runtime)

    async def modify_project_async(
        self,
        request: cgcs20211111_models.ModifyProjectRequest,
    ) -> cgcs20211111_models.ModifyProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_project_with_options_async(request, runtime)

    def page_query_project_with_options(
        self,
        request: cgcs20211111_models.PageQueryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.PageQueryProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key_search):
            body['KeySearch'] = request.key_search
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageQueryProject',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.PageQueryProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_query_project_with_options_async(
        self,
        request: cgcs20211111_models.PageQueryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.PageQueryProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key_search):
            body['KeySearch'] = request.key_search
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageQueryProject',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.PageQueryProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_query_project(
        self,
        request: cgcs20211111_models.PageQueryProjectRequest,
    ) -> cgcs20211111_models.PageQueryProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.page_query_project_with_options(request, runtime)

    async def page_query_project_async(
        self,
        request: cgcs20211111_models.PageQueryProjectRequest,
    ) -> cgcs20211111_models.PageQueryProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.page_query_project_with_options_async(request, runtime)

    def page_query_project_apps_with_options(
        self,
        request: cgcs20211111_models.PageQueryProjectAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.PageQueryProjectAppsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageQueryProjectApps',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.PageQueryProjectAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_query_project_apps_with_options_async(
        self,
        request: cgcs20211111_models.PageQueryProjectAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.PageQueryProjectAppsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageQueryProjectApps',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.PageQueryProjectAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_query_project_apps(
        self,
        request: cgcs20211111_models.PageQueryProjectAppsRequest,
    ) -> cgcs20211111_models.PageQueryProjectAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.page_query_project_apps_with_options(request, runtime)

    async def page_query_project_apps_async(
        self,
        request: cgcs20211111_models.PageQueryProjectAppsRequest,
    ) -> cgcs20211111_models.PageQueryProjectAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.page_query_project_apps_with_options_async(request, runtime)

    def refresh_district_meta_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.RefreshDistrictMetaResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RefreshDistrictMeta',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.RefreshDistrictMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_district_meta_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.RefreshDistrictMetaResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RefreshDistrictMeta',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.RefreshDistrictMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_district_meta(self) -> cgcs20211111_models.RefreshDistrictMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_district_meta_with_options(runtime)

    async def refresh_district_meta_async(self) -> cgcs20211111_models.RefreshDistrictMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_district_meta_with_options_async(runtime)

    def release_capacity_with_options(
        self,
        request: cgcs20211111_models.ReleaseCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ReleaseCapacityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.expect_release_session_capacity):
            body['ExpectReleaseSessionCapacity'] = request.expect_release_session_capacity
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseCapacity',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReleaseCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_capacity_with_options_async(
        self,
        request: cgcs20211111_models.ReleaseCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ReleaseCapacityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.expect_release_session_capacity):
            body['ExpectReleaseSessionCapacity'] = request.expect_release_session_capacity
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseCapacity',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReleaseCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_capacity(
        self,
        request: cgcs20211111_models.ReleaseCapacityRequest,
    ) -> cgcs20211111_models.ReleaseCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_capacity_with_options(request, runtime)

    async def release_capacity_async(
        self,
        request: cgcs20211111_models.ReleaseCapacityRequest,
    ) -> cgcs20211111_models.ReleaseCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_capacity_with_options_async(request, runtime)

    def stop_app_session_with_options(
        self,
        tmp_req: cgcs20211111_models.StopAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.StopAppSessionResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.StopAppSessionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stop_param):
            request.stop_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stop_param, 'StopParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        if not UtilClient.is_unset(request.stop_param_shrink):
            query['StopParam'] = request.stop_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.StopAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_app_session_with_options_async(
        self,
        tmp_req: cgcs20211111_models.StopAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.StopAppSessionResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.StopAppSessionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stop_param):
            request.stop_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stop_param, 'StopParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        if not UtilClient.is_unset(request.stop_param_shrink):
            query['StopParam'] = request.stop_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.StopAppSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_app_session(
        self,
        request: cgcs20211111_models.StopAppSessionRequest,
    ) -> cgcs20211111_models.StopAppSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_app_session_with_options(request, runtime)

    async def stop_app_session_async(
        self,
        request: cgcs20211111_models.StopAppSessionRequest,
    ) -> cgcs20211111_models.StopAppSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_app_session_with_options_async(request, runtime)

    def stop_app_session_batch_with_options(
        self,
        tmp_req: cgcs20211111_models.StopAppSessionBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.StopAppSessionBatchResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.StopAppSessionBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stop_param):
            request.stop_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stop_param, 'StopParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.stop_param_shrink):
            query['StopParam'] = request.stop_param_shrink
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppSessionBatch',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.StopAppSessionBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_app_session_batch_with_options_async(
        self,
        tmp_req: cgcs20211111_models.StopAppSessionBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.StopAppSessionBatchResponse:
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.StopAppSessionBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stop_param):
            request.stop_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stop_param, 'StopParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.stop_param_shrink):
            query['StopParam'] = request.stop_param_shrink
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppSessionBatch',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.StopAppSessionBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_app_session_batch(
        self,
        request: cgcs20211111_models.StopAppSessionBatchRequest,
    ) -> cgcs20211111_models.StopAppSessionBatchResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_app_session_batch_with_options(request, runtime)

    async def stop_app_session_batch_async(
        self,
        request: cgcs20211111_models.StopAppSessionBatchRequest,
    ) -> cgcs20211111_models.StopAppSessionBatchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_app_session_batch_with_options_async(request, runtime)

    def version_check_same_name_service_with_options(
        self,
        request: cgcs20211111_models.VersionCheckSameNameServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.VersionCheckSameNameServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VersionCheckSameNameService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.VersionCheckSameNameServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def version_check_same_name_service_with_options_async(
        self,
        request: cgcs20211111_models.VersionCheckSameNameServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.VersionCheckSameNameServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VersionCheckSameNameService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.VersionCheckSameNameServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def version_check_same_name_service(
        self,
        request: cgcs20211111_models.VersionCheckSameNameServiceRequest,
    ) -> cgcs20211111_models.VersionCheckSameNameServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.version_check_same_name_service_with_options(request, runtime)

    async def version_check_same_name_service_async(
        self,
        request: cgcs20211111_models.VersionCheckSameNameServiceRequest,
    ) -> cgcs20211111_models.VersionCheckSameNameServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.version_check_same_name_service_with_options_async(request, runtime)
