# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nlp_automl20191111 import models as nlp_automl_20191111_models
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
        self._endpoint = self.get_endpoint('nlp-automl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_async_predict_with_options(
        self,
        request: nlp_automl_20191111_models.CreateAsyncPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateAsyncPredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.CreateAsyncPredictResponse().from_map(
            self.do_rpcrequest('CreateAsyncPredict', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_async_predict_with_options_async(
        self,
        request: nlp_automl_20191111_models.CreateAsyncPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateAsyncPredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.CreateAsyncPredictResponse().from_map(
            await self.do_rpcrequest_async('CreateAsyncPredict', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_async_predict(
        self,
        request: nlp_automl_20191111_models.CreateAsyncPredictRequest,
    ) -> nlp_automl_20191111_models.CreateAsyncPredictResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_async_predict_with_options(request, runtime)

    async def create_async_predict_async(
        self,
        request: nlp_automl_20191111_models.CreateAsyncPredictRequest,
    ) -> nlp_automl_20191111_models.CreateAsyncPredictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_async_predict_with_options_async(request, runtime)

    def create_dataset_with_options(
        self,
        request: nlp_automl_20191111_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateDatasetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.CreateDatasetResponse().from_map(
            self.do_rpcrequest('CreateDataset', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        request: nlp_automl_20191111_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateDatasetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.CreateDatasetResponse().from_map(
            await self.do_rpcrequest_async('CreateDataset', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dataset(
        self,
        request: nlp_automl_20191111_models.CreateDatasetRequest,
    ) -> nlp_automl_20191111_models.CreateDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    async def create_dataset_async(
        self,
        request: nlp_automl_20191111_models.CreateDatasetRequest,
    ) -> nlp_automl_20191111_models.CreateDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dataset_with_options_async(request, runtime)

    def create_dataset_record_with_options(
        self,
        request: nlp_automl_20191111_models.CreateDatasetRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateDatasetRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.CreateDatasetRecordResponse().from_map(
            self.do_rpcrequest('CreateDatasetRecord', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dataset_record_with_options_async(
        self,
        request: nlp_automl_20191111_models.CreateDatasetRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateDatasetRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.CreateDatasetRecordResponse().from_map(
            await self.do_rpcrequest_async('CreateDatasetRecord', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dataset_record(
        self,
        request: nlp_automl_20191111_models.CreateDatasetRecordRequest,
    ) -> nlp_automl_20191111_models.CreateDatasetRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_record_with_options(request, runtime)

    async def create_dataset_record_async(
        self,
        request: nlp_automl_20191111_models.CreateDatasetRecordRequest,
    ) -> nlp_automl_20191111_models.CreateDatasetRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dataset_record_with_options_async(request, runtime)

    def create_model_with_options(
        self,
        tmp_req: nlp_automl_20191111_models.CreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateModelResponse:
        UtilClient.validate_model(tmp_req)
        request = nlp_automl_20191111_models.CreateModelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dataset_id_list):
            request.dataset_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dataset_id_list, 'DatasetIdList', 'json')
        if not UtilClient.is_unset(tmp_req.test_dataset_id_list):
            request.test_dataset_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.test_dataset_id_list, 'TestDatasetIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.CreateModelResponse().from_map(
            self.do_rpcrequest('CreateModel', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_model_with_options_async(
        self,
        tmp_req: nlp_automl_20191111_models.CreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateModelResponse:
        UtilClient.validate_model(tmp_req)
        request = nlp_automl_20191111_models.CreateModelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dataset_id_list):
            request.dataset_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dataset_id_list, 'DatasetIdList', 'json')
        if not UtilClient.is_unset(tmp_req.test_dataset_id_list):
            request.test_dataset_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.test_dataset_id_list, 'TestDatasetIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.CreateModelResponse().from_map(
            await self.do_rpcrequest_async('CreateModel', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_model(
        self,
        request: nlp_automl_20191111_models.CreateModelRequest,
    ) -> nlp_automl_20191111_models.CreateModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_model_with_options(request, runtime)

    async def create_model_async(
        self,
        request: nlp_automl_20191111_models.CreateModelRequest,
    ) -> nlp_automl_20191111_models.CreateModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_model_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        request: nlp_automl_20191111_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.CreateProjectResponse().from_map(
            self.do_rpcrequest('CreateProject', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: nlp_automl_20191111_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.CreateProjectResponse().from_map(
            await self.do_rpcrequest_async('CreateProject', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(
        self,
        request: nlp_automl_20191111_models.CreateProjectRequest,
    ) -> nlp_automl_20191111_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: nlp_automl_20191111_models.CreateProjectRequest,
    ) -> nlp_automl_20191111_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def delete_model_with_options(
        self,
        request: nlp_automl_20191111_models.DeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.DeleteModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.DeleteModelResponse().from_map(
            self.do_rpcrequest('DeleteModel', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        request: nlp_automl_20191111_models.DeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.DeleteModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.DeleteModelResponse().from_map(
            await self.do_rpcrequest_async('DeleteModel', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_model(
        self,
        request: nlp_automl_20191111_models.DeleteModelRequest,
    ) -> nlp_automl_20191111_models.DeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_model_with_options(request, runtime)

    async def delete_model_async(
        self,
        request: nlp_automl_20191111_models.DeleteModelRequest,
    ) -> nlp_automl_20191111_models.DeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_model_with_options_async(request, runtime)

    def deploy_model_with_options(
        self,
        request: nlp_automl_20191111_models.DeployModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.DeployModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.DeployModelResponse().from_map(
            self.do_rpcrequest('DeployModel', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deploy_model_with_options_async(
        self,
        request: nlp_automl_20191111_models.DeployModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.DeployModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.DeployModelResponse().from_map(
            await self.do_rpcrequest_async('DeployModel', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_model(
        self,
        request: nlp_automl_20191111_models.DeployModelRequest,
    ) -> nlp_automl_20191111_models.DeployModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_model_with_options(request, runtime)

    async def deploy_model_async(
        self,
        request: nlp_automl_20191111_models.DeployModelRequest,
    ) -> nlp_automl_20191111_models.DeployModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_model_with_options_async(request, runtime)

    def get_async_predict_with_options(
        self,
        request: nlp_automl_20191111_models.GetAsyncPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.GetAsyncPredictResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return nlp_automl_20191111_models.GetAsyncPredictResponse().from_map(
            self.do_rpcrequest('GetAsyncPredict', '2019-11-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_async_predict_with_options_async(
        self,
        request: nlp_automl_20191111_models.GetAsyncPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.GetAsyncPredictResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return nlp_automl_20191111_models.GetAsyncPredictResponse().from_map(
            await self.do_rpcrequest_async('GetAsyncPredict', '2019-11-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_async_predict(
        self,
        request: nlp_automl_20191111_models.GetAsyncPredictRequest,
    ) -> nlp_automl_20191111_models.GetAsyncPredictResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_predict_with_options(request, runtime)

    async def get_async_predict_async(
        self,
        request: nlp_automl_20191111_models.GetAsyncPredictRequest,
    ) -> nlp_automl_20191111_models.GetAsyncPredictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_predict_with_options_async(request, runtime)

    def get_model_with_options(
        self,
        request: nlp_automl_20191111_models.GetModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.GetModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.GetModelResponse().from_map(
            self.do_rpcrequest('GetModel', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_model_with_options_async(
        self,
        request: nlp_automl_20191111_models.GetModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.GetModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.GetModelResponse().from_map(
            await self.do_rpcrequest_async('GetModel', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_model(
        self,
        request: nlp_automl_20191111_models.GetModelRequest,
    ) -> nlp_automl_20191111_models.GetModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_model_with_options(request, runtime)

    async def get_model_async(
        self,
        request: nlp_automl_20191111_models.GetModelRequest,
    ) -> nlp_automl_20191111_models.GetModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_model_with_options_async(request, runtime)

    def get_predict_result_with_options(
        self,
        request: nlp_automl_20191111_models.GetPredictResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.GetPredictResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.GetPredictResultResponse().from_map(
            self.do_rpcrequest('GetPredictResult', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_predict_result_with_options_async(
        self,
        request: nlp_automl_20191111_models.GetPredictResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.GetPredictResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.GetPredictResultResponse().from_map(
            await self.do_rpcrequest_async('GetPredictResult', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_predict_result(
        self,
        request: nlp_automl_20191111_models.GetPredictResultRequest,
    ) -> nlp_automl_20191111_models.GetPredictResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_predict_result_with_options(request, runtime)

    async def get_predict_result_async(
        self,
        request: nlp_automl_20191111_models.GetPredictResultRequest,
    ) -> nlp_automl_20191111_models.GetPredictResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_predict_result_with_options_async(request, runtime)

    def list_dataset_with_options(
        self,
        request: nlp_automl_20191111_models.ListDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.ListDatasetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.ListDatasetResponse().from_map(
            self.do_rpcrequest('ListDataset', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dataset_with_options_async(
        self,
        request: nlp_automl_20191111_models.ListDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.ListDatasetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.ListDatasetResponse().from_map(
            await self.do_rpcrequest_async('ListDataset', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dataset(
        self,
        request: nlp_automl_20191111_models.ListDatasetRequest,
    ) -> nlp_automl_20191111_models.ListDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dataset_with_options(request, runtime)

    async def list_dataset_async(
        self,
        request: nlp_automl_20191111_models.ListDatasetRequest,
    ) -> nlp_automl_20191111_models.ListDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dataset_with_options_async(request, runtime)

    def list_models_with_options(
        self,
        request: nlp_automl_20191111_models.ListModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.ListModelsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.ListModelsResponse().from_map(
            self.do_rpcrequest('ListModels', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_models_with_options_async(
        self,
        request: nlp_automl_20191111_models.ListModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.ListModelsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.ListModelsResponse().from_map(
            await self.do_rpcrequest_async('ListModels', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_models(
        self,
        request: nlp_automl_20191111_models.ListModelsRequest,
    ) -> nlp_automl_20191111_models.ListModelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_models_with_options(request, runtime)

    async def list_models_async(
        self,
        request: nlp_automl_20191111_models.ListModelsRequest,
    ) -> nlp_automl_20191111_models.ListModelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_models_with_options_async(request, runtime)

    def run_contact_review_with_options(
        self,
        request: nlp_automl_20191111_models.RunContactReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.RunContactReviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.RunContactReviewResponse().from_map(
            self.do_rpcrequest('RunContactReview', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_contact_review_with_options_async(
        self,
        request: nlp_automl_20191111_models.RunContactReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.RunContactReviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.RunContactReviewResponse().from_map(
            await self.do_rpcrequest_async('RunContactReview', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_contact_review(
        self,
        request: nlp_automl_20191111_models.RunContactReviewRequest,
    ) -> nlp_automl_20191111_models.RunContactReviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_contact_review_with_options(request, runtime)

    async def run_contact_review_async(
        self,
        request: nlp_automl_20191111_models.RunContactReviewRequest,
    ) -> nlp_automl_20191111_models.RunContactReviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_contact_review_with_options_async(request, runtime)

    def run_pre_train_service_with_options(
        self,
        request: nlp_automl_20191111_models.RunPreTrainServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.RunPreTrainServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.RunPreTrainServiceResponse().from_map(
            self.do_rpcrequest('RunPreTrainService', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_pre_train_service_with_options_async(
        self,
        request: nlp_automl_20191111_models.RunPreTrainServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.RunPreTrainServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.RunPreTrainServiceResponse().from_map(
            await self.do_rpcrequest_async('RunPreTrainService', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_pre_train_service(
        self,
        request: nlp_automl_20191111_models.RunPreTrainServiceRequest,
    ) -> nlp_automl_20191111_models.RunPreTrainServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_pre_train_service_with_options(request, runtime)

    async def run_pre_train_service_async(
        self,
        request: nlp_automl_20191111_models.RunPreTrainServiceRequest,
    ) -> nlp_automl_20191111_models.RunPreTrainServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_pre_train_service_with_options_async(request, runtime)

    def run_smart_call_service_with_options(
        self,
        request: nlp_automl_20191111_models.RunSmartCallServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.RunSmartCallServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.RunSmartCallServiceResponse().from_map(
            self.do_rpcrequest('RunSmartCallService', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_smart_call_service_with_options_async(
        self,
        request: nlp_automl_20191111_models.RunSmartCallServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.RunSmartCallServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return nlp_automl_20191111_models.RunSmartCallServiceResponse().from_map(
            await self.do_rpcrequest_async('RunSmartCallService', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_smart_call_service(
        self,
        request: nlp_automl_20191111_models.RunSmartCallServiceRequest,
    ) -> nlp_automl_20191111_models.RunSmartCallServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_smart_call_service_with_options(request, runtime)

    async def run_smart_call_service_async(
        self,
        request: nlp_automl_20191111_models.RunSmartCallServiceRequest,
    ) -> nlp_automl_20191111_models.RunSmartCallServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_smart_call_service_with_options_async(request, runtime)
