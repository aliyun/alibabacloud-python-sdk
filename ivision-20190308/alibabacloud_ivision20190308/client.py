# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ivision20190308 import models as ivision_20190308_models
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
        self._endpoint = self.get_endpoint('ivision', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_face_group_with_options(
        self,
        request: ivision_20190308_models.CreateFaceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.CreateFaceGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.CreateFaceGroupResponse(),
            self.do_rpcrequest('CreateFaceGroup', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_face_group_with_options_async(
        self,
        request: ivision_20190308_models.CreateFaceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.CreateFaceGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.CreateFaceGroupResponse(),
            await self.do_rpcrequest_async('CreateFaceGroup', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_face_group(
        self,
        request: ivision_20190308_models.CreateFaceGroupRequest,
    ) -> ivision_20190308_models.CreateFaceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_face_group_with_options(request, runtime)

    async def create_face_group_async(
        self,
        request: ivision_20190308_models.CreateFaceGroupRequest,
    ) -> ivision_20190308_models.CreateFaceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_face_group_with_options_async(request, runtime)

    def create_file_predict_with_options(
        self,
        request: ivision_20190308_models.CreateFilePredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.CreateFilePredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.CreateFilePredictResponse(),
            self.do_rpcrequest('CreateFilePredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_file_predict_with_options_async(
        self,
        request: ivision_20190308_models.CreateFilePredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.CreateFilePredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.CreateFilePredictResponse(),
            await self.do_rpcrequest_async('CreateFilePredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_file_predict(
        self,
        request: ivision_20190308_models.CreateFilePredictRequest,
    ) -> ivision_20190308_models.CreateFilePredictResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_file_predict_with_options(request, runtime)

    async def create_file_predict_async(
        self,
        request: ivision_20190308_models.CreateFilePredictRequest,
    ) -> ivision_20190308_models.CreateFilePredictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_file_predict_with_options_async(request, runtime)

    def create_stream_predict_with_options(
        self,
        request: ivision_20190308_models.CreateStreamPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.CreateStreamPredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.CreateStreamPredictResponse(),
            self.do_rpcrequest('CreateStreamPredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_stream_predict_with_options_async(
        self,
        request: ivision_20190308_models.CreateStreamPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.CreateStreamPredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.CreateStreamPredictResponse(),
            await self.do_rpcrequest_async('CreateStreamPredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_stream_predict(
        self,
        request: ivision_20190308_models.CreateStreamPredictRequest,
    ) -> ivision_20190308_models.CreateStreamPredictResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_stream_predict_with_options(request, runtime)

    async def create_stream_predict_async(
        self,
        request: ivision_20190308_models.CreateStreamPredictRequest,
    ) -> ivision_20190308_models.CreateStreamPredictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_stream_predict_with_options_async(request, runtime)

    def delete_face_group_with_options(
        self,
        request: ivision_20190308_models.DeleteFaceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DeleteFaceGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.DeleteFaceGroupResponse(),
            self.do_rpcrequest('DeleteFaceGroup', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_face_group_with_options_async(
        self,
        request: ivision_20190308_models.DeleteFaceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DeleteFaceGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.DeleteFaceGroupResponse(),
            await self.do_rpcrequest_async('DeleteFaceGroup', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_face_group(
        self,
        request: ivision_20190308_models.DeleteFaceGroupRequest,
    ) -> ivision_20190308_models.DeleteFaceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_group_with_options(request, runtime)

    async def delete_face_group_async(
        self,
        request: ivision_20190308_models.DeleteFaceGroupRequest,
    ) -> ivision_20190308_models.DeleteFaceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_group_with_options_async(request, runtime)

    def delete_file_predict_with_options(
        self,
        request: ivision_20190308_models.DeleteFilePredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DeleteFilePredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.DeleteFilePredictResponse(),
            self.do_rpcrequest('DeleteFilePredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_file_predict_with_options_async(
        self,
        request: ivision_20190308_models.DeleteFilePredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DeleteFilePredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.DeleteFilePredictResponse(),
            await self.do_rpcrequest_async('DeleteFilePredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_file_predict(
        self,
        request: ivision_20190308_models.DeleteFilePredictRequest,
    ) -> ivision_20190308_models.DeleteFilePredictResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_file_predict_with_options(request, runtime)

    async def delete_file_predict_async(
        self,
        request: ivision_20190308_models.DeleteFilePredictRequest,
    ) -> ivision_20190308_models.DeleteFilePredictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_predict_with_options_async(request, runtime)

    def delete_stream_predict_with_options(
        self,
        request: ivision_20190308_models.DeleteStreamPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DeleteStreamPredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.DeleteStreamPredictResponse(),
            self.do_rpcrequest('DeleteStreamPredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_stream_predict_with_options_async(
        self,
        request: ivision_20190308_models.DeleteStreamPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DeleteStreamPredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.DeleteStreamPredictResponse(),
            await self.do_rpcrequest_async('DeleteStreamPredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_stream_predict(
        self,
        request: ivision_20190308_models.DeleteStreamPredictRequest,
    ) -> ivision_20190308_models.DeleteStreamPredictResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stream_predict_with_options(request, runtime)

    async def delete_stream_predict_async(
        self,
        request: ivision_20190308_models.DeleteStreamPredictRequest,
    ) -> ivision_20190308_models.DeleteStreamPredictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stream_predict_with_options_async(request, runtime)

    def describe_face_groups_with_options(
        self,
        request: ivision_20190308_models.DescribeFaceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DescribeFaceGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.DescribeFaceGroupsResponse(),
            self.do_rpcrequest('DescribeFaceGroups', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_face_groups_with_options_async(
        self,
        request: ivision_20190308_models.DescribeFaceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DescribeFaceGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.DescribeFaceGroupsResponse(),
            await self.do_rpcrequest_async('DescribeFaceGroups', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_face_groups(
        self,
        request: ivision_20190308_models.DescribeFaceGroupsRequest,
    ) -> ivision_20190308_models.DescribeFaceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_face_groups_with_options(request, runtime)

    async def describe_face_groups_async(
        self,
        request: ivision_20190308_models.DescribeFaceGroupsRequest,
    ) -> ivision_20190308_models.DescribeFaceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_face_groups_with_options_async(request, runtime)

    def describe_stream_predict_result_with_options(
        self,
        request: ivision_20190308_models.DescribeStreamPredictResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DescribeStreamPredictResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.DescribeStreamPredictResultResponse(),
            self.do_rpcrequest('DescribeStreamPredictResult', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_stream_predict_result_with_options_async(
        self,
        request: ivision_20190308_models.DescribeStreamPredictResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DescribeStreamPredictResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.DescribeStreamPredictResultResponse(),
            await self.do_rpcrequest_async('DescribeStreamPredictResult', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_stream_predict_result(
        self,
        request: ivision_20190308_models.DescribeStreamPredictResultRequest,
    ) -> ivision_20190308_models.DescribeStreamPredictResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_stream_predict_result_with_options(request, runtime)

    async def describe_stream_predict_result_async(
        self,
        request: ivision_20190308_models.DescribeStreamPredictResultRequest,
    ) -> ivision_20190308_models.DescribeStreamPredictResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_stream_predict_result_with_options_async(request, runtime)

    def describe_stream_predicts_with_options(
        self,
        request: ivision_20190308_models.DescribeStreamPredictsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DescribeStreamPredictsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.DescribeStreamPredictsResponse(),
            self.do_rpcrequest('DescribeStreamPredicts', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_stream_predicts_with_options_async(
        self,
        request: ivision_20190308_models.DescribeStreamPredictsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.DescribeStreamPredictsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.DescribeStreamPredictsResponse(),
            await self.do_rpcrequest_async('DescribeStreamPredicts', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_stream_predicts(
        self,
        request: ivision_20190308_models.DescribeStreamPredictsRequest,
    ) -> ivision_20190308_models.DescribeStreamPredictsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_stream_predicts_with_options(request, runtime)

    async def describe_stream_predicts_async(
        self,
        request: ivision_20190308_models.DescribeStreamPredictsRequest,
    ) -> ivision_20190308_models.DescribeStreamPredictsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_stream_predicts_with_options_async(request, runtime)

    def get_algorithm_detail_with_options(
        self,
        request: ivision_20190308_models.GetAlgorithmDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.GetAlgorithmDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.GetAlgorithmDetailResponse(),
            self.do_rpcrequest('GetAlgorithmDetail', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_algorithm_detail_with_options_async(
        self,
        request: ivision_20190308_models.GetAlgorithmDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.GetAlgorithmDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.GetAlgorithmDetailResponse(),
            await self.do_rpcrequest_async('GetAlgorithmDetail', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_algorithm_detail(
        self,
        request: ivision_20190308_models.GetAlgorithmDetailRequest,
    ) -> ivision_20190308_models.GetAlgorithmDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_detail_with_options(request, runtime)

    async def get_algorithm_detail_async(
        self,
        request: ivision_20190308_models.GetAlgorithmDetailRequest,
    ) -> ivision_20190308_models.GetAlgorithmDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_algorithm_detail_with_options_async(request, runtime)

    def get_algorithm_histograms_with_options(
        self,
        request: ivision_20190308_models.GetAlgorithmHistogramsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.GetAlgorithmHistogramsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.GetAlgorithmHistogramsResponse(),
            self.do_rpcrequest('GetAlgorithmHistograms', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_algorithm_histograms_with_options_async(
        self,
        request: ivision_20190308_models.GetAlgorithmHistogramsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.GetAlgorithmHistogramsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.GetAlgorithmHistogramsResponse(),
            await self.do_rpcrequest_async('GetAlgorithmHistograms', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_algorithm_histograms(
        self,
        request: ivision_20190308_models.GetAlgorithmHistogramsRequest,
    ) -> ivision_20190308_models.GetAlgorithmHistogramsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_histograms_with_options(request, runtime)

    async def get_algorithm_histograms_async(
        self,
        request: ivision_20190308_models.GetAlgorithmHistogramsRequest,
    ) -> ivision_20190308_models.GetAlgorithmHistogramsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_algorithm_histograms_with_options_async(request, runtime)

    def image_predict_with_options(
        self,
        request: ivision_20190308_models.ImagePredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.ImagePredictResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.ImagePredictResponse(),
            self.do_rpcrequest('ImagePredict', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def image_predict_with_options_async(
        self,
        request: ivision_20190308_models.ImagePredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.ImagePredictResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.ImagePredictResponse(),
            await self.do_rpcrequest_async('ImagePredict', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def image_predict(
        self,
        request: ivision_20190308_models.ImagePredictRequest,
    ) -> ivision_20190308_models.ImagePredictResponse:
        runtime = util_models.RuntimeOptions()
        return self.image_predict_with_options(request, runtime)

    async def image_predict_async(
        self,
        request: ivision_20190308_models.ImagePredictRequest,
    ) -> ivision_20190308_models.ImagePredictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.image_predict_with_options_async(request, runtime)

    def list_my_algorithm_with_options(
        self,
        request: ivision_20190308_models.ListMyAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.ListMyAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.ListMyAlgorithmResponse(),
            self.do_rpcrequest('ListMyAlgorithm', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_my_algorithm_with_options_async(
        self,
        request: ivision_20190308_models.ListMyAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.ListMyAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.ListMyAlgorithmResponse(),
            await self.do_rpcrequest_async('ListMyAlgorithm', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_my_algorithm(
        self,
        request: ivision_20190308_models.ListMyAlgorithmRequest,
    ) -> ivision_20190308_models.ListMyAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_my_algorithm_with_options(request, runtime)

    async def list_my_algorithm_async(
        self,
        request: ivision_20190308_models.ListMyAlgorithmRequest,
    ) -> ivision_20190308_models.ListMyAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_my_algorithm_with_options_async(request, runtime)

    def predict_picture_with_options(
        self,
        request: ivision_20190308_models.PredictPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.PredictPictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.PredictPictureResponse(),
            self.do_rpcrequest('PredictPicture', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def predict_picture_with_options_async(
        self,
        request: ivision_20190308_models.PredictPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.PredictPictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.PredictPictureResponse(),
            await self.do_rpcrequest_async('PredictPicture', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def predict_picture(
        self,
        request: ivision_20190308_models.PredictPictureRequest,
    ) -> ivision_20190308_models.PredictPictureResponse:
        runtime = util_models.RuntimeOptions()
        return self.predict_picture_with_options(request, runtime)

    async def predict_picture_async(
        self,
        request: ivision_20190308_models.PredictPictureRequest,
    ) -> ivision_20190308_models.PredictPictureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.predict_picture_with_options_async(request, runtime)

    def register_face_with_options(
        self,
        request: ivision_20190308_models.RegisterFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.RegisterFaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.RegisterFaceResponse(),
            self.do_rpcrequest('RegisterFace', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def register_face_with_options_async(
        self,
        request: ivision_20190308_models.RegisterFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.RegisterFaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.RegisterFaceResponse(),
            await self.do_rpcrequest_async('RegisterFace', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def register_face(
        self,
        request: ivision_20190308_models.RegisterFaceRequest,
    ) -> ivision_20190308_models.RegisterFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_face_with_options(request, runtime)

    async def register_face_async(
        self,
        request: ivision_20190308_models.RegisterFaceRequest,
    ) -> ivision_20190308_models.RegisterFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_face_with_options_async(request, runtime)

    def search_face_with_options(
        self,
        request: ivision_20190308_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.SearchFaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.SearchFaceResponse(),
            self.do_rpcrequest('SearchFace', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def search_face_with_options_async(
        self,
        request: ivision_20190308_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.SearchFaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.SearchFaceResponse(),
            await self.do_rpcrequest_async('SearchFace', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def search_face(
        self,
        request: ivision_20190308_models.SearchFaceRequest,
    ) -> ivision_20190308_models.SearchFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_face_with_options(request, runtime)

    async def search_face_async(
        self,
        request: ivision_20190308_models.SearchFaceRequest,
    ) -> ivision_20190308_models.SearchFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_face_with_options_async(request, runtime)

    def start_stream_predict_with_options(
        self,
        request: ivision_20190308_models.StartStreamPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.StartStreamPredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.StartStreamPredictResponse(),
            self.do_rpcrequest('StartStreamPredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_stream_predict_with_options_async(
        self,
        request: ivision_20190308_models.StartStreamPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.StartStreamPredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.StartStreamPredictResponse(),
            await self.do_rpcrequest_async('StartStreamPredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_stream_predict(
        self,
        request: ivision_20190308_models.StartStreamPredictRequest,
    ) -> ivision_20190308_models.StartStreamPredictResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_stream_predict_with_options(request, runtime)

    async def start_stream_predict_async(
        self,
        request: ivision_20190308_models.StartStreamPredictRequest,
    ) -> ivision_20190308_models.StartStreamPredictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_stream_predict_with_options_async(request, runtime)

    def stop_stream_predict_with_options(
        self,
        request: ivision_20190308_models.StopStreamPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.StopStreamPredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.StopStreamPredictResponse(),
            self.do_rpcrequest('StopStreamPredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_stream_predict_with_options_async(
        self,
        request: ivision_20190308_models.StopStreamPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.StopStreamPredictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ivision_20190308_models.StopStreamPredictResponse(),
            await self.do_rpcrequest_async('StopStreamPredict', '2019-03-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_stream_predict(
        self,
        request: ivision_20190308_models.StopStreamPredictRequest,
    ) -> ivision_20190308_models.StopStreamPredictResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_stream_predict_with_options(request, runtime)

    async def stop_stream_predict_async(
        self,
        request: ivision_20190308_models.StopStreamPredictRequest,
    ) -> ivision_20190308_models.StopStreamPredictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_stream_predict_with_options_async(request, runtime)

    def unregister_face_with_options(
        self,
        request: ivision_20190308_models.UnregisterFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.UnregisterFaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.UnregisterFaceResponse(),
            self.do_rpcrequest('UnregisterFace', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def unregister_face_with_options_async(
        self,
        request: ivision_20190308_models.UnregisterFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivision_20190308_models.UnregisterFaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ivision_20190308_models.UnregisterFaceResponse(),
            await self.do_rpcrequest_async('UnregisterFace', '2019-03-08', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def unregister_face(
        self,
        request: ivision_20190308_models.UnregisterFaceRequest,
    ) -> ivision_20190308_models.UnregisterFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unregister_face_with_options(request, runtime)

    async def unregister_face_async(
        self,
        request: ivision_20190308_models.UnregisterFaceRequest,
    ) -> ivision_20190308_models.UnregisterFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unregister_face_with_options_async(request, runtime)
