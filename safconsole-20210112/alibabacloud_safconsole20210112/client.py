# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_safconsole20210112 import models as safconsole_20210112_models
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
        self._endpoint = self.get_endpoint('safconsole', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def revoke_feedback_with_options(
        self,
        request: safconsole_20210112_models.RevokeFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safconsole_20210112_models.RevokeFeedbackResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sample_type):
            body['SampleType'] = request.sample_type
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeFeedback',
            version='2021-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safconsole_20210112_models.RevokeFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_feedback_with_options_async(
        self,
        request: safconsole_20210112_models.RevokeFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safconsole_20210112_models.RevokeFeedbackResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sample_type):
            body['SampleType'] = request.sample_type
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeFeedback',
            version='2021-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safconsole_20210112_models.RevokeFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_feedback(
        self,
        request: safconsole_20210112_models.RevokeFeedbackRequest,
    ) -> safconsole_20210112_models.RevokeFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_feedback_with_options(request, runtime)

    async def revoke_feedback_async(
        self,
        request: safconsole_20210112_models.RevokeFeedbackRequest,
    ) -> safconsole_20210112_models.RevokeFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_feedback_with_options_async(request, runtime)

    def send_feedback_with_options(
        self,
        request: safconsole_20210112_models.SendFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safconsole_20210112_models.SendFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.risk_label):
            query['RiskLabel'] = request.risk_label
        if not UtilClient.is_unset(request.sample_type):
            query['SampleType'] = request.sample_type
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendFeedback',
            version='2021-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safconsole_20210112_models.SendFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_feedback_with_options_async(
        self,
        request: safconsole_20210112_models.SendFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safconsole_20210112_models.SendFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.risk_label):
            query['RiskLabel'] = request.risk_label
        if not UtilClient.is_unset(request.sample_type):
            query['SampleType'] = request.sample_type
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendFeedback',
            version='2021-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safconsole_20210112_models.SendFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_feedback(
        self,
        request: safconsole_20210112_models.SendFeedbackRequest,
    ) -> safconsole_20210112_models.SendFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_feedback_with_options(request, runtime)

    async def send_feedback_async(
        self,
        request: safconsole_20210112_models.SendFeedbackRequest,
    ) -> safconsole_20210112_models.SendFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_feedback_with_options_async(request, runtime)

    def upload_sample_api_with_options(
        self,
        request: safconsole_20210112_models.UploadSampleApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safconsole_20210112_models.UploadSampleApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.data_value):
            query['DataValue'] = request.data_value
        if not UtilClient.is_unset(request.sample_type):
            query['SampleType'] = request.sample_type
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadSampleApi',
            version='2021-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safconsole_20210112_models.UploadSampleApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_sample_api_with_options_async(
        self,
        request: safconsole_20210112_models.UploadSampleApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safconsole_20210112_models.UploadSampleApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.data_value):
            query['DataValue'] = request.data_value
        if not UtilClient.is_unset(request.sample_type):
            query['SampleType'] = request.sample_type
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadSampleApi',
            version='2021-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safconsole_20210112_models.UploadSampleApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_sample_api(
        self,
        request: safconsole_20210112_models.UploadSampleApiRequest,
    ) -> safconsole_20210112_models.UploadSampleApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_sample_api_with_options(request, runtime)

    async def upload_sample_api_async(
        self,
        request: safconsole_20210112_models.UploadSampleApiRequest,
    ) -> safconsole_20210112_models.UploadSampleApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_sample_api_with_options_async(request, runtime)
