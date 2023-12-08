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

    def add_enterprise_tag_with_options(
        self,
        request: bailian_20230601_models.AddEnterpriseTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.AddEnterpriseTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEnterpriseTag',
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
            bailian_20230601_models.AddEnterpriseTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_enterprise_tag_with_options_async(
        self,
        request: bailian_20230601_models.AddEnterpriseTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.AddEnterpriseTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEnterpriseTag',
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
            bailian_20230601_models.AddEnterpriseTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_enterprise_tag(
        self,
        request: bailian_20230601_models.AddEnterpriseTagRequest,
    ) -> bailian_20230601_models.AddEnterpriseTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_enterprise_tag_with_options(request, runtime)

    async def add_enterprise_tag_async(
        self,
        request: bailian_20230601_models.AddEnterpriseTagRequest,
    ) -> bailian_20230601_models.AddEnterpriseTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_enterprise_tag_with_options_async(request, runtime)

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

    def del_enterprise_tag_with_options(
        self,
        request: bailian_20230601_models.DelEnterpriseTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DelEnterpriseTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelEnterpriseTag',
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
            bailian_20230601_models.DelEnterpriseTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_enterprise_tag_with_options_async(
        self,
        request: bailian_20230601_models.DelEnterpriseTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DelEnterpriseTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelEnterpriseTag',
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
            bailian_20230601_models.DelEnterpriseTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_enterprise_tag(
        self,
        request: bailian_20230601_models.DelEnterpriseTagRequest,
    ) -> bailian_20230601_models.DelEnterpriseTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.del_enterprise_tag_with_options(request, runtime)

    async def del_enterprise_tag_async(
        self,
        request: bailian_20230601_models.DelEnterpriseTagRequest,
    ) -> bailian_20230601_models.DelEnterpriseTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.del_enterprise_tag_with_options_async(request, runtime)

    def delete_enterprise_data_with_options(
        self,
        request: bailian_20230601_models.DeleteEnterpriseDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DeleteEnterpriseDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnterpriseData',
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
            bailian_20230601_models.DeleteEnterpriseDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_enterprise_data_with_options_async(
        self,
        request: bailian_20230601_models.DeleteEnterpriseDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.DeleteEnterpriseDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnterpriseData',
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
            bailian_20230601_models.DeleteEnterpriseDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_enterprise_data(
        self,
        request: bailian_20230601_models.DeleteEnterpriseDataRequest,
    ) -> bailian_20230601_models.DeleteEnterpriseDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_enterprise_data_with_options(request, runtime)

    async def delete_enterprise_data_async(
        self,
        request: bailian_20230601_models.DeleteEnterpriseDataRequest,
    ) -> bailian_20230601_models.DeleteEnterpriseDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_enterprise_data_with_options_async(request, runtime)

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

    def get_enterprise_data_by_data_id_with_options(
        self,
        request: bailian_20230601_models.GetEnterpriseDataByDataIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetEnterpriseDataByDataIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataByDataId',
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
            bailian_20230601_models.GetEnterpriseDataByDataIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_data_by_data_id_with_options_async(
        self,
        request: bailian_20230601_models.GetEnterpriseDataByDataIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetEnterpriseDataByDataIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataByDataId',
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
            bailian_20230601_models.GetEnterpriseDataByDataIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_data_by_data_id(
        self,
        request: bailian_20230601_models.GetEnterpriseDataByDataIdRequest,
    ) -> bailian_20230601_models.GetEnterpriseDataByDataIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_data_by_data_id_with_options(request, runtime)

    async def get_enterprise_data_by_data_id_async(
        self,
        request: bailian_20230601_models.GetEnterpriseDataByDataIdRequest,
    ) -> bailian_20230601_models.GetEnterpriseDataByDataIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_enterprise_data_by_data_id_with_options_async(request, runtime)

    def get_enterprise_data_chunk_with_options(
        self,
        request: bailian_20230601_models.GetEnterpriseDataChunkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetEnterpriseDataChunkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataChunk',
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
            bailian_20230601_models.GetEnterpriseDataChunkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_data_chunk_with_options_async(
        self,
        request: bailian_20230601_models.GetEnterpriseDataChunkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetEnterpriseDataChunkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataChunk',
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
            bailian_20230601_models.GetEnterpriseDataChunkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_data_chunk(
        self,
        request: bailian_20230601_models.GetEnterpriseDataChunkRequest,
    ) -> bailian_20230601_models.GetEnterpriseDataChunkResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_data_chunk_with_options(request, runtime)

    async def get_enterprise_data_chunk_async(
        self,
        request: bailian_20230601_models.GetEnterpriseDataChunkRequest,
    ) -> bailian_20230601_models.GetEnterpriseDataChunkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_enterprise_data_chunk_with_options_async(request, runtime)

    def get_enterprise_data_page_image_with_options(
        self,
        request: bailian_20230601_models.GetEnterpriseDataPageImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetEnterpriseDataPageImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataPageImage',
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
            bailian_20230601_models.GetEnterpriseDataPageImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_data_page_image_with_options_async(
        self,
        request: bailian_20230601_models.GetEnterpriseDataPageImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetEnterpriseDataPageImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataPageImage',
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
            bailian_20230601_models.GetEnterpriseDataPageImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_data_page_image(
        self,
        request: bailian_20230601_models.GetEnterpriseDataPageImageRequest,
    ) -> bailian_20230601_models.GetEnterpriseDataPageImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_data_page_image_with_options(request, runtime)

    async def get_enterprise_data_page_image_async(
        self,
        request: bailian_20230601_models.GetEnterpriseDataPageImageRequest,
    ) -> bailian_20230601_models.GetEnterpriseDataPageImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_enterprise_data_page_image_with_options_async(request, runtime)

    def get_enterprise_data_parse_result_with_options(
        self,
        request: bailian_20230601_models.GetEnterpriseDataParseResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetEnterpriseDataParseResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataParseResult',
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
            bailian_20230601_models.GetEnterpriseDataParseResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_data_parse_result_with_options_async(
        self,
        request: bailian_20230601_models.GetEnterpriseDataParseResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetEnterpriseDataParseResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataParseResult',
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
            bailian_20230601_models.GetEnterpriseDataParseResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_data_parse_result(
        self,
        request: bailian_20230601_models.GetEnterpriseDataParseResultRequest,
    ) -> bailian_20230601_models.GetEnterpriseDataParseResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_data_parse_result_with_options(request, runtime)

    async def get_enterprise_data_parse_result_async(
        self,
        request: bailian_20230601_models.GetEnterpriseDataParseResultRequest,
    ) -> bailian_20230601_models.GetEnterpriseDataParseResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_enterprise_data_parse_result_with_options_async(request, runtime)

    def get_file_store_upload_policy_with_options(
        self,
        request: bailian_20230601_models.GetFileStoreUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetFileStoreUploadPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_store_id):
            query['FileStoreId'] = request.file_store_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileStoreUploadPolicy',
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
            bailian_20230601_models.GetFileStoreUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_store_upload_policy_with_options_async(
        self,
        request: bailian_20230601_models.GetFileStoreUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetFileStoreUploadPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_store_id):
            query['FileStoreId'] = request.file_store_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileStoreUploadPolicy',
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
            bailian_20230601_models.GetFileStoreUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_store_upload_policy(
        self,
        request: bailian_20230601_models.GetFileStoreUploadPolicyRequest,
    ) -> bailian_20230601_models.GetFileStoreUploadPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_file_store_upload_policy_with_options(request, runtime)

    async def get_file_store_upload_policy_async(
        self,
        request: bailian_20230601_models.GetFileStoreUploadPolicyRequest,
    ) -> bailian_20230601_models.GetFileStoreUploadPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_file_store_upload_policy_with_options_async(request, runtime)

    def get_import_task_result_with_options(
        self,
        request: bailian_20230601_models.GetImportTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetImportTaskResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImportTaskResult',
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
            bailian_20230601_models.GetImportTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_import_task_result_with_options_async(
        self,
        request: bailian_20230601_models.GetImportTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetImportTaskResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImportTaskResult',
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
            bailian_20230601_models.GetImportTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_import_task_result(
        self,
        request: bailian_20230601_models.GetImportTaskResultRequest,
    ) -> bailian_20230601_models.GetImportTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_import_task_result_with_options(request, runtime)

    async def get_import_task_result_async(
        self,
        request: bailian_20230601_models.GetImportTaskResultRequest,
    ) -> bailian_20230601_models.GetImportTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_import_task_result_with_options_async(request, runtime)

    def get_prompt_with_options(
        self,
        request: bailian_20230601_models.GetPromptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetPromptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.prompt_id):
            query['PromptId'] = request.prompt_id
        if not UtilClient.is_unset(request.vars):
            query['Vars'] = request.vars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrompt',
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
            bailian_20230601_models.GetPromptResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prompt_with_options_async(
        self,
        request: bailian_20230601_models.GetPromptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.GetPromptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.prompt_id):
            query['PromptId'] = request.prompt_id
        if not UtilClient.is_unset(request.vars):
            query['Vars'] = request.vars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrompt',
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
            bailian_20230601_models.GetPromptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prompt(
        self,
        request: bailian_20230601_models.GetPromptRequest,
    ) -> bailian_20230601_models.GetPromptResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_prompt_with_options(request, runtime)

    async def get_prompt_async(
        self,
        request: bailian_20230601_models.GetPromptRequest,
    ) -> bailian_20230601_models.GetPromptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_prompt_with_options_async(request, runtime)

    def import_enterprise_document_with_options(
        self,
        tmp_req: bailian_20230601_models.ImportEnterpriseDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.ImportEnterpriseDocumentResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.ImportEnterpriseDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.document_list):
            request.document_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_list, 'DocumentList', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.document_list_shrink):
            query['DocumentList'] = request.document_list_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.store_id):
            query['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportEnterpriseDocument',
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
            bailian_20230601_models.ImportEnterpriseDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_enterprise_document_with_options_async(
        self,
        tmp_req: bailian_20230601_models.ImportEnterpriseDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.ImportEnterpriseDocumentResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.ImportEnterpriseDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.document_list):
            request.document_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_list, 'DocumentList', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.document_list_shrink):
            query['DocumentList'] = request.document_list_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.store_id):
            query['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportEnterpriseDocument',
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
            bailian_20230601_models.ImportEnterpriseDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_enterprise_document(
        self,
        request: bailian_20230601_models.ImportEnterpriseDocumentRequest,
    ) -> bailian_20230601_models.ImportEnterpriseDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_enterprise_document_with_options(request, runtime)

    async def import_enterprise_document_async(
        self,
        request: bailian_20230601_models.ImportEnterpriseDocumentRequest,
    ) -> bailian_20230601_models.ImportEnterpriseDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_enterprise_document_with_options_async(request, runtime)

    def import_user_document_with_options(
        self,
        request: bailian_20230601_models.ImportUserDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.ImportUserDocumentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_store_id):
            query['FileStoreId'] = request.file_store_id
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        if not UtilClient.is_unset(request.store_id):
            query['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportUserDocument',
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
            bailian_20230601_models.ImportUserDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_user_document_with_options_async(
        self,
        request: bailian_20230601_models.ImportUserDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.ImportUserDocumentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_store_id):
            query['FileStoreId'] = request.file_store_id
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        if not UtilClient.is_unset(request.store_id):
            query['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportUserDocument',
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
            bailian_20230601_models.ImportUserDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_user_document(
        self,
        request: bailian_20230601_models.ImportUserDocumentRequest,
    ) -> bailian_20230601_models.ImportUserDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_user_document_with_options(request, runtime)

    async def import_user_document_async(
        self,
        request: bailian_20230601_models.ImportUserDocumentRequest,
    ) -> bailian_20230601_models.ImportUserDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_user_document_with_options_async(request, runtime)

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

    def query_enterprise_data_list_with_options(
        self,
        tmp_req: bailian_20230601_models.QueryEnterpriseDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.QueryEnterpriseDataListResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.QueryEnterpriseDataListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_name):
            query['DataName'] = request.data_name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_type):
            query['StoreType'] = request.store_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnterpriseDataList',
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
            bailian_20230601_models.QueryEnterpriseDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_enterprise_data_list_with_options_async(
        self,
        tmp_req: bailian_20230601_models.QueryEnterpriseDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.QueryEnterpriseDataListResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.QueryEnterpriseDataListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_name):
            query['DataName'] = request.data_name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_type):
            query['StoreType'] = request.store_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnterpriseDataList',
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
            bailian_20230601_models.QueryEnterpriseDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_enterprise_data_list(
        self,
        request: bailian_20230601_models.QueryEnterpriseDataListRequest,
    ) -> bailian_20230601_models.QueryEnterpriseDataListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_enterprise_data_list_with_options(request, runtime)

    async def query_enterprise_data_list_async(
        self,
        request: bailian_20230601_models.QueryEnterpriseDataListRequest,
    ) -> bailian_20230601_models.QueryEnterpriseDataListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_enterprise_data_list_with_options_async(request, runtime)

    def query_enterprise_data_tag_with_options(
        self,
        request: bailian_20230601_models.QueryEnterpriseDataTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.QueryEnterpriseDataTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnterpriseDataTag',
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
            bailian_20230601_models.QueryEnterpriseDataTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_enterprise_data_tag_with_options_async(
        self,
        request: bailian_20230601_models.QueryEnterpriseDataTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.QueryEnterpriseDataTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnterpriseDataTag',
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
            bailian_20230601_models.QueryEnterpriseDataTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_enterprise_data_tag(
        self,
        request: bailian_20230601_models.QueryEnterpriseDataTagRequest,
    ) -> bailian_20230601_models.QueryEnterpriseDataTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_enterprise_data_tag_with_options(request, runtime)

    async def query_enterprise_data_tag_async(
        self,
        request: bailian_20230601_models.QueryEnterpriseDataTagRequest,
    ) -> bailian_20230601_models.QueryEnterpriseDataTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_enterprise_data_tag_with_options_async(request, runtime)

    def query_enterprise_tag_list_with_options(
        self,
        request: bailian_20230601_models.QueryEnterpriseTagListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.QueryEnterpriseTagListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnterpriseTagList',
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
            bailian_20230601_models.QueryEnterpriseTagListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_enterprise_tag_list_with_options_async(
        self,
        request: bailian_20230601_models.QueryEnterpriseTagListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.QueryEnterpriseTagListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnterpriseTagList',
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
            bailian_20230601_models.QueryEnterpriseTagListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_enterprise_tag_list(
        self,
        request: bailian_20230601_models.QueryEnterpriseTagListRequest,
    ) -> bailian_20230601_models.QueryEnterpriseTagListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_enterprise_tag_list_with_options(request, runtime)

    async def query_enterprise_tag_list_async(
        self,
        request: bailian_20230601_models.QueryEnterpriseTagListRequest,
    ) -> bailian_20230601_models.QueryEnterpriseTagListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_enterprise_tag_list_with_options_async(request, runtime)

    def query_user_document_with_options(
        self,
        request: bailian_20230601_models.QueryUserDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.QueryUserDocumentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserDocument',
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
            bailian_20230601_models.QueryUserDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_document_with_options_async(
        self,
        request: bailian_20230601_models.QueryUserDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.QueryUserDocumentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserDocument',
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
            bailian_20230601_models.QueryUserDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_document(
        self,
        request: bailian_20230601_models.QueryUserDocumentRequest,
    ) -> bailian_20230601_models.QueryUserDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_document_with_options(request, runtime)

    async def query_user_document_async(
        self,
        request: bailian_20230601_models.QueryUserDocumentRequest,
    ) -> bailian_20230601_models.QueryUserDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_document_with_options_async(request, runtime)

    def search_enterprise_data_with_options(
        self,
        tmp_req: bailian_20230601_models.SearchEnterpriseDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.SearchEnterpriseDataResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.SearchEnterpriseDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_id_list):
            request.data_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_id_list, 'DataIdList', 'json')
        if not UtilClient.is_unset(tmp_req.tag_id_list):
            request.tag_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id_list_shrink):
            query['DataIdList'] = request.data_id_list_shrink
        if not UtilClient.is_unset(request.enable_rank):
            query['EnableRank'] = request.enable_rank
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.store_id):
            query['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.tag_id_list_shrink):
            query['TagIdList'] = request.tag_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchEnterpriseData',
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
            bailian_20230601_models.SearchEnterpriseDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_enterprise_data_with_options_async(
        self,
        tmp_req: bailian_20230601_models.SearchEnterpriseDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.SearchEnterpriseDataResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.SearchEnterpriseDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_id_list):
            request.data_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_id_list, 'DataIdList', 'json')
        if not UtilClient.is_unset(tmp_req.tag_id_list):
            request.tag_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id_list_shrink):
            query['DataIdList'] = request.data_id_list_shrink
        if not UtilClient.is_unset(request.enable_rank):
            query['EnableRank'] = request.enable_rank
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.store_id):
            query['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.tag_id_list_shrink):
            query['TagIdList'] = request.tag_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchEnterpriseData',
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
            bailian_20230601_models.SearchEnterpriseDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_enterprise_data(
        self,
        request: bailian_20230601_models.SearchEnterpriseDataRequest,
    ) -> bailian_20230601_models.SearchEnterpriseDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_enterprise_data_with_options(request, runtime)

    async def search_enterprise_data_async(
        self,
        request: bailian_20230601_models.SearchEnterpriseDataRequest,
    ) -> bailian_20230601_models.SearchEnterpriseDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_enterprise_data_with_options_async(request, runtime)

    def update_enterprise_data_info_with_options(
        self,
        request: bailian_20230601_models.UpdateEnterpriseDataInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.UpdateEnterpriseDataInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.data_name):
            query['DataName'] = request.data_name
        if not UtilClient.is_unset(request.file_preview_link):
            query['FilePreviewLink'] = request.file_preview_link
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseDataInfo',
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
            bailian_20230601_models.UpdateEnterpriseDataInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_enterprise_data_info_with_options_async(
        self,
        request: bailian_20230601_models.UpdateEnterpriseDataInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.UpdateEnterpriseDataInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.data_name):
            query['DataName'] = request.data_name
        if not UtilClient.is_unset(request.file_preview_link):
            query['FilePreviewLink'] = request.file_preview_link
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseDataInfo',
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
            bailian_20230601_models.UpdateEnterpriseDataInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_enterprise_data_info(
        self,
        request: bailian_20230601_models.UpdateEnterpriseDataInfoRequest,
    ) -> bailian_20230601_models.UpdateEnterpriseDataInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_enterprise_data_info_with_options(request, runtime)

    async def update_enterprise_data_info_async(
        self,
        request: bailian_20230601_models.UpdateEnterpriseDataInfoRequest,
    ) -> bailian_20230601_models.UpdateEnterpriseDataInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_enterprise_data_info_with_options_async(request, runtime)

    def update_enterprise_data_tag_with_options(
        self,
        tmp_req: bailian_20230601_models.UpdateEnterpriseDataTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.UpdateEnterpriseDataTagResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.UpdateEnterpriseDataTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseDataTag',
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
            bailian_20230601_models.UpdateEnterpriseDataTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_enterprise_data_tag_with_options_async(
        self,
        tmp_req: bailian_20230601_models.UpdateEnterpriseDataTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.UpdateEnterpriseDataTagResponse:
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.UpdateEnterpriseDataTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseDataTag',
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
            bailian_20230601_models.UpdateEnterpriseDataTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_enterprise_data_tag(
        self,
        request: bailian_20230601_models.UpdateEnterpriseDataTagRequest,
    ) -> bailian_20230601_models.UpdateEnterpriseDataTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_enterprise_data_tag_with_options(request, runtime)

    async def update_enterprise_data_tag_async(
        self,
        request: bailian_20230601_models.UpdateEnterpriseDataTagRequest,
    ) -> bailian_20230601_models.UpdateEnterpriseDataTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_enterprise_data_tag_with_options_async(request, runtime)

    def update_enterprise_tag_with_options(
        self,
        request: bailian_20230601_models.UpdateEnterpriseTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.UpdateEnterpriseTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseTag',
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
            bailian_20230601_models.UpdateEnterpriseTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_enterprise_tag_with_options_async(
        self,
        request: bailian_20230601_models.UpdateEnterpriseTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bailian_20230601_models.UpdateEnterpriseTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseTag',
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
            bailian_20230601_models.UpdateEnterpriseTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_enterprise_tag(
        self,
        request: bailian_20230601_models.UpdateEnterpriseTagRequest,
    ) -> bailian_20230601_models.UpdateEnterpriseTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_enterprise_tag_with_options(request, runtime)

    async def update_enterprise_tag_async(
        self,
        request: bailian_20230601_models.UpdateEnterpriseTagRequest,
    ) -> bailian_20230601_models.UpdateEnterpriseTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_enterprise_tag_with_options_async(request, runtime)
