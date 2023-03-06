# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloud_siem20220616 import models as cloud_siem_20220616_models
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
        self._endpoint = self.get_endpoint('cloud-siem', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_job_check_with_options(
        self,
        request: cloud_siem_20220616_models.BatchJobCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.BatchJobCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.submit_id):
            body['SubmitId'] = request.submit_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchJobCheck',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.BatchJobCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_job_check_with_options_async(
        self,
        request: cloud_siem_20220616_models.BatchJobCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.BatchJobCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.submit_id):
            body['SubmitId'] = request.submit_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchJobCheck',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.BatchJobCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_job_check(
        self,
        request: cloud_siem_20220616_models.BatchJobCheckRequest,
    ) -> cloud_siem_20220616_models.BatchJobCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_job_check_with_options(request, runtime)

    async def batch_job_check_async(
        self,
        request: cloud_siem_20220616_models.BatchJobCheckRequest,
    ) -> cloud_siem_20220616_models.BatchJobCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_job_check_with_options_async(request, runtime)

    def batch_job_submit_with_options(
        self,
        request: cloud_siem_20220616_models.BatchJobSubmitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.BatchJobSubmitResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.json_config):
            body['JsonConfig'] = request.json_config
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchJobSubmit',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.BatchJobSubmitResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_job_submit_with_options_async(
        self,
        request: cloud_siem_20220616_models.BatchJobSubmitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.BatchJobSubmitResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.json_config):
            body['JsonConfig'] = request.json_config
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchJobSubmit',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.BatchJobSubmitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_job_submit(
        self,
        request: cloud_siem_20220616_models.BatchJobSubmitRequest,
    ) -> cloud_siem_20220616_models.BatchJobSubmitResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_job_submit_with_options(request, runtime)

    async def batch_job_submit_async(
        self,
        request: cloud_siem_20220616_models.BatchJobSubmitRequest,
    ) -> cloud_siem_20220616_models.BatchJobSubmitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_job_submit_with_options_async(request, runtime)

    def send_message_with_options(
        self,
        request: cloud_siem_20220616_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SendMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.receive_uid):
            body['ReceiveUid'] = request.receive_uid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        request: cloud_siem_20220616_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_siem_20220616_models.SendMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.receive_uid):
            body['ReceiveUid'] = request.receive_uid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: cloud_siem_20220616_models.SendMessageRequest,
    ) -> cloud_siem_20220616_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    async def send_message_async(
        self,
        request: cloud_siem_20220616_models.SendMessageRequest,
    ) -> cloud_siem_20220616_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_message_with_options_async(request, runtime)
