# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aiearth_engine20220609 import models as aiearth__engine_20220609_models
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
        self._endpoint = self.get_endpoint('aiearth-engine', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_aijob_with_options(
        self,
        tmp_req: aiearth__engine_20220609_models.CreateAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.CreateAIJobResponse:
        UtilClient.validate_model(tmp_req)
        request = aiearth__engine_20220609_models.CreateAIJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs):
            request.inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        body = {}
        if not UtilClient.is_unset(request.app):
            body['App'] = request.app
        if not UtilClient.is_unset(request.area_threshold):
            body['AreaThreshold'] = request.area_threshold
        if not UtilClient.is_unset(request.confidence):
            body['Confidence'] = request.confidence
        if not UtilClient.is_unset(request.inputs_shrink):
            body['Inputs'] = request.inputs_shrink
        if not UtilClient.is_unset(request.job_name):
            body['JobName'] = request.job_name
        if not UtilClient.is_unset(request.model_project_id):
            body['ModelProjectId'] = request.model_project_id
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.shape_data_id):
            body['ShapeDataId'] = request.shape_data_id
        if not UtilClient.is_unset(request.shape_wkt):
            body['ShapeWkt'] = request.shape_wkt
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAIJob',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.CreateAIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aijob_with_options_async(
        self,
        tmp_req: aiearth__engine_20220609_models.CreateAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.CreateAIJobResponse:
        UtilClient.validate_model(tmp_req)
        request = aiearth__engine_20220609_models.CreateAIJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs):
            request.inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        body = {}
        if not UtilClient.is_unset(request.app):
            body['App'] = request.app
        if not UtilClient.is_unset(request.area_threshold):
            body['AreaThreshold'] = request.area_threshold
        if not UtilClient.is_unset(request.confidence):
            body['Confidence'] = request.confidence
        if not UtilClient.is_unset(request.inputs_shrink):
            body['Inputs'] = request.inputs_shrink
        if not UtilClient.is_unset(request.job_name):
            body['JobName'] = request.job_name
        if not UtilClient.is_unset(request.model_project_id):
            body['ModelProjectId'] = request.model_project_id
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.shape_data_id):
            body['ShapeDataId'] = request.shape_data_id
        if not UtilClient.is_unset(request.shape_wkt):
            body['ShapeWkt'] = request.shape_wkt
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAIJob',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.CreateAIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aijob(
        self,
        request: aiearth__engine_20220609_models.CreateAIJobRequest,
    ) -> aiearth__engine_20220609_models.CreateAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_aijob_with_options(request, runtime)

    async def create_aijob_async(
        self,
        request: aiearth__engine_20220609_models.CreateAIJobRequest,
    ) -> aiearth__engine_20220609_models.CreateAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_aijob_with_options_async(request, runtime)

    def delete_jobs_with_options(
        self,
        tmp_req: aiearth__engine_20220609_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.DeleteJobsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiearth__engine_20220609_models.DeleteJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.DeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_jobs_with_options_async(
        self,
        tmp_req: aiearth__engine_20220609_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.DeleteJobsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiearth__engine_20220609_models.DeleteJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.DeleteJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_jobs(
        self,
        request: aiearth__engine_20220609_models.DeleteJobsRequest,
    ) -> aiearth__engine_20220609_models.DeleteJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_jobs_with_options(request, runtime)

    async def delete_jobs_async(
        self,
        request: aiearth__engine_20220609_models.DeleteJobsRequest,
    ) -> aiearth__engine_20220609_models.DeleteJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_jobs_with_options_async(request, runtime)

    def download_data_with_options(
        self,
        request: aiearth__engine_20220609_models.DownloadDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.DownloadDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.band_no):
            body['BandNo'] = request.band_no
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadData',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.DownloadDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_data_with_options_async(
        self,
        request: aiearth__engine_20220609_models.DownloadDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.DownloadDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.band_no):
            body['BandNo'] = request.band_no
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadData',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.DownloadDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_data(
        self,
        request: aiearth__engine_20220609_models.DownloadDataRequest,
    ) -> aiearth__engine_20220609_models.DownloadDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_data_with_options(request, runtime)

    async def download_data_async(
        self,
        request: aiearth__engine_20220609_models.DownloadDataRequest,
    ) -> aiearth__engine_20220609_models.DownloadDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_data_with_options_async(request, runtime)

    def get_jobs_with_options(
        self,
        tmp_req: aiearth__engine_20220609_models.GetJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.GetJobsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiearth__engine_20220609_models.GetJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobs',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.GetJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_jobs_with_options_async(
        self,
        tmp_req: aiearth__engine_20220609_models.GetJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.GetJobsResponse:
        UtilClient.validate_model(tmp_req)
        request = aiearth__engine_20220609_models.GetJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.job_ids_shrink):
            body['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobs',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.GetJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_jobs(
        self,
        request: aiearth__engine_20220609_models.GetJobsRequest,
    ) -> aiearth__engine_20220609_models.GetJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_jobs_with_options(request, runtime)

    async def get_jobs_async(
        self,
        request: aiearth__engine_20220609_models.GetJobsRequest,
    ) -> aiearth__engine_20220609_models.GetJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_jobs_with_options_async(request, runtime)

    def list_datas_with_options(
        self,
        tmp_req: aiearth__engine_20220609_models.ListDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.ListDatasResponse:
        UtilClient.validate_model(tmp_req)
        request = aiearth__engine_20220609_models.ListDatasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_type_list):
            request.source_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_type_list, 'SourceTypeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.cloudage_max):
            body['CloudageMax'] = request.cloudage_max
        if not UtilClient.is_unset(request.cloudage_min):
            body['CloudageMin'] = request.cloudage_min
        if not UtilClient.is_unset(request.date_end):
            body['DateEnd'] = request.date_end
        if not UtilClient.is_unset(request.date_start):
            body['DateStart'] = request.date_start
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_wkt):
            body['RegionWkt'] = request.region_wkt
        if not UtilClient.is_unset(request.source_type_list_shrink):
            body['SourceTypeList'] = request.source_type_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatas',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.ListDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datas_with_options_async(
        self,
        tmp_req: aiearth__engine_20220609_models.ListDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.ListDatasResponse:
        UtilClient.validate_model(tmp_req)
        request = aiearth__engine_20220609_models.ListDatasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_type_list):
            request.source_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_type_list, 'SourceTypeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.cloudage_max):
            body['CloudageMax'] = request.cloudage_max
        if not UtilClient.is_unset(request.cloudage_min):
            body['CloudageMin'] = request.cloudage_min
        if not UtilClient.is_unset(request.date_end):
            body['DateEnd'] = request.date_end
        if not UtilClient.is_unset(request.date_start):
            body['DateStart'] = request.date_start
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_wkt):
            body['RegionWkt'] = request.region_wkt
        if not UtilClient.is_unset(request.source_type_list_shrink):
            body['SourceTypeList'] = request.source_type_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatas',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.ListDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datas(
        self,
        request: aiearth__engine_20220609_models.ListDatasRequest,
    ) -> aiearth__engine_20220609_models.ListDatasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_datas_with_options(request, runtime)

    async def list_datas_async(
        self,
        request: aiearth__engine_20220609_models.ListDatasRequest,
    ) -> aiearth__engine_20220609_models.ListDatasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_datas_with_options_async(request, runtime)

    def list_user_raster_datas_with_options(
        self,
        request: aiearth__engine_20220609_models.ListUserRasterDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.ListUserRasterDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acquisition_date):
            body['AcquisitionDate'] = request.acquisition_date
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resolution):
            body['Resolution'] = request.resolution
        if not UtilClient.is_unset(request.upload_date):
            body['UploadDate'] = request.upload_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserRasterDatas',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.ListUserRasterDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_raster_datas_with_options_async(
        self,
        request: aiearth__engine_20220609_models.ListUserRasterDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.ListUserRasterDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acquisition_date):
            body['AcquisitionDate'] = request.acquisition_date
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resolution):
            body['Resolution'] = request.resolution
        if not UtilClient.is_unset(request.upload_date):
            body['UploadDate'] = request.upload_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserRasterDatas',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.ListUserRasterDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_raster_datas(
        self,
        request: aiearth__engine_20220609_models.ListUserRasterDatasRequest,
    ) -> aiearth__engine_20220609_models.ListUserRasterDatasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_raster_datas_with_options(request, runtime)

    async def list_user_raster_datas_async(
        self,
        request: aiearth__engine_20220609_models.ListUserRasterDatasRequest,
    ) -> aiearth__engine_20220609_models.ListUserRasterDatasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_raster_datas_with_options_async(request, runtime)

    def list_user_vector_datas_with_options(
        self,
        request: aiearth__engine_20220609_models.ListUserVectorDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.ListUserVectorDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.upload_date):
            body['UploadDate'] = request.upload_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserVectorDatas',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.ListUserVectorDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_vector_datas_with_options_async(
        self,
        request: aiearth__engine_20220609_models.ListUserVectorDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.ListUserVectorDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_type):
            body['FromType'] = request.from_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.upload_date):
            body['UploadDate'] = request.upload_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserVectorDatas',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.ListUserVectorDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_vector_datas(
        self,
        request: aiearth__engine_20220609_models.ListUserVectorDatasRequest,
    ) -> aiearth__engine_20220609_models.ListUserVectorDatasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_vector_datas_with_options(request, runtime)

    async def list_user_vector_datas_async(
        self,
        request: aiearth__engine_20220609_models.ListUserVectorDatasRequest,
    ) -> aiearth__engine_20220609_models.ListUserVectorDatasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_vector_datas_with_options_async(request, runtime)
