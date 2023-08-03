# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bailian20230601 import models as bailian_20230601_models
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
        self._endpoint = self.get_endpoint('bailian', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_fine_tune_job_with_options(
        self,
        request: bailian_20230601_models.CancelFineTuneJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.CancelFineTuneJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CancelFineTuneJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_fine_tune_job_with_options_async(
        self,
        request: bailian_20230601_models.CancelFineTuneJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.CancelFineTuneJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CancelFineTuneJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_fine_tune_job(
        self,
        request: bailian_20230601_models.CancelFineTuneJobRequest,
    ) -> bailian_20230601_models.CancelFineTuneJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_fine_tune_job_with_options(request, runtime)

    async def cancel_fine_tune_job_async(
        self,
        request: bailian_20230601_models.CancelFineTuneJobRequest,
    ) -> bailian_20230601_models.CancelFineTuneJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_fine_tune_job_with_options_async(request, runtime)

    def create_fine_tune_job_with_options(
        self,
        tmp_req: bailian_20230601_models.CreateFineTuneJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.CreateFineTuneJobResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.CreateFineTuneJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hyper_parameters):
            request.hyper_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hyper_parameters, 'HyperParameters', 'json')
        if not UtilClient.is_unset(tmp_req.training_files):
            request.training_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.training_files, 'TrainingFiles', 'json')
        if not UtilClient.is_unset(tmp_req.validation_files):
            request.validation_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.validation_files, 'ValidationFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.base_model):
            body['BaseModel'] = request.base_model
        if not UtilClient.is_unset(request.hyper_parameters_shrink):
            body['HyperParameters'] = request.hyper_parameters_shrink
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.training_files_shrink):
            body['TrainingFiles'] = request.training_files_shrink
        if not UtilClient.is_unset(request.training_type):
            body['TrainingType'] = request.training_type
        if not UtilClient.is_unset(request.validation_files_shrink):
            body['ValidationFiles'] = request.validation_files_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateFineTuneJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fine_tune_job_with_options_async(
        self,
        tmp_req: bailian_20230601_models.CreateFineTuneJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.CreateFineTuneJobResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.CreateFineTuneJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hyper_parameters):
            request.hyper_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hyper_parameters, 'HyperParameters', 'json')
        if not UtilClient.is_unset(tmp_req.training_files):
            request.training_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.training_files, 'TrainingFiles', 'json')
        if not UtilClient.is_unset(tmp_req.validation_files):
            request.validation_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.validation_files, 'ValidationFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.base_model):
            body['BaseModel'] = request.base_model
        if not UtilClient.is_unset(request.hyper_parameters_shrink):
            body['HyperParameters'] = request.hyper_parameters_shrink
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.training_files_shrink):
            body['TrainingFiles'] = request.training_files_shrink
        if not UtilClient.is_unset(request.training_type):
            body['TrainingType'] = request.training_type
        if not UtilClient.is_unset(request.validation_files_shrink):
            body['ValidationFiles'] = request.validation_files_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateFineTuneJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fine_tune_job(
        self,
        request: bailian_20230601_models.CreateFineTuneJobRequest,
    ) -> bailian_20230601_models.CreateFineTuneJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fine_tune_job_with_options(request, runtime)

    async def create_fine_tune_job_async(
        self,
        request: bailian_20230601_models.CreateFineTuneJobRequest,
    ) -> bailian_20230601_models.CreateFineTuneJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fine_tune_job_with_options_async(request, runtime)

    def create_service_with_options(
        self,
        request: bailian_20230601_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: bailian_20230601_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: bailian_20230601_models.CreateServiceRequest,
    ) -> bailian_20230601_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    async def create_service_async(
        self,
        request: bailian_20230601_models.CreateServiceRequest,
    ) -> bailian_20230601_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_with_options_async(request, runtime)

    def create_text_embeddings_with_options(
        self,
        tmp_req: bailian_20230601_models.CreateTextEmbeddingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.CreateTextEmbeddingsResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.CreateTextEmbeddingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.text_type):
            query['TextType'] = request.text_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTextEmbeddings',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateTextEmbeddingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_text_embeddings_with_options_async(
        self,
        tmp_req: bailian_20230601_models.CreateTextEmbeddingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.CreateTextEmbeddingsResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.CreateTextEmbeddingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.text_type):
            query['TextType'] = request.text_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTextEmbeddings',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateTextEmbeddingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_text_embeddings(
        self,
        request: bailian_20230601_models.CreateTextEmbeddingsRequest,
    ) -> bailian_20230601_models.CreateTextEmbeddingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_text_embeddings_with_options(request, runtime)

    async def create_text_embeddings_async(
        self,
        request: bailian_20230601_models.CreateTextEmbeddingsRequest,
    ) -> bailian_20230601_models.CreateTextEmbeddingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_text_embeddings_with_options_async(request, runtime)

    def create_token_with_options(
        self,
        request: bailian_20230601_models.CreateTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.CreateTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateToken',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_token_with_options_async(
        self,
        request: bailian_20230601_models.CreateTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.CreateTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateToken',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_token(
        self,
        request: bailian_20230601_models.CreateTokenRequest,
    ) -> bailian_20230601_models.CreateTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_token_with_options(request, runtime)

    async def create_token_async(
        self,
        request: bailian_20230601_models.CreateTokenRequest,
    ) -> bailian_20230601_models.CreateTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_token_with_options_async(request, runtime)

    def delete_fine_tune_job_with_options(
        self,
        request: bailian_20230601_models.DeleteFineTuneJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DeleteFineTuneJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DeleteFineTuneJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_fine_tune_job_with_options_async(
        self,
        request: bailian_20230601_models.DeleteFineTuneJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DeleteFineTuneJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DeleteFineTuneJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_fine_tune_job(
        self,
        request: bailian_20230601_models.DeleteFineTuneJobRequest,
    ) -> bailian_20230601_models.DeleteFineTuneJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_fine_tune_job_with_options(request, runtime)

    async def delete_fine_tune_job_async(
        self,
        request: bailian_20230601_models.DeleteFineTuneJobRequest,
    ) -> bailian_20230601_models.DeleteFineTuneJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_fine_tune_job_with_options_async(request, runtime)

    def delete_service_with_options(
        self,
        request: bailian_20230601_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.model_service_id):
            body['ModelServiceId'] = request.model_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        request: bailian_20230601_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.model_service_id):
            body['ModelServiceId'] = request.model_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        request: bailian_20230601_models.DeleteServiceRequest,
    ) -> bailian_20230601_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    async def delete_service_async(
        self,
        request: bailian_20230601_models.DeleteServiceRequest,
    ) -> bailian_20230601_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_with_options_async(request, runtime)

    def describe_fine_tune_job_with_options(
        self,
        request: bailian_20230601_models.DescribeFineTuneJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DescribeFineTuneJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DescribeFineTuneJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fine_tune_job_with_options_async(
        self,
        request: bailian_20230601_models.DescribeFineTuneJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DescribeFineTuneJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DescribeFineTuneJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fine_tune_job(
        self,
        request: bailian_20230601_models.DescribeFineTuneJobRequest,
    ) -> bailian_20230601_models.DescribeFineTuneJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fine_tune_job_with_options(request, runtime)

    async def describe_fine_tune_job_async(
        self,
        request: bailian_20230601_models.DescribeFineTuneJobRequest,
    ) -> bailian_20230601_models.DescribeFineTuneJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fine_tune_job_with_options_async(request, runtime)

    def describe_service_with_options(
        self,
        request: bailian_20230601_models.DescribeServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DescribeServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.model_service_id):
            body['ModelServiceId'] = request.model_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeService',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DescribeServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_with_options_async(
        self,
        request: bailian_20230601_models.DescribeServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DescribeServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.model_service_id):
            body['ModelServiceId'] = request.model_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeService',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DescribeServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service(
        self,
        request: bailian_20230601_models.DescribeServiceRequest,
    ) -> bailian_20230601_models.DescribeServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_with_options(request, runtime)

    async def describe_service_async(
        self,
        request: bailian_20230601_models.DescribeServiceRequest,
    ) -> bailian_20230601_models.DescribeServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_with_options_async(request, runtime)

    def list_fine_tune_jobs_with_options(
        self,
        request: bailian_20230601_models.ListFineTuneJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.ListFineTuneJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFineTuneJobs',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.ListFineTuneJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fine_tune_jobs_with_options_async(
        self,
        request: bailian_20230601_models.ListFineTuneJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.ListFineTuneJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFineTuneJobs',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.ListFineTuneJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fine_tune_jobs(
        self,
        request: bailian_20230601_models.ListFineTuneJobsRequest,
    ) -> bailian_20230601_models.ListFineTuneJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_fine_tune_jobs_with_options(request, runtime)

    async def list_fine_tune_jobs_async(
        self,
        request: bailian_20230601_models.ListFineTuneJobsRequest,
    ) -> bailian_20230601_models.ListFineTuneJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_fine_tune_jobs_with_options_async(request, runtime)

    def list_services_with_options(
        self,
        request: bailian_20230601_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.ListServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_key):
            body['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: bailian_20230601_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.ListServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_key):
            body['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: bailian_20230601_models.ListServicesRequest,
    ) -> bailian_20230601_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    async def list_services_async(
        self,
        request: bailian_20230601_models.ListServicesRequest,
    ) -> bailian_20230601_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_services_with_options_async(request, runtime)
