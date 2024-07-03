# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nlp_automl20190701 import models as nlp_automl_20190701_models
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

    def add_mtintervene_word_with_options(
        self,
        request: nlp_automl_20190701_models.AddMTInterveneWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20190701_models.AddMTInterveneWordResponse:
        """
        @param request: AddMTInterveneWordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMTInterveneWordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.package_id):
            query['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.source_text):
            query['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_text):
            query['TargetText'] = request.target_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMTInterveneWord',
            version='2019-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20190701_models.AddMTInterveneWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_mtintervene_word_with_options_async(
        self,
        request: nlp_automl_20190701_models.AddMTInterveneWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20190701_models.AddMTInterveneWordResponse:
        """
        @param request: AddMTInterveneWordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMTInterveneWordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.package_id):
            query['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.source_text):
            query['SourceText'] = request.source_text
        if not UtilClient.is_unset(request.target_text):
            query['TargetText'] = request.target_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMTInterveneWord',
            version='2019-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20190701_models.AddMTInterveneWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_mtintervene_word(
        self,
        request: nlp_automl_20190701_models.AddMTInterveneWordRequest,
    ) -> nlp_automl_20190701_models.AddMTInterveneWordResponse:
        """
        @param request: AddMTInterveneWordRequest
        @return: AddMTInterveneWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_mtintervene_word_with_options(request, runtime)

    async def add_mtintervene_word_async(
        self,
        request: nlp_automl_20190701_models.AddMTInterveneWordRequest,
    ) -> nlp_automl_20190701_models.AddMTInterveneWordResponse:
        """
        @param request: AddMTInterveneWordRequest
        @return: AddMTInterveneWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_mtintervene_word_with_options_async(request, runtime)

    def get_predict_doc_with_options(
        self,
        request: nlp_automl_20190701_models.GetPredictDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20190701_models.GetPredictDocResponse:
        """
        @param request: GetPredictDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPredictDocResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_id):
            query['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPredictDoc',
            version='2019-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20190701_models.GetPredictDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_predict_doc_with_options_async(
        self,
        request: nlp_automl_20190701_models.GetPredictDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20190701_models.GetPredictDocResponse:
        """
        @param request: GetPredictDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPredictDocResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_id):
            query['DocId'] = request.doc_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPredictDoc',
            version='2019-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20190701_models.GetPredictDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_predict_doc(
        self,
        request: nlp_automl_20190701_models.GetPredictDocRequest,
    ) -> nlp_automl_20190701_models.GetPredictDocResponse:
        """
        @param request: GetPredictDocRequest
        @return: GetPredictDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_predict_doc_with_options(request, runtime)

    async def get_predict_doc_async(
        self,
        request: nlp_automl_20190701_models.GetPredictDocRequest,
    ) -> nlp_automl_20190701_models.GetPredictDocResponse:
        """
        @param request: GetPredictDocRequest
        @return: GetPredictDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_predict_doc_with_options_async(request, runtime)

    def predict_mtmodel_by_doc_with_options(
        self,
        request: nlp_automl_20190701_models.PredictMTModelByDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20190701_models.PredictMTModelByDocResponse:
        """
        @param request: PredictMTModelByDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PredictMTModelByDocResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.need_xliff):
            query['NeedXLIFF'] = request.need_xliff
        body = {}
        if not UtilClient.is_unset(request.file_content):
            body['FileContent'] = request.file_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PredictMTModelByDoc',
            version='2019-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20190701_models.PredictMTModelByDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def predict_mtmodel_by_doc_with_options_async(
        self,
        request: nlp_automl_20190701_models.PredictMTModelByDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20190701_models.PredictMTModelByDocResponse:
        """
        @param request: PredictMTModelByDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PredictMTModelByDocResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.need_xliff):
            query['NeedXLIFF'] = request.need_xliff
        body = {}
        if not UtilClient.is_unset(request.file_content):
            body['FileContent'] = request.file_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PredictMTModelByDoc',
            version='2019-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20190701_models.PredictMTModelByDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def predict_mtmodel_by_doc(
        self,
        request: nlp_automl_20190701_models.PredictMTModelByDocRequest,
    ) -> nlp_automl_20190701_models.PredictMTModelByDocResponse:
        """
        @param request: PredictMTModelByDocRequest
        @return: PredictMTModelByDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.predict_mtmodel_by_doc_with_options(request, runtime)

    async def predict_mtmodel_by_doc_async(
        self,
        request: nlp_automl_20190701_models.PredictMTModelByDocRequest,
    ) -> nlp_automl_20190701_models.PredictMTModelByDocResponse:
        """
        @param request: PredictMTModelByDocRequest
        @return: PredictMTModelByDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.predict_mtmodel_by_doc_with_options_async(request, runtime)
