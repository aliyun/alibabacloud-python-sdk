# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imm20200930 import models as imm_20200930_models
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
            'cn-beijing-gov-1': 'imm-vpc.cn-beijing-gov-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('imm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_image_mosaic_with_options(
        self,
        tmp_req: imm_20200930_models.AddImageMosaicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AddImageMosaicResponse:
        """
        @summary Adds mosaics, Gaussian blurs, or solid color shapes to blur one or more areas of an image for privacy protection and saves the output image to the specified path in Object Storage Service (OSS).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        The operation accepts JPG and PNG images with a maximum side length of 30,000 pixels and a total of up to 250 million pixels.
        
        @param tmp_req: AddImageMosaicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageMosaicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.AddImageMosaicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.image_format):
            query['ImageFormat'] = request.image_format
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddImageMosaic',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AddImageMosaicResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_mosaic_with_options_async(
        self,
        tmp_req: imm_20200930_models.AddImageMosaicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AddImageMosaicResponse:
        """
        @summary Adds mosaics, Gaussian blurs, or solid color shapes to blur one or more areas of an image for privacy protection and saves the output image to the specified path in Object Storage Service (OSS).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        The operation accepts JPG and PNG images with a maximum side length of 30,000 pixels and a total of up to 250 million pixels.
        
        @param tmp_req: AddImageMosaicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageMosaicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.AddImageMosaicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.image_format):
            query['ImageFormat'] = request.image_format
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddImageMosaic',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AddImageMosaicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image_mosaic(
        self,
        request: imm_20200930_models.AddImageMosaicRequest,
    ) -> imm_20200930_models.AddImageMosaicResponse:
        """
        @summary Adds mosaics, Gaussian blurs, or solid color shapes to blur one or more areas of an image for privacy protection and saves the output image to the specified path in Object Storage Service (OSS).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        The operation accepts JPG and PNG images with a maximum side length of 30,000 pixels and a total of up to 250 million pixels.
        
        @param request: AddImageMosaicRequest
        @return: AddImageMosaicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_image_mosaic_with_options(request, runtime)

    async def add_image_mosaic_async(
        self,
        request: imm_20200930_models.AddImageMosaicRequest,
    ) -> imm_20200930_models.AddImageMosaicResponse:
        """
        @summary Adds mosaics, Gaussian blurs, or solid color shapes to blur one or more areas of an image for privacy protection and saves the output image to the specified path in Object Storage Service (OSS).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        The operation accepts JPG and PNG images with a maximum side length of 30,000 pixels and a total of up to 250 million pixels.
        
        @param request: AddImageMosaicRequest
        @return: AddImageMosaicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_image_mosaic_with_options_async(request, runtime)

    def add_story_files_with_options(
        self,
        tmp_req: imm_20200930_models.AddStoryFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AddStoryFilesResponse:
        """
        @summary Adds objects to a story.
        
        @param tmp_req: AddStoryFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddStoryFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.AddStoryFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddStoryFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AddStoryFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_story_files_with_options_async(
        self,
        tmp_req: imm_20200930_models.AddStoryFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AddStoryFilesResponse:
        """
        @summary Adds objects to a story.
        
        @param tmp_req: AddStoryFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddStoryFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.AddStoryFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddStoryFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AddStoryFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_story_files(
        self,
        request: imm_20200930_models.AddStoryFilesRequest,
    ) -> imm_20200930_models.AddStoryFilesResponse:
        """
        @summary Adds objects to a story.
        
        @param request: AddStoryFilesRequest
        @return: AddStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_story_files_with_options(request, runtime)

    async def add_story_files_async(
        self,
        request: imm_20200930_models.AddStoryFilesRequest,
    ) -> imm_20200930_models.AddStoryFilesResponse:
        """
        @summary Adds objects to a story.
        
        @param request: AddStoryFilesRequest
        @return: AddStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_story_files_with_options_async(request, runtime)

    def attach_ossbucket_with_options(
        self,
        request: imm_20200930_models.AttachOSSBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AttachOSSBucketResponse:
        """
        @summary Binds an Object Storage Service (OSS) bucket to the specified project. The binding enables you to use IMM features by using the x-oss-process parameter.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        To use data processing capabilities of IMM based on the x-oss-process parameter, you must bind an OSS bucket to an IMM project. For more information, see [x-oss-process](https://help.aliyun.com/document_detail/2391270.html).
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        
        @param request: AttachOSSBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachOSSBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachOSSBucket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AttachOSSBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_ossbucket_with_options_async(
        self,
        request: imm_20200930_models.AttachOSSBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AttachOSSBucketResponse:
        """
        @summary Binds an Object Storage Service (OSS) bucket to the specified project. The binding enables you to use IMM features by using the x-oss-process parameter.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        To use data processing capabilities of IMM based on the x-oss-process parameter, you must bind an OSS bucket to an IMM project. For more information, see [x-oss-process](https://help.aliyun.com/document_detail/2391270.html).
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        
        @param request: AttachOSSBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachOSSBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachOSSBucket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AttachOSSBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_ossbucket(
        self,
        request: imm_20200930_models.AttachOSSBucketRequest,
    ) -> imm_20200930_models.AttachOSSBucketResponse:
        """
        @summary Binds an Object Storage Service (OSS) bucket to the specified project. The binding enables you to use IMM features by using the x-oss-process parameter.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        To use data processing capabilities of IMM based on the x-oss-process parameter, you must bind an OSS bucket to an IMM project. For more information, see [x-oss-process](https://help.aliyun.com/document_detail/2391270.html).
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        
        @param request: AttachOSSBucketRequest
        @return: AttachOSSBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_ossbucket_with_options(request, runtime)

    async def attach_ossbucket_async(
        self,
        request: imm_20200930_models.AttachOSSBucketRequest,
    ) -> imm_20200930_models.AttachOSSBucketResponse:
        """
        @summary Binds an Object Storage Service (OSS) bucket to the specified project. The binding enables you to use IMM features by using the x-oss-process parameter.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        To use data processing capabilities of IMM based on the x-oss-process parameter, you must bind an OSS bucket to an IMM project. For more information, see [x-oss-process](https://help.aliyun.com/document_detail/2391270.html).
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        
        @param request: AttachOSSBucketRequest
        @return: AttachOSSBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_ossbucket_with_options_async(request, runtime)

    def batch_delete_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchDeleteFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchDeleteFileMetaResponse:
        """
        @summary Deletes the metadata of multiple files from a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        A successful deletion message is returned regardless of whether the metadata of the file exists in the dataset.
        >
        If you delete the metadata of a file from a dataset, the file stored in Object Storage Service (OSS) or Photo and Drive Service is **not** deleted. If you want to delete the file, use the operations provided by OSS or Photo and Drive Service.
        Metadata deletion affects existing face groups and stories but does not affect existing spatiotemporal groups.
        
        @param tmp_req: BatchDeleteFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchDeleteFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchDeleteFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.BatchDeleteFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchDeleteFileMetaResponse:
        """
        @summary Deletes the metadata of multiple files from a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        A successful deletion message is returned regardless of whether the metadata of the file exists in the dataset.
        >
        If you delete the metadata of a file from a dataset, the file stored in Object Storage Service (OSS) or Photo and Drive Service is **not** deleted. If you want to delete the file, use the operations provided by OSS or Photo and Drive Service.
        Metadata deletion affects existing face groups and stories but does not affect existing spatiotemporal groups.
        
        @param tmp_req: BatchDeleteFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchDeleteFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchDeleteFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_file_meta(
        self,
        request: imm_20200930_models.BatchDeleteFileMetaRequest,
    ) -> imm_20200930_models.BatchDeleteFileMetaResponse:
        """
        @summary Deletes the metadata of multiple files from a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        A successful deletion message is returned regardless of whether the metadata of the file exists in the dataset.
        >
        If you delete the metadata of a file from a dataset, the file stored in Object Storage Service (OSS) or Photo and Drive Service is **not** deleted. If you want to delete the file, use the operations provided by OSS or Photo and Drive Service.
        Metadata deletion affects existing face groups and stories but does not affect existing spatiotemporal groups.
        
        @param request: BatchDeleteFileMetaRequest
        @return: BatchDeleteFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_file_meta_with_options(request, runtime)

    async def batch_delete_file_meta_async(
        self,
        request: imm_20200930_models.BatchDeleteFileMetaRequest,
    ) -> imm_20200930_models.BatchDeleteFileMetaResponse:
        """
        @summary Deletes the metadata of multiple files from a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        A successful deletion message is returned regardless of whether the metadata of the file exists in the dataset.
        >
        If you delete the metadata of a file from a dataset, the file stored in Object Storage Service (OSS) or Photo and Drive Service is **not** deleted. If you want to delete the file, use the operations provided by OSS or Photo and Drive Service.
        Metadata deletion affects existing face groups and stories but does not affect existing spatiotemporal groups.
        
        @param request: BatchDeleteFileMetaRequest
        @return: BatchDeleteFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_file_meta_with_options_async(request, runtime)

    def batch_get_figure_cluster_with_options(
        self,
        tmp_req: imm_20200930_models.BatchGetFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchGetFigureClusterResponse:
        """
        @summary Queries face clusters.
        
        @param tmp_req: BatchGetFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.object_ids):
            request.object_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_ids_shrink):
            query['ObjectIds'] = request.object_ids_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_figure_cluster_with_options_async(
        self,
        tmp_req: imm_20200930_models.BatchGetFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchGetFigureClusterResponse:
        """
        @summary Queries face clusters.
        
        @param tmp_req: BatchGetFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.object_ids):
            request.object_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_ids_shrink):
            query['ObjectIds'] = request.object_ids_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_figure_cluster(
        self,
        request: imm_20200930_models.BatchGetFigureClusterRequest,
    ) -> imm_20200930_models.BatchGetFigureClusterResponse:
        """
        @summary Queries face clusters.
        
        @param request: BatchGetFigureClusterRequest
        @return: BatchGetFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_get_figure_cluster_with_options(request, runtime)

    async def batch_get_figure_cluster_async(
        self,
        request: imm_20200930_models.BatchGetFigureClusterRequest,
    ) -> imm_20200930_models.BatchGetFigureClusterResponse:
        """
        @summary Queries face clusters.
        
        @param request: BatchGetFigureClusterRequest
        @return: BatchGetFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_figure_cluster_with_options_async(request, runtime)

    def batch_get_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchGetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchGetFileMetaResponse:
        """
        @summary Queries metadata of multiple objects or files in the specified dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, feel free to join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        
        @param tmp_req: BatchGetFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.BatchGetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchGetFileMetaResponse:
        """
        @summary Queries metadata of multiple objects or files in the specified dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, feel free to join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        
        @param tmp_req: BatchGetFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_file_meta(
        self,
        request: imm_20200930_models.BatchGetFileMetaRequest,
    ) -> imm_20200930_models.BatchGetFileMetaResponse:
        """
        @summary Queries metadata of multiple objects or files in the specified dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, feel free to join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        
        @param request: BatchGetFileMetaRequest
        @return: BatchGetFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_get_file_meta_with_options(request, runtime)

    async def batch_get_file_meta_async(
        self,
        request: imm_20200930_models.BatchGetFileMetaRequest,
    ) -> imm_20200930_models.BatchGetFileMetaResponse:
        """
        @summary Queries metadata of multiple objects or files in the specified dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, feel free to join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        
        @param request: BatchGetFileMetaRequest
        @return: BatchGetFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_file_meta_with_options_async(request, runtime)

    def batch_index_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchIndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchIndexFileMetaResponse:
        """
        @summary Indexes metadata of multiple objects into the specified dataset. The process involves data processing operations such as label detection, face detection, and location detection. Metadata indexing helps meet diverse data retrieval requirements.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Data processing operations supported for metadata processing vary with workflow templates. For more information, see [Workflow templates and operators](https://help.aliyun.com/document_detail/466304.html).
        Metadata indexing poses limits on the total number and size of objects. For more information about these limits, see [Limits](https://help.aliyun.com/document_detail/475569.html). For more information about how to create
        Metadata indexing is available in specific regions. For information about regions that support metadata indexing, see the "Data management and indexing" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic.
        
        @param tmp_req: BatchIndexFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchIndexFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchIndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchIndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchIndexFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_index_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.BatchIndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchIndexFileMetaResponse:
        """
        @summary Indexes metadata of multiple objects into the specified dataset. The process involves data processing operations such as label detection, face detection, and location detection. Metadata indexing helps meet diverse data retrieval requirements.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Data processing operations supported for metadata processing vary with workflow templates. For more information, see [Workflow templates and operators](https://help.aliyun.com/document_detail/466304.html).
        Metadata indexing poses limits on the total number and size of objects. For more information about these limits, see [Limits](https://help.aliyun.com/document_detail/475569.html). For more information about how to create
        Metadata indexing is available in specific regions. For information about regions that support metadata indexing, see the "Data management and indexing" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic.
        
        @param tmp_req: BatchIndexFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchIndexFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchIndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchIndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchIndexFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_index_file_meta(
        self,
        request: imm_20200930_models.BatchIndexFileMetaRequest,
    ) -> imm_20200930_models.BatchIndexFileMetaResponse:
        """
        @summary Indexes metadata of multiple objects into the specified dataset. The process involves data processing operations such as label detection, face detection, and location detection. Metadata indexing helps meet diverse data retrieval requirements.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Data processing operations supported for metadata processing vary with workflow templates. For more information, see [Workflow templates and operators](https://help.aliyun.com/document_detail/466304.html).
        Metadata indexing poses limits on the total number and size of objects. For more information about these limits, see [Limits](https://help.aliyun.com/document_detail/475569.html). For more information about how to create
        Metadata indexing is available in specific regions. For information about regions that support metadata indexing, see the "Data management and indexing" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic.
        
        @param request: BatchIndexFileMetaRequest
        @return: BatchIndexFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_index_file_meta_with_options(request, runtime)

    async def batch_index_file_meta_async(
        self,
        request: imm_20200930_models.BatchIndexFileMetaRequest,
    ) -> imm_20200930_models.BatchIndexFileMetaResponse:
        """
        @summary Indexes metadata of multiple objects into the specified dataset. The process involves data processing operations such as label detection, face detection, and location detection. Metadata indexing helps meet diverse data retrieval requirements.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Data processing operations supported for metadata processing vary with workflow templates. For more information, see [Workflow templates and operators](https://help.aliyun.com/document_detail/466304.html).
        Metadata indexing poses limits on the total number and size of objects. For more information about these limits, see [Limits](https://help.aliyun.com/document_detail/475569.html). For more information about how to create
        Metadata indexing is available in specific regions. For information about regions that support metadata indexing, see the "Data management and indexing" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic.
        
        @param request: BatchIndexFileMetaRequest
        @return: BatchIndexFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_index_file_meta_with_options_async(request, runtime)

    def batch_update_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchUpdateFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchUpdateFileMetaResponse:
        """
        @summary Updates some metadata items of files indexed into a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        You cannot call this operation to update all metadata. You can update only metadata fields such as CustomLabels, CustomId, and Figures. For more information, see the "Request parameters" section of this topic.
        
        @param tmp_req: BatchUpdateFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchUpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchUpdateFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.BatchUpdateFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchUpdateFileMetaResponse:
        """
        @summary Updates some metadata items of files indexed into a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        You cannot call this operation to update all metadata. You can update only metadata fields such as CustomLabels, CustomId, and Figures. For more information, see the "Request parameters" section of this topic.
        
        @param tmp_req: BatchUpdateFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchUpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchUpdateFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_file_meta(
        self,
        request: imm_20200930_models.BatchUpdateFileMetaRequest,
    ) -> imm_20200930_models.BatchUpdateFileMetaResponse:
        """
        @summary Updates some metadata items of files indexed into a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        You cannot call this operation to update all metadata. You can update only metadata fields such as CustomLabels, CustomId, and Figures. For more information, see the "Request parameters" section of this topic.
        
        @param request: BatchUpdateFileMetaRequest
        @return: BatchUpdateFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_update_file_meta_with_options(request, runtime)

    async def batch_update_file_meta_async(
        self,
        request: imm_20200930_models.BatchUpdateFileMetaRequest,
    ) -> imm_20200930_models.BatchUpdateFileMetaResponse:
        """
        @summary Updates some metadata items of files indexed into a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        You cannot call this operation to update all metadata. You can update only metadata fields such as CustomLabels, CustomId, and Figures. For more information, see the "Request parameters" section of this topic.
        
        @param request: BatchUpdateFileMetaRequest
        @return: BatchUpdateFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_update_file_meta_with_options_async(request, runtime)

    def compare_image_faces_with_options(
        self,
        tmp_req: imm_20200930_models.CompareImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CompareImageFacesResponse:
        """
        @summary Compares the similarity of the largest faces in two images. The largest face refers to the largest face frame in an image after face detection.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        For the input image, only the face with the largest face frame in the image is used for face comparison. The face frame detection result is consistent with the responses of the [DetectImageFaces](https://help.aliyun.com/document_detail/478213.html) operation.
        
        @param tmp_req: CompareImageFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareImageFacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CompareImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_shrink):
            query['Source'] = request.source_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompareImageFaces',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CompareImageFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_image_faces_with_options_async(
        self,
        tmp_req: imm_20200930_models.CompareImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CompareImageFacesResponse:
        """
        @summary Compares the similarity of the largest faces in two images. The largest face refers to the largest face frame in an image after face detection.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        For the input image, only the face with the largest face frame in the image is used for face comparison. The face frame detection result is consistent with the responses of the [DetectImageFaces](https://help.aliyun.com/document_detail/478213.html) operation.
        
        @param tmp_req: CompareImageFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareImageFacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CompareImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_shrink):
            query['Source'] = request.source_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompareImageFaces',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CompareImageFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_image_faces(
        self,
        request: imm_20200930_models.CompareImageFacesRequest,
    ) -> imm_20200930_models.CompareImageFacesResponse:
        """
        @summary Compares the similarity of the largest faces in two images. The largest face refers to the largest face frame in an image after face detection.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        For the input image, only the face with the largest face frame in the image is used for face comparison. The face frame detection result is consistent with the responses of the [DetectImageFaces](https://help.aliyun.com/document_detail/478213.html) operation.
        
        @param request: CompareImageFacesRequest
        @return: CompareImageFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.compare_image_faces_with_options(request, runtime)

    async def compare_image_faces_async(
        self,
        request: imm_20200930_models.CompareImageFacesRequest,
    ) -> imm_20200930_models.CompareImageFacesResponse:
        """
        @summary Compares the similarity of the largest faces in two images. The largest face refers to the largest face frame in an image after face detection.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        For the input image, only the face with the largest face frame in the image is used for face comparison. The face frame detection result is consistent with the responses of the [DetectImageFaces](https://help.aliyun.com/document_detail/478213.html) operation.
        
        @param request: CompareImageFacesRequest
        @return: CompareImageFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.compare_image_faces_with_options_async(request, runtime)

    def contextual_answer_with_options(
        self,
        tmp_req: imm_20200930_models.ContextualAnswerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ContextualAnswerResponse:
        """
        @summary AI 助手二期，问答API
        
        @param tmp_req: ContextualAnswerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContextualAnswerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ContextualAnswerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not UtilClient.is_unset(tmp_req.messages):
            request.messages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.messages, 'Messages', 'json')
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.messages_shrink):
            body['Messages'] = request.messages_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContextualAnswer',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ContextualAnswerResponse(),
            self.call_api(params, req, runtime)
        )

    async def contextual_answer_with_options_async(
        self,
        tmp_req: imm_20200930_models.ContextualAnswerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ContextualAnswerResponse:
        """
        @summary AI 助手二期，问答API
        
        @param tmp_req: ContextualAnswerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContextualAnswerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ContextualAnswerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not UtilClient.is_unset(tmp_req.messages):
            request.messages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.messages, 'Messages', 'json')
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.messages_shrink):
            body['Messages'] = request.messages_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContextualAnswer',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ContextualAnswerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def contextual_answer(
        self,
        request: imm_20200930_models.ContextualAnswerRequest,
    ) -> imm_20200930_models.ContextualAnswerResponse:
        """
        @summary AI 助手二期，问答API
        
        @param request: ContextualAnswerRequest
        @return: ContextualAnswerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.contextual_answer_with_options(request, runtime)

    async def contextual_answer_async(
        self,
        request: imm_20200930_models.ContextualAnswerRequest,
    ) -> imm_20200930_models.ContextualAnswerResponse:
        """
        @summary AI 助手二期，问答API
        
        @param request: ContextualAnswerRequest
        @return: ContextualAnswerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.contextual_answer_with_options_async(request, runtime)

    def contextual_retrieval_with_options(
        self,
        tmp_req: imm_20200930_models.ContextualRetrievalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ContextualRetrievalResponse:
        """
        @summary AI助手二期，检索API
        
        @param tmp_req: ContextualRetrievalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContextualRetrievalResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ContextualRetrievalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.messages):
            request.messages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.messages, 'Messages', 'json')
        if not UtilClient.is_unset(tmp_req.smart_cluster_ids):
            request.smart_cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.smart_cluster_ids, 'SmartClusterIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.recall_only):
            query['RecallOnly'] = request.recall_only
        body = {}
        if not UtilClient.is_unset(request.messages_shrink):
            body['Messages'] = request.messages_shrink
        if not UtilClient.is_unset(request.smart_cluster_ids_shrink):
            body['SmartClusterIds'] = request.smart_cluster_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContextualRetrieval',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ContextualRetrievalResponse(),
            self.call_api(params, req, runtime)
        )

    async def contextual_retrieval_with_options_async(
        self,
        tmp_req: imm_20200930_models.ContextualRetrievalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ContextualRetrievalResponse:
        """
        @summary AI助手二期，检索API
        
        @param tmp_req: ContextualRetrievalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContextualRetrievalResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ContextualRetrievalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.messages):
            request.messages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.messages, 'Messages', 'json')
        if not UtilClient.is_unset(tmp_req.smart_cluster_ids):
            request.smart_cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.smart_cluster_ids, 'SmartClusterIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.recall_only):
            query['RecallOnly'] = request.recall_only
        body = {}
        if not UtilClient.is_unset(request.messages_shrink):
            body['Messages'] = request.messages_shrink
        if not UtilClient.is_unset(request.smart_cluster_ids_shrink):
            body['SmartClusterIds'] = request.smart_cluster_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContextualRetrieval',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ContextualRetrievalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def contextual_retrieval(
        self,
        request: imm_20200930_models.ContextualRetrievalRequest,
    ) -> imm_20200930_models.ContextualRetrievalResponse:
        """
        @summary AI助手二期，检索API
        
        @param request: ContextualRetrievalRequest
        @return: ContextualRetrievalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.contextual_retrieval_with_options(request, runtime)

    async def contextual_retrieval_async(
        self,
        request: imm_20200930_models.ContextualRetrievalRequest,
    ) -> imm_20200930_models.ContextualRetrievalResponse:
        """
        @summary AI助手二期，检索API
        
        @param request: ContextualRetrievalRequest
        @return: ContextualRetrievalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.contextual_retrieval_with_options_async(request, runtime)

    def create_archive_file_inspection_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateArchiveFileInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateArchiveFileInspectionTaskResponse:
        """
        @summary Creates an archive file inspection task to preview the files in a package without decompressing the package.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk chat group (ID: 31690030817) and share your questions with us.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports a package that contains up to 80,000 files.
        The operation supports ZIP or RAR packages up to 200 GB in size, or 7z packages up to 50 GB in size.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateArchiveFileInspectionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateArchiveFileInspectionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateArchiveFileInspectionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateArchiveFileInspectionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateArchiveFileInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_archive_file_inspection_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateArchiveFileInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateArchiveFileInspectionTaskResponse:
        """
        @summary Creates an archive file inspection task to preview the files in a package without decompressing the package.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk chat group (ID: 31690030817) and share your questions with us.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports a package that contains up to 80,000 files.
        The operation supports ZIP or RAR packages up to 200 GB in size, or 7z packages up to 50 GB in size.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateArchiveFileInspectionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateArchiveFileInspectionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateArchiveFileInspectionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateArchiveFileInspectionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateArchiveFileInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_archive_file_inspection_task(
        self,
        request: imm_20200930_models.CreateArchiveFileInspectionTaskRequest,
    ) -> imm_20200930_models.CreateArchiveFileInspectionTaskResponse:
        """
        @summary Creates an archive file inspection task to preview the files in a package without decompressing the package.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk chat group (ID: 31690030817) and share your questions with us.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports a package that contains up to 80,000 files.
        The operation supports ZIP or RAR packages up to 200 GB in size, or 7z packages up to 50 GB in size.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateArchiveFileInspectionTaskRequest
        @return: CreateArchiveFileInspectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_archive_file_inspection_task_with_options(request, runtime)

    async def create_archive_file_inspection_task_async(
        self,
        request: imm_20200930_models.CreateArchiveFileInspectionTaskRequest,
    ) -> imm_20200930_models.CreateArchiveFileInspectionTaskResponse:
        """
        @summary Creates an archive file inspection task to preview the files in a package without decompressing the package.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk chat group (ID: 31690030817) and share your questions with us.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports a package that contains up to 80,000 files.
        The operation supports ZIP or RAR packages up to 200 GB in size, or 7z packages up to 50 GB in size.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateArchiveFileInspectionTaskRequest
        @return: CreateArchiveFileInspectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_archive_file_inspection_task_with_options_async(request, runtime)

    def create_batch_with_options(
        self,
        tmp_req: imm_20200930_models.CreateBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateBatchResponse:
        """
        @summary Creates a batch processing task to perform a data processing operation, such as transcoding or format conversion, on multiple existing files at a time.
        
        @description If you want to create a batch processing task to process data in [OSS](https://help.aliyun.com/document_detail/99372.html), make sure that you have bound the dataset to the OSS bucket where the data is stored. For more information about how to bind a dataset to a bucket, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param tmp_req: CreateBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            body['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateBatchResponse:
        """
        @summary Creates a batch processing task to perform a data processing operation, such as transcoding or format conversion, on multiple existing files at a time.
        
        @description If you want to create a batch processing task to process data in [OSS](https://help.aliyun.com/document_detail/99372.html), make sure that you have bound the dataset to the OSS bucket where the data is stored. For more information about how to bind a dataset to a bucket, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param tmp_req: CreateBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            body['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch(
        self,
        request: imm_20200930_models.CreateBatchRequest,
    ) -> imm_20200930_models.CreateBatchResponse:
        """
        @summary Creates a batch processing task to perform a data processing operation, such as transcoding or format conversion, on multiple existing files at a time.
        
        @description If you want to create a batch processing task to process data in [OSS](https://help.aliyun.com/document_detail/99372.html), make sure that you have bound the dataset to the OSS bucket where the data is stored. For more information about how to bind a dataset to a bucket, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: CreateBatchRequest
        @return: CreateBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_batch_with_options(request, runtime)

    async def create_batch_async(
        self,
        request: imm_20200930_models.CreateBatchRequest,
    ) -> imm_20200930_models.CreateBatchResponse:
        """
        @summary Creates a batch processing task to perform a data processing operation, such as transcoding or format conversion, on multiple existing files at a time.
        
        @description If you want to create a batch processing task to process data in [OSS](https://help.aliyun.com/document_detail/99372.html), make sure that you have bound the dataset to the OSS bucket where the data is stored. For more information about how to bind a dataset to a bucket, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: CreateBatchRequest
        @return: CreateBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_batch_with_options_async(request, runtime)

    def create_binding_with_options(
        self,
        request: imm_20200930_models.CreateBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateBindingResponse:
        """
        @summary Creates a binding relationship between a dataset and an Object Storage Service (OSS) bucket. This allows for the automatic synchronization of incremental and full data and indexing.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).***\
        Before you create a binding relationship, make sure that the project and the dataset that you want to use exist.
        For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For information about how to create a dataset, see [CreateDataset](https://help.aliyun.com/document_detail/478160.html).
        >  The CreateBinding operation works by using the [workflow template](https://help.aliyun.com/document_detail/466304.html) that is specified when you created the project or dataset.
        After you create a binding relationship between a dataset and an OSS bucket, IMM scans the existing objects in the bucket and extracts metadata based on the scanning result. Then, IMM creates an index from the extracted metadata. If new objects are added to the OSS bucket, IMM constantly tracks and scans the objects and updates the index. For objects whose index is created in this way, you can call the [SimpleQuery](https://help.aliyun.com/document_detail/478175.html) operation to query, manage, and collect statistics from the objects.
        
        @param request: CreateBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_binding_with_options_async(
        self,
        request: imm_20200930_models.CreateBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateBindingResponse:
        """
        @summary Creates a binding relationship between a dataset and an Object Storage Service (OSS) bucket. This allows for the automatic synchronization of incremental and full data and indexing.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).***\
        Before you create a binding relationship, make sure that the project and the dataset that you want to use exist.
        For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For information about how to create a dataset, see [CreateDataset](https://help.aliyun.com/document_detail/478160.html).
        >  The CreateBinding operation works by using the [workflow template](https://help.aliyun.com/document_detail/466304.html) that is specified when you created the project or dataset.
        After you create a binding relationship between a dataset and an OSS bucket, IMM scans the existing objects in the bucket and extracts metadata based on the scanning result. Then, IMM creates an index from the extracted metadata. If new objects are added to the OSS bucket, IMM constantly tracks and scans the objects and updates the index. For objects whose index is created in this way, you can call the [SimpleQuery](https://help.aliyun.com/document_detail/478175.html) operation to query, manage, and collect statistics from the objects.
        
        @param request: CreateBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_binding(
        self,
        request: imm_20200930_models.CreateBindingRequest,
    ) -> imm_20200930_models.CreateBindingResponse:
        """
        @summary Creates a binding relationship between a dataset and an Object Storage Service (OSS) bucket. This allows for the automatic synchronization of incremental and full data and indexing.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).***\
        Before you create a binding relationship, make sure that the project and the dataset that you want to use exist.
        For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For information about how to create a dataset, see [CreateDataset](https://help.aliyun.com/document_detail/478160.html).
        >  The CreateBinding operation works by using the [workflow template](https://help.aliyun.com/document_detail/466304.html) that is specified when you created the project or dataset.
        After you create a binding relationship between a dataset and an OSS bucket, IMM scans the existing objects in the bucket and extracts metadata based on the scanning result. Then, IMM creates an index from the extracted metadata. If new objects are added to the OSS bucket, IMM constantly tracks and scans the objects and updates the index. For objects whose index is created in this way, you can call the [SimpleQuery](https://help.aliyun.com/document_detail/478175.html) operation to query, manage, and collect statistics from the objects.
        
        @param request: CreateBindingRequest
        @return: CreateBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_binding_with_options(request, runtime)

    async def create_binding_async(
        self,
        request: imm_20200930_models.CreateBindingRequest,
    ) -> imm_20200930_models.CreateBindingResponse:
        """
        @summary Creates a binding relationship between a dataset and an Object Storage Service (OSS) bucket. This allows for the automatic synchronization of incremental and full data and indexing.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).***\
        Before you create a binding relationship, make sure that the project and the dataset that you want to use exist.
        For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For information about how to create a dataset, see [CreateDataset](https://help.aliyun.com/document_detail/478160.html).
        >  The CreateBinding operation works by using the [workflow template](https://help.aliyun.com/document_detail/466304.html) that is specified when you created the project or dataset.
        After you create a binding relationship between a dataset and an OSS bucket, IMM scans the existing objects in the bucket and extracts metadata based on the scanning result. Then, IMM creates an index from the extracted metadata. If new objects are added to the OSS bucket, IMM constantly tracks and scans the objects and updates the index. For objects whose index is created in this way, you can call the [SimpleQuery](https://help.aliyun.com/document_detail/478175.html) operation to query, manage, and collect statistics from the objects.
        
        @param request: CreateBindingRequest
        @return: CreateBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_binding_with_options_async(request, runtime)

    def create_compress_point_cloud_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateCompressPointCloudTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateCompressPointCloudTaskResponse:
        """
        @summary Compresses point cloud data (PCD) in Object Storage Service (OSS) to reduce the amount of data transferred over networks.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        This operation supports only Point Cloud Data (PCD) files.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications. >
        
        @param tmp_req: CreateCompressPointCloudTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCompressPointCloudTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateCompressPointCloudTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.kdtree_option):
            request.kdtree_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.kdtree_option, 'KdtreeOption', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.octree_option):
            request.octree_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.octree_option, 'OctreeOption', 'json')
        if not UtilClient.is_unset(tmp_req.point_cloud_fields):
            request.point_cloud_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.point_cloud_fields, 'PointCloudFields', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.compress_method):
            query['CompressMethod'] = request.compress_method
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.kdtree_option_shrink):
            query['KdtreeOption'] = request.kdtree_option_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.octree_option_shrink):
            query['OctreeOption'] = request.octree_option_shrink
        if not UtilClient.is_unset(request.point_cloud_fields_shrink):
            query['PointCloudFields'] = request.point_cloud_fields_shrink
        if not UtilClient.is_unset(request.point_cloud_file_format):
            query['PointCloudFileFormat'] = request.point_cloud_file_format
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCompressPointCloudTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateCompressPointCloudTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compress_point_cloud_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateCompressPointCloudTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateCompressPointCloudTaskResponse:
        """
        @summary Compresses point cloud data (PCD) in Object Storage Service (OSS) to reduce the amount of data transferred over networks.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        This operation supports only Point Cloud Data (PCD) files.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications. >
        
        @param tmp_req: CreateCompressPointCloudTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCompressPointCloudTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateCompressPointCloudTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.kdtree_option):
            request.kdtree_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.kdtree_option, 'KdtreeOption', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.octree_option):
            request.octree_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.octree_option, 'OctreeOption', 'json')
        if not UtilClient.is_unset(tmp_req.point_cloud_fields):
            request.point_cloud_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.point_cloud_fields, 'PointCloudFields', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.compress_method):
            query['CompressMethod'] = request.compress_method
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.kdtree_option_shrink):
            query['KdtreeOption'] = request.kdtree_option_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.octree_option_shrink):
            query['OctreeOption'] = request.octree_option_shrink
        if not UtilClient.is_unset(request.point_cloud_fields_shrink):
            query['PointCloudFields'] = request.point_cloud_fields_shrink
        if not UtilClient.is_unset(request.point_cloud_file_format):
            query['PointCloudFileFormat'] = request.point_cloud_file_format
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCompressPointCloudTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateCompressPointCloudTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compress_point_cloud_task(
        self,
        request: imm_20200930_models.CreateCompressPointCloudTaskRequest,
    ) -> imm_20200930_models.CreateCompressPointCloudTaskResponse:
        """
        @summary Compresses point cloud data (PCD) in Object Storage Service (OSS) to reduce the amount of data transferred over networks.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        This operation supports only Point Cloud Data (PCD) files.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications. >
        
        @param request: CreateCompressPointCloudTaskRequest
        @return: CreateCompressPointCloudTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_compress_point_cloud_task_with_options(request, runtime)

    async def create_compress_point_cloud_task_async(
        self,
        request: imm_20200930_models.CreateCompressPointCloudTaskRequest,
    ) -> imm_20200930_models.CreateCompressPointCloudTaskResponse:
        """
        @summary Compresses point cloud data (PCD) in Object Storage Service (OSS) to reduce the amount of data transferred over networks.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        This operation supports only Point Cloud Data (PCD) files.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications. >
        
        @param request: CreateCompressPointCloudTaskRequest
        @return: CreateCompressPointCloudTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_compress_point_cloud_task_with_options_async(request, runtime)

    def create_customized_story_with_options(
        self,
        tmp_req: imm_20200930_models.CreateCustomizedStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateCustomizedStoryResponse:
        """
        @summary Creates a story based on the specified images and videos.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        
        @param tmp_req: CreateCustomizedStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomizedStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateCustomizedStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCustomizedStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateCustomizedStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_customized_story_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateCustomizedStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateCustomizedStoryResponse:
        """
        @summary Creates a story based on the specified images and videos.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        
        @param tmp_req: CreateCustomizedStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomizedStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateCustomizedStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCustomizedStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateCustomizedStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_customized_story(
        self,
        request: imm_20200930_models.CreateCustomizedStoryRequest,
    ) -> imm_20200930_models.CreateCustomizedStoryResponse:
        """
        @summary Creates a story based on the specified images and videos.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        
        @param request: CreateCustomizedStoryRequest
        @return: CreateCustomizedStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_customized_story_with_options(request, runtime)

    async def create_customized_story_async(
        self,
        request: imm_20200930_models.CreateCustomizedStoryRequest,
    ) -> imm_20200930_models.CreateCustomizedStoryResponse:
        """
        @summary Creates a story based on the specified images and videos.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        
        @param request: CreateCustomizedStoryRequest
        @return: CreateCustomizedStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_customized_story_with_options_async(request, runtime)

    def create_dataset_with_options(
        self,
        tmp_req: imm_20200930_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDatasetResponse:
        """
        @summary Creates a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        A dataset name must be unique within the same project.
        A project has an upper limit on the number of datasets that can be created in the project. You can call the [GetProjcet](https://help.aliyun.com/document_detail/478155.html) operation to query the dataset limit of the project.
        After creating a dataset, you can call the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) operation to index metadata. Metadata indexing enhances [data retrieval efficiency and statistics collection](https://help.aliyun.com/document_detail/478175.html), and enables intelligent data management.
        
        @param tmp_req: CreateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_parameters):
            request.workflow_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_parameters, 'WorkflowParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.workflow_parameters_shrink):
            query['WorkflowParameters'] = request.workflow_parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDatasetResponse:
        """
        @summary Creates a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        A dataset name must be unique within the same project.
        A project has an upper limit on the number of datasets that can be created in the project. You can call the [GetProjcet](https://help.aliyun.com/document_detail/478155.html) operation to query the dataset limit of the project.
        After creating a dataset, you can call the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) operation to index metadata. Metadata indexing enhances [data retrieval efficiency and statistics collection](https://help.aliyun.com/document_detail/478175.html), and enables intelligent data management.
        
        @param tmp_req: CreateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_parameters):
            request.workflow_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_parameters, 'WorkflowParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.workflow_parameters_shrink):
            query['WorkflowParameters'] = request.workflow_parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        request: imm_20200930_models.CreateDatasetRequest,
    ) -> imm_20200930_models.CreateDatasetResponse:
        """
        @summary Creates a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        A dataset name must be unique within the same project.
        A project has an upper limit on the number of datasets that can be created in the project. You can call the [GetProjcet](https://help.aliyun.com/document_detail/478155.html) operation to query the dataset limit of the project.
        After creating a dataset, you can call the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) operation to index metadata. Metadata indexing enhances [data retrieval efficiency and statistics collection](https://help.aliyun.com/document_detail/478175.html), and enables intelligent data management.
        
        @param request: CreateDatasetRequest
        @return: CreateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    async def create_dataset_async(
        self,
        request: imm_20200930_models.CreateDatasetRequest,
    ) -> imm_20200930_models.CreateDatasetResponse:
        """
        @summary Creates a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        A dataset name must be unique within the same project.
        A project has an upper limit on the number of datasets that can be created in the project. You can call the [GetProjcet](https://help.aliyun.com/document_detail/478155.html) operation to query the dataset limit of the project.
        After creating a dataset, you can call the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) operation to index metadata. Metadata indexing enhances [data retrieval efficiency and statistics collection](https://help.aliyun.com/document_detail/478175.html), and enables intelligent data management.
        
        @param request: CreateDatasetRequest
        @return: CreateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dataset_with_options_async(request, runtime)

    def create_decode_blind_watermark_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateDecodeBlindWatermarkTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse:
        """
        @summary Decodes the blind watermark in an image.
        
        @description    Before you call this operation, make sure that you are familiar with the billing of Intelligent Media Management (IMM).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        The region and project specified in the request to decode a blind watermark must match those in the [EncodeBlindWatermark](https://help.aliyun.com/document_detail/2743655.html) request to encode the blind watermark.
        A blind watermark can still be extracted even if attacks, such as compression, scaling, cropping, rotation, and color transformation, are performed on the image.
        This operation is compatible with its earlier version DecodeBlindWatermark.
        This operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateDecodeBlindWatermarkTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDecodeBlindWatermarkTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateDecodeBlindWatermarkTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.original_image_uri):
            query['OriginalImageURI'] = request.original_image_uri
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDecodeBlindWatermarkTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_decode_blind_watermark_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateDecodeBlindWatermarkTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse:
        """
        @summary Decodes the blind watermark in an image.
        
        @description    Before you call this operation, make sure that you are familiar with the billing of Intelligent Media Management (IMM).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        The region and project specified in the request to decode a blind watermark must match those in the [EncodeBlindWatermark](https://help.aliyun.com/document_detail/2743655.html) request to encode the blind watermark.
        A blind watermark can still be extracted even if attacks, such as compression, scaling, cropping, rotation, and color transformation, are performed on the image.
        This operation is compatible with its earlier version DecodeBlindWatermark.
        This operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateDecodeBlindWatermarkTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDecodeBlindWatermarkTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateDecodeBlindWatermarkTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.original_image_uri):
            query['OriginalImageURI'] = request.original_image_uri
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDecodeBlindWatermarkTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_decode_blind_watermark_task(
        self,
        request: imm_20200930_models.CreateDecodeBlindWatermarkTaskRequest,
    ) -> imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse:
        """
        @summary Decodes the blind watermark in an image.
        
        @description    Before you call this operation, make sure that you are familiar with the billing of Intelligent Media Management (IMM).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        The region and project specified in the request to decode a blind watermark must match those in the [EncodeBlindWatermark](https://help.aliyun.com/document_detail/2743655.html) request to encode the blind watermark.
        A blind watermark can still be extracted even if attacks, such as compression, scaling, cropping, rotation, and color transformation, are performed on the image.
        This operation is compatible with its earlier version DecodeBlindWatermark.
        This operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateDecodeBlindWatermarkTaskRequest
        @return: CreateDecodeBlindWatermarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_decode_blind_watermark_task_with_options(request, runtime)

    async def create_decode_blind_watermark_task_async(
        self,
        request: imm_20200930_models.CreateDecodeBlindWatermarkTaskRequest,
    ) -> imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse:
        """
        @summary Decodes the blind watermark in an image.
        
        @description    Before you call this operation, make sure that you are familiar with the billing of Intelligent Media Management (IMM).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        The region and project specified in the request to decode a blind watermark must match those in the [EncodeBlindWatermark](https://help.aliyun.com/document_detail/2743655.html) request to encode the blind watermark.
        A blind watermark can still be extracted even if attacks, such as compression, scaling, cropping, rotation, and color transformation, are performed on the image.
        This operation is compatible with its earlier version DecodeBlindWatermark.
        This operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateDecodeBlindWatermarkTaskRequest
        @return: CreateDecodeBlindWatermarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_decode_blind_watermark_task_with_options_async(request, runtime)

    def create_faces_searching_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFacesSearchingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFacesSearchingTaskResponse:
        """
        @summary Searches the dataset for the specified number of images most similar to the specified image or face and returns face IDs and boundaries in descending order of similarity.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation searches for faces that are similar to the face within the largest bounding box in each input image.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateFacesSearchingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFacesSearchingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFacesSearchingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFacesSearchingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFacesSearchingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_faces_searching_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateFacesSearchingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFacesSearchingTaskResponse:
        """
        @summary Searches the dataset for the specified number of images most similar to the specified image or face and returns face IDs and boundaries in descending order of similarity.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation searches for faces that are similar to the face within the largest bounding box in each input image.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateFacesSearchingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFacesSearchingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFacesSearchingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFacesSearchingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFacesSearchingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_faces_searching_task(
        self,
        request: imm_20200930_models.CreateFacesSearchingTaskRequest,
    ) -> imm_20200930_models.CreateFacesSearchingTaskResponse:
        """
        @summary Searches the dataset for the specified number of images most similar to the specified image or face and returns face IDs and boundaries in descending order of similarity.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation searches for faces that are similar to the face within the largest bounding box in each input image.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateFacesSearchingTaskRequest
        @return: CreateFacesSearchingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_faces_searching_task_with_options(request, runtime)

    async def create_faces_searching_task_async(
        self,
        request: imm_20200930_models.CreateFacesSearchingTaskRequest,
    ) -> imm_20200930_models.CreateFacesSearchingTaskResponse:
        """
        @summary Searches the dataset for the specified number of images most similar to the specified image or face and returns face IDs and boundaries in descending order of similarity.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation searches for faces that are similar to the face within the largest bounding box in each input image.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateFacesSearchingTaskRequest
        @return: CreateFacesSearchingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_faces_searching_task_with_options_async(request, runtime)

    def create_figure_clustering_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFigureClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFigureClusteringTaskResponse:
        """
        @summary Creates a face clustering task to cluster faces of different persons in images by person based on the intelligent algorithms.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the CreateBinding operation or manually by calling the IndexFileMeta or BatchIndexFileMeta operation.
        Each call to the operation incrementally processes metadata in the dataset. You can regularly call this operation to process incremental files.
        After the clustering task is completed, you can call the GetFigureCluster or BatchGetFigureCluster  operation to query information about a specific cluster. You can also call the QueryFigureClusters operation to query all face clusters of the specified dataset.
        Removing image information from the dataset causes changes to face clusters. When images that contain all faces in a cluster are removed, the cluster is deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateFigureClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFigureClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFigureClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFigureClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_figure_clustering_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateFigureClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFigureClusteringTaskResponse:
        """
        @summary Creates a face clustering task to cluster faces of different persons in images by person based on the intelligent algorithms.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the CreateBinding operation or manually by calling the IndexFileMeta or BatchIndexFileMeta operation.
        Each call to the operation incrementally processes metadata in the dataset. You can regularly call this operation to process incremental files.
        After the clustering task is completed, you can call the GetFigureCluster or BatchGetFigureCluster  operation to query information about a specific cluster. You can also call the QueryFigureClusters operation to query all face clusters of the specified dataset.
        Removing image information from the dataset causes changes to face clusters. When images that contain all faces in a cluster are removed, the cluster is deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateFigureClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFigureClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFigureClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFigureClusteringTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_figure_clustering_task(
        self,
        request: imm_20200930_models.CreateFigureClusteringTaskRequest,
    ) -> imm_20200930_models.CreateFigureClusteringTaskResponse:
        """
        @summary Creates a face clustering task to cluster faces of different persons in images by person based on the intelligent algorithms.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the CreateBinding operation or manually by calling the IndexFileMeta or BatchIndexFileMeta operation.
        Each call to the operation incrementally processes metadata in the dataset. You can regularly call this operation to process incremental files.
        After the clustering task is completed, you can call the GetFigureCluster or BatchGetFigureCluster  operation to query information about a specific cluster. You can also call the QueryFigureClusters operation to query all face clusters of the specified dataset.
        Removing image information from the dataset causes changes to face clusters. When images that contain all faces in a cluster are removed, the cluster is deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateFigureClusteringTaskRequest
        @return: CreateFigureClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_figure_clustering_task_with_options(request, runtime)

    async def create_figure_clustering_task_async(
        self,
        request: imm_20200930_models.CreateFigureClusteringTaskRequest,
    ) -> imm_20200930_models.CreateFigureClusteringTaskResponse:
        """
        @summary Creates a face clustering task to cluster faces of different persons in images by person based on the intelligent algorithms.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the CreateBinding operation or manually by calling the IndexFileMeta or BatchIndexFileMeta operation.
        Each call to the operation incrementally processes metadata in the dataset. You can regularly call this operation to process incremental files.
        After the clustering task is completed, you can call the GetFigureCluster or BatchGetFigureCluster  operation to query information about a specific cluster. You can also call the QueryFigureClusters operation to query all face clusters of the specified dataset.
        Removing image information from the dataset causes changes to face clusters. When images that contain all faces in a cluster are removed, the cluster is deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateFigureClusteringTaskRequest
        @return: CreateFigureClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_figure_clustering_task_with_options_async(request, runtime)

    def create_figure_clusters_merging_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFigureClustersMergingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFigureClustersMergingTaskResponse:
        """
        @summary Merges two or more face clustering groups into one face clustering group.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        If you merge unrelated groups, the feature values of the target groups are affected. As a result, the incremental data may be inaccurately grouped when you create a face clustering task.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateFigureClustersMergingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFigureClustersMergingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClustersMergingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.froms):
            request.froms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.froms, 'Froms', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.froms_shrink):
            query['Froms'] = request.froms_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFigureClustersMergingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFigureClustersMergingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_figure_clusters_merging_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateFigureClustersMergingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFigureClustersMergingTaskResponse:
        """
        @summary Merges two or more face clustering groups into one face clustering group.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        If you merge unrelated groups, the feature values of the target groups are affected. As a result, the incremental data may be inaccurately grouped when you create a face clustering task.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateFigureClustersMergingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFigureClustersMergingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClustersMergingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.froms):
            request.froms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.froms, 'Froms', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.froms_shrink):
            query['Froms'] = request.froms_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFigureClustersMergingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFigureClustersMergingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_figure_clusters_merging_task(
        self,
        request: imm_20200930_models.CreateFigureClustersMergingTaskRequest,
    ) -> imm_20200930_models.CreateFigureClustersMergingTaskResponse:
        """
        @summary Merges two or more face clustering groups into one face clustering group.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        If you merge unrelated groups, the feature values of the target groups are affected. As a result, the incremental data may be inaccurately grouped when you create a face clustering task.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateFigureClustersMergingTaskRequest
        @return: CreateFigureClustersMergingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_figure_clusters_merging_task_with_options(request, runtime)

    async def create_figure_clusters_merging_task_async(
        self,
        request: imm_20200930_models.CreateFigureClustersMergingTaskRequest,
    ) -> imm_20200930_models.CreateFigureClustersMergingTaskResponse:
        """
        @summary Merges two or more face clustering groups into one face clustering group.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        If you merge unrelated groups, the feature values of the target groups are affected. As a result, the incremental data may be inaccurately grouped when you create a face clustering task.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateFigureClustersMergingTaskRequest
        @return: CreateFigureClustersMergingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_figure_clusters_merging_task_with_options_async(request, runtime)

    def create_file_compression_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFileCompressionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFileCompressionTaskResponse:
        """
        @summary Creates a file packing task.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk group (ID: 88490020073) and share your questions with us.
        >  The operation supports file packing only. Compression support will be added later.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        A call to the operation can pack up to 80,000 objects into a package.
        The total size of all objects to be packed into a package cannot exceed 200 GB.
        The operation can pack only Standard objects in Object Storage Service (OSS). To pack an object in another storage class, you must first [convert the storage class of the object](https://help.aliyun.com/document_detail/90090.html).
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateFileCompressionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileCompressionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFileCompressionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not UtilClient.is_unset(request.compressed_format):
            query['CompressedFormat'] = request.compressed_format
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_manifest_uri):
            query['SourceManifestURI'] = request.source_manifest_uri
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileCompressionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFileCompressionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_compression_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateFileCompressionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFileCompressionTaskResponse:
        """
        @summary Creates a file packing task.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk group (ID: 88490020073) and share your questions with us.
        >  The operation supports file packing only. Compression support will be added later.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        A call to the operation can pack up to 80,000 objects into a package.
        The total size of all objects to be packed into a package cannot exceed 200 GB.
        The operation can pack only Standard objects in Object Storage Service (OSS). To pack an object in another storage class, you must first [convert the storage class of the object](https://help.aliyun.com/document_detail/90090.html).
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateFileCompressionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileCompressionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFileCompressionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not UtilClient.is_unset(request.compressed_format):
            query['CompressedFormat'] = request.compressed_format
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_manifest_uri):
            query['SourceManifestURI'] = request.source_manifest_uri
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileCompressionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFileCompressionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_compression_task(
        self,
        request: imm_20200930_models.CreateFileCompressionTaskRequest,
    ) -> imm_20200930_models.CreateFileCompressionTaskResponse:
        """
        @summary Creates a file packing task.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk group (ID: 88490020073) and share your questions with us.
        >  The operation supports file packing only. Compression support will be added later.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        A call to the operation can pack up to 80,000 objects into a package.
        The total size of all objects to be packed into a package cannot exceed 200 GB.
        The operation can pack only Standard objects in Object Storage Service (OSS). To pack an object in another storage class, you must first [convert the storage class of the object](https://help.aliyun.com/document_detail/90090.html).
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateFileCompressionTaskRequest
        @return: CreateFileCompressionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_compression_task_with_options(request, runtime)

    async def create_file_compression_task_async(
        self,
        request: imm_20200930_models.CreateFileCompressionTaskRequest,
    ) -> imm_20200930_models.CreateFileCompressionTaskResponse:
        """
        @summary Creates a file packing task.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk group (ID: 88490020073) and share your questions with us.
        >  The operation supports file packing only. Compression support will be added later.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        A call to the operation can pack up to 80,000 objects into a package.
        The total size of all objects to be packed into a package cannot exceed 200 GB.
        The operation can pack only Standard objects in Object Storage Service (OSS). To pack an object in another storage class, you must first [convert the storage class of the object](https://help.aliyun.com/document_detail/90090.html).
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateFileCompressionTaskRequest
        @return: CreateFileCompressionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_file_compression_task_with_options_async(request, runtime)

    def create_file_uncompression_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFileUncompressionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFileUncompressionTaskResponse:
        """
        @summary Extracts the specified files from a ZIP, RAR, or 7z package to the specified directory or decompresses the entire package.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk group (ID: 88490020073) and share your questions with us.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports a package that contains up to 80,000 files.
        The operation supports ZIP or RAR packages up to 200 GB in size, or 7z packages up to 50 GB in size.
        The operation extracts files in streams to the specified directory. If the file extraction task is interrupted by a corrupt file, files that have been extracted are not deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateFileUncompressionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileUncompressionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFileUncompressionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.selected_files):
            request.selected_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.selected_files, 'SelectedFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.selected_files_shrink):
            query['SelectedFiles'] = request.selected_files_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileUncompressionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFileUncompressionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_uncompression_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateFileUncompressionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFileUncompressionTaskResponse:
        """
        @summary Extracts the specified files from a ZIP, RAR, or 7z package to the specified directory or decompresses the entire package.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk group (ID: 88490020073) and share your questions with us.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports a package that contains up to 80,000 files.
        The operation supports ZIP or RAR packages up to 200 GB in size, or 7z packages up to 50 GB in size.
        The operation extracts files in streams to the specified directory. If the file extraction task is interrupted by a corrupt file, files that have been extracted are not deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateFileUncompressionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileUncompressionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFileUncompressionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.selected_files):
            request.selected_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.selected_files, 'SelectedFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.selected_files_shrink):
            query['SelectedFiles'] = request.selected_files_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileUncompressionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFileUncompressionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_uncompression_task(
        self,
        request: imm_20200930_models.CreateFileUncompressionTaskRequest,
    ) -> imm_20200930_models.CreateFileUncompressionTaskResponse:
        """
        @summary Extracts the specified files from a ZIP, RAR, or 7z package to the specified directory or decompresses the entire package.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk group (ID: 88490020073) and share your questions with us.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports a package that contains up to 80,000 files.
        The operation supports ZIP or RAR packages up to 200 GB in size, or 7z packages up to 50 GB in size.
        The operation extracts files in streams to the specified directory. If the file extraction task is interrupted by a corrupt file, files that have been extracted are not deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateFileUncompressionTaskRequest
        @return: CreateFileUncompressionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_uncompression_task_with_options(request, runtime)

    async def create_file_uncompression_task_async(
        self,
        request: imm_20200930_models.CreateFileUncompressionTaskRequest,
    ) -> imm_20200930_models.CreateFileUncompressionTaskResponse:
        """
        @summary Extracts the specified files from a ZIP, RAR, or 7z package to the specified directory or decompresses the entire package.
        
        @description >  The operation is in public preview. For any inquires, join our DingTalk group (ID: 88490020073) and share your questions with us.
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports a package that contains up to 80,000 files.
        The operation supports ZIP or RAR packages up to 200 GB in size, or 7z packages up to 50 GB in size.
        The operation extracts files in streams to the specified directory. If the file extraction task is interrupted by a corrupt file, files that have been extracted are not deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateFileUncompressionTaskRequest
        @return: CreateFileUncompressionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_file_uncompression_task_with_options_async(request, runtime)

    def create_image_moderation_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateImageModerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageModerationTaskResponse:
        """
        @summary Creates an image moderation task to ensure image content compliance. You can call this operation to identify inappropriate content, such as pornography, violence, terrorism, politically sensitive content, undesirable scenes, unauthorized logos, and non-compliant ads.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The image for which you want to create a content moderation task must meet the following requirements:
        The image URL supports the HTTP and HTTPS protocols.
        The image is in one of the following formats: PNG, JPG, JPEG, BMP, GIF, and WebP
        The image size is limited to 20 MB for synchronous and asynchronous calls, with a maximum height or width of 30,000 pixels. The total number of pixels cannot exceed 250 million. GIF images are limited to 4,194,304 pixels, with a maximum height or width of 30,000 pixels.
        The image download time is limited to 3 seconds. If the download takes longer, a timeout error occurs.
        To ensure effective moderation, we recommend that you submit an image with dimensions of at least 256 × 256 pixels.
        The response time of the CreateImageModerationTask operation varies based on the duration of the image download. Make sure that the image is stored in a stable and reliable service. We recommend that you store images on Alibaba Cloud Object Storage Service (OSS) or cache them on Alibaba Cloud CDN.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478241.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can also obtain information about the task based on notifications.
        >  The detection result is sent as an asynchronous notification. The Suggestion field of the notification can have one of the following values:
        pass: No non-compliant content is found.
        block: Non-compliant content is detected. The Categories field value indicates the non-compliance categories. For more information, see Content moderation results.
        review: A manual review is needed. After the manual review is finished, another asynchronous notification is sent to inform you about the review result. >
        
        @param tmp_req: CreateImageModerationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageModerationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.scenes):
            request.scenes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageModerationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageModerationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_moderation_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateImageModerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageModerationTaskResponse:
        """
        @summary Creates an image moderation task to ensure image content compliance. You can call this operation to identify inappropriate content, such as pornography, violence, terrorism, politically sensitive content, undesirable scenes, unauthorized logos, and non-compliant ads.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The image for which you want to create a content moderation task must meet the following requirements:
        The image URL supports the HTTP and HTTPS protocols.
        The image is in one of the following formats: PNG, JPG, JPEG, BMP, GIF, and WebP
        The image size is limited to 20 MB for synchronous and asynchronous calls, with a maximum height or width of 30,000 pixels. The total number of pixels cannot exceed 250 million. GIF images are limited to 4,194,304 pixels, with a maximum height or width of 30,000 pixels.
        The image download time is limited to 3 seconds. If the download takes longer, a timeout error occurs.
        To ensure effective moderation, we recommend that you submit an image with dimensions of at least 256 × 256 pixels.
        The response time of the CreateImageModerationTask operation varies based on the duration of the image download. Make sure that the image is stored in a stable and reliable service. We recommend that you store images on Alibaba Cloud Object Storage Service (OSS) or cache them on Alibaba Cloud CDN.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478241.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can also obtain information about the task based on notifications.
        >  The detection result is sent as an asynchronous notification. The Suggestion field of the notification can have one of the following values:
        pass: No non-compliant content is found.
        block: Non-compliant content is detected. The Categories field value indicates the non-compliance categories. For more information, see Content moderation results.
        review: A manual review is needed. After the manual review is finished, another asynchronous notification is sent to inform you about the review result. >
        
        @param tmp_req: CreateImageModerationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageModerationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.scenes):
            request.scenes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageModerationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageModerationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_moderation_task(
        self,
        request: imm_20200930_models.CreateImageModerationTaskRequest,
    ) -> imm_20200930_models.CreateImageModerationTaskResponse:
        """
        @summary Creates an image moderation task to ensure image content compliance. You can call this operation to identify inappropriate content, such as pornography, violence, terrorism, politically sensitive content, undesirable scenes, unauthorized logos, and non-compliant ads.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The image for which you want to create a content moderation task must meet the following requirements:
        The image URL supports the HTTP and HTTPS protocols.
        The image is in one of the following formats: PNG, JPG, JPEG, BMP, GIF, and WebP
        The image size is limited to 20 MB for synchronous and asynchronous calls, with a maximum height or width of 30,000 pixels. The total number of pixels cannot exceed 250 million. GIF images are limited to 4,194,304 pixels, with a maximum height or width of 30,000 pixels.
        The image download time is limited to 3 seconds. If the download takes longer, a timeout error occurs.
        To ensure effective moderation, we recommend that you submit an image with dimensions of at least 256 × 256 pixels.
        The response time of the CreateImageModerationTask operation varies based on the duration of the image download. Make sure that the image is stored in a stable and reliable service. We recommend that you store images on Alibaba Cloud Object Storage Service (OSS) or cache them on Alibaba Cloud CDN.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478241.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can also obtain information about the task based on notifications.
        >  The detection result is sent as an asynchronous notification. The Suggestion field of the notification can have one of the following values:
        pass: No non-compliant content is found.
        block: Non-compliant content is detected. The Categories field value indicates the non-compliance categories. For more information, see Content moderation results.
        review: A manual review is needed. After the manual review is finished, another asynchronous notification is sent to inform you about the review result. >
        
        @param request: CreateImageModerationTaskRequest
        @return: CreateImageModerationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_image_moderation_task_with_options(request, runtime)

    async def create_image_moderation_task_async(
        self,
        request: imm_20200930_models.CreateImageModerationTaskRequest,
    ) -> imm_20200930_models.CreateImageModerationTaskResponse:
        """
        @summary Creates an image moderation task to ensure image content compliance. You can call this operation to identify inappropriate content, such as pornography, violence, terrorism, politically sensitive content, undesirable scenes, unauthorized logos, and non-compliant ads.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The image for which you want to create a content moderation task must meet the following requirements:
        The image URL supports the HTTP and HTTPS protocols.
        The image is in one of the following formats: PNG, JPG, JPEG, BMP, GIF, and WebP
        The image size is limited to 20 MB for synchronous and asynchronous calls, with a maximum height or width of 30,000 pixels. The total number of pixels cannot exceed 250 million. GIF images are limited to 4,194,304 pixels, with a maximum height or width of 30,000 pixels.
        The image download time is limited to 3 seconds. If the download takes longer, a timeout error occurs.
        To ensure effective moderation, we recommend that you submit an image with dimensions of at least 256 × 256 pixels.
        The response time of the CreateImageModerationTask operation varies based on the duration of the image download. Make sure that the image is stored in a stable and reliable service. We recommend that you store images on Alibaba Cloud Object Storage Service (OSS) or cache them on Alibaba Cloud CDN.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478241.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can also obtain information about the task based on notifications.
        >  The detection result is sent as an asynchronous notification. The Suggestion field of the notification can have one of the following values:
        pass: No non-compliant content is found.
        block: Non-compliant content is detected. The Categories field value indicates the non-compliance categories. For more information, see Content moderation results.
        review: A manual review is needed. After the manual review is finished, another asynchronous notification is sent to inform you about the review result. >
        
        @param request: CreateImageModerationTaskRequest
        @return: CreateImageModerationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_image_moderation_task_with_options_async(request, runtime)

    def create_image_splicing_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateImageSplicingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageSplicingTaskResponse:
        """
        @summary Creates an image splicing task. You can call this operation to splice multiple images into one based on a given rule and save the final image into an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        You can call this operation to merge up to 10 images. Each side of an image cannot exceed 32,876 pixels, and the total number of pixels of the image cannot exceed 1 billion.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateImageSplicingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageSplicingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageSplicingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.align):
            query['Align'] = request.align
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.image_format):
            query['ImageFormat'] = request.image_format
        if not UtilClient.is_unset(request.margin):
            query['Margin'] = request.margin
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.padding):
            query['Padding'] = request.padding
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageSplicingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageSplicingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_splicing_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateImageSplicingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageSplicingTaskResponse:
        """
        @summary Creates an image splicing task. You can call this operation to splice multiple images into one based on a given rule and save the final image into an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        You can call this operation to merge up to 10 images. Each side of an image cannot exceed 32,876 pixels, and the total number of pixels of the image cannot exceed 1 billion.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateImageSplicingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageSplicingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageSplicingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.align):
            query['Align'] = request.align
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.image_format):
            query['ImageFormat'] = request.image_format
        if not UtilClient.is_unset(request.margin):
            query['Margin'] = request.margin
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.padding):
            query['Padding'] = request.padding
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageSplicingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageSplicingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_splicing_task(
        self,
        request: imm_20200930_models.CreateImageSplicingTaskRequest,
    ) -> imm_20200930_models.CreateImageSplicingTaskResponse:
        """
        @summary Creates an image splicing task. You can call this operation to splice multiple images into one based on a given rule and save the final image into an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        You can call this operation to merge up to 10 images. Each side of an image cannot exceed 32,876 pixels, and the total number of pixels of the image cannot exceed 1 billion.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateImageSplicingTaskRequest
        @return: CreateImageSplicingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_image_splicing_task_with_options(request, runtime)

    async def create_image_splicing_task_async(
        self,
        request: imm_20200930_models.CreateImageSplicingTaskRequest,
    ) -> imm_20200930_models.CreateImageSplicingTaskResponse:
        """
        @summary Creates an image splicing task. You can call this operation to splice multiple images into one based on a given rule and save the final image into an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        You can call this operation to merge up to 10 images. Each side of an image cannot exceed 32,876 pixels, and the total number of pixels of the image cannot exceed 1 billion.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateImageSplicingTaskRequest
        @return: CreateImageSplicingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_image_splicing_task_with_options_async(request, runtime)

    def create_image_to_pdftask_with_options(
        self,
        tmp_req: imm_20200930_models.CreateImageToPDFTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageToPDFTaskResponse:
        """
        @summary Converts multiple images into one single PDF file and stores the PDF file to the specified path in Object Storage Service (OSS).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        You can specify up to 100 images in a call to the operation.
        This operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateImageToPDFTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageToPDFTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageToPDFTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageToPDFTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageToPDFTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_to_pdftask_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateImageToPDFTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageToPDFTaskResponse:
        """
        @summary Converts multiple images into one single PDF file and stores the PDF file to the specified path in Object Storage Service (OSS).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        You can specify up to 100 images in a call to the operation.
        This operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateImageToPDFTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageToPDFTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageToPDFTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageToPDFTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageToPDFTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_to_pdftask(
        self,
        request: imm_20200930_models.CreateImageToPDFTaskRequest,
    ) -> imm_20200930_models.CreateImageToPDFTaskResponse:
        """
        @summary Converts multiple images into one single PDF file and stores the PDF file to the specified path in Object Storage Service (OSS).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        You can specify up to 100 images in a call to the operation.
        This operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateImageToPDFTaskRequest
        @return: CreateImageToPDFTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_image_to_pdftask_with_options(request, runtime)

    async def create_image_to_pdftask_async(
        self,
        request: imm_20200930_models.CreateImageToPDFTaskRequest,
    ) -> imm_20200930_models.CreateImageToPDFTaskResponse:
        """
        @summary Converts multiple images into one single PDF file and stores the PDF file to the specified path in Object Storage Service (OSS).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        You can specify up to 100 images in a call to the operation.
        This operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateImageToPDFTaskRequest
        @return: CreateImageToPDFTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_image_to_pdftask_with_options_async(request, runtime)

    def create_location_date_clustering_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateLocationDateClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateLocationDateClusteringTaskResponse:
        """
        @summary Creates a spatiotemporal clustering task to cluster photos and videos based on geolocation and time information. Spatiotemporal clustering allows you to group photos and videos taken during a travel or at different places by their spatial and temporal similarity. Based on spatiotemporal clustering, you can develop media capabilities such as media file categorization, photo collections, and image and video-based stories.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Each call to the operation incrementally processes metadata in the dataset.****`` You can regularly call this operation to process incremental files.
        After a spatiotemporal clustering task is complete, you can call the [QueryLocationDateClusters](https://help.aliyun.com/document_detail/478189.html) operation to query the spatiotemporal clustering result.
        Removing metadata from a dataset does not affect existing spatiotemporal clusters for the dataset. To delete a spatiotemporal cluster, call the [DeleteLocationDateCluster](https://help.aliyun.com/document_detail/478191.html) operation.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateLocationDateClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLocationDateClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateLocationDateClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.date_options):
            request.date_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.date_options, 'DateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.location_options):
            request.location_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_options, 'LocationOptions', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.date_options_shrink):
            query['DateOptions'] = request.date_options_shrink
        if not UtilClient.is_unset(request.location_options_shrink):
            query['LocationOptions'] = request.location_options_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLocationDateClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateLocationDateClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_location_date_clustering_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateLocationDateClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateLocationDateClusteringTaskResponse:
        """
        @summary Creates a spatiotemporal clustering task to cluster photos and videos based on geolocation and time information. Spatiotemporal clustering allows you to group photos and videos taken during a travel or at different places by their spatial and temporal similarity. Based on spatiotemporal clustering, you can develop media capabilities such as media file categorization, photo collections, and image and video-based stories.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Each call to the operation incrementally processes metadata in the dataset.****`` You can regularly call this operation to process incremental files.
        After a spatiotemporal clustering task is complete, you can call the [QueryLocationDateClusters](https://help.aliyun.com/document_detail/478189.html) operation to query the spatiotemporal clustering result.
        Removing metadata from a dataset does not affect existing spatiotemporal clusters for the dataset. To delete a spatiotemporal cluster, call the [DeleteLocationDateCluster](https://help.aliyun.com/document_detail/478191.html) operation.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateLocationDateClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLocationDateClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateLocationDateClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.date_options):
            request.date_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.date_options, 'DateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.location_options):
            request.location_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_options, 'LocationOptions', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.date_options_shrink):
            query['DateOptions'] = request.date_options_shrink
        if not UtilClient.is_unset(request.location_options_shrink):
            query['LocationOptions'] = request.location_options_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLocationDateClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateLocationDateClusteringTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_location_date_clustering_task(
        self,
        request: imm_20200930_models.CreateLocationDateClusteringTaskRequest,
    ) -> imm_20200930_models.CreateLocationDateClusteringTaskResponse:
        """
        @summary Creates a spatiotemporal clustering task to cluster photos and videos based on geolocation and time information. Spatiotemporal clustering allows you to group photos and videos taken during a travel or at different places by their spatial and temporal similarity. Based on spatiotemporal clustering, you can develop media capabilities such as media file categorization, photo collections, and image and video-based stories.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Each call to the operation incrementally processes metadata in the dataset.****`` You can regularly call this operation to process incremental files.
        After a spatiotemporal clustering task is complete, you can call the [QueryLocationDateClusters](https://help.aliyun.com/document_detail/478189.html) operation to query the spatiotemporal clustering result.
        Removing metadata from a dataset does not affect existing spatiotemporal clusters for the dataset. To delete a spatiotemporal cluster, call the [DeleteLocationDateCluster](https://help.aliyun.com/document_detail/478191.html) operation.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateLocationDateClusteringTaskRequest
        @return: CreateLocationDateClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_location_date_clustering_task_with_options(request, runtime)

    async def create_location_date_clustering_task_async(
        self,
        request: imm_20200930_models.CreateLocationDateClusteringTaskRequest,
    ) -> imm_20200930_models.CreateLocationDateClusteringTaskResponse:
        """
        @summary Creates a spatiotemporal clustering task to cluster photos and videos based on geolocation and time information. Spatiotemporal clustering allows you to group photos and videos taken during a travel or at different places by their spatial and temporal similarity. Based on spatiotemporal clustering, you can develop media capabilities such as media file categorization, photo collections, and image and video-based stories.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Each call to the operation incrementally processes metadata in the dataset.****`` You can regularly call this operation to process incremental files.
        After a spatiotemporal clustering task is complete, you can call the [QueryLocationDateClusters](https://help.aliyun.com/document_detail/478189.html) operation to query the spatiotemporal clustering result.
        Removing metadata from a dataset does not affect existing spatiotemporal clusters for the dataset. To delete a spatiotemporal cluster, call the [DeleteLocationDateCluster](https://help.aliyun.com/document_detail/478191.html) operation.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateLocationDateClusteringTaskRequest
        @return: CreateLocationDateClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_location_date_clustering_task_with_options_async(request, runtime)

    def create_media_convert_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateMediaConvertTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateMediaConvertTaskResponse:
        """
        @summary Creates an asynchronous media transcoding task to provide audio and video file processing abilities, such as media transcoding, media splicing, video frame capturing, and video to GIF conversion.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        By default, only one type of video, audio, and subtitle streams is processed when you call this operation to process media transcoding. However, you can specify the number of video, audio, or subtitle streams that you want to process.
        When you use this operation to execute a media merging task, up to 11 media files are supported. In this case, the parameters that involve media transcoding and frame capturing apply to the merged media data.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        *\
        ***\
        
        @param tmp_req: CreateMediaConvertTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMediaConvertTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateMediaConvertTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.alignment_index):
            query['AlignmentIndex'] = request.alignment_index
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMediaConvertTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateMediaConvertTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_media_convert_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateMediaConvertTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateMediaConvertTaskResponse:
        """
        @summary Creates an asynchronous media transcoding task to provide audio and video file processing abilities, such as media transcoding, media splicing, video frame capturing, and video to GIF conversion.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        By default, only one type of video, audio, and subtitle streams is processed when you call this operation to process media transcoding. However, you can specify the number of video, audio, or subtitle streams that you want to process.
        When you use this operation to execute a media merging task, up to 11 media files are supported. In this case, the parameters that involve media transcoding and frame capturing apply to the merged media data.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        *\
        ***\
        
        @param tmp_req: CreateMediaConvertTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMediaConvertTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateMediaConvertTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.alignment_index):
            query['AlignmentIndex'] = request.alignment_index
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMediaConvertTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateMediaConvertTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_media_convert_task(
        self,
        request: imm_20200930_models.CreateMediaConvertTaskRequest,
    ) -> imm_20200930_models.CreateMediaConvertTaskResponse:
        """
        @summary Creates an asynchronous media transcoding task to provide audio and video file processing abilities, such as media transcoding, media splicing, video frame capturing, and video to GIF conversion.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        By default, only one type of video, audio, and subtitle streams is processed when you call this operation to process media transcoding. However, you can specify the number of video, audio, or subtitle streams that you want to process.
        When you use this operation to execute a media merging task, up to 11 media files are supported. In this case, the parameters that involve media transcoding and frame capturing apply to the merged media data.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        *\
        ***\
        
        @param request: CreateMediaConvertTaskRequest
        @return: CreateMediaConvertTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_media_convert_task_with_options(request, runtime)

    async def create_media_convert_task_async(
        self,
        request: imm_20200930_models.CreateMediaConvertTaskRequest,
    ) -> imm_20200930_models.CreateMediaConvertTaskResponse:
        """
        @summary Creates an asynchronous media transcoding task to provide audio and video file processing abilities, such as media transcoding, media splicing, video frame capturing, and video to GIF conversion.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        By default, only one type of video, audio, and subtitle streams is processed when you call this operation to process media transcoding. However, you can specify the number of video, audio, or subtitle streams that you want to process.
        When you use this operation to execute a media merging task, up to 11 media files are supported. In this case, the parameters that involve media transcoding and frame capturing apply to the merged media data.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        *\
        ***\
        
        @param request: CreateMediaConvertTaskRequest
        @return: CreateMediaConvertTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_media_convert_task_with_options_async(request, runtime)

    def create_office_conversion_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        """
        @summary Creates a document format conversion task to convert the format of a document stored in an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports the following input formats:
        Text documents: doc, docx, wps, wpss, docm, dotm, dot, dotx, and html
        Presentation documents: pptx, ppt, pot, potx, pps, ppsx, dps, dpt, pptm, potm, ppsm, and dpss
        Spreadsheet documents: xls, xlt, et, ett, xlsx, xltx, csv, xlsb, xlsm, xltm, and ets
        PDF documents: pdf
        The operation supports the following output formats:
        Image files: png and jpg
        Text files: txt
        PDF files: pdf
        Each input document can be up to 200 MB in size.
        The maximum conversion time is 120 seconds. If the document contains too much or complex content, the conversion may time out.
        The operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can use one of the following methods to query task information:
        Call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.``
        In the region in which the IMM project is located, configure a Simple Message Queue (SMQ) subscription to receive task information notifications. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html). For information about SMQ SDKs, see [Use queues](https://help.aliyun.com/document_detail/32449.html).
        In the region in which the IMM project is located, create an ApsaraMQ for RocketMQ 4.0 instance, a topic, and a group to receive task notifications. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html). For more information about how to use ApsaraMQ for RocketMQ, see [Call HTTP SDKs to send and subscribe to messages](https://help.aliyun.com/document_detail/169009.html).
        In the region in which the IMM project is located, use [EventBridge](https://www.alibabacloud.com/en/product/eventbridge) to receive task information notifications. For more information, see [IMM events](https://help.aliyun.com/document_detail/205730.html).
        
        @param tmp_req: CreateOfficeConversionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOfficeConversionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateOfficeConversionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.trim_policy):
            request.trim_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trim_policy, 'TrimPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.end_page):
            query['EndPage'] = request.end_page
        if not UtilClient.is_unset(request.first_page):
            query['FirstPage'] = request.first_page
        if not UtilClient.is_unset(request.fit_to_height):
            query['FitToHeight'] = request.fit_to_height
        if not UtilClient.is_unset(request.fit_to_width):
            query['FitToWidth'] = request.fit_to_width
        if not UtilClient.is_unset(request.hold_line_feed):
            query['HoldLineFeed'] = request.hold_line_feed
        if not UtilClient.is_unset(request.image_dpi):
            query['ImageDPI'] = request.image_dpi
        if not UtilClient.is_unset(request.long_picture):
            query['LongPicture'] = request.long_picture
        if not UtilClient.is_unset(request.long_text):
            query['LongText'] = request.long_text
        if not UtilClient.is_unset(request.max_sheet_column):
            query['MaxSheetColumn'] = request.max_sheet_column
        if not UtilClient.is_unset(request.max_sheet_row):
            query['MaxSheetRow'] = request.max_sheet_row
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.pages):
            query['Pages'] = request.pages
        if not UtilClient.is_unset(request.paper_horizontal):
            query['PaperHorizontal'] = request.paper_horizontal
        if not UtilClient.is_unset(request.paper_size):
            query['PaperSize'] = request.paper_size
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.scale_percentage):
            query['ScalePercentage'] = request.scale_percentage
        if not UtilClient.is_unset(request.sheet_count):
            query['SheetCount'] = request.sheet_count
        if not UtilClient.is_unset(request.sheet_index):
            query['SheetIndex'] = request.sheet_index
        if not UtilClient.is_unset(request.show_comments):
            query['ShowComments'] = request.show_comments
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.start_page):
            query['StartPage'] = request.start_page
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.target_uriprefix):
            query['TargetURIPrefix'] = request.target_uriprefix
        if not UtilClient.is_unset(request.trim_policy_shrink):
            query['TrimPolicy'] = request.trim_policy_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not UtilClient.is_unset(request.sources_shrink):
            body['Sources'] = request.sources_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOfficeConversionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateOfficeConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_office_conversion_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        """
        @summary Creates a document format conversion task to convert the format of a document stored in an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports the following input formats:
        Text documents: doc, docx, wps, wpss, docm, dotm, dot, dotx, and html
        Presentation documents: pptx, ppt, pot, potx, pps, ppsx, dps, dpt, pptm, potm, ppsm, and dpss
        Spreadsheet documents: xls, xlt, et, ett, xlsx, xltx, csv, xlsb, xlsm, xltm, and ets
        PDF documents: pdf
        The operation supports the following output formats:
        Image files: png and jpg
        Text files: txt
        PDF files: pdf
        Each input document can be up to 200 MB in size.
        The maximum conversion time is 120 seconds. If the document contains too much or complex content, the conversion may time out.
        The operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can use one of the following methods to query task information:
        Call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.``
        In the region in which the IMM project is located, configure a Simple Message Queue (SMQ) subscription to receive task information notifications. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html). For information about SMQ SDKs, see [Use queues](https://help.aliyun.com/document_detail/32449.html).
        In the region in which the IMM project is located, create an ApsaraMQ for RocketMQ 4.0 instance, a topic, and a group to receive task notifications. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html). For more information about how to use ApsaraMQ for RocketMQ, see [Call HTTP SDKs to send and subscribe to messages](https://help.aliyun.com/document_detail/169009.html).
        In the region in which the IMM project is located, use [EventBridge](https://www.alibabacloud.com/en/product/eventbridge) to receive task information notifications. For more information, see [IMM events](https://help.aliyun.com/document_detail/205730.html).
        
        @param tmp_req: CreateOfficeConversionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOfficeConversionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateOfficeConversionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.trim_policy):
            request.trim_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trim_policy, 'TrimPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.end_page):
            query['EndPage'] = request.end_page
        if not UtilClient.is_unset(request.first_page):
            query['FirstPage'] = request.first_page
        if not UtilClient.is_unset(request.fit_to_height):
            query['FitToHeight'] = request.fit_to_height
        if not UtilClient.is_unset(request.fit_to_width):
            query['FitToWidth'] = request.fit_to_width
        if not UtilClient.is_unset(request.hold_line_feed):
            query['HoldLineFeed'] = request.hold_line_feed
        if not UtilClient.is_unset(request.image_dpi):
            query['ImageDPI'] = request.image_dpi
        if not UtilClient.is_unset(request.long_picture):
            query['LongPicture'] = request.long_picture
        if not UtilClient.is_unset(request.long_text):
            query['LongText'] = request.long_text
        if not UtilClient.is_unset(request.max_sheet_column):
            query['MaxSheetColumn'] = request.max_sheet_column
        if not UtilClient.is_unset(request.max_sheet_row):
            query['MaxSheetRow'] = request.max_sheet_row
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.pages):
            query['Pages'] = request.pages
        if not UtilClient.is_unset(request.paper_horizontal):
            query['PaperHorizontal'] = request.paper_horizontal
        if not UtilClient.is_unset(request.paper_size):
            query['PaperSize'] = request.paper_size
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.scale_percentage):
            query['ScalePercentage'] = request.scale_percentage
        if not UtilClient.is_unset(request.sheet_count):
            query['SheetCount'] = request.sheet_count
        if not UtilClient.is_unset(request.sheet_index):
            query['SheetIndex'] = request.sheet_index
        if not UtilClient.is_unset(request.show_comments):
            query['ShowComments'] = request.show_comments
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.start_page):
            query['StartPage'] = request.start_page
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.target_uriprefix):
            query['TargetURIPrefix'] = request.target_uriprefix
        if not UtilClient.is_unset(request.trim_policy_shrink):
            query['TrimPolicy'] = request.trim_policy_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not UtilClient.is_unset(request.sources_shrink):
            body['Sources'] = request.sources_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOfficeConversionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateOfficeConversionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_office_conversion_task(
        self,
        request: imm_20200930_models.CreateOfficeConversionTaskRequest,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        """
        @summary Creates a document format conversion task to convert the format of a document stored in an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports the following input formats:
        Text documents: doc, docx, wps, wpss, docm, dotm, dot, dotx, and html
        Presentation documents: pptx, ppt, pot, potx, pps, ppsx, dps, dpt, pptm, potm, ppsm, and dpss
        Spreadsheet documents: xls, xlt, et, ett, xlsx, xltx, csv, xlsb, xlsm, xltm, and ets
        PDF documents: pdf
        The operation supports the following output formats:
        Image files: png and jpg
        Text files: txt
        PDF files: pdf
        Each input document can be up to 200 MB in size.
        The maximum conversion time is 120 seconds. If the document contains too much or complex content, the conversion may time out.
        The operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can use one of the following methods to query task information:
        Call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.``
        In the region in which the IMM project is located, configure a Simple Message Queue (SMQ) subscription to receive task information notifications. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html). For information about SMQ SDKs, see [Use queues](https://help.aliyun.com/document_detail/32449.html).
        In the region in which the IMM project is located, create an ApsaraMQ for RocketMQ 4.0 instance, a topic, and a group to receive task notifications. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html). For more information about how to use ApsaraMQ for RocketMQ, see [Call HTTP SDKs to send and subscribe to messages](https://help.aliyun.com/document_detail/169009.html).
        In the region in which the IMM project is located, use [EventBridge](https://www.alibabacloud.com/en/product/eventbridge) to receive task information notifications. For more information, see [IMM events](https://help.aliyun.com/document_detail/205730.html).
        
        @param request: CreateOfficeConversionTaskRequest
        @return: CreateOfficeConversionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_office_conversion_task_with_options(request, runtime)

    async def create_office_conversion_task_async(
        self,
        request: imm_20200930_models.CreateOfficeConversionTaskRequest,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        """
        @summary Creates a document format conversion task to convert the format of a document stored in an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The operation supports the following input formats:
        Text documents: doc, docx, wps, wpss, docm, dotm, dot, dotx, and html
        Presentation documents: pptx, ppt, pot, potx, pps, ppsx, dps, dpt, pptm, potm, ppsm, and dpss
        Spreadsheet documents: xls, xlt, et, ett, xlsx, xltx, csv, xlsb, xlsm, xltm, and ets
        PDF documents: pdf
        The operation supports the following output formats:
        Image files: png and jpg
        Text files: txt
        PDF files: pdf
        Each input document can be up to 200 MB in size.
        The maximum conversion time is 120 seconds. If the document contains too much or complex content, the conversion may time out.
        The operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can use one of the following methods to query task information:
        Call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.``
        In the region in which the IMM project is located, configure a Simple Message Queue (SMQ) subscription to receive task information notifications. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html). For information about SMQ SDKs, see [Use queues](https://help.aliyun.com/document_detail/32449.html).
        In the region in which the IMM project is located, create an ApsaraMQ for RocketMQ 4.0 instance, a topic, and a group to receive task notifications. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html). For more information about how to use ApsaraMQ for RocketMQ, see [Call HTTP SDKs to send and subscribe to messages](https://help.aliyun.com/document_detail/169009.html).
        In the region in which the IMM project is located, use [EventBridge](https://www.alibabacloud.com/en/product/eventbridge) to receive task information notifications. For more information, see [IMM events](https://help.aliyun.com/document_detail/205730.html).
        
        @param request: CreateOfficeConversionTaskRequest
        @return: CreateOfficeConversionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_office_conversion_task_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        tmp_req: imm_20200930_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateProjectResponse:
        """
        @summary Creates a project.
        
        @description    The name of a project must be unique in a region.
        By default, you can create up to 100 projects in a region. If you want to request a quota increase to create more projects, submit a ticket or join the DingTalk chat group (ID: 88490020073).
        After you create a project, you can create other Intelligent Media Management (IMM) resources in the project. For more information, see the following links:
        [CreateDataset](https://help.aliyun.com/document_detail/478160.html)
        [CreateTrigger](https://help.aliyun.com/document_detail/479912.html)
        [CreateBatch](https://help.aliyun.com/document_detail/606694.html)
        [CreateBinding](https://help.aliyun.com/document_detail/478202.html)
        
        @param tmp_req: CreateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateProjectResponse:
        """
        @summary Creates a project.
        
        @description    The name of a project must be unique in a region.
        By default, you can create up to 100 projects in a region. If you want to request a quota increase to create more projects, submit a ticket or join the DingTalk chat group (ID: 88490020073).
        After you create a project, you can create other Intelligent Media Management (IMM) resources in the project. For more information, see the following links:
        [CreateDataset](https://help.aliyun.com/document_detail/478160.html)
        [CreateTrigger](https://help.aliyun.com/document_detail/479912.html)
        [CreateBatch](https://help.aliyun.com/document_detail/606694.html)
        [CreateBinding](https://help.aliyun.com/document_detail/478202.html)
        
        @param tmp_req: CreateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: imm_20200930_models.CreateProjectRequest,
    ) -> imm_20200930_models.CreateProjectResponse:
        """
        @summary Creates a project.
        
        @description    The name of a project must be unique in a region.
        By default, you can create up to 100 projects in a region. If you want to request a quota increase to create more projects, submit a ticket or join the DingTalk chat group (ID: 88490020073).
        After you create a project, you can create other Intelligent Media Management (IMM) resources in the project. For more information, see the following links:
        [CreateDataset](https://help.aliyun.com/document_detail/478160.html)
        [CreateTrigger](https://help.aliyun.com/document_detail/479912.html)
        [CreateBatch](https://help.aliyun.com/document_detail/606694.html)
        [CreateBinding](https://help.aliyun.com/document_detail/478202.html)
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: imm_20200930_models.CreateProjectRequest,
    ) -> imm_20200930_models.CreateProjectResponse:
        """
        @summary Creates a project.
        
        @description    The name of a project must be unique in a region.
        By default, you can create up to 100 projects in a region. If you want to request a quota increase to create more projects, submit a ticket or join the DingTalk chat group (ID: 88490020073).
        After you create a project, you can create other Intelligent Media Management (IMM) resources in the project. For more information, see the following links:
        [CreateDataset](https://help.aliyun.com/document_detail/478160.html)
        [CreateTrigger](https://help.aliyun.com/document_detail/479912.html)
        [CreateBatch](https://help.aliyun.com/document_detail/606694.html)
        [CreateBinding](https://help.aliyun.com/document_detail/478202.html)
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_similar_image_clustering_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateSimilarImageClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateSimilarImageClusteringTaskResponse:
        """
        @summary Clusters images indexed into a dataset by similarity. Image clustering is suitable for image deduplication and selection. For example, you can use image clustering to filter photos in your album that are taken in continuous shooting mode.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note that** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Each call to the operation incrementally processes metadata in the dataset.****`` You can regularly call this operation to process incremental files.
        After clustering is completed, you can call the [QuerySimilarImageClusters](https://help.aliyun.com/document_detail/611304.html) operation to query image clustering results.
        An image cluster contains at lest two images. Removing similar images from the dataset affects existing image clusters. If image deletion reduces the number of images in a cluster to less than 2, the cluster is automatically deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateSimilarImageClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSimilarImageClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateSimilarImageClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimilarImageClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateSimilarImageClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_similar_image_clustering_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateSimilarImageClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateSimilarImageClusteringTaskResponse:
        """
        @summary Clusters images indexed into a dataset by similarity. Image clustering is suitable for image deduplication and selection. For example, you can use image clustering to filter photos in your album that are taken in continuous shooting mode.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note that** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Each call to the operation incrementally processes metadata in the dataset.****`` You can regularly call this operation to process incremental files.
        After clustering is completed, you can call the [QuerySimilarImageClusters](https://help.aliyun.com/document_detail/611304.html) operation to query image clustering results.
        An image cluster contains at lest two images. Removing similar images from the dataset affects existing image clusters. If image deletion reduces the number of images in a cluster to less than 2, the cluster is automatically deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateSimilarImageClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSimilarImageClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateSimilarImageClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimilarImageClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateSimilarImageClusteringTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_similar_image_clustering_task(
        self,
        request: imm_20200930_models.CreateSimilarImageClusteringTaskRequest,
    ) -> imm_20200930_models.CreateSimilarImageClusteringTaskResponse:
        """
        @summary Clusters images indexed into a dataset by similarity. Image clustering is suitable for image deduplication and selection. For example, you can use image clustering to filter photos in your album that are taken in continuous shooting mode.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note that** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Each call to the operation incrementally processes metadata in the dataset.****`` You can regularly call this operation to process incremental files.
        After clustering is completed, you can call the [QuerySimilarImageClusters](https://help.aliyun.com/document_detail/611304.html) operation to query image clustering results.
        An image cluster contains at lest two images. Removing similar images from the dataset affects existing image clusters. If image deletion reduces the number of images in a cluster to less than 2, the cluster is automatically deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateSimilarImageClusteringTaskRequest
        @return: CreateSimilarImageClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_similar_image_clustering_task_with_options(request, runtime)

    async def create_similar_image_clustering_task_async(
        self,
        request: imm_20200930_models.CreateSimilarImageClusteringTaskRequest,
    ) -> imm_20200930_models.CreateSimilarImageClusteringTaskResponse:
        """
        @summary Clusters images indexed into a dataset by similarity. Image clustering is suitable for image deduplication and selection. For example, you can use image clustering to filter photos in your album that are taken in continuous shooting mode.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        *\
        *Note that** Asynchronous processing does not guarantee timely task completion.
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Each call to the operation incrementally processes metadata in the dataset.****`` You can regularly call this operation to process incremental files.
        After clustering is completed, you can call the [QuerySimilarImageClusters](https://help.aliyun.com/document_detail/611304.html) operation to query image clustering results.
        An image cluster contains at lest two images. Removing similar images from the dataset affects existing image clusters. If image deletion reduces the number of images in a cluster to less than 2, the cluster is automatically deleted.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateSimilarImageClusteringTaskRequest
        @return: CreateSimilarImageClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_similar_image_clustering_task_with_options_async(request, runtime)

    def create_story_with_options(
        self,
        tmp_req: imm_20200930_models.CreateStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateStoryResponse:
        """
        @summary Creates a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not UtilClient.is_unset(request.address_shrink):
            body['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_file_count):
            body['MaxFileCount'] = request.max_file_count
        if not UtilClient.is_unset(request.min_file_count):
            body['MinFileCount'] = request.min_file_count
        if not UtilClient.is_unset(request.notify_topic_name):
            body['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_end_time):
            body['StoryEndTime'] = request.story_end_time
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time):
            body['StoryStartTime'] = request.story_start_time
        if not UtilClient.is_unset(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_story_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateStoryResponse:
        """
        @summary Creates a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not UtilClient.is_unset(request.address_shrink):
            body['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_file_count):
            body['MaxFileCount'] = request.max_file_count
        if not UtilClient.is_unset(request.min_file_count):
            body['MinFileCount'] = request.min_file_count
        if not UtilClient.is_unset(request.notify_topic_name):
            body['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_end_time):
            body['StoryEndTime'] = request.story_end_time
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time):
            body['StoryStartTime'] = request.story_start_time
        if not UtilClient.is_unset(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_story(
        self,
        request: imm_20200930_models.CreateStoryRequest,
    ) -> imm_20200930_models.CreateStoryResponse:
        """
        @summary Creates a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateStoryRequest
        @return: CreateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_story_with_options(request, runtime)

    async def create_story_async(
        self,
        request: imm_20200930_models.CreateStoryRequest,
    ) -> imm_20200930_models.CreateStoryResponse:
        """
        @summary Creates a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The operation is an asynchronous operation. After a task is executed, the task information is saved only for seven days. When the retention period ends, the task information can no longer be retrieved. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) to query information about the task. If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateStoryRequest
        @return: CreateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_story_with_options_async(request, runtime)

    def create_trigger_with_options(
        self,
        tmp_req: imm_20200930_models.CreateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateTriggerResponse:
        """
        @summary Creates a trigger. A trigger can trigger Intelligent Media Management (IMM) based on events such as events in Object Storage Service (OSS) to process files, such as images, videos, and documents based on data processing templates.
        
        @description If you want to create a trigger to process data in [OSS](https://help.aliyun.com/document_detail/99372.html), make sure that you have bound the dataset to the OSS bucket where the data is stored. For more information about how to bind a dataset to a bucket, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param tmp_req: CreateTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTriggerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateTriggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            body['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trigger_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateTriggerResponse:
        """
        @summary Creates a trigger. A trigger can trigger Intelligent Media Management (IMM) based on events such as events in Object Storage Service (OSS) to process files, such as images, videos, and documents based on data processing templates.
        
        @description If you want to create a trigger to process data in [OSS](https://help.aliyun.com/document_detail/99372.html), make sure that you have bound the dataset to the OSS bucket where the data is stored. For more information about how to bind a dataset to a bucket, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param tmp_req: CreateTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTriggerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateTriggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            body['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trigger(
        self,
        request: imm_20200930_models.CreateTriggerRequest,
    ) -> imm_20200930_models.CreateTriggerResponse:
        """
        @summary Creates a trigger. A trigger can trigger Intelligent Media Management (IMM) based on events such as events in Object Storage Service (OSS) to process files, such as images, videos, and documents based on data processing templates.
        
        @description If you want to create a trigger to process data in [OSS](https://help.aliyun.com/document_detail/99372.html), make sure that you have bound the dataset to the OSS bucket where the data is stored. For more information about how to bind a dataset to a bucket, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: CreateTriggerRequest
        @return: CreateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_trigger_with_options(request, runtime)

    async def create_trigger_async(
        self,
        request: imm_20200930_models.CreateTriggerRequest,
    ) -> imm_20200930_models.CreateTriggerResponse:
        """
        @summary Creates a trigger. A trigger can trigger Intelligent Media Management (IMM) based on events such as events in Object Storage Service (OSS) to process files, such as images, videos, and documents based on data processing templates.
        
        @description If you want to create a trigger to process data in [OSS](https://help.aliyun.com/document_detail/99372.html), make sure that you have bound the dataset to the OSS bucket where the data is stored. For more information about how to bind a dataset to a bucket, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: CreateTriggerRequest
        @return: CreateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_trigger_with_options_async(request, runtime)

    def create_video_label_classification_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateVideoLabelClassificationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateVideoLabelClassificationTaskResponse:
        """
        @summary Detects the scene, object, and event tag information of video content. Scene information includes categories such as natural landscapes, life scenes, and disaster scenes. Event information includes categories such as talent shows, office events, performances, and production events. Object information includes categories such as tableware, electronic products, furniture, and transportation. Video tag detection supports more than 30 tag categories and thousands of tags.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/2747104.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        For more information about video label detection, see [Video label detection](https://help.aliyun.com/document_detail/477189.html).
        This operation supports multiple video formats, such as MP4, MPEG-TS, MKV, MOV, AVI, FLV, and M3U8.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateVideoLabelClassificationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVideoLabelClassificationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoLabelClassificationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoLabelClassificationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateVideoLabelClassificationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_label_classification_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateVideoLabelClassificationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateVideoLabelClassificationTaskResponse:
        """
        @summary Detects the scene, object, and event tag information of video content. Scene information includes categories such as natural landscapes, life scenes, and disaster scenes. Event information includes categories such as talent shows, office events, performances, and production events. Object information includes categories such as tableware, electronic products, furniture, and transportation. Video tag detection supports more than 30 tag categories and thousands of tags.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/2747104.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        For more information about video label detection, see [Video label detection](https://help.aliyun.com/document_detail/477189.html).
        This operation supports multiple video formats, such as MP4, MPEG-TS, MKV, MOV, AVI, FLV, and M3U8.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param tmp_req: CreateVideoLabelClassificationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVideoLabelClassificationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoLabelClassificationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoLabelClassificationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateVideoLabelClassificationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_label_classification_task(
        self,
        request: imm_20200930_models.CreateVideoLabelClassificationTaskRequest,
    ) -> imm_20200930_models.CreateVideoLabelClassificationTaskResponse:
        """
        @summary Detects the scene, object, and event tag information of video content. Scene information includes categories such as natural landscapes, life scenes, and disaster scenes. Event information includes categories such as talent shows, office events, performances, and production events. Object information includes categories such as tableware, electronic products, furniture, and transportation. Video tag detection supports more than 30 tag categories and thousands of tags.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/2747104.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        For more information about video label detection, see [Video label detection](https://help.aliyun.com/document_detail/477189.html).
        This operation supports multiple video formats, such as MP4, MPEG-TS, MKV, MOV, AVI, FLV, and M3U8.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateVideoLabelClassificationTaskRequest
        @return: CreateVideoLabelClassificationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_video_label_classification_task_with_options(request, runtime)

    async def create_video_label_classification_task_async(
        self,
        request: imm_20200930_models.CreateVideoLabelClassificationTaskRequest,
    ) -> imm_20200930_models.CreateVideoLabelClassificationTaskResponse:
        """
        @summary Detects the scene, object, and event tag information of video content. Scene information includes categories such as natural landscapes, life scenes, and disaster scenes. Event information includes categories such as talent shows, office events, performances, and production events. Object information includes categories such as tableware, electronic products, furniture, and transportation. Video tag detection supports more than 30 tag categories and thousands of tags.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/2747104.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        For more information about video label detection, see [Video label detection](https://help.aliyun.com/document_detail/477189.html).
        This operation supports multiple video formats, such as MP4, MPEG-TS, MKV, MOV, AVI, FLV, and M3U8.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications.
        
        @param request: CreateVideoLabelClassificationTaskRequest
        @return: CreateVideoLabelClassificationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_video_label_classification_task_with_options_async(request, runtime)

    def create_video_moderation_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateVideoModerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateVideoModerationTaskResponse:
        """
        @summary Detects risky or non-compliant content from videos. You can use this operation in scenarios such as intelligent pornography detection, terrorist content and political bias detection, ad violation detection, and logo detection.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The detection result is sent as an asynchronous notification. The Suggestion parameter in asynchronous notifications supports the following values:
        pass: No non-compliant content is found.
        block: Non-compliant content is detected. The Categories field value indicates the non-compliance category. For more information, see [Content moderation results](https://help.aliyun.com/document_detail/2743995.html).
        review: A manual review is needed. After the manual review is completed, an asynchronous notification is sent to inform you about the result.
        The following video frame requirements apply:
        The URLs for video frames must use HTTP or HTTPS.
        Video frames must be in PNG, JPG, JPEG, BMP, GIF, or WebP format.
        The size of a video frame cannot exceed 10 MB.
        The resolution for video frames is not lower than 256 × 256 pixels. A frame resolution lower than this recommended resolution may affect detection accuracy.
        The response time of the operation varies based on the amount of time required to download frames. Make sure that video frames to be detected are stored in a reliable and stable service. We recommend that you store video frames in OSS or cache video frames on Alibaba Cloud CDN.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications. >
        
        @param tmp_req: CreateVideoModerationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVideoModerationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.scenes):
            request.scenes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoModerationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateVideoModerationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_moderation_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateVideoModerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateVideoModerationTaskResponse:
        """
        @summary Detects risky or non-compliant content from videos. You can use this operation in scenarios such as intelligent pornography detection, terrorist content and political bias detection, ad violation detection, and logo detection.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The detection result is sent as an asynchronous notification. The Suggestion parameter in asynchronous notifications supports the following values:
        pass: No non-compliant content is found.
        block: Non-compliant content is detected. The Categories field value indicates the non-compliance category. For more information, see [Content moderation results](https://help.aliyun.com/document_detail/2743995.html).
        review: A manual review is needed. After the manual review is completed, an asynchronous notification is sent to inform you about the result.
        The following video frame requirements apply:
        The URLs for video frames must use HTTP or HTTPS.
        Video frames must be in PNG, JPG, JPEG, BMP, GIF, or WebP format.
        The size of a video frame cannot exceed 10 MB.
        The resolution for video frames is not lower than 256 × 256 pixels. A frame resolution lower than this recommended resolution may affect detection accuracy.
        The response time of the operation varies based on the amount of time required to download frames. Make sure that video frames to be detected are stored in a reliable and stable service. We recommend that you store video frames in OSS or cache video frames on Alibaba Cloud CDN.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications. >
        
        @param tmp_req: CreateVideoModerationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVideoModerationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.scenes):
            request.scenes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoModerationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateVideoModerationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_moderation_task(
        self,
        request: imm_20200930_models.CreateVideoModerationTaskRequest,
    ) -> imm_20200930_models.CreateVideoModerationTaskResponse:
        """
        @summary Detects risky or non-compliant content from videos. You can use this operation in scenarios such as intelligent pornography detection, terrorist content and political bias detection, ad violation detection, and logo detection.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The detection result is sent as an asynchronous notification. The Suggestion parameter in asynchronous notifications supports the following values:
        pass: No non-compliant content is found.
        block: Non-compliant content is detected. The Categories field value indicates the non-compliance category. For more information, see [Content moderation results](https://help.aliyun.com/document_detail/2743995.html).
        review: A manual review is needed. After the manual review is completed, an asynchronous notification is sent to inform you about the result.
        The following video frame requirements apply:
        The URLs for video frames must use HTTP or HTTPS.
        Video frames must be in PNG, JPG, JPEG, BMP, GIF, or WebP format.
        The size of a video frame cannot exceed 10 MB.
        The resolution for video frames is not lower than 256 × 256 pixels. A frame resolution lower than this recommended resolution may affect detection accuracy.
        The response time of the operation varies based on the amount of time required to download frames. Make sure that video frames to be detected are stored in a reliable and stable service. We recommend that you store video frames in OSS or cache video frames on Alibaba Cloud CDN.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications. >
        
        @param request: CreateVideoModerationTaskRequest
        @return: CreateVideoModerationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_video_moderation_task_with_options(request, runtime)

    async def create_video_moderation_task_async(
        self,
        request: imm_20200930_models.CreateVideoModerationTaskRequest,
    ) -> imm_20200930_models.CreateVideoModerationTaskResponse:
        """
        @summary Detects risky or non-compliant content from videos. You can use this operation in scenarios such as intelligent pornography detection, terrorist content and political bias detection, ad violation detection, and logo detection.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        *\
        *Note** Asynchronous processing does not guarantee timely task completion.
        The detection result is sent as an asynchronous notification. The Suggestion parameter in asynchronous notifications supports the following values:
        pass: No non-compliant content is found.
        block: Non-compliant content is detected. The Categories field value indicates the non-compliance category. For more information, see [Content moderation results](https://help.aliyun.com/document_detail/2743995.html).
        review: A manual review is needed. After the manual review is completed, an asynchronous notification is sent to inform you about the result.
        The following video frame requirements apply:
        The URLs for video frames must use HTTP or HTTPS.
        Video frames must be in PNG, JPG, JPEG, BMP, GIF, or WebP format.
        The size of a video frame cannot exceed 10 MB.
        The resolution for video frames is not lower than 256 × 256 pixels. A frame resolution lower than this recommended resolution may affect detection accuracy.
        The response time of the operation varies based on the amount of time required to download frames. Make sure that video frames to be detected are stored in a reliable and stable service. We recommend that you store video frames in OSS or cache video frames on Alibaba Cloud CDN.
        This operation is an asynchronous operation. After a task is executed, the task information is retained only for seven days and cannot be retrieved when the retention period elapses. You can call the [GetTask](https://help.aliyun.com/document_detail/478241.html) or [ListTasks](https://help.aliyun.com/document_detail/478242.html) operation to query information about the task.`` If you specify [Notification](https://help.aliyun.com/document_detail/2743997.html), you can obtain information about the task based on notifications. >
        
        @param request: CreateVideoModerationTaskRequest
        @return: CreateVideoModerationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_video_moderation_task_with_options_async(request, runtime)

    def delete_batch_with_options(
        self,
        request: imm_20200930_models.DeleteBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteBatchResponse:
        """
        @summary Deletes a batch processing task.
        
        @description    You can delete only a batch processing task that is in one of the following states: Ready, Failed, Suspended, and Succeeded.
        Before you delete a batch processing task, you can call the [GetBatch](https://help.aliyun.com/document_detail/479922.html) operation to query the task status. This ensures a successful deletion.
        
        @param request: DeleteBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_batch_with_options_async(
        self,
        request: imm_20200930_models.DeleteBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteBatchResponse:
        """
        @summary Deletes a batch processing task.
        
        @description    You can delete only a batch processing task that is in one of the following states: Ready, Failed, Suspended, and Succeeded.
        Before you delete a batch processing task, you can call the [GetBatch](https://help.aliyun.com/document_detail/479922.html) operation to query the task status. This ensures a successful deletion.
        
        @param request: DeleteBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_batch(
        self,
        request: imm_20200930_models.DeleteBatchRequest,
    ) -> imm_20200930_models.DeleteBatchResponse:
        """
        @summary Deletes a batch processing task.
        
        @description    You can delete only a batch processing task that is in one of the following states: Ready, Failed, Suspended, and Succeeded.
        Before you delete a batch processing task, you can call the [GetBatch](https://help.aliyun.com/document_detail/479922.html) operation to query the task status. This ensures a successful deletion.
        
        @param request: DeleteBatchRequest
        @return: DeleteBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_batch_with_options(request, runtime)

    async def delete_batch_async(
        self,
        request: imm_20200930_models.DeleteBatchRequest,
    ) -> imm_20200930_models.DeleteBatchResponse:
        """
        @summary Deletes a batch processing task.
        
        @description    You can delete only a batch processing task that is in one of the following states: Ready, Failed, Suspended, and Succeeded.
        Before you delete a batch processing task, you can call the [GetBatch](https://help.aliyun.com/document_detail/479922.html) operation to query the task status. This ensures a successful deletion.
        
        @param request: DeleteBatchRequest
        @return: DeleteBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_batch_with_options_async(request, runtime)

    def delete_binding_with_options(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteBindingResponse:
        """
        @summary Deletes the binding between a dataset and an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        If you delete a binding, new changes in the OSS bucket are not synchronized to the dataset. Exercise caution when you perform this operation.
        
        @param request: DeleteBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_binding_with_options_async(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteBindingResponse:
        """
        @summary Deletes the binding between a dataset and an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        If you delete a binding, new changes in the OSS bucket are not synchronized to the dataset. Exercise caution when you perform this operation.
        
        @param request: DeleteBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_binding(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
    ) -> imm_20200930_models.DeleteBindingResponse:
        """
        @summary Deletes the binding between a dataset and an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        If you delete a binding, new changes in the OSS bucket are not synchronized to the dataset. Exercise caution when you perform this operation.
        
        @param request: DeleteBindingRequest
        @return: DeleteBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_binding_with_options(request, runtime)

    async def delete_binding_async(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
    ) -> imm_20200930_models.DeleteBindingResponse:
        """
        @summary Deletes the binding between a dataset and an Object Storage Service (OSS) bucket.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        If you delete a binding, new changes in the OSS bucket are not synchronized to the dataset. Exercise caution when you perform this operation.
        
        @param request: DeleteBindingRequest
        @return: DeleteBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_binding_with_options_async(request, runtime)

    def delete_dataset_with_options(
        self,
        request: imm_20200930_models.DeleteDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteDatasetResponse:
        """
        @summary Deletes a dataset.
        
        @description    Before you delete a dataset, make sure that you have deleted all indexes in the dataset. For more information about how to delete indexes, see [DeleteFileMeta](https://help.aliyun.com/document_detail/478172.html) and [BatchDeleteFileMeta](https://help.aliyun.com/document_detail/478173.html).
        Before you [delete a dataset](https://help.aliyun.com/document_detail/478160.html), make sure that you have deleted all bindings between the dataset and Object Storage Service (OSS) buckets. For more information about how to delete a binding, see [DeleteBinding](https://help.aliyun.com/document_detail/478205.html). The [DeleteBinding](https://help.aliyun.com/document_detail/478205.html) operation does not delete an index that is manually created, even if you set the `Cleanup` parameter to `true`. To delete indexes that are manually created, you must call the [DeleteFileMeta](https://help.aliyun.com/document_detail/478172.html) or [BatchDeleteFileMeta](https://help.aliyun.com/document_detail/478173.html) operation. For more information about the differences between automatically and manually created indexes, see [Create a metadata index](https://help.aliyun.com/document_detail/478166.html).
        
        @param request: DeleteDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        request: imm_20200930_models.DeleteDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteDatasetResponse:
        """
        @summary Deletes a dataset.
        
        @description    Before you delete a dataset, make sure that you have deleted all indexes in the dataset. For more information about how to delete indexes, see [DeleteFileMeta](https://help.aliyun.com/document_detail/478172.html) and [BatchDeleteFileMeta](https://help.aliyun.com/document_detail/478173.html).
        Before you [delete a dataset](https://help.aliyun.com/document_detail/478160.html), make sure that you have deleted all bindings between the dataset and Object Storage Service (OSS) buckets. For more information about how to delete a binding, see [DeleteBinding](https://help.aliyun.com/document_detail/478205.html). The [DeleteBinding](https://help.aliyun.com/document_detail/478205.html) operation does not delete an index that is manually created, even if you set the `Cleanup` parameter to `true`. To delete indexes that are manually created, you must call the [DeleteFileMeta](https://help.aliyun.com/document_detail/478172.html) or [BatchDeleteFileMeta](https://help.aliyun.com/document_detail/478173.html) operation. For more information about the differences between automatically and manually created indexes, see [Create a metadata index](https://help.aliyun.com/document_detail/478166.html).
        
        @param request: DeleteDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        request: imm_20200930_models.DeleteDatasetRequest,
    ) -> imm_20200930_models.DeleteDatasetResponse:
        """
        @summary Deletes a dataset.
        
        @description    Before you delete a dataset, make sure that you have deleted all indexes in the dataset. For more information about how to delete indexes, see [DeleteFileMeta](https://help.aliyun.com/document_detail/478172.html) and [BatchDeleteFileMeta](https://help.aliyun.com/document_detail/478173.html).
        Before you [delete a dataset](https://help.aliyun.com/document_detail/478160.html), make sure that you have deleted all bindings between the dataset and Object Storage Service (OSS) buckets. For more information about how to delete a binding, see [DeleteBinding](https://help.aliyun.com/document_detail/478205.html). The [DeleteBinding](https://help.aliyun.com/document_detail/478205.html) operation does not delete an index that is manually created, even if you set the `Cleanup` parameter to `true`. To delete indexes that are manually created, you must call the [DeleteFileMeta](https://help.aliyun.com/document_detail/478172.html) or [BatchDeleteFileMeta](https://help.aliyun.com/document_detail/478173.html) operation. For more information about the differences between automatically and manually created indexes, see [Create a metadata index](https://help.aliyun.com/document_detail/478166.html).
        
        @param request: DeleteDatasetRequest
        @return: DeleteDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    async def delete_dataset_async(
        self,
        request: imm_20200930_models.DeleteDatasetRequest,
    ) -> imm_20200930_models.DeleteDatasetResponse:
        """
        @summary Deletes a dataset.
        
        @description    Before you delete a dataset, make sure that you have deleted all indexes in the dataset. For more information about how to delete indexes, see [DeleteFileMeta](https://help.aliyun.com/document_detail/478172.html) and [BatchDeleteFileMeta](https://help.aliyun.com/document_detail/478173.html).
        Before you [delete a dataset](https://help.aliyun.com/document_detail/478160.html), make sure that you have deleted all bindings between the dataset and Object Storage Service (OSS) buckets. For more information about how to delete a binding, see [DeleteBinding](https://help.aliyun.com/document_detail/478205.html). The [DeleteBinding](https://help.aliyun.com/document_detail/478205.html) operation does not delete an index that is manually created, even if you set the `Cleanup` parameter to `true`. To delete indexes that are manually created, you must call the [DeleteFileMeta](https://help.aliyun.com/document_detail/478172.html) or [BatchDeleteFileMeta](https://help.aliyun.com/document_detail/478173.html) operation. For more information about the differences between automatically and manually created indexes, see [Create a metadata index](https://help.aliyun.com/document_detail/478166.html).
        
        @param request: DeleteDatasetRequest
        @return: DeleteDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dataset_with_options_async(request, runtime)

    def delete_file_meta_with_options(
        self,
        request: imm_20200930_models.DeleteFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteFileMetaResponse:
        """
        @summary Removes the metadata of a file from a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        A successful deletion message is returned regardless of whether the metadata of the file exists in the dataset.
        >
        The objects stored in Object Storage Service (OSS) or Photo and Drive Service are **not** deleted if you delete metadata from a dataset. If you want to delete the file, call the corresponding operations of OSS and Photo and Drive Service.
        When you delete file metadata, the corresponding face clustering group information and story (if any) are changed, but the spatiotemporal clustering is not changed.
        
        @param request: DeleteFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_meta_with_options_async(
        self,
        request: imm_20200930_models.DeleteFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteFileMetaResponse:
        """
        @summary Removes the metadata of a file from a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        A successful deletion message is returned regardless of whether the metadata of the file exists in the dataset.
        >
        The objects stored in Object Storage Service (OSS) or Photo and Drive Service are **not** deleted if you delete metadata from a dataset. If you want to delete the file, call the corresponding operations of OSS and Photo and Drive Service.
        When you delete file metadata, the corresponding face clustering group information and story (if any) are changed, but the spatiotemporal clustering is not changed.
        
        @param request: DeleteFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file_meta(
        self,
        request: imm_20200930_models.DeleteFileMetaRequest,
    ) -> imm_20200930_models.DeleteFileMetaResponse:
        """
        @summary Removes the metadata of a file from a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        A successful deletion message is returned regardless of whether the metadata of the file exists in the dataset.
        >
        The objects stored in Object Storage Service (OSS) or Photo and Drive Service are **not** deleted if you delete metadata from a dataset. If you want to delete the file, call the corresponding operations of OSS and Photo and Drive Service.
        When you delete file metadata, the corresponding face clustering group information and story (if any) are changed, but the spatiotemporal clustering is not changed.
        
        @param request: DeleteFileMetaRequest
        @return: DeleteFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_file_meta_with_options(request, runtime)

    async def delete_file_meta_async(
        self,
        request: imm_20200930_models.DeleteFileMetaRequest,
    ) -> imm_20200930_models.DeleteFileMetaResponse:
        """
        @summary Removes the metadata of a file from a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        A successful deletion message is returned regardless of whether the metadata of the file exists in the dataset.
        >
        The objects stored in Object Storage Service (OSS) or Photo and Drive Service are **not** deleted if you delete metadata from a dataset. If you want to delete the file, call the corresponding operations of OSS and Photo and Drive Service.
        When you delete file metadata, the corresponding face clustering group information and story (if any) are changed, but the spatiotemporal clustering is not changed.
        
        @param request: DeleteFileMetaRequest
        @return: DeleteFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_meta_with_options_async(request, runtime)

    def delete_location_date_cluster_with_options(
        self,
        request: imm_20200930_models.DeleteLocationDateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteLocationDateClusterResponse:
        """
        @summary Deletes a spatiotemporal cluster.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        Before you call this operation, you must call the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to perform spatiotemporal clustering.
        A successful deletion is returned regardless of whether a spatiotemporal clustering group ID exists.
        
        @param request: DeleteLocationDateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLocationDateClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLocationDateCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteLocationDateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_location_date_cluster_with_options_async(
        self,
        request: imm_20200930_models.DeleteLocationDateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteLocationDateClusterResponse:
        """
        @summary Deletes a spatiotemporal cluster.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        Before you call this operation, you must call the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to perform spatiotemporal clustering.
        A successful deletion is returned regardless of whether a spatiotemporal clustering group ID exists.
        
        @param request: DeleteLocationDateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLocationDateClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLocationDateCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteLocationDateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_location_date_cluster(
        self,
        request: imm_20200930_models.DeleteLocationDateClusterRequest,
    ) -> imm_20200930_models.DeleteLocationDateClusterResponse:
        """
        @summary Deletes a spatiotemporal cluster.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        Before you call this operation, you must call the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to perform spatiotemporal clustering.
        A successful deletion is returned regardless of whether a spatiotemporal clustering group ID exists.
        
        @param request: DeleteLocationDateClusterRequest
        @return: DeleteLocationDateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_location_date_cluster_with_options(request, runtime)

    async def delete_location_date_cluster_async(
        self,
        request: imm_20200930_models.DeleteLocationDateClusterRequest,
    ) -> imm_20200930_models.DeleteLocationDateClusterResponse:
        """
        @summary Deletes a spatiotemporal cluster.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        Before you call this operation, you must call the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to perform spatiotemporal clustering.
        A successful deletion is returned regardless of whether a spatiotemporal clustering group ID exists.
        
        @param request: DeleteLocationDateClusterRequest
        @return: DeleteLocationDateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_location_date_cluster_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: imm_20200930_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteProjectResponse:
        """
        @summary Deletes a project.
        
        @description    Before you delete a project, make sure that all resources in the project, such as datasets, bindings, batch processing tasks, and triggers, are deleted. For more information, see [DeleteDataset](https://help.aliyun.com/document_detail/478164.html), [DeleteBatch](https://help.aliyun.com/document_detail/479918.html), and [DeleteTrigger](https://help.aliyun.com/document_detail/479915.html).
        After a project is deleted, all resources used by the project are recycled, and all related data is lost and cannot be recovered.
        
        @param request: DeleteProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: imm_20200930_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteProjectResponse:
        """
        @summary Deletes a project.
        
        @description    Before you delete a project, make sure that all resources in the project, such as datasets, bindings, batch processing tasks, and triggers, are deleted. For more information, see [DeleteDataset](https://help.aliyun.com/document_detail/478164.html), [DeleteBatch](https://help.aliyun.com/document_detail/479918.html), and [DeleteTrigger](https://help.aliyun.com/document_detail/479915.html).
        After a project is deleted, all resources used by the project are recycled, and all related data is lost and cannot be recovered.
        
        @param request: DeleteProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        request: imm_20200930_models.DeleteProjectRequest,
    ) -> imm_20200930_models.DeleteProjectResponse:
        """
        @summary Deletes a project.
        
        @description    Before you delete a project, make sure that all resources in the project, such as datasets, bindings, batch processing tasks, and triggers, are deleted. For more information, see [DeleteDataset](https://help.aliyun.com/document_detail/478164.html), [DeleteBatch](https://help.aliyun.com/document_detail/479918.html), and [DeleteTrigger](https://help.aliyun.com/document_detail/479915.html).
        After a project is deleted, all resources used by the project are recycled, and all related data is lost and cannot be recovered.
        
        @param request: DeleteProjectRequest
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: imm_20200930_models.DeleteProjectRequest,
    ) -> imm_20200930_models.DeleteProjectResponse:
        """
        @summary Deletes a project.
        
        @description    Before you delete a project, make sure that all resources in the project, such as datasets, bindings, batch processing tasks, and triggers, are deleted. For more information, see [DeleteDataset](https://help.aliyun.com/document_detail/478164.html), [DeleteBatch](https://help.aliyun.com/document_detail/479918.html), and [DeleteTrigger](https://help.aliyun.com/document_detail/479915.html).
        After a project is deleted, all resources used by the project are recycled, and all related data is lost and cannot be recovered.
        
        @param request: DeleteProjectRequest
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delete_story_with_options(
        self,
        request: imm_20200930_models.DeleteStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteStoryResponse:
        """
        @summary Deletes a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param request: DeleteStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_story_with_options_async(
        self,
        request: imm_20200930_models.DeleteStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteStoryResponse:
        """
        @summary Deletes a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param request: DeleteStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_story(
        self,
        request: imm_20200930_models.DeleteStoryRequest,
    ) -> imm_20200930_models.DeleteStoryResponse:
        """
        @summary Deletes a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param request: DeleteStoryRequest
        @return: DeleteStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_story_with_options(request, runtime)

    async def delete_story_async(
        self,
        request: imm_20200930_models.DeleteStoryRequest,
    ) -> imm_20200930_models.DeleteStoryResponse:
        """
        @summary Deletes a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param request: DeleteStoryRequest
        @return: DeleteStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_story_with_options_async(request, runtime)

    def delete_trigger_with_options(
        self,
        request: imm_20200930_models.DeleteTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteTriggerResponse:
        """
        @summary Deletes a trigger.
        
        @description You can delete a trigger only if the trigger is in one of the following states: Ready, Failed, Suspended, and Succeeded. You cannot delete a trigger that is in the Running state.
        
        @param request: DeleteTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trigger_with_options_async(
        self,
        request: imm_20200930_models.DeleteTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteTriggerResponse:
        """
        @summary Deletes a trigger.
        
        @description You can delete a trigger only if the trigger is in one of the following states: Ready, Failed, Suspended, and Succeeded. You cannot delete a trigger that is in the Running state.
        
        @param request: DeleteTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trigger(
        self,
        request: imm_20200930_models.DeleteTriggerRequest,
    ) -> imm_20200930_models.DeleteTriggerResponse:
        """
        @summary Deletes a trigger.
        
        @description You can delete a trigger only if the trigger is in one of the following states: Ready, Failed, Suspended, and Succeeded. You cannot delete a trigger that is in the Running state.
        
        @param request: DeleteTriggerRequest
        @return: DeleteTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_trigger_with_options(request, runtime)

    async def delete_trigger_async(
        self,
        request: imm_20200930_models.DeleteTriggerRequest,
    ) -> imm_20200930_models.DeleteTriggerResponse:
        """
        @summary Deletes a trigger.
        
        @description You can delete a trigger only if the trigger is in one of the following states: Ready, Failed, Suspended, and Succeeded. You cannot delete a trigger that is in the Running state.
        
        @param request: DeleteTriggerRequest
        @return: DeleteTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_trigger_with_options_async(request, runtime)

    def detach_ossbucket_with_options(
        self,
        request: imm_20200930_models.DetachOSSBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetachOSSBucketResponse:
        """
        @summary Unbinds an Object Storage Service (OSS) bucket from the corresponding project.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that the project is bound to a bucket. For more information, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: DetachOSSBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachOSSBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachOSSBucket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetachOSSBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_ossbucket_with_options_async(
        self,
        request: imm_20200930_models.DetachOSSBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetachOSSBucketResponse:
        """
        @summary Unbinds an Object Storage Service (OSS) bucket from the corresponding project.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that the project is bound to a bucket. For more information, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: DetachOSSBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachOSSBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachOSSBucket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetachOSSBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_ossbucket(
        self,
        request: imm_20200930_models.DetachOSSBucketRequest,
    ) -> imm_20200930_models.DetachOSSBucketResponse:
        """
        @summary Unbinds an Object Storage Service (OSS) bucket from the corresponding project.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that the project is bound to a bucket. For more information, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: DetachOSSBucketRequest
        @return: DetachOSSBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_ossbucket_with_options(request, runtime)

    async def detach_ossbucket_async(
        self,
        request: imm_20200930_models.DetachOSSBucketRequest,
    ) -> imm_20200930_models.DetachOSSBucketResponse:
        """
        @summary Unbinds an Object Storage Service (OSS) bucket from the corresponding project.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that the project is bound to a bucket. For more information, see [AttachOSSBucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: DetachOSSBucketRequest
        @return: DetachOSSBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_ossbucket_with_options_async(request, runtime)

    def detect_image_bodies_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageBodiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageBodiesResponse:
        """
        @summary Detects human body information, such as the confidence level and body bounding box, in an image.
        
        @description    Before you call this operation, make sure that an Intelligent Media Management (IMM) project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageBodiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageBodiesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageBodiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sensitivity):
            query['Sensitivity'] = request.sensitivity
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageBodies',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageBodiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_bodies_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageBodiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageBodiesResponse:
        """
        @summary Detects human body information, such as the confidence level and body bounding box, in an image.
        
        @description    Before you call this operation, make sure that an Intelligent Media Management (IMM) project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageBodiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageBodiesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageBodiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sensitivity):
            query['Sensitivity'] = request.sensitivity
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageBodies',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageBodiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_bodies(
        self,
        request: imm_20200930_models.DetectImageBodiesRequest,
    ) -> imm_20200930_models.DetectImageBodiesResponse:
        """
        @summary Detects human body information, such as the confidence level and body bounding box, in an image.
        
        @description    Before you call this operation, make sure that an Intelligent Media Management (IMM) project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageBodiesRequest
        @return: DetectImageBodiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_bodies_with_options(request, runtime)

    async def detect_image_bodies_async(
        self,
        request: imm_20200930_models.DetectImageBodiesRequest,
    ) -> imm_20200930_models.DetectImageBodiesResponse:
        """
        @summary Detects human body information, such as the confidence level and body bounding box, in an image.
        
        @description    Before you call this operation, make sure that an Intelligent Media Management (IMM) project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageBodiesRequest
        @return: DetectImageBodiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_bodies_with_options_async(request, runtime)

    def detect_image_cars_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageCarsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCarsResponse:
        """
        @summary Detects the outline data, attributes, and license plate information of vehicles in an image. The vehicle attributes include the vehicle color (CarColor) and vehicle type (CarType). The license plate information includes the recognition content (Content) and plate frame (Boundary).
        
        @description    For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageCarsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCarsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCarsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCars',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCarsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_cars_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageCarsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCarsResponse:
        """
        @summary Detects the outline data, attributes, and license plate information of vehicles in an image. The vehicle attributes include the vehicle color (CarColor) and vehicle type (CarType). The license plate information includes the recognition content (Content) and plate frame (Boundary).
        
        @description    For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageCarsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCarsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCarsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCars',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCarsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_cars(
        self,
        request: imm_20200930_models.DetectImageCarsRequest,
    ) -> imm_20200930_models.DetectImageCarsResponse:
        """
        @summary Detects the outline data, attributes, and license plate information of vehicles in an image. The vehicle attributes include the vehicle color (CarColor) and vehicle type (CarType). The license plate information includes the recognition content (Content) and plate frame (Boundary).
        
        @description    For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageCarsRequest
        @return: DetectImageCarsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_cars_with_options(request, runtime)

    async def detect_image_cars_async(
        self,
        request: imm_20200930_models.DetectImageCarsRequest,
    ) -> imm_20200930_models.DetectImageCarsResponse:
        """
        @summary Detects the outline data, attributes, and license plate information of vehicles in an image. The vehicle attributes include the vehicle color (CarColor) and vehicle type (CarType). The license plate information includes the recognition content (Content) and plate frame (Boundary).
        
        @description    For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageCarsRequest
        @return: DetectImageCarsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_cars_with_options_async(request, runtime)

    def detect_image_codes_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCodesResponse:
        """
        @summary Detects barcodes and QR codes in an image.
        
        @description    For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageCodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCodes',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_codes_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCodesResponse:
        """
        @summary Detects barcodes and QR codes in an image.
        
        @description    For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageCodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCodes',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_codes(
        self,
        request: imm_20200930_models.DetectImageCodesRequest,
    ) -> imm_20200930_models.DetectImageCodesResponse:
        """
        @summary Detects barcodes and QR codes in an image.
        
        @description    For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageCodesRequest
        @return: DetectImageCodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_codes_with_options(request, runtime)

    async def detect_image_codes_async(
        self,
        request: imm_20200930_models.DetectImageCodesRequest,
    ) -> imm_20200930_models.DetectImageCodesResponse:
        """
        @summary Detects barcodes and QR codes in an image.
        
        @description    For information about the image encoding formats supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageCodesRequest
        @return: DetectImageCodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_codes_with_options_async(request, runtime)

    def detect_image_cropping_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageCroppingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCroppingResponse:
        """
        @summary Detects the cropping area that produces the optimal visual effect based on a given image ratio by using AI model capabilities.
        
        @param tmp_req: DetectImageCroppingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCroppingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCroppingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.aspect_ratios):
            query['AspectRatios'] = request.aspect_ratios
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCropping',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCroppingResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_cropping_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageCroppingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCroppingResponse:
        """
        @summary Detects the cropping area that produces the optimal visual effect based on a given image ratio by using AI model capabilities.
        
        @param tmp_req: DetectImageCroppingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCroppingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCroppingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.aspect_ratios):
            query['AspectRatios'] = request.aspect_ratios
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCropping',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCroppingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_cropping(
        self,
        request: imm_20200930_models.DetectImageCroppingRequest,
    ) -> imm_20200930_models.DetectImageCroppingResponse:
        """
        @summary Detects the cropping area that produces the optimal visual effect based on a given image ratio by using AI model capabilities.
        
        @param request: DetectImageCroppingRequest
        @return: DetectImageCroppingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_cropping_with_options(request, runtime)

    async def detect_image_cropping_async(
        self,
        request: imm_20200930_models.DetectImageCroppingRequest,
    ) -> imm_20200930_models.DetectImageCroppingResponse:
        """
        @summary Detects the cropping area that produces the optimal visual effect based on a given image ratio by using AI model capabilities.
        
        @param request: DetectImageCroppingRequest
        @return: DetectImageCroppingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_cropping_with_options_async(request, runtime)

    def detect_image_faces_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageFacesResponse:
        """
        @summary Detects faces from an image, including face boundary information, attributes, and quality. The boundary information includes the distance from the y-coordinate of the vertex to the top edge (Top), distance from the x-coordinate of the vertex to the left edge (Left), height (Height), and width (Width). Face attributes include the age (Age), age standard deviation (AgeSD), gender (Gender), emotion (Emotion), mouth opening (Mouth), beard (Beard), hat wearing (Hat), mask wearing (Mask), glasses wearing (Glasses), head orientation (HeadPose), attractiveness (Attractive), and confidence levels for preceding attributes. Quality information includes the face quality score (FaceQuality) and face resolution (Sharpness).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        For information about the image encoding formats supported by this operation, see [Limits](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageFacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageFaces',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_faces_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageFacesResponse:
        """
        @summary Detects faces from an image, including face boundary information, attributes, and quality. The boundary information includes the distance from the y-coordinate of the vertex to the top edge (Top), distance from the x-coordinate of the vertex to the left edge (Left), height (Height), and width (Width). Face attributes include the age (Age), age standard deviation (AgeSD), gender (Gender), emotion (Emotion), mouth opening (Mouth), beard (Beard), hat wearing (Hat), mask wearing (Mask), glasses wearing (Glasses), head orientation (HeadPose), attractiveness (Attractive), and confidence levels for preceding attributes. Quality information includes the face quality score (FaceQuality) and face resolution (Sharpness).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        For information about the image encoding formats supported by this operation, see [Limits](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageFacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageFaces',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_faces(
        self,
        request: imm_20200930_models.DetectImageFacesRequest,
    ) -> imm_20200930_models.DetectImageFacesResponse:
        """
        @summary Detects faces from an image, including face boundary information, attributes, and quality. The boundary information includes the distance from the y-coordinate of the vertex to the top edge (Top), distance from the x-coordinate of the vertex to the left edge (Left), height (Height), and width (Width). Face attributes include the age (Age), age standard deviation (AgeSD), gender (Gender), emotion (Emotion), mouth opening (Mouth), beard (Beard), hat wearing (Hat), mask wearing (Mask), glasses wearing (Glasses), head orientation (HeadPose), attractiveness (Attractive), and confidence levels for preceding attributes. Quality information includes the face quality score (FaceQuality) and face resolution (Sharpness).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        For information about the image encoding formats supported by this operation, see [Limits](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageFacesRequest
        @return: DetectImageFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_faces_with_options(request, runtime)

    async def detect_image_faces_async(
        self,
        request: imm_20200930_models.DetectImageFacesRequest,
    ) -> imm_20200930_models.DetectImageFacesResponse:
        """
        @summary Detects faces from an image, including face boundary information, attributes, and quality. The boundary information includes the distance from the y-coordinate of the vertex to the top edge (Top), distance from the x-coordinate of the vertex to the left edge (Left), height (Height), and width (Width). Face attributes include the age (Age), age standard deviation (AgeSD), gender (Gender), emotion (Emotion), mouth opening (Mouth), beard (Beard), hat wearing (Hat), mask wearing (Mask), glasses wearing (Glasses), head orientation (HeadPose), attractiveness (Attractive), and confidence levels for preceding attributes. Quality information includes the face quality score (FaceQuality) and face resolution (Sharpness).
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        For information about the image encoding formats supported by this operation, see [Limits](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageFacesRequest
        @return: DetectImageFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_faces_with_options_async(request, runtime)

    def detect_image_labels_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        """
        @summary Detects scene, object, and event information in an image. Scene information includes natural landscapes, daily life, and disasters. Event information includes talent shows, office events, performances, and production events. Object information includes tableware, electronics, furniture, and transportation. The DetectImageLabels operation supports more than 30 different categories and thousands of labels.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Make sure that an IMM [project](https://help.aliyun.com/document_detail/478273.html) is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For more information about the features of this operation, see [Image label detection](https://help.aliyun.com/document_detail/477179.html).
        For more information about the input images supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageLabelsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageLabelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageLabels',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_labels_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        """
        @summary Detects scene, object, and event information in an image. Scene information includes natural landscapes, daily life, and disasters. Event information includes talent shows, office events, performances, and production events. Object information includes tableware, electronics, furniture, and transportation. The DetectImageLabels operation supports more than 30 different categories and thousands of labels.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Make sure that an IMM [project](https://help.aliyun.com/document_detail/478273.html) is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For more information about the features of this operation, see [Image label detection](https://help.aliyun.com/document_detail/477179.html).
        For more information about the input images supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageLabelsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageLabelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageLabels',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_labels(
        self,
        request: imm_20200930_models.DetectImageLabelsRequest,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        """
        @summary Detects scene, object, and event information in an image. Scene information includes natural landscapes, daily life, and disasters. Event information includes talent shows, office events, performances, and production events. Object information includes tableware, electronics, furniture, and transportation. The DetectImageLabels operation supports more than 30 different categories and thousands of labels.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Make sure that an IMM [project](https://help.aliyun.com/document_detail/478273.html) is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For more information about the features of this operation, see [Image label detection](https://help.aliyun.com/document_detail/477179.html).
        For more information about the input images supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageLabelsRequest
        @return: DetectImageLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_labels_with_options(request, runtime)

    async def detect_image_labels_async(
        self,
        request: imm_20200930_models.DetectImageLabelsRequest,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        """
        @summary Detects scene, object, and event information in an image. Scene information includes natural landscapes, daily life, and disasters. Event information includes talent shows, office events, performances, and production events. Object information includes tableware, electronics, furniture, and transportation. The DetectImageLabels operation supports more than 30 different categories and thousands of labels.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Make sure that an IMM [project](https://help.aliyun.com/document_detail/478273.html) is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        For more information about the features of this operation, see [Image label detection](https://help.aliyun.com/document_detail/477179.html).
        For more information about the input images supported by this operation, see [Limits on images](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageLabelsRequest
        @return: DetectImageLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_labels_with_options_async(request, runtime)

    def detect_image_score_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageScoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageScoreResponse:
        """
        @summary Calculates the aesthetics quality score of an image based on metrics such as the composition, brightness, contrast, color, and resolution. The operation returns a score within the range from 0 to 1. A higher score indicates better image quality.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478273.html).[](~~478152~~)
        For information about the image encoding formats supported by this operation, see [Limits](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageScoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageScoreResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageScoreShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageScore',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageScoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_score_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageScoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageScoreResponse:
        """
        @summary Calculates the aesthetics quality score of an image based on metrics such as the composition, brightness, contrast, color, and resolution. The operation returns a score within the range from 0 to 1. A higher score indicates better image quality.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478273.html).[](~~478152~~)
        For information about the image encoding formats supported by this operation, see [Limits](https://help.aliyun.com/document_detail/475569.html).
        
        @param tmp_req: DetectImageScoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageScoreResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageScoreShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageScore',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageScoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_score(
        self,
        request: imm_20200930_models.DetectImageScoreRequest,
    ) -> imm_20200930_models.DetectImageScoreResponse:
        """
        @summary Calculates the aesthetics quality score of an image based on metrics such as the composition, brightness, contrast, color, and resolution. The operation returns a score within the range from 0 to 1. A higher score indicates better image quality.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478273.html).[](~~478152~~)
        For information about the image encoding formats supported by this operation, see [Limits](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageScoreRequest
        @return: DetectImageScoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_score_with_options(request, runtime)

    async def detect_image_score_async(
        self,
        request: imm_20200930_models.DetectImageScoreRequest,
    ) -> imm_20200930_models.DetectImageScoreResponse:
        """
        @summary Calculates the aesthetics quality score of an image based on metrics such as the composition, brightness, contrast, color, and resolution. The operation returns a score within the range from 0 to 1. A higher score indicates better image quality.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478273.html).[](~~478152~~)
        For information about the image encoding formats supported by this operation, see [Limits](https://help.aliyun.com/document_detail/475569.html).
        
        @param request: DetectImageScoreRequest
        @return: DetectImageScoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_score_with_options_async(request, runtime)

    def detect_image_texts_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageTextsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageTextsResponse:
        """
        @summary Recognizes and extracts text content from an image.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The size of the image cannot exceed 20 MB.
        The shortest side of the image is not less than 20 px, and the longest side is not more than 30,000 px.
        The aspect ratio of the image is less than 1:2.
        We recommend that you do not use an image that is smaller than 15 px × 15 px in size. Otherwise, the recognition rate is low.
        
        @param tmp_req: DetectImageTextsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageTextsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageTextsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageTexts',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageTextsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_texts_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageTextsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageTextsResponse:
        """
        @summary Recognizes and extracts text content from an image.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The size of the image cannot exceed 20 MB.
        The shortest side of the image is not less than 20 px, and the longest side is not more than 30,000 px.
        The aspect ratio of the image is less than 1:2.
        We recommend that you do not use an image that is smaller than 15 px × 15 px in size. Otherwise, the recognition rate is low.
        
        @param tmp_req: DetectImageTextsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageTextsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageTextsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageTexts',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageTextsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_texts(
        self,
        request: imm_20200930_models.DetectImageTextsRequest,
    ) -> imm_20200930_models.DetectImageTextsResponse:
        """
        @summary Recognizes and extracts text content from an image.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The size of the image cannot exceed 20 MB.
        The shortest side of the image is not less than 20 px, and the longest side is not more than 30,000 px.
        The aspect ratio of the image is less than 1:2.
        We recommend that you do not use an image that is smaller than 15 px × 15 px in size. Otherwise, the recognition rate is low.
        
        @param request: DetectImageTextsRequest
        @return: DetectImageTextsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_texts_with_options(request, runtime)

    async def detect_image_texts_async(
        self,
        request: imm_20200930_models.DetectImageTextsRequest,
    ) -> imm_20200930_models.DetectImageTextsResponse:
        """
        @summary Recognizes and extracts text content from an image.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The size of the image cannot exceed 20 MB.
        The shortest side of the image is not less than 20 px, and the longest side is not more than 30,000 px.
        The aspect ratio of the image is less than 1:2.
        We recommend that you do not use an image that is smaller than 15 px × 15 px in size. Otherwise, the recognition rate is low.
        
        @param request: DetectImageTextsRequest
        @return: DetectImageTextsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_texts_with_options_async(request, runtime)

    def detect_media_meta_with_options(
        self,
        tmp_req: imm_20200930_models.DetectMediaMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectMediaMetaResponse:
        """
        @summary Queries media metadata, including the media format and stream information.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        
        @param tmp_req: DetectMediaMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectMediaMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectMediaMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectMediaMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectMediaMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_media_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectMediaMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectMediaMetaResponse:
        """
        @summary Queries media metadata, including the media format and stream information.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        
        @param tmp_req: DetectMediaMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectMediaMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectMediaMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectMediaMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectMediaMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_media_meta(
        self,
        request: imm_20200930_models.DetectMediaMetaRequest,
    ) -> imm_20200930_models.DetectMediaMetaResponse:
        """
        @summary Queries media metadata, including the media format and stream information.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        
        @param request: DetectMediaMetaRequest
        @return: DetectMediaMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_media_meta_with_options(request, runtime)

    async def detect_media_meta_async(
        self,
        request: imm_20200930_models.DetectMediaMetaRequest,
    ) -> imm_20200930_models.DetectMediaMetaResponse:
        """
        @summary Queries media metadata, including the media format and stream information.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478152.html).
        
        @param request: DetectMediaMetaRequest
        @return: DetectMediaMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_media_meta_with_options_async(request, runtime)

    def detect_text_anomaly_with_options(
        self,
        request: imm_20200930_models.DetectTextAnomalyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectTextAnomalyResponse:
        """
        @summary Detects whether specified text contains anomalies, such as pornography, advertisements, excessive junk content, politically sensitive content, and abuse.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        >  The text compliance detection feature only supports Chinese characters.
        
        @param request: DetectTextAnomalyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectTextAnomalyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectTextAnomaly',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectTextAnomalyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_text_anomaly_with_options_async(
        self,
        request: imm_20200930_models.DetectTextAnomalyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectTextAnomalyResponse:
        """
        @summary Detects whether specified text contains anomalies, such as pornography, advertisements, excessive junk content, politically sensitive content, and abuse.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        >  The text compliance detection feature only supports Chinese characters.
        
        @param request: DetectTextAnomalyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectTextAnomalyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectTextAnomaly',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectTextAnomalyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_text_anomaly(
        self,
        request: imm_20200930_models.DetectTextAnomalyRequest,
    ) -> imm_20200930_models.DetectTextAnomalyResponse:
        """
        @summary Detects whether specified text contains anomalies, such as pornography, advertisements, excessive junk content, politically sensitive content, and abuse.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        >  The text compliance detection feature only supports Chinese characters.
        
        @param request: DetectTextAnomalyRequest
        @return: DetectTextAnomalyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_text_anomaly_with_options(request, runtime)

    async def detect_text_anomaly_async(
        self,
        request: imm_20200930_models.DetectTextAnomalyRequest,
    ) -> imm_20200930_models.DetectTextAnomalyResponse:
        """
        @summary Detects whether specified text contains anomalies, such as pornography, advertisements, excessive junk content, politically sensitive content, and abuse.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        >  The text compliance detection feature only supports Chinese characters.
        
        @param request: DetectTextAnomalyRequest
        @return: DetectTextAnomalyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_text_anomaly_with_options_async(request, runtime)

    def encode_blind_watermark_with_options(
        self,
        request: imm_20200930_models.EncodeBlindWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.EncodeBlindWatermarkResponse:
        """
        @summary Embeds specific textual information into an image as watermarks. These watermarks are visually imperceptible and do not affect the aesthetics of the image or the integrity of the original data. The watermarks can be extracted by using the CreateDecodeBlindWatermarkTask operation.
        
        @description    Before you call this operation, make sure that you are familiar with the billing of Intelligent Media Management (IMM).
        Make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        You can embed only text as blind watermarks to an image.
        The format of the output image is the same as that of the input image.
        The watermarks can still be extracted even if attacks, such as compression, scaling, cropping, rotation, and color transformation, are performed on the image.
        Pure black and white images and images with low resolution (roughly less than 200 px × 200 px,) are not supported.
        
        @param request: EncodeBlindWatermarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncodeBlindWatermarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EncodeBlindWatermark',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.EncodeBlindWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def encode_blind_watermark_with_options_async(
        self,
        request: imm_20200930_models.EncodeBlindWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.EncodeBlindWatermarkResponse:
        """
        @summary Embeds specific textual information into an image as watermarks. These watermarks are visually imperceptible and do not affect the aesthetics of the image or the integrity of the original data. The watermarks can be extracted by using the CreateDecodeBlindWatermarkTask operation.
        
        @description    Before you call this operation, make sure that you are familiar with the billing of Intelligent Media Management (IMM).
        Make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        You can embed only text as blind watermarks to an image.
        The format of the output image is the same as that of the input image.
        The watermarks can still be extracted even if attacks, such as compression, scaling, cropping, rotation, and color transformation, are performed on the image.
        Pure black and white images and images with low resolution (roughly less than 200 px × 200 px,) are not supported.
        
        @param request: EncodeBlindWatermarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncodeBlindWatermarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EncodeBlindWatermark',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.EncodeBlindWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encode_blind_watermark(
        self,
        request: imm_20200930_models.EncodeBlindWatermarkRequest,
    ) -> imm_20200930_models.EncodeBlindWatermarkResponse:
        """
        @summary Embeds specific textual information into an image as watermarks. These watermarks are visually imperceptible and do not affect the aesthetics of the image or the integrity of the original data. The watermarks can be extracted by using the CreateDecodeBlindWatermarkTask operation.
        
        @description    Before you call this operation, make sure that you are familiar with the billing of Intelligent Media Management (IMM).
        Make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        You can embed only text as blind watermarks to an image.
        The format of the output image is the same as that of the input image.
        The watermarks can still be extracted even if attacks, such as compression, scaling, cropping, rotation, and color transformation, are performed on the image.
        Pure black and white images and images with low resolution (roughly less than 200 px × 200 px,) are not supported.
        
        @param request: EncodeBlindWatermarkRequest
        @return: EncodeBlindWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.encode_blind_watermark_with_options(request, runtime)

    async def encode_blind_watermark_async(
        self,
        request: imm_20200930_models.EncodeBlindWatermarkRequest,
    ) -> imm_20200930_models.EncodeBlindWatermarkResponse:
        """
        @summary Embeds specific textual information into an image as watermarks. These watermarks are visually imperceptible and do not affect the aesthetics of the image or the integrity of the original data. The watermarks can be extracted by using the CreateDecodeBlindWatermarkTask operation.
        
        @description    Before you call this operation, make sure that you are familiar with the billing of Intelligent Media Management (IMM).
        Make sure that an IMM project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        You can embed only text as blind watermarks to an image.
        The format of the output image is the same as that of the input image.
        The watermarks can still be extracted even if attacks, such as compression, scaling, cropping, rotation, and color transformation, are performed on the image.
        Pure black and white images and images with low resolution (roughly less than 200 px × 200 px,) are not supported.
        
        @param request: EncodeBlindWatermarkRequest
        @return: EncodeBlindWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.encode_blind_watermark_with_options_async(request, runtime)

    def extract_document_text_with_options(
        self,
        tmp_req: imm_20200930_models.ExtractDocumentTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ExtractDocumentTextResponse:
        """
        @summary Extracts the text from the document body.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).**\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478273.html).[](~~478152~~)
        The following document formats are supported: Word, Excel, PPT, PDF, and TXT.
        The document cannot exceed 200 MB in size. The size of the extracted text cannot exceed 2 MB in size (approximately 1.2 million letters).
        >  If the format of the document is complex or the document body is too large, a timeout error may occur. In this case, we recommend that you call the CreateOfficeConversionTask operation to convert the document to the TXT format before you call the ExtractDocumentText operation.
        
        @param tmp_req: ExtractDocumentTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExtractDocumentTextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ExtractDocumentTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExtractDocumentText',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ExtractDocumentTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def extract_document_text_with_options_async(
        self,
        tmp_req: imm_20200930_models.ExtractDocumentTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ExtractDocumentTextResponse:
        """
        @summary Extracts the text from the document body.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).**\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478273.html).[](~~478152~~)
        The following document formats are supported: Word, Excel, PPT, PDF, and TXT.
        The document cannot exceed 200 MB in size. The size of the extracted text cannot exceed 2 MB in size (approximately 1.2 million letters).
        >  If the format of the document is complex or the document body is too large, a timeout error may occur. In this case, we recommend that you call the CreateOfficeConversionTask operation to convert the document to the TXT format before you call the ExtractDocumentText operation.
        
        @param tmp_req: ExtractDocumentTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExtractDocumentTextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ExtractDocumentTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExtractDocumentText',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ExtractDocumentTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extract_document_text(
        self,
        request: imm_20200930_models.ExtractDocumentTextRequest,
    ) -> imm_20200930_models.ExtractDocumentTextResponse:
        """
        @summary Extracts the text from the document body.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).**\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478273.html).[](~~478152~~)
        The following document formats are supported: Word, Excel, PPT, PDF, and TXT.
        The document cannot exceed 200 MB in size. The size of the extracted text cannot exceed 2 MB in size (approximately 1.2 million letters).
        >  If the format of the document is complex or the document body is too large, a timeout error may occur. In this case, we recommend that you call the CreateOfficeConversionTask operation to convert the document to the TXT format before you call the ExtractDocumentText operation.
        
        @param request: ExtractDocumentTextRequest
        @return: ExtractDocumentTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.extract_document_text_with_options(request, runtime)

    async def extract_document_text_async(
        self,
        request: imm_20200930_models.ExtractDocumentTextRequest,
    ) -> imm_20200930_models.ExtractDocumentTextResponse:
        """
        @summary Extracts the text from the document body.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).**\
        Make sure that the specified project exists in the current region. For more information, see [Project management](https://help.aliyun.com/document_detail/478273.html).[](~~478152~~)
        The following document formats are supported: Word, Excel, PPT, PDF, and TXT.
        The document cannot exceed 200 MB in size. The size of the extracted text cannot exceed 2 MB in size (approximately 1.2 million letters).
        >  If the format of the document is complex or the document body is too large, a timeout error may occur. In this case, we recommend that you call the CreateOfficeConversionTask operation to convert the document to the TXT format before you call the ExtractDocumentText operation.
        
        @param request: ExtractDocumentTextRequest
        @return: ExtractDocumentTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.extract_document_text_with_options_async(request, runtime)

    def fuzzy_query_with_options(
        self,
        tmp_req: imm_20200930_models.FuzzyQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        """
        @summary Queries the extracted file metadata, including the file name, labels, path, custom tags, text, and other fields. If the value of a metadata field of a file matches the specified string, the metadata of the file is returned.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 88490020073) and share your questions with us.
        For information about the fields that you can use as query conditions, see [Supported fields and operators](https://help.aliyun.com/document_detail/2743991.html).
        
        @param tmp_req: FuzzyQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FuzzyQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.FuzzyQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FuzzyQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.FuzzyQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def fuzzy_query_with_options_async(
        self,
        tmp_req: imm_20200930_models.FuzzyQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        """
        @summary Queries the extracted file metadata, including the file name, labels, path, custom tags, text, and other fields. If the value of a metadata field of a file matches the specified string, the metadata of the file is returned.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 88490020073) and share your questions with us.
        For information about the fields that you can use as query conditions, see [Supported fields and operators](https://help.aliyun.com/document_detail/2743991.html).
        
        @param tmp_req: FuzzyQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FuzzyQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.FuzzyQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FuzzyQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.FuzzyQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fuzzy_query(
        self,
        request: imm_20200930_models.FuzzyQueryRequest,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        """
        @summary Queries the extracted file metadata, including the file name, labels, path, custom tags, text, and other fields. If the value of a metadata field of a file matches the specified string, the metadata of the file is returned.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 88490020073) and share your questions with us.
        For information about the fields that you can use as query conditions, see [Supported fields and operators](https://help.aliyun.com/document_detail/2743991.html).
        
        @param request: FuzzyQueryRequest
        @return: FuzzyQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fuzzy_query_with_options(request, runtime)

    async def fuzzy_query_async(
        self,
        request: imm_20200930_models.FuzzyQueryRequest,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        """
        @summary Queries the extracted file metadata, including the file name, labels, path, custom tags, text, and other fields. If the value of a metadata field of a file matches the specified string, the metadata of the file is returned.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 88490020073) and share your questions with us.
        For information about the fields that you can use as query conditions, see [Supported fields and operators](https://help.aliyun.com/document_detail/2743991.html).
        
        @param request: FuzzyQueryRequest
        @return: FuzzyQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fuzzy_query_with_options_async(request, runtime)

    def generate_video_playlist_with_options(
        self,
        tmp_req: imm_20200930_models.GenerateVideoPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GenerateVideoPlaylistResponse:
        """
        @summary Generates a live transcoding playlist and converts video files into M3U8 files. After a playlist is generated, the videos in the playlist are immediately played and the video files are transcoded based on the playback progress. Compared with offline transcoding, online transcoding significantly reduces the time spent in waiting for the videos to be transcoded and reduces transcoding and storage costs.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).**\
        Make sure that the project that you want to use is available in the current region. For more information, see [Project Management](https://help.aliyun.com/document_detail/478152.html).
        By default, you can call this operation to process only one video, audio, or subtitle track. You can specify the number of the video, audio, or subtitle tracks that you want to process.
        You can call this operation to generate a media playlist and a master playlist. For more information, see the parameter description.
        This operation is a synchronous operation. Synchronous or asynchronous transcoding is triggered only during playback or pre-transcoding. You can configure the [Notification](https://help.aliyun.com/document_detail/2743997.html) parameter to obtain the transcoding task result.
        For information about the feature description of this operation, see [Live transcoding](https://help.aliyun.com/document_detail/477192.html).
        The data processing capability of Object Storage Service (OSS) also provides the playlist generation feature. However, this feature can generate only a media playlist, and related parameters are simplified.
        
        @param tmp_req: GenerateVideoPlaylistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateVideoPlaylistResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GenerateVideoPlaylistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.source_subtitles):
            request.source_subtitles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_subtitles, 'SourceSubtitles', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.master_uri):
            query['MasterURI'] = request.master_uri
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.overwrite_policy):
            query['OverwritePolicy'] = request.overwrite_policy
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_duration):
            query['SourceDuration'] = request.source_duration
        if not UtilClient.is_unset(request.source_start_time):
            query['SourceStartTime'] = request.source_start_time
        if not UtilClient.is_unset(request.source_subtitles_shrink):
            query['SourceSubtitles'] = request.source_subtitles_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateVideoPlaylist',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GenerateVideoPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_video_playlist_with_options_async(
        self,
        tmp_req: imm_20200930_models.GenerateVideoPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GenerateVideoPlaylistResponse:
        """
        @summary Generates a live transcoding playlist and converts video files into M3U8 files. After a playlist is generated, the videos in the playlist are immediately played and the video files are transcoded based on the playback progress. Compared with offline transcoding, online transcoding significantly reduces the time spent in waiting for the videos to be transcoded and reduces transcoding and storage costs.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).**\
        Make sure that the project that you want to use is available in the current region. For more information, see [Project Management](https://help.aliyun.com/document_detail/478152.html).
        By default, you can call this operation to process only one video, audio, or subtitle track. You can specify the number of the video, audio, or subtitle tracks that you want to process.
        You can call this operation to generate a media playlist and a master playlist. For more information, see the parameter description.
        This operation is a synchronous operation. Synchronous or asynchronous transcoding is triggered only during playback or pre-transcoding. You can configure the [Notification](https://help.aliyun.com/document_detail/2743997.html) parameter to obtain the transcoding task result.
        For information about the feature description of this operation, see [Live transcoding](https://help.aliyun.com/document_detail/477192.html).
        The data processing capability of Object Storage Service (OSS) also provides the playlist generation feature. However, this feature can generate only a media playlist, and related parameters are simplified.
        
        @param tmp_req: GenerateVideoPlaylistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateVideoPlaylistResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GenerateVideoPlaylistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.source_subtitles):
            request.source_subtitles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_subtitles, 'SourceSubtitles', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.master_uri):
            query['MasterURI'] = request.master_uri
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.overwrite_policy):
            query['OverwritePolicy'] = request.overwrite_policy
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_duration):
            query['SourceDuration'] = request.source_duration
        if not UtilClient.is_unset(request.source_start_time):
            query['SourceStartTime'] = request.source_start_time
        if not UtilClient.is_unset(request.source_subtitles_shrink):
            query['SourceSubtitles'] = request.source_subtitles_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateVideoPlaylist',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GenerateVideoPlaylistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_video_playlist(
        self,
        request: imm_20200930_models.GenerateVideoPlaylistRequest,
    ) -> imm_20200930_models.GenerateVideoPlaylistResponse:
        """
        @summary Generates a live transcoding playlist and converts video files into M3U8 files. After a playlist is generated, the videos in the playlist are immediately played and the video files are transcoded based on the playback progress. Compared with offline transcoding, online transcoding significantly reduces the time spent in waiting for the videos to be transcoded and reduces transcoding and storage costs.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).**\
        Make sure that the project that you want to use is available in the current region. For more information, see [Project Management](https://help.aliyun.com/document_detail/478152.html).
        By default, you can call this operation to process only one video, audio, or subtitle track. You can specify the number of the video, audio, or subtitle tracks that you want to process.
        You can call this operation to generate a media playlist and a master playlist. For more information, see the parameter description.
        This operation is a synchronous operation. Synchronous or asynchronous transcoding is triggered only during playback or pre-transcoding. You can configure the [Notification](https://help.aliyun.com/document_detail/2743997.html) parameter to obtain the transcoding task result.
        For information about the feature description of this operation, see [Live transcoding](https://help.aliyun.com/document_detail/477192.html).
        The data processing capability of Object Storage Service (OSS) also provides the playlist generation feature. However, this feature can generate only a media playlist, and related parameters are simplified.
        
        @param request: GenerateVideoPlaylistRequest
        @return: GenerateVideoPlaylistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_video_playlist_with_options(request, runtime)

    async def generate_video_playlist_async(
        self,
        request: imm_20200930_models.GenerateVideoPlaylistRequest,
    ) -> imm_20200930_models.GenerateVideoPlaylistResponse:
        """
        @summary Generates a live transcoding playlist and converts video files into M3U8 files. After a playlist is generated, the videos in the playlist are immediately played and the video files are transcoded based on the playback progress. Compared with offline transcoding, online transcoding significantly reduces the time spent in waiting for the videos to be transcoded and reduces transcoding and storage costs.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).**\
        Make sure that the project that you want to use is available in the current region. For more information, see [Project Management](https://help.aliyun.com/document_detail/478152.html).
        By default, you can call this operation to process only one video, audio, or subtitle track. You can specify the number of the video, audio, or subtitle tracks that you want to process.
        You can call this operation to generate a media playlist and a master playlist. For more information, see the parameter description.
        This operation is a synchronous operation. Synchronous or asynchronous transcoding is triggered only during playback or pre-transcoding. You can configure the [Notification](https://help.aliyun.com/document_detail/2743997.html) parameter to obtain the transcoding task result.
        For information about the feature description of this operation, see [Live transcoding](https://help.aliyun.com/document_detail/477192.html).
        The data processing capability of Object Storage Service (OSS) also provides the playlist generation feature. However, this feature can generate only a media playlist, and related parameters are simplified.
        
        @param request: GenerateVideoPlaylistRequest
        @return: GenerateVideoPlaylistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_video_playlist_with_options_async(request, runtime)

    def generate_weboffice_token_with_options(
        self,
        tmp_req: imm_20200930_models.GenerateWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GenerateWebofficeTokenResponse:
        """
        @summary Generates an access token for document preview or editing.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The operation generates an access token that is valid for 30 minutes and a refresh token that is valid for 1 day.
        The returned expiration time is in UTC.
        The operation supports the following document types:
        Word files: .doc, .docx, .txt, .dot, .wps, .wpt, .dotx, .docm, .dotm, and .rtf
        Presentation files: .ppt, .pptx, .pptm, .ppsx, .ppsm, .pps, .potx, .potm, .dpt, and .dps
        Spreadsheet documents: .et, .xls, .xlt, .xlsx, .xlsm, .xltx, .xltm, and .csv
        PDF files: .pdf
        The operation supports an input document that is up to 200 MB in size.
        The operation supports an input document that contains up to 5,000 pages.
        For a project created before December 1, 2023, you are charged for previewing or editing a document in the project based on the number of times the document is opened. For a project created on or after December 1, 2023, you are charged based on the number of API operation calls made for previewing or editing a document. If you want to switch to API call-based billing for document previewing and editing, use a project created on or after December 1, 2023. In API call-based billing, one API call allows only one user to use the feature. If multiple users use the information returned by the API call, only the last user has access to the document and the access permissions of other users are revoked.
        You can use the NotifyTopicName parameter to specify a Simple Message Queue (SMQ) topic in the same region as the IMM project for getting notified of file save operations. For more information about how to send and receive messages by using the SMQ SDK, see [Use queues](https://help.aliyun.com/document_detail/32449.html). For more information about the JSON example of the Message field, see [WebOffice message example](https://help.aliyun.com/document_detail/2743999.html).
        >  To manage multiple versions of the document, you must enable versioning for the bucket that stores the document and set the History parameter to true.
        
        @param tmp_req: GenerateWebofficeTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateWebofficeTokenResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GenerateWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.permission):
            request.permission_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.permission, 'Permission', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        query = {}
        if not UtilClient.is_unset(request.cache_preview):
            query['CachePreview'] = request.cache_preview
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.external_uploaded):
            query['ExternalUploaded'] = request.external_uploaded
        if not UtilClient.is_unset(request.filename):
            query['Filename'] = request.filename
        if not UtilClient.is_unset(request.hidecmb):
            query['Hidecmb'] = request.hidecmb
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.permission_shrink):
            query['Permission'] = request.permission_shrink
        if not UtilClient.is_unset(request.preview_pages):
            query['PreviewPages'] = request.preview_pages
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.referer):
            query['Referer'] = request.referer
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.user_shrink):
            query['User'] = request.user_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.watermark_shrink):
            query['Watermark'] = request.watermark_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GenerateWebofficeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_weboffice_token_with_options_async(
        self,
        tmp_req: imm_20200930_models.GenerateWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GenerateWebofficeTokenResponse:
        """
        @summary Generates an access token for document preview or editing.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The operation generates an access token that is valid for 30 minutes and a refresh token that is valid for 1 day.
        The returned expiration time is in UTC.
        The operation supports the following document types:
        Word files: .doc, .docx, .txt, .dot, .wps, .wpt, .dotx, .docm, .dotm, and .rtf
        Presentation files: .ppt, .pptx, .pptm, .ppsx, .ppsm, .pps, .potx, .potm, .dpt, and .dps
        Spreadsheet documents: .et, .xls, .xlt, .xlsx, .xlsm, .xltx, .xltm, and .csv
        PDF files: .pdf
        The operation supports an input document that is up to 200 MB in size.
        The operation supports an input document that contains up to 5,000 pages.
        For a project created before December 1, 2023, you are charged for previewing or editing a document in the project based on the number of times the document is opened. For a project created on or after December 1, 2023, you are charged based on the number of API operation calls made for previewing or editing a document. If you want to switch to API call-based billing for document previewing and editing, use a project created on or after December 1, 2023. In API call-based billing, one API call allows only one user to use the feature. If multiple users use the information returned by the API call, only the last user has access to the document and the access permissions of other users are revoked.
        You can use the NotifyTopicName parameter to specify a Simple Message Queue (SMQ) topic in the same region as the IMM project for getting notified of file save operations. For more information about how to send and receive messages by using the SMQ SDK, see [Use queues](https://help.aliyun.com/document_detail/32449.html). For more information about the JSON example of the Message field, see [WebOffice message example](https://help.aliyun.com/document_detail/2743999.html).
        >  To manage multiple versions of the document, you must enable versioning for the bucket that stores the document and set the History parameter to true.
        
        @param tmp_req: GenerateWebofficeTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateWebofficeTokenResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GenerateWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.permission):
            request.permission_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.permission, 'Permission', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        query = {}
        if not UtilClient.is_unset(request.cache_preview):
            query['CachePreview'] = request.cache_preview
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.external_uploaded):
            query['ExternalUploaded'] = request.external_uploaded
        if not UtilClient.is_unset(request.filename):
            query['Filename'] = request.filename
        if not UtilClient.is_unset(request.hidecmb):
            query['Hidecmb'] = request.hidecmb
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.permission_shrink):
            query['Permission'] = request.permission_shrink
        if not UtilClient.is_unset(request.preview_pages):
            query['PreviewPages'] = request.preview_pages
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.referer):
            query['Referer'] = request.referer
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.user_shrink):
            query['User'] = request.user_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.watermark_shrink):
            query['Watermark'] = request.watermark_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GenerateWebofficeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_weboffice_token(
        self,
        request: imm_20200930_models.GenerateWebofficeTokenRequest,
    ) -> imm_20200930_models.GenerateWebofficeTokenResponse:
        """
        @summary Generates an access token for document preview or editing.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The operation generates an access token that is valid for 30 minutes and a refresh token that is valid for 1 day.
        The returned expiration time is in UTC.
        The operation supports the following document types:
        Word files: .doc, .docx, .txt, .dot, .wps, .wpt, .dotx, .docm, .dotm, and .rtf
        Presentation files: .ppt, .pptx, .pptm, .ppsx, .ppsm, .pps, .potx, .potm, .dpt, and .dps
        Spreadsheet documents: .et, .xls, .xlt, .xlsx, .xlsm, .xltx, .xltm, and .csv
        PDF files: .pdf
        The operation supports an input document that is up to 200 MB in size.
        The operation supports an input document that contains up to 5,000 pages.
        For a project created before December 1, 2023, you are charged for previewing or editing a document in the project based on the number of times the document is opened. For a project created on or after December 1, 2023, you are charged based on the number of API operation calls made for previewing or editing a document. If you want to switch to API call-based billing for document previewing and editing, use a project created on or after December 1, 2023. In API call-based billing, one API call allows only one user to use the feature. If multiple users use the information returned by the API call, only the last user has access to the document and the access permissions of other users are revoked.
        You can use the NotifyTopicName parameter to specify a Simple Message Queue (SMQ) topic in the same region as the IMM project for getting notified of file save operations. For more information about how to send and receive messages by using the SMQ SDK, see [Use queues](https://help.aliyun.com/document_detail/32449.html). For more information about the JSON example of the Message field, see [WebOffice message example](https://help.aliyun.com/document_detail/2743999.html).
        >  To manage multiple versions of the document, you must enable versioning for the bucket that stores the document and set the History parameter to true.
        
        @param request: GenerateWebofficeTokenRequest
        @return: GenerateWebofficeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_weboffice_token_with_options(request, runtime)

    async def generate_weboffice_token_async(
        self,
        request: imm_20200930_models.GenerateWebofficeTokenRequest,
    ) -> imm_20200930_models.GenerateWebofficeTokenResponse:
        """
        @summary Generates an access token for document preview or editing.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The operation generates an access token that is valid for 30 minutes and a refresh token that is valid for 1 day.
        The returned expiration time is in UTC.
        The operation supports the following document types:
        Word files: .doc, .docx, .txt, .dot, .wps, .wpt, .dotx, .docm, .dotm, and .rtf
        Presentation files: .ppt, .pptx, .pptm, .ppsx, .ppsm, .pps, .potx, .potm, .dpt, and .dps
        Spreadsheet documents: .et, .xls, .xlt, .xlsx, .xlsm, .xltx, .xltm, and .csv
        PDF files: .pdf
        The operation supports an input document that is up to 200 MB in size.
        The operation supports an input document that contains up to 5,000 pages.
        For a project created before December 1, 2023, you are charged for previewing or editing a document in the project based on the number of times the document is opened. For a project created on or after December 1, 2023, you are charged based on the number of API operation calls made for previewing or editing a document. If you want to switch to API call-based billing for document previewing and editing, use a project created on or after December 1, 2023. In API call-based billing, one API call allows only one user to use the feature. If multiple users use the information returned by the API call, only the last user has access to the document and the access permissions of other users are revoked.
        You can use the NotifyTopicName parameter to specify a Simple Message Queue (SMQ) topic in the same region as the IMM project for getting notified of file save operations. For more information about how to send and receive messages by using the SMQ SDK, see [Use queues](https://help.aliyun.com/document_detail/32449.html). For more information about the JSON example of the Message field, see [WebOffice message example](https://help.aliyun.com/document_detail/2743999.html).
        >  To manage multiple versions of the document, you must enable versioning for the bucket that stores the document and set the History parameter to true.
        
        @param request: GenerateWebofficeTokenRequest
        @return: GenerateWebofficeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_weboffice_token_with_options_async(request, runtime)

    def get_batch_with_options(
        self,
        request: imm_20200930_models.GetBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetBatchResponse:
        """
        @summary Queries the information about a batch processing task.
        
        @param request: GetBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_with_options_async(
        self,
        request: imm_20200930_models.GetBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetBatchResponse:
        """
        @summary Queries the information about a batch processing task.
        
        @param request: GetBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch(
        self,
        request: imm_20200930_models.GetBatchRequest,
    ) -> imm_20200930_models.GetBatchResponse:
        """
        @summary Queries the information about a batch processing task.
        
        @param request: GetBatchRequest
        @return: GetBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_batch_with_options(request, runtime)

    async def get_batch_async(
        self,
        request: imm_20200930_models.GetBatchRequest,
    ) -> imm_20200930_models.GetBatchResponse:
        """
        @summary Queries the information about a batch processing task.
        
        @param request: GetBatchRequest
        @return: GetBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_with_options_async(request, runtime)

    def get_binding_with_options(
        self,
        request: imm_20200930_models.GetBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetBindingResponse:
        """
        @summary Queries the binding relationship between a specific dataset and an Object Storage Service (OSS) bucket.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Make sure that the binding relationship that you want to query exists. For information about how to create a binding relationship, see [CreateBinding](https://help.aliyun.com/document_detail/478202.html).
        
        @param request: GetBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_binding_with_options_async(
        self,
        request: imm_20200930_models.GetBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetBindingResponse:
        """
        @summary Queries the binding relationship between a specific dataset and an Object Storage Service (OSS) bucket.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Make sure that the binding relationship that you want to query exists. For information about how to create a binding relationship, see [CreateBinding](https://help.aliyun.com/document_detail/478202.html).
        
        @param request: GetBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_binding(
        self,
        request: imm_20200930_models.GetBindingRequest,
    ) -> imm_20200930_models.GetBindingResponse:
        """
        @summary Queries the binding relationship between a specific dataset and an Object Storage Service (OSS) bucket.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Make sure that the binding relationship that you want to query exists. For information about how to create a binding relationship, see [CreateBinding](https://help.aliyun.com/document_detail/478202.html).
        
        @param request: GetBindingRequest
        @return: GetBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_binding_with_options(request, runtime)

    async def get_binding_async(
        self,
        request: imm_20200930_models.GetBindingRequest,
    ) -> imm_20200930_models.GetBindingResponse:
        """
        @summary Queries the binding relationship between a specific dataset and an Object Storage Service (OSS) bucket.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Make sure that the binding relationship that you want to query exists. For information about how to create a binding relationship, see [CreateBinding](https://help.aliyun.com/document_detail/478202.html).
        
        @param request: GetBindingRequest
        @return: GetBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_binding_with_options_async(request, runtime)

    def get_drmlicense_with_options(
        self,
        request: imm_20200930_models.GetDRMLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDRMLicenseResponse:
        """
        @deprecated OpenAPI GetDRMLicense is deprecated
        
        @summary drmlicense获取
        
        @param request: GetDRMLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDRMLicenseResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.protection_system):
            query['ProtectionSystem'] = request.protection_system
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDRMLicense',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDRMLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_drmlicense_with_options_async(
        self,
        request: imm_20200930_models.GetDRMLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDRMLicenseResponse:
        """
        @deprecated OpenAPI GetDRMLicense is deprecated
        
        @summary drmlicense获取
        
        @param request: GetDRMLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDRMLicenseResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.protection_system):
            query['ProtectionSystem'] = request.protection_system
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDRMLicense',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDRMLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_drmlicense(
        self,
        request: imm_20200930_models.GetDRMLicenseRequest,
    ) -> imm_20200930_models.GetDRMLicenseResponse:
        """
        @deprecated OpenAPI GetDRMLicense is deprecated
        
        @summary drmlicense获取
        
        @param request: GetDRMLicenseRequest
        @return: GetDRMLicenseResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_drmlicense_with_options(request, runtime)

    async def get_drmlicense_async(
        self,
        request: imm_20200930_models.GetDRMLicenseRequest,
    ) -> imm_20200930_models.GetDRMLicenseResponse:
        """
        @deprecated OpenAPI GetDRMLicense is deprecated
        
        @summary drmlicense获取
        
        @param request: GetDRMLicenseRequest
        @return: GetDRMLicenseResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_drmlicense_with_options_async(request, runtime)

    def get_dataset_with_options(
        self,
        request: imm_20200930_models.GetDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDatasetResponse:
        """
        @summary Queries a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The GetDataset operation supports real-time retrieval of file statistics. You can specify WithStatistics to enable real-time retrieval of file statistics.
        
        @param request: GetDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        request: imm_20200930_models.GetDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDatasetResponse:
        """
        @summary Queries a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The GetDataset operation supports real-time retrieval of file statistics. You can specify WithStatistics to enable real-time retrieval of file statistics.
        
        @param request: GetDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset(
        self,
        request: imm_20200930_models.GetDatasetRequest,
    ) -> imm_20200930_models.GetDatasetResponse:
        """
        @summary Queries a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The GetDataset operation supports real-time retrieval of file statistics. You can specify WithStatistics to enable real-time retrieval of file statistics.
        
        @param request: GetDatasetRequest
        @return: GetDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dataset_with_options(request, runtime)

    async def get_dataset_async(
        self,
        request: imm_20200930_models.GetDatasetRequest,
    ) -> imm_20200930_models.GetDatasetResponse:
        """
        @summary Queries a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        The GetDataset operation supports real-time retrieval of file statistics. You can specify WithStatistics to enable real-time retrieval of file statistics.
        
        @param request: GetDatasetRequest
        @return: GetDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dataset_with_options_async(request, runtime)

    def get_decode_blind_watermark_result_with_options(
        self,
        request: imm_20200930_models.GetDecodeBlindWatermarkResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDecodeBlindWatermarkResultResponse:
        """
        @summary Queries the result of an invisible watermark parsing task.
        
        @description    Before you call this operation, make sure that an Intelligent Media Management (IMM) project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        Before you call this operation, make sure that an invisible watermark task is created and the task ID is obtained.``
        
        @param request: GetDecodeBlindWatermarkResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDecodeBlindWatermarkResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDecodeBlindWatermarkResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDecodeBlindWatermarkResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_decode_blind_watermark_result_with_options_async(
        self,
        request: imm_20200930_models.GetDecodeBlindWatermarkResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDecodeBlindWatermarkResultResponse:
        """
        @summary Queries the result of an invisible watermark parsing task.
        
        @description    Before you call this operation, make sure that an Intelligent Media Management (IMM) project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        Before you call this operation, make sure that an invisible watermark task is created and the task ID is obtained.``
        
        @param request: GetDecodeBlindWatermarkResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDecodeBlindWatermarkResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDecodeBlindWatermarkResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDecodeBlindWatermarkResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_decode_blind_watermark_result(
        self,
        request: imm_20200930_models.GetDecodeBlindWatermarkResultRequest,
    ) -> imm_20200930_models.GetDecodeBlindWatermarkResultResponse:
        """
        @summary Queries the result of an invisible watermark parsing task.
        
        @description    Before you call this operation, make sure that an Intelligent Media Management (IMM) project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        Before you call this operation, make sure that an invisible watermark task is created and the task ID is obtained.``
        
        @param request: GetDecodeBlindWatermarkResultRequest
        @return: GetDecodeBlindWatermarkResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_decode_blind_watermark_result_with_options(request, runtime)

    async def get_decode_blind_watermark_result_async(
        self,
        request: imm_20200930_models.GetDecodeBlindWatermarkResultRequest,
    ) -> imm_20200930_models.GetDecodeBlindWatermarkResultResponse:
        """
        @summary Queries the result of an invisible watermark parsing task.
        
        @description    Before you call this operation, make sure that an Intelligent Media Management (IMM) project is created. For information about how to create a project, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        Before you call this operation, make sure that an invisible watermark task is created and the task ID is obtained.``
        
        @param request: GetDecodeBlindWatermarkResultRequest
        @return: GetDecodeBlindWatermarkResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_decode_blind_watermark_result_with_options_async(request, runtime)

    def get_figure_cluster_with_options(
        self,
        request: imm_20200930_models.GetFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFigureClusterResponse:
        """
        @summary Obtains basic information about face clustering, including the creation time, number of images, and cover.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Before you call this operation, make sure that a face clustering task is created to group all faces in a dataset. For information about how to create a face clustering task, see [CreateFigureClusteringTask](~~CreateFigureClusteringTask~~). For information about how to create a dataset, see [CreateDataset](~~CreateDataset~~).
        
        @param request: GetFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFigureClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_figure_cluster_with_options_async(
        self,
        request: imm_20200930_models.GetFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFigureClusterResponse:
        """
        @summary Obtains basic information about face clustering, including the creation time, number of images, and cover.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Before you call this operation, make sure that a face clustering task is created to group all faces in a dataset. For information about how to create a face clustering task, see [CreateFigureClusteringTask](~~CreateFigureClusteringTask~~). For information about how to create a dataset, see [CreateDataset](~~CreateDataset~~).
        
        @param request: GetFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFigureClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_figure_cluster(
        self,
        request: imm_20200930_models.GetFigureClusterRequest,
    ) -> imm_20200930_models.GetFigureClusterResponse:
        """
        @summary Obtains basic information about face clustering, including the creation time, number of images, and cover.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Before you call this operation, make sure that a face clustering task is created to group all faces in a dataset. For information about how to create a face clustering task, see [CreateFigureClusteringTask](~~CreateFigureClusteringTask~~). For information about how to create a dataset, see [CreateDataset](~~CreateDataset~~).
        
        @param request: GetFigureClusterRequest
        @return: GetFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_figure_cluster_with_options(request, runtime)

    async def get_figure_cluster_async(
        self,
        request: imm_20200930_models.GetFigureClusterRequest,
    ) -> imm_20200930_models.GetFigureClusterResponse:
        """
        @summary Obtains basic information about face clustering, including the creation time, number of images, and cover.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Before you call this operation, make sure that a face clustering task is created to group all faces in a dataset. For information about how to create a face clustering task, see [CreateFigureClusteringTask](~~CreateFigureClusteringTask~~). For information about how to create a dataset, see [CreateDataset](~~CreateDataset~~).
        
        @param request: GetFigureClusterRequest
        @return: GetFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_figure_cluster_with_options_async(request, runtime)

    def get_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.GetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFileMetaResponse:
        """
        @summary Queries metadata of a file whose metadata is indexed into the dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        
        @param tmp_req: GetFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GetFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.GetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFileMetaResponse:
        """
        @summary Queries metadata of a file whose metadata is indexed into the dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        
        @param tmp_req: GetFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GetFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_meta(
        self,
        request: imm_20200930_models.GetFileMetaRequest,
    ) -> imm_20200930_models.GetFileMetaResponse:
        """
        @summary Queries metadata of a file whose metadata is indexed into the dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        
        @param request: GetFileMetaRequest
        @return: GetFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_file_meta_with_options(request, runtime)

    async def get_file_meta_async(
        self,
        request: imm_20200930_models.GetFileMetaRequest,
    ) -> imm_20200930_models.GetFileMetaResponse:
        """
        @summary Queries metadata of a file whose metadata is indexed into the dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        
        @param request: GetFileMetaRequest
        @return: GetFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_file_meta_with_options_async(request, runtime)

    def get_image_moderation_result_with_options(
        self,
        request: imm_20200930_models.GetImageModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetImageModerationResultResponse:
        """
        @summary Queries an image compliance detection task.
        
        @param request: GetImageModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageModerationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetImageModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_moderation_result_with_options_async(
        self,
        request: imm_20200930_models.GetImageModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetImageModerationResultResponse:
        """
        @summary Queries an image compliance detection task.
        
        @param request: GetImageModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageModerationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetImageModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_moderation_result(
        self,
        request: imm_20200930_models.GetImageModerationResultRequest,
    ) -> imm_20200930_models.GetImageModerationResultResponse:
        """
        @summary Queries an image compliance detection task.
        
        @param request: GetImageModerationResultRequest
        @return: GetImageModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_image_moderation_result_with_options(request, runtime)

    async def get_image_moderation_result_async(
        self,
        request: imm_20200930_models.GetImageModerationResultRequest,
    ) -> imm_20200930_models.GetImageModerationResultResponse:
        """
        @summary Queries an image compliance detection task.
        
        @param request: GetImageModerationResultRequest
        @return: GetImageModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_image_moderation_result_with_options_async(request, runtime)

    def get_ossbucket_attachment_with_options(
        self,
        request: imm_20200930_models.GetOSSBucketAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetOSSBucketAttachmentResponse:
        """
        @summary Queries the name of the project bound to an Object Storage Service (OSS) bucket.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Before you call this operation, make sure that [the project whose name you want to query is bound to the specified OSS bucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: GetOSSBucketAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOSSBucketAttachmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOSSBucketAttachment',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetOSSBucketAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ossbucket_attachment_with_options_async(
        self,
        request: imm_20200930_models.GetOSSBucketAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetOSSBucketAttachmentResponse:
        """
        @summary Queries the name of the project bound to an Object Storage Service (OSS) bucket.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Before you call this operation, make sure that [the project whose name you want to query is bound to the specified OSS bucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: GetOSSBucketAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOSSBucketAttachmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOSSBucketAttachment',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetOSSBucketAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ossbucket_attachment(
        self,
        request: imm_20200930_models.GetOSSBucketAttachmentRequest,
    ) -> imm_20200930_models.GetOSSBucketAttachmentResponse:
        """
        @summary Queries the name of the project bound to an Object Storage Service (OSS) bucket.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Before you call this operation, make sure that [the project whose name you want to query is bound to the specified OSS bucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: GetOSSBucketAttachmentRequest
        @return: GetOSSBucketAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ossbucket_attachment_with_options(request, runtime)

    async def get_ossbucket_attachment_async(
        self,
        request: imm_20200930_models.GetOSSBucketAttachmentRequest,
    ) -> imm_20200930_models.GetOSSBucketAttachmentResponse:
        """
        @summary Queries the name of the project bound to an Object Storage Service (OSS) bucket.
        
        @description    **Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**\
        Before you call this operation, make sure that [the project whose name you want to query is bound to the specified OSS bucket](https://help.aliyun.com/document_detail/478206.html).
        
        @param request: GetOSSBucketAttachmentRequest
        @return: GetOSSBucketAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ossbucket_attachment_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: imm_20200930_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetProjectResponse:
        """
        @summary Queries the basic information, datasets, and file statistics of a project.
        
        @description When you call this operation, you can enable the real-time retrieval of file statistics based on your business requirements. For more information, see the "Request parameters" section of this topic.
        
        @param request: GetProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: imm_20200930_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetProjectResponse:
        """
        @summary Queries the basic information, datasets, and file statistics of a project.
        
        @description When you call this operation, you can enable the real-time retrieval of file statistics based on your business requirements. For more information, see the "Request parameters" section of this topic.
        
        @param request: GetProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        request: imm_20200930_models.GetProjectRequest,
    ) -> imm_20200930_models.GetProjectResponse:
        """
        @summary Queries the basic information, datasets, and file statistics of a project.
        
        @description When you call this operation, you can enable the real-time retrieval of file statistics based on your business requirements. For more information, see the "Request parameters" section of this topic.
        
        @param request: GetProjectRequest
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: imm_20200930_models.GetProjectRequest,
    ) -> imm_20200930_models.GetProjectResponse:
        """
        @summary Queries the basic information, datasets, and file statistics of a project.
        
        @description When you call this operation, you can enable the real-time retrieval of file statistics based on your business requirements. For more information, see the "Request parameters" section of this topic.
        
        @param request: GetProjectRequest
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_story_with_options(
        self,
        request: imm_20200930_models.GetStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetStoryResponse:
        """
        @summary Queries a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param request: GetStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_story_with_options_async(
        self,
        request: imm_20200930_models.GetStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetStoryResponse:
        """
        @summary Queries a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param request: GetStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_story(
        self,
        request: imm_20200930_models.GetStoryRequest,
    ) -> imm_20200930_models.GetStoryResponse:
        """
        @summary Queries a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param request: GetStoryRequest
        @return: GetStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_story_with_options(request, runtime)

    async def get_story_async(
        self,
        request: imm_20200930_models.GetStoryRequest,
    ) -> imm_20200930_models.GetStoryResponse:
        """
        @summary Queries a story.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param request: GetStoryRequest
        @return: GetStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_story_with_options_async(request, runtime)

    def get_task_with_options(
        self,
        request: imm_20200930_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetTaskResponse:
        """
        @summary Queries information about an asynchronous task. Intelligent Media Management (IMM) has multiple asynchronous data processing capabilities, each of which has its own operation for creating tasks. For example, you can call the CreateFigureClusteringTask operation to create a face clustering task and the CreateFileCompressionTask operation to create a file compression task. The GetTask operation is a general operation. You can call this operation to query information about asynchronous tasks by task ID or type.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.
        
        @param request: GetTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: imm_20200930_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetTaskResponse:
        """
        @summary Queries information about an asynchronous task. Intelligent Media Management (IMM) has multiple asynchronous data processing capabilities, each of which has its own operation for creating tasks. For example, you can call the CreateFigureClusteringTask operation to create a face clustering task and the CreateFileCompressionTask operation to create a file compression task. The GetTask operation is a general operation. You can call this operation to query information about asynchronous tasks by task ID or type.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.
        
        @param request: GetTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        request: imm_20200930_models.GetTaskRequest,
    ) -> imm_20200930_models.GetTaskResponse:
        """
        @summary Queries information about an asynchronous task. Intelligent Media Management (IMM) has multiple asynchronous data processing capabilities, each of which has its own operation for creating tasks. For example, you can call the CreateFigureClusteringTask operation to create a face clustering task and the CreateFileCompressionTask operation to create a file compression task. The GetTask operation is a general operation. You can call this operation to query information about asynchronous tasks by task ID or type.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.
        
        @param request: GetTaskRequest
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: imm_20200930_models.GetTaskRequest,
    ) -> imm_20200930_models.GetTaskResponse:
        """
        @summary Queries information about an asynchronous task. Intelligent Media Management (IMM) has multiple asynchronous data processing capabilities, each of which has its own operation for creating tasks. For example, you can call the CreateFigureClusteringTask operation to create a face clustering task and the CreateFileCompressionTask operation to create a file compression task. The GetTask operation is a general operation. You can call this operation to query information about asynchronous tasks by task ID or type.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.
        
        @param request: GetTaskRequest
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_trigger_with_options(
        self,
        request: imm_20200930_models.GetTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetTriggerResponse:
        """
        @summary Queries the information about a trigger.
        
        @param request: GetTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTriggerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trigger_with_options_async(
        self,
        request: imm_20200930_models.GetTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetTriggerResponse:
        """
        @summary Queries the information about a trigger.
        
        @param request: GetTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTriggerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trigger(
        self,
        request: imm_20200930_models.GetTriggerRequest,
    ) -> imm_20200930_models.GetTriggerResponse:
        """
        @summary Queries the information about a trigger.
        
        @param request: GetTriggerRequest
        @return: GetTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_trigger_with_options(request, runtime)

    async def get_trigger_async(
        self,
        request: imm_20200930_models.GetTriggerRequest,
    ) -> imm_20200930_models.GetTriggerResponse:
        """
        @summary Queries the information about a trigger.
        
        @param request: GetTriggerRequest
        @return: GetTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_trigger_with_options_async(request, runtime)

    def get_video_label_classification_result_with_options(
        self,
        request: imm_20200930_models.GetVideoLabelClassificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetVideoLabelClassificationResultResponse:
        """
        @summary Queries the results of a video label detection task.
        
        @description    Before you call this operation, make sure that a [project](https://help.aliyun.com/document_detail/478273.html) is created on Intelligent Media Management (IMM). For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        Before you call this operation, make sure that a video label detection task is created and the `TaskId` of the task is obtained. For more information, see [CreateVideoLabelClassificationTask](https://help.aliyun.com/document_detail/478223.html).
        
        @param request: GetVideoLabelClassificationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoLabelClassificationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoLabelClassificationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetVideoLabelClassificationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_label_classification_result_with_options_async(
        self,
        request: imm_20200930_models.GetVideoLabelClassificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetVideoLabelClassificationResultResponse:
        """
        @summary Queries the results of a video label detection task.
        
        @description    Before you call this operation, make sure that a [project](https://help.aliyun.com/document_detail/478273.html) is created on Intelligent Media Management (IMM). For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        Before you call this operation, make sure that a video label detection task is created and the `TaskId` of the task is obtained. For more information, see [CreateVideoLabelClassificationTask](https://help.aliyun.com/document_detail/478223.html).
        
        @param request: GetVideoLabelClassificationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoLabelClassificationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoLabelClassificationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetVideoLabelClassificationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_label_classification_result(
        self,
        request: imm_20200930_models.GetVideoLabelClassificationResultRequest,
    ) -> imm_20200930_models.GetVideoLabelClassificationResultResponse:
        """
        @summary Queries the results of a video label detection task.
        
        @description    Before you call this operation, make sure that a [project](https://help.aliyun.com/document_detail/478273.html) is created on Intelligent Media Management (IMM). For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        Before you call this operation, make sure that a video label detection task is created and the `TaskId` of the task is obtained. For more information, see [CreateVideoLabelClassificationTask](https://help.aliyun.com/document_detail/478223.html).
        
        @param request: GetVideoLabelClassificationResultRequest
        @return: GetVideoLabelClassificationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_video_label_classification_result_with_options(request, runtime)

    async def get_video_label_classification_result_async(
        self,
        request: imm_20200930_models.GetVideoLabelClassificationResultRequest,
    ) -> imm_20200930_models.GetVideoLabelClassificationResultResponse:
        """
        @summary Queries the results of a video label detection task.
        
        @description    Before you call this operation, make sure that a [project](https://help.aliyun.com/document_detail/478273.html) is created on Intelligent Media Management (IMM). For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        Before you call this operation, make sure that a video label detection task is created and the `TaskId` of the task is obtained. For more information, see [CreateVideoLabelClassificationTask](https://help.aliyun.com/document_detail/478223.html).
        
        @param request: GetVideoLabelClassificationResultRequest
        @return: GetVideoLabelClassificationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_video_label_classification_result_with_options_async(request, runtime)

    def get_video_moderation_result_with_options(
        self,
        request: imm_20200930_models.GetVideoModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetVideoModerationResultResponse:
        """
        @summary 获取视频审核任务结果
        
        @param request: GetVideoModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoModerationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetVideoModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_moderation_result_with_options_async(
        self,
        request: imm_20200930_models.GetVideoModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetVideoModerationResultResponse:
        """
        @summary 获取视频审核任务结果
        
        @param request: GetVideoModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoModerationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetVideoModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_moderation_result(
        self,
        request: imm_20200930_models.GetVideoModerationResultRequest,
    ) -> imm_20200930_models.GetVideoModerationResultResponse:
        """
        @summary 获取视频审核任务结果
        
        @param request: GetVideoModerationResultRequest
        @return: GetVideoModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_video_moderation_result_with_options(request, runtime)

    async def get_video_moderation_result_async(
        self,
        request: imm_20200930_models.GetVideoModerationResultRequest,
    ) -> imm_20200930_models.GetVideoModerationResultResponse:
        """
        @summary 获取视频审核任务结果
        
        @param request: GetVideoModerationResultRequest
        @return: GetVideoModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_video_moderation_result_with_options_async(request, runtime)

    def index_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.IndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        """
        @summary Creates an index from metadata extracted by using techniques such as label recognition, face detection, and location detection from input files. You can retrieve data from the same dataset by using multiple methods.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        For information about how to create indexes from metadata, see [Workflow templates and operators](https://help.aliyun.com/document_detail/466304.html).
        For information about the limits on the maximum number and size of index files that you can create, see the "Limits on datasets" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic. For information about how to create a dataset, see the "CreateDataset" topic.
        For information about the regions in which you can create index files from metadata, see the "Datasets and indexes" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic.
        After you create an index from metadata, you can try [simple query](https://help.aliyun.com/document_detail/478175.html) to retrieve data. For information about other query capabilities, see [Query and statistics](https://help.aliyun.com/document_detail/2402363.html). You can also [create a face clustering task](https://help.aliyun.com/document_detail/478180.html) to group faces. For information about other clustering capabilities, see [Intelligent management](https://help.aliyun.com/document_detail/2402365.html).
        *\
        *Usage notes**\
        The IndexFileMeta operation is asynchronous, indicating that it takes some time to process the data after a request is submitted. After the processing is complete, the metadata is stored in your dataset. The amount of time it takes for this process varies based on [the workflow template, the operator](https://help.aliyun.com/document_detail/466304.html), and the content of the file, ranging from several seconds to several minutes or even longer. You can subscribe to [Simple Message Service](https://help.aliyun.com/document_detail/2743997.html) for task completion notifications.
        
        @param tmp_req: IndexFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IndexFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.IndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.IndexFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def index_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.IndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        """
        @summary Creates an index from metadata extracted by using techniques such as label recognition, face detection, and location detection from input files. You can retrieve data from the same dataset by using multiple methods.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        For information about how to create indexes from metadata, see [Workflow templates and operators](https://help.aliyun.com/document_detail/466304.html).
        For information about the limits on the maximum number and size of index files that you can create, see the "Limits on datasets" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic. For information about how to create a dataset, see the "CreateDataset" topic.
        For information about the regions in which you can create index files from metadata, see the "Datasets and indexes" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic.
        After you create an index from metadata, you can try [simple query](https://help.aliyun.com/document_detail/478175.html) to retrieve data. For information about other query capabilities, see [Query and statistics](https://help.aliyun.com/document_detail/2402363.html). You can also [create a face clustering task](https://help.aliyun.com/document_detail/478180.html) to group faces. For information about other clustering capabilities, see [Intelligent management](https://help.aliyun.com/document_detail/2402365.html).
        *\
        *Usage notes**\
        The IndexFileMeta operation is asynchronous, indicating that it takes some time to process the data after a request is submitted. After the processing is complete, the metadata is stored in your dataset. The amount of time it takes for this process varies based on [the workflow template, the operator](https://help.aliyun.com/document_detail/466304.html), and the content of the file, ranging from several seconds to several minutes or even longer. You can subscribe to [Simple Message Service](https://help.aliyun.com/document_detail/2743997.html) for task completion notifications.
        
        @param tmp_req: IndexFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IndexFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.IndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.IndexFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def index_file_meta(
        self,
        request: imm_20200930_models.IndexFileMetaRequest,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        """
        @summary Creates an index from metadata extracted by using techniques such as label recognition, face detection, and location detection from input files. You can retrieve data from the same dataset by using multiple methods.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        For information about how to create indexes from metadata, see [Workflow templates and operators](https://help.aliyun.com/document_detail/466304.html).
        For information about the limits on the maximum number and size of index files that you can create, see the "Limits on datasets" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic. For information about how to create a dataset, see the "CreateDataset" topic.
        For information about the regions in which you can create index files from metadata, see the "Datasets and indexes" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic.
        After you create an index from metadata, you can try [simple query](https://help.aliyun.com/document_detail/478175.html) to retrieve data. For information about other query capabilities, see [Query and statistics](https://help.aliyun.com/document_detail/2402363.html). You can also [create a face clustering task](https://help.aliyun.com/document_detail/478180.html) to group faces. For information about other clustering capabilities, see [Intelligent management](https://help.aliyun.com/document_detail/2402365.html).
        *\
        *Usage notes**\
        The IndexFileMeta operation is asynchronous, indicating that it takes some time to process the data after a request is submitted. After the processing is complete, the metadata is stored in your dataset. The amount of time it takes for this process varies based on [the workflow template, the operator](https://help.aliyun.com/document_detail/466304.html), and the content of the file, ranging from several seconds to several minutes or even longer. You can subscribe to [Simple Message Service](https://help.aliyun.com/document_detail/2743997.html) for task completion notifications.
        
        @param request: IndexFileMetaRequest
        @return: IndexFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.index_file_meta_with_options(request, runtime)

    async def index_file_meta_async(
        self,
        request: imm_20200930_models.IndexFileMetaRequest,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        """
        @summary Creates an index from metadata extracted by using techniques such as label recognition, face detection, and location detection from input files. You can retrieve data from the same dataset by using multiple methods.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        For information about how to create indexes from metadata, see [Workflow templates and operators](https://help.aliyun.com/document_detail/466304.html).
        For information about the limits on the maximum number and size of index files that you can create, see the "Limits on datasets" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic. For information about how to create a dataset, see the "CreateDataset" topic.
        For information about the regions in which you can create index files from metadata, see the "Datasets and indexes" section of the [Limits](https://help.aliyun.com/document_detail/475569.html) topic.
        After you create an index from metadata, you can try [simple query](https://help.aliyun.com/document_detail/478175.html) to retrieve data. For information about other query capabilities, see [Query and statistics](https://help.aliyun.com/document_detail/2402363.html). You can also [create a face clustering task](https://help.aliyun.com/document_detail/478180.html) to group faces. For information about other clustering capabilities, see [Intelligent management](https://help.aliyun.com/document_detail/2402365.html).
        *\
        *Usage notes**\
        The IndexFileMeta operation is asynchronous, indicating that it takes some time to process the data after a request is submitted. After the processing is complete, the metadata is stored in your dataset. The amount of time it takes for this process varies based on [the workflow template, the operator](https://help.aliyun.com/document_detail/466304.html), and the content of the file, ranging from several seconds to several minutes or even longer. You can subscribe to [Simple Message Service](https://help.aliyun.com/document_detail/2743997.html) for task completion notifications.
        
        @param request: IndexFileMetaRequest
        @return: IndexFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.index_file_meta_with_options_async(request, runtime)

    def list_batches_with_options(
        self,
        request: imm_20200930_models.ListBatchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListBatchesResponse:
        """
        @summary Queries batch processing tasks. You can query batch processing tasks based on conditions such task tags and status. The results can be sorted.
        
        @param request: ListBatchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBatchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBatches',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBatchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_batches_with_options_async(
        self,
        request: imm_20200930_models.ListBatchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListBatchesResponse:
        """
        @summary Queries batch processing tasks. You can query batch processing tasks based on conditions such task tags and status. The results can be sorted.
        
        @param request: ListBatchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBatchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBatches',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBatchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_batches(
        self,
        request: imm_20200930_models.ListBatchesRequest,
    ) -> imm_20200930_models.ListBatchesResponse:
        """
        @summary Queries batch processing tasks. You can query batch processing tasks based on conditions such task tags and status. The results can be sorted.
        
        @param request: ListBatchesRequest
        @return: ListBatchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_batches_with_options(request, runtime)

    async def list_batches_async(
        self,
        request: imm_20200930_models.ListBatchesRequest,
    ) -> imm_20200930_models.ListBatchesResponse:
        """
        @summary Queries batch processing tasks. You can query batch processing tasks based on conditions such task tags and status. The results can be sorted.
        
        @param request: ListBatchesRequest
        @return: ListBatchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_batches_with_options_async(request, runtime)

    def list_bindings_with_options(
        self,
        request: imm_20200930_models.ListBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListBindingsResponse:
        """
        @summary Queries bindings between a dataset and Object Storage Service (OSS) buckets.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).
        
        @param request: ListBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBindings',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bindings_with_options_async(
        self,
        request: imm_20200930_models.ListBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListBindingsResponse:
        """
        @summary Queries bindings between a dataset and Object Storage Service (OSS) buckets.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).
        
        @param request: ListBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBindings',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bindings(
        self,
        request: imm_20200930_models.ListBindingsRequest,
    ) -> imm_20200930_models.ListBindingsResponse:
        """
        @summary Queries bindings between a dataset and Object Storage Service (OSS) buckets.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).
        
        @param request: ListBindingsRequest
        @return: ListBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_bindings_with_options(request, runtime)

    async def list_bindings_async(
        self,
        request: imm_20200930_models.ListBindingsRequest,
    ) -> imm_20200930_models.ListBindingsResponse:
        """
        @summary Queries bindings between a dataset and Object Storage Service (OSS) buckets.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).
        
        @param request: ListBindingsRequest
        @return: ListBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_bindings_with_options_async(request, runtime)

    def list_datasets_with_options(
        self,
        request: imm_20200930_models.ListDatasetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListDatasetsResponse:
        """
        @summary Queries a list of datasets. You can query the list by dataset prefix.
        
        @param request: ListDatasetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        request: imm_20200930_models.ListDatasetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListDatasetsResponse:
        """
        @summary Queries a list of datasets. You can query the list by dataset prefix.
        
        @param request: ListDatasetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListDatasetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasets(
        self,
        request: imm_20200930_models.ListDatasetsRequest,
    ) -> imm_20200930_models.ListDatasetsResponse:
        """
        @summary Queries a list of datasets. You can query the list by dataset prefix.
        
        @param request: ListDatasetsRequest
        @return: ListDatasetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_datasets_with_options(request, runtime)

    async def list_datasets_async(
        self,
        request: imm_20200930_models.ListDatasetsRequest,
    ) -> imm_20200930_models.ListDatasetsResponse:
        """
        @summary Queries a list of datasets. You can query the list by dataset prefix.
        
        @param request: ListDatasetsRequest
        @return: ListDatasetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_datasets_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        tmp_req: imm_20200930_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListProjectsResponse:
        """
        @summary Queries projects. You can call this operation to query the basic information, datasets, and file statistics of multiple projects at the same time.
        
        @description The ListProjects operation supports pagination. When you call this operation, you must specify the token that is obtained from the previous query as the value of NextToken. You must also specify MaxResults to limit the number of entries to return.
        
        @param tmp_req: ListProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        tmp_req: imm_20200930_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListProjectsResponse:
        """
        @summary Queries projects. You can call this operation to query the basic information, datasets, and file statistics of multiple projects at the same time.
        
        @description The ListProjects operation supports pagination. When you call this operation, you must specify the token that is obtained from the previous query as the value of NextToken. You must also specify MaxResults to limit the number of entries to return.
        
        @param tmp_req: ListProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: imm_20200930_models.ListProjectsRequest,
    ) -> imm_20200930_models.ListProjectsResponse:
        """
        @summary Queries projects. You can call this operation to query the basic information, datasets, and file statistics of multiple projects at the same time.
        
        @description The ListProjects operation supports pagination. When you call this operation, you must specify the token that is obtained from the previous query as the value of NextToken. You must also specify MaxResults to limit the number of entries to return.
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: imm_20200930_models.ListProjectsRequest,
    ) -> imm_20200930_models.ListProjectsResponse:
        """
        @summary Queries projects. You can call this operation to query the basic information, datasets, and file statistics of multiple projects at the same time.
        
        @description The ListProjects operation supports pagination. When you call this operation, you must specify the token that is obtained from the previous query as the value of NextToken. You must also specify MaxResults to limit the number of entries to return.
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: imm_20200930_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListRegionsResponse:
        """
        @summary Queries the regions where Intelligent Media Management (IMM) is available and the supported languages.
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        request: imm_20200930_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListRegionsResponse:
        """
        @summary Queries the regions where Intelligent Media Management (IMM) is available and the supported languages.
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(
        self,
        request: imm_20200930_models.ListRegionsRequest,
    ) -> imm_20200930_models.ListRegionsResponse:
        """
        @summary Queries the regions where Intelligent Media Management (IMM) is available and the supported languages.
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: imm_20200930_models.ListRegionsRequest,
    ) -> imm_20200930_models.ListRegionsResponse:
        """
        @summary Queries the regions where Intelligent Media Management (IMM) is available and the supported languages.
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        tmp_req: imm_20200930_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListTasksResponse:
        """
        @summary Lists tasks based on specific conditions, such as by time range and by tag.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).
        
        @param tmp_req: ListTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time_range):
            request.end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end_time_range, 'EndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.start_time_range):
            request.start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time_range, 'StartTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.task_types):
            request.task_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_types, 'TaskTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time_range_shrink):
            query['EndTimeRange'] = request.end_time_range_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.start_time_range_shrink):
            query['StartTimeRange'] = request.start_time_range_shrink
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        if not UtilClient.is_unset(request.task_types_shrink):
            query['TaskTypes'] = request.task_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        tmp_req: imm_20200930_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListTasksResponse:
        """
        @summary Lists tasks based on specific conditions, such as by time range and by tag.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).
        
        @param tmp_req: ListTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time_range):
            request.end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end_time_range, 'EndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.start_time_range):
            request.start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time_range, 'StartTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.task_types):
            request.task_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_types, 'TaskTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time_range_shrink):
            query['EndTimeRange'] = request.end_time_range_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.start_time_range_shrink):
            query['StartTimeRange'] = request.start_time_range_shrink
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        if not UtilClient.is_unset(request.task_types_shrink):
            query['TaskTypes'] = request.task_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: imm_20200930_models.ListTasksRequest,
    ) -> imm_20200930_models.ListTasksResponse:
        """
        @summary Lists tasks based on specific conditions, such as by time range and by tag.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: imm_20200930_models.ListTasksRequest,
    ) -> imm_20200930_models.ListTasksResponse:
        """
        @summary Lists tasks based on specific conditions, such as by time range and by tag.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_triggers_with_options(
        self,
        request: imm_20200930_models.ListTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListTriggersResponse:
        """
        @summary Queries triggers by tag or status.
        
        @param request: ListTriggersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTriggersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTriggers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListTriggersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_triggers_with_options_async(
        self,
        request: imm_20200930_models.ListTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListTriggersResponse:
        """
        @summary Queries triggers by tag or status.
        
        @param request: ListTriggersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTriggersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTriggers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListTriggersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_triggers(
        self,
        request: imm_20200930_models.ListTriggersRequest,
    ) -> imm_20200930_models.ListTriggersResponse:
        """
        @summary Queries triggers by tag or status.
        
        @param request: ListTriggersRequest
        @return: ListTriggersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_triggers_with_options(request, runtime)

    async def list_triggers_async(
        self,
        request: imm_20200930_models.ListTriggersRequest,
    ) -> imm_20200930_models.ListTriggersResponse:
        """
        @summary Queries triggers by tag or status.
        
        @param request: ListTriggersRequest
        @return: ListTriggersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_triggers_with_options_async(request, runtime)

    def query_figure_clusters_with_options(
        self,
        tmp_req: imm_20200930_models.QueryFigureClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryFigureClustersResponse:
        """
        @summary Queries face groups based on given conditions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that a face clustering task is created to group all faces in a dataset. For information about how to create a face clustering task, see [CreateFigureClusteringTask](~~CreateFigureClusteringTask~~). For information about how to create a dataset, see [CreateDataset](~~CreateDataset~~).
        
        @param tmp_req: QueryFigureClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFigureClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryFigureClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.update_time_range):
            request.update_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        if not UtilClient.is_unset(request.with_total_count):
            query['WithTotalCount'] = request.with_total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFigureClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryFigureClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_figure_clusters_with_options_async(
        self,
        tmp_req: imm_20200930_models.QueryFigureClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryFigureClustersResponse:
        """
        @summary Queries face groups based on given conditions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that a face clustering task is created to group all faces in a dataset. For information about how to create a face clustering task, see [CreateFigureClusteringTask](~~CreateFigureClusteringTask~~). For information about how to create a dataset, see [CreateDataset](~~CreateDataset~~).
        
        @param tmp_req: QueryFigureClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFigureClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryFigureClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.update_time_range):
            request.update_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        if not UtilClient.is_unset(request.with_total_count):
            query['WithTotalCount'] = request.with_total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFigureClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryFigureClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_figure_clusters(
        self,
        request: imm_20200930_models.QueryFigureClustersRequest,
    ) -> imm_20200930_models.QueryFigureClustersResponse:
        """
        @summary Queries face groups based on given conditions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that a face clustering task is created to group all faces in a dataset. For information about how to create a face clustering task, see [CreateFigureClusteringTask](~~CreateFigureClusteringTask~~). For information about how to create a dataset, see [CreateDataset](~~CreateDataset~~).
        
        @param request: QueryFigureClustersRequest
        @return: QueryFigureClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_figure_clusters_with_options(request, runtime)

    async def query_figure_clusters_async(
        self,
        request: imm_20200930_models.QueryFigureClustersRequest,
    ) -> imm_20200930_models.QueryFigureClustersResponse:
        """
        @summary Queries face groups based on given conditions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that a face clustering task is created to group all faces in a dataset. For information about how to create a face clustering task, see [CreateFigureClusteringTask](~~CreateFigureClusteringTask~~). For information about how to create a dataset, see [CreateDataset](~~CreateDataset~~).
        
        @param request: QueryFigureClustersRequest
        @return: QueryFigureClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_figure_clusters_with_options_async(request, runtime)

    def query_location_date_clusters_with_options(
        self,
        tmp_req: imm_20200930_models.QueryLocationDateClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryLocationDateClustersResponse:
        """
        @summary Queries a list of spatiotemporal clustering groups. Multiple conditions are supported. For more information, see the request parameters.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, you must call the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to perform spatiotemporal clustering.
        
        @param tmp_req: QueryLocationDateClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLocationDateClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryLocationDateClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_end_time_range):
            request.location_date_cluster_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_end_time_range, 'LocationDateClusterEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_levels):
            request.location_date_cluster_levels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_levels, 'LocationDateClusterLevels', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_start_time_range):
            request.location_date_cluster_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_start_time_range, 'LocationDateClusterStartTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.update_time_range):
            request.update_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.address_shrink):
            query['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.location_date_cluster_end_time_range_shrink):
            query['LocationDateClusterEndTimeRange'] = request.location_date_cluster_end_time_range_shrink
        if not UtilClient.is_unset(request.location_date_cluster_levels_shrink):
            query['LocationDateClusterLevels'] = request.location_date_cluster_levels_shrink
        if not UtilClient.is_unset(request.location_date_cluster_start_time_range_shrink):
            query['LocationDateClusterStartTimeRange'] = request.location_date_cluster_start_time_range_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLocationDateClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryLocationDateClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_location_date_clusters_with_options_async(
        self,
        tmp_req: imm_20200930_models.QueryLocationDateClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryLocationDateClustersResponse:
        """
        @summary Queries a list of spatiotemporal clustering groups. Multiple conditions are supported. For more information, see the request parameters.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, you must call the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to perform spatiotemporal clustering.
        
        @param tmp_req: QueryLocationDateClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLocationDateClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryLocationDateClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_end_time_range):
            request.location_date_cluster_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_end_time_range, 'LocationDateClusterEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_levels):
            request.location_date_cluster_levels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_levels, 'LocationDateClusterLevels', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_start_time_range):
            request.location_date_cluster_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_start_time_range, 'LocationDateClusterStartTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.update_time_range):
            request.update_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.address_shrink):
            query['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.location_date_cluster_end_time_range_shrink):
            query['LocationDateClusterEndTimeRange'] = request.location_date_cluster_end_time_range_shrink
        if not UtilClient.is_unset(request.location_date_cluster_levels_shrink):
            query['LocationDateClusterLevels'] = request.location_date_cluster_levels_shrink
        if not UtilClient.is_unset(request.location_date_cluster_start_time_range_shrink):
            query['LocationDateClusterStartTimeRange'] = request.location_date_cluster_start_time_range_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLocationDateClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryLocationDateClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_location_date_clusters(
        self,
        request: imm_20200930_models.QueryLocationDateClustersRequest,
    ) -> imm_20200930_models.QueryLocationDateClustersResponse:
        """
        @summary Queries a list of spatiotemporal clustering groups. Multiple conditions are supported. For more information, see the request parameters.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, you must call the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to perform spatiotemporal clustering.
        
        @param request: QueryLocationDateClustersRequest
        @return: QueryLocationDateClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_location_date_clusters_with_options(request, runtime)

    async def query_location_date_clusters_async(
        self,
        request: imm_20200930_models.QueryLocationDateClustersRequest,
    ) -> imm_20200930_models.QueryLocationDateClustersResponse:
        """
        @summary Queries a list of spatiotemporal clustering groups. Multiple conditions are supported. For more information, see the request parameters.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, you must call the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to perform spatiotemporal clustering.
        
        @param request: QueryLocationDateClustersRequest
        @return: QueryLocationDateClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_location_date_clusters_with_options_async(request, runtime)

    def query_similar_image_clusters_with_options(
        self,
        request: imm_20200930_models.QuerySimilarImageClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QuerySimilarImageClustersResponse:
        """
        @summary You can call this operation to query the list of similar image clusters.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, you must call the [CreateSimilarImageClusteringTask](https://help.aliyun.com/document_detail/611302.html) operation to cluster similar images in the dataset.
        
        @param request: QuerySimilarImageClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySimilarImageClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySimilarImageClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QuerySimilarImageClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_similar_image_clusters_with_options_async(
        self,
        request: imm_20200930_models.QuerySimilarImageClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QuerySimilarImageClustersResponse:
        """
        @summary You can call this operation to query the list of similar image clusters.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, you must call the [CreateSimilarImageClusteringTask](https://help.aliyun.com/document_detail/611302.html) operation to cluster similar images in the dataset.
        
        @param request: QuerySimilarImageClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySimilarImageClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySimilarImageClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QuerySimilarImageClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_similar_image_clusters(
        self,
        request: imm_20200930_models.QuerySimilarImageClustersRequest,
    ) -> imm_20200930_models.QuerySimilarImageClustersResponse:
        """
        @summary You can call this operation to query the list of similar image clusters.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, you must call the [CreateSimilarImageClusteringTask](https://help.aliyun.com/document_detail/611302.html) operation to cluster similar images in the dataset.
        
        @param request: QuerySimilarImageClustersRequest
        @return: QuerySimilarImageClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_similar_image_clusters_with_options(request, runtime)

    async def query_similar_image_clusters_async(
        self,
        request: imm_20200930_models.QuerySimilarImageClustersRequest,
    ) -> imm_20200930_models.QuerySimilarImageClustersResponse:
        """
        @summary You can call this operation to query the list of similar image clusters.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, you must call the [CreateSimilarImageClusteringTask](https://help.aliyun.com/document_detail/611302.html) operation to cluster similar images in the dataset.
        
        @param request: QuerySimilarImageClustersRequest
        @return: QuerySimilarImageClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_similar_image_clusters_with_options_async(request, runtime)

    def query_stories_with_options(
        self,
        tmp_req: imm_20200930_models.QueryStoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryStoriesResponse:
        """
        @summary Queries stories based on the specified conditions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param tmp_req: QueryStoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStoriesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryStoriesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.figure_cluster_ids):
            request.figure_cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster_ids, 'FigureClusterIds', 'json')
        if not UtilClient.is_unset(tmp_req.story_end_time_range):
            request.story_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.story_end_time_range, 'StoryEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.story_start_time_range):
            request.story_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.story_start_time_range, 'StoryStartTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_cluster_ids_shrink):
            query['FigureClusterIds'] = request.figure_cluster_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.story_end_time_range_shrink):
            query['StoryEndTimeRange'] = request.story_end_time_range_shrink
        if not UtilClient.is_unset(request.story_name):
            query['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time_range_shrink):
            query['StoryStartTimeRange'] = request.story_start_time_range_shrink
        if not UtilClient.is_unset(request.story_sub_type):
            query['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            query['StoryType'] = request.story_type
        if not UtilClient.is_unset(request.with_empty_stories):
            query['WithEmptyStories'] = request.with_empty_stories
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStories',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryStoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_stories_with_options_async(
        self,
        tmp_req: imm_20200930_models.QueryStoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryStoriesResponse:
        """
        @summary Queries stories based on the specified conditions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param tmp_req: QueryStoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStoriesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryStoriesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.figure_cluster_ids):
            request.figure_cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster_ids, 'FigureClusterIds', 'json')
        if not UtilClient.is_unset(tmp_req.story_end_time_range):
            request.story_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.story_end_time_range, 'StoryEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.story_start_time_range):
            request.story_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.story_start_time_range, 'StoryStartTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_cluster_ids_shrink):
            query['FigureClusterIds'] = request.figure_cluster_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.story_end_time_range_shrink):
            query['StoryEndTimeRange'] = request.story_end_time_range_shrink
        if not UtilClient.is_unset(request.story_name):
            query['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time_range_shrink):
            query['StoryStartTimeRange'] = request.story_start_time_range_shrink
        if not UtilClient.is_unset(request.story_sub_type):
            query['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            query['StoryType'] = request.story_type
        if not UtilClient.is_unset(request.with_empty_stories):
            query['WithEmptyStories'] = request.with_empty_stories
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStories',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryStoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_stories(
        self,
        request: imm_20200930_models.QueryStoriesRequest,
    ) -> imm_20200930_models.QueryStoriesResponse:
        """
        @summary Queries stories based on the specified conditions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param request: QueryStoriesRequest
        @return: QueryStoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_stories_with_options(request, runtime)

    async def query_stories_async(
        self,
        request: imm_20200930_models.QueryStoriesRequest,
    ) -> imm_20200930_models.QueryStoriesResponse:
        """
        @summary Queries stories based on the specified conditions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        Before you call this operation, make sure that you have called the [CreateStory](https://help.aliyun.com/document_detail/478193.html) or [CreateCustomizedStory](https://help.aliyun.com/document_detail/478196.html) operation to create a story.
        
        @param request: QueryStoriesRequest
        @return: QueryStoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_stories_with_options_async(request, runtime)

    def refresh_weboffice_token_with_options(
        self,
        tmp_req: imm_20200930_models.RefreshWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.RefreshWebofficeTokenResponse:
        """
        @summary Refreshes the access credential of WebOffice. The access credential of WebOffice is valid for 30 minutes. After the credential expires, you cannot access Weboffice. To access Weboffice again, call this operation to obtain a new credential. The new credential is also valid for 30 minutes.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.***\
        For more information, see [WebOffice billing](https://help.aliyun.com/document_detail/2639703.html).
        The access token returned by this operation is valid for 30 minutes. After the access token expires, you cannot use it to access the document.
        The refresh token returned by this operation is valid for one day. You need to use the refresh token for the next call to the operation before the refresh token expires. After the validity period elapses, the refresh token is invalid.
        The returned expiration time is displayed in UTC.
        >  An access token is used to actually access a document, whereas a refresh token is used to avoid repeated access configurations.
        
        @param tmp_req: RefreshWebofficeTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshWebofficeTokenResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RefreshWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.refresh_token):
            query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.RefreshWebofficeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_weboffice_token_with_options_async(
        self,
        tmp_req: imm_20200930_models.RefreshWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.RefreshWebofficeTokenResponse:
        """
        @summary Refreshes the access credential of WebOffice. The access credential of WebOffice is valid for 30 minutes. After the credential expires, you cannot access Weboffice. To access Weboffice again, call this operation to obtain a new credential. The new credential is also valid for 30 minutes.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.***\
        For more information, see [WebOffice billing](https://help.aliyun.com/document_detail/2639703.html).
        The access token returned by this operation is valid for 30 minutes. After the access token expires, you cannot use it to access the document.
        The refresh token returned by this operation is valid for one day. You need to use the refresh token for the next call to the operation before the refresh token expires. After the validity period elapses, the refresh token is invalid.
        The returned expiration time is displayed in UTC.
        >  An access token is used to actually access a document, whereas a refresh token is used to avoid repeated access configurations.
        
        @param tmp_req: RefreshWebofficeTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshWebofficeTokenResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RefreshWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.refresh_token):
            query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.RefreshWebofficeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_weboffice_token(
        self,
        request: imm_20200930_models.RefreshWebofficeTokenRequest,
    ) -> imm_20200930_models.RefreshWebofficeTokenResponse:
        """
        @summary Refreshes the access credential of WebOffice. The access credential of WebOffice is valid for 30 minutes. After the credential expires, you cannot access Weboffice. To access Weboffice again, call this operation to obtain a new credential. The new credential is also valid for 30 minutes.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.***\
        For more information, see [WebOffice billing](https://help.aliyun.com/document_detail/2639703.html).
        The access token returned by this operation is valid for 30 minutes. After the access token expires, you cannot use it to access the document.
        The refresh token returned by this operation is valid for one day. You need to use the refresh token for the next call to the operation before the refresh token expires. After the validity period elapses, the refresh token is invalid.
        The returned expiration time is displayed in UTC.
        >  An access token is used to actually access a document, whereas a refresh token is used to avoid repeated access configurations.
        
        @param request: RefreshWebofficeTokenRequest
        @return: RefreshWebofficeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_weboffice_token_with_options(request, runtime)

    async def refresh_weboffice_token_async(
        self,
        request: imm_20200930_models.RefreshWebofficeTokenRequest,
    ) -> imm_20200930_models.RefreshWebofficeTokenResponse:
        """
        @summary Refreshes the access credential of WebOffice. The access credential of WebOffice is valid for 30 minutes. After the credential expires, you cannot access Weboffice. To access Weboffice again, call this operation to obtain a new credential. The new credential is also valid for 30 minutes.
        
        @description Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of IMM.***\
        For more information, see [WebOffice billing](https://help.aliyun.com/document_detail/2639703.html).
        The access token returned by this operation is valid for 30 minutes. After the access token expires, you cannot use it to access the document.
        The refresh token returned by this operation is valid for one day. You need to use the refresh token for the next call to the operation before the refresh token expires. After the validity period elapses, the refresh token is invalid.
        The returned expiration time is displayed in UTC.
        >  An access token is used to actually access a document, whereas a refresh token is used to avoid repeated access configurations.
        
        @param request: RefreshWebofficeTokenRequest
        @return: RefreshWebofficeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_weboffice_token_with_options_async(request, runtime)

    def remove_story_files_with_options(
        self,
        tmp_req: imm_20200930_models.RemoveStoryFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.RemoveStoryFilesResponse:
        """
        @summary Deletes files from a story.
        
        @param tmp_req: RemoveStoryFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveStoryFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RemoveStoryFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveStoryFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.RemoveStoryFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_story_files_with_options_async(
        self,
        tmp_req: imm_20200930_models.RemoveStoryFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.RemoveStoryFilesResponse:
        """
        @summary Deletes files from a story.
        
        @param tmp_req: RemoveStoryFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveStoryFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RemoveStoryFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveStoryFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.RemoveStoryFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_story_files(
        self,
        request: imm_20200930_models.RemoveStoryFilesRequest,
    ) -> imm_20200930_models.RemoveStoryFilesResponse:
        """
        @summary Deletes files from a story.
        
        @param request: RemoveStoryFilesRequest
        @return: RemoveStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_story_files_with_options(request, runtime)

    async def remove_story_files_async(
        self,
        request: imm_20200930_models.RemoveStoryFilesRequest,
    ) -> imm_20200930_models.RemoveStoryFilesResponse:
        """
        @summary Deletes files from a story.
        
        @param request: RemoveStoryFilesRequest
        @return: RemoveStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_story_files_with_options_async(request, runtime)

    def resume_batch_with_options(
        self,
        request: imm_20200930_models.ResumeBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeBatchResponse:
        """
        @summary Resumes a batch processing task that is in the Suspended or Failed state.
        
        @description You can resume a batch processing task only when the task is in the Suspended or Failed state. A batch processing task continues to provide services after you resume the task.
        
        @param request: ResumeBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_batch_with_options_async(
        self,
        request: imm_20200930_models.ResumeBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeBatchResponse:
        """
        @summary Resumes a batch processing task that is in the Suspended or Failed state.
        
        @description You can resume a batch processing task only when the task is in the Suspended or Failed state. A batch processing task continues to provide services after you resume the task.
        
        @param request: ResumeBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_batch(
        self,
        request: imm_20200930_models.ResumeBatchRequest,
    ) -> imm_20200930_models.ResumeBatchResponse:
        """
        @summary Resumes a batch processing task that is in the Suspended or Failed state.
        
        @description You can resume a batch processing task only when the task is in the Suspended or Failed state. A batch processing task continues to provide services after you resume the task.
        
        @param request: ResumeBatchRequest
        @return: ResumeBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_batch_with_options(request, runtime)

    async def resume_batch_async(
        self,
        request: imm_20200930_models.ResumeBatchRequest,
    ) -> imm_20200930_models.ResumeBatchResponse:
        """
        @summary Resumes a batch processing task that is in the Suspended or Failed state.
        
        @description You can resume a batch processing task only when the task is in the Suspended or Failed state. A batch processing task continues to provide services after you resume the task.
        
        @param request: ResumeBatchRequest
        @return: ResumeBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_batch_with_options_async(request, runtime)

    def resume_trigger_with_options(
        self,
        request: imm_20200930_models.ResumeTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeTriggerResponse:
        """
        @summary Resumes a trigger that is in the Suspended or Failed state.
        
        @description You can resume only a trigger that is in the Suspended or Failed state. After you resume a trigger, the trigger continues to provide services as expected.
        
        @param request: ResumeTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_trigger_with_options_async(
        self,
        request: imm_20200930_models.ResumeTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeTriggerResponse:
        """
        @summary Resumes a trigger that is in the Suspended or Failed state.
        
        @description You can resume only a trigger that is in the Suspended or Failed state. After you resume a trigger, the trigger continues to provide services as expected.
        
        @param request: ResumeTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_trigger(
        self,
        request: imm_20200930_models.ResumeTriggerRequest,
    ) -> imm_20200930_models.ResumeTriggerResponse:
        """
        @summary Resumes a trigger that is in the Suspended or Failed state.
        
        @description You can resume only a trigger that is in the Suspended or Failed state. After you resume a trigger, the trigger continues to provide services as expected.
        
        @param request: ResumeTriggerRequest
        @return: ResumeTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_trigger_with_options(request, runtime)

    async def resume_trigger_async(
        self,
        request: imm_20200930_models.ResumeTriggerRequest,
    ) -> imm_20200930_models.ResumeTriggerResponse:
        """
        @summary Resumes a trigger that is in the Suspended or Failed state.
        
        @description You can resume only a trigger that is in the Suspended or Failed state. After you resume a trigger, the trigger continues to provide services as expected.
        
        @param request: ResumeTriggerRequest
        @return: ResumeTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_trigger_with_options_async(request, runtime)

    def search_image_figure_cluster_with_options(
        self,
        tmp_req: imm_20200930_models.SearchImageFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SearchImageFigureClusterResponse:
        """
        @summary Queries face clusters that contain a specific face in an image. Each face cluster contains information such as bounding boxes and similarity.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have created a face clustering task by calling the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        
        @param tmp_req: SearchImageFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SearchImageFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchImageFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SearchImageFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_figure_cluster_with_options_async(
        self,
        tmp_req: imm_20200930_models.SearchImageFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SearchImageFigureClusterResponse:
        """
        @summary Queries face clusters that contain a specific face in an image. Each face cluster contains information such as bounding boxes and similarity.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have created a face clustering task by calling the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        
        @param tmp_req: SearchImageFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SearchImageFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchImageFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SearchImageFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image_figure_cluster(
        self,
        request: imm_20200930_models.SearchImageFigureClusterRequest,
    ) -> imm_20200930_models.SearchImageFigureClusterResponse:
        """
        @summary Queries face clusters that contain a specific face in an image. Each face cluster contains information such as bounding boxes and similarity.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have created a face clustering task by calling the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        
        @param request: SearchImageFigureClusterRequest
        @return: SearchImageFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_image_figure_cluster_with_options(request, runtime)

    async def search_image_figure_cluster_async(
        self,
        request: imm_20200930_models.SearchImageFigureClusterRequest,
    ) -> imm_20200930_models.SearchImageFigureClusterResponse:
        """
        @summary Queries face clusters that contain a specific face in an image. Each face cluster contains information such as bounding boxes and similarity.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/88317.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have created a face clustering task by calling the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        
        @param request: SearchImageFigureClusterRequest
        @return: SearchImageFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_image_figure_cluster_with_options_async(request, runtime)

    def semantic_query_with_options(
        self,
        tmp_req: imm_20200930_models.SemanticQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SemanticQueryResponse:
        """
        @summary Queries metadata in a dataset by inputting natural language.
        
        @description ### [](#)Precautions
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**** Each time you call this operation, you are charged for semantic understanding and query fees.
        Before you call this operation, make sure that the file that you want to use is indexed into the dataset that you use. To index a file into a dataset, you can call one of the following operations: [CreateBinding](https://help.aliyun.com/document_detail/478202.html), [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html), and [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html).
        The response provided in this example is for reference only. The categories and content of metadata vary based on configurations of [workflow templates](https://help.aliyun.com/document_detail/466304.html). If you have questions, search for and join the DingTalk group numbered 21714099.
        ### [](#)Usage limits
        Each time you call this operation, up to 1,000 metadata files are returned.
        Pagination is not supported.
        The natural language processing capability may not always produce completely accurate results.
        ### [](#)Usage methods
        You can query files within a dataset by using natural language keywords. Key information supported for understanding includes labels (Labels.LabelName), time (ProduceTime), and location (Address.AddressLine). For example, if you use `2023 Hangzhou scenery` as the query criterion, the operation intelligently breaks the query criterion down into the following sub-criteria, and returns the files that meet all the sub-criteria:
        ProduceTime: 00:00 on January 1, 2023 to 00:00 on December 31, 2023.
        Address.AddressLine: `Hangzhou`
        Labels.LabelName: `scenery`.
        When you call this operation, you can configure a [workflow template](https://help.aliyun.com/document_detail/466304.html) that includes the `ImageEmbeddingExtraction` operator. This allows the operation to return image content when the query you input matches the image content, thereby achieving intelligent image retrieval.``
        
        @param tmp_req: SemanticQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SemanticQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SemanticQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.media_types):
            request.media_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.media_types, 'MediaTypes', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.media_types_shrink):
            query['MediaTypes'] = request.media_types_shrink
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SemanticQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SemanticQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def semantic_query_with_options_async(
        self,
        tmp_req: imm_20200930_models.SemanticQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SemanticQueryResponse:
        """
        @summary Queries metadata in a dataset by inputting natural language.
        
        @description ### [](#)Precautions
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**** Each time you call this operation, you are charged for semantic understanding and query fees.
        Before you call this operation, make sure that the file that you want to use is indexed into the dataset that you use. To index a file into a dataset, you can call one of the following operations: [CreateBinding](https://help.aliyun.com/document_detail/478202.html), [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html), and [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html).
        The response provided in this example is for reference only. The categories and content of metadata vary based on configurations of [workflow templates](https://help.aliyun.com/document_detail/466304.html). If you have questions, search for and join the DingTalk group numbered 21714099.
        ### [](#)Usage limits
        Each time you call this operation, up to 1,000 metadata files are returned.
        Pagination is not supported.
        The natural language processing capability may not always produce completely accurate results.
        ### [](#)Usage methods
        You can query files within a dataset by using natural language keywords. Key information supported for understanding includes labels (Labels.LabelName), time (ProduceTime), and location (Address.AddressLine). For example, if you use `2023 Hangzhou scenery` as the query criterion, the operation intelligently breaks the query criterion down into the following sub-criteria, and returns the files that meet all the sub-criteria:
        ProduceTime: 00:00 on January 1, 2023 to 00:00 on December 31, 2023.
        Address.AddressLine: `Hangzhou`
        Labels.LabelName: `scenery`.
        When you call this operation, you can configure a [workflow template](https://help.aliyun.com/document_detail/466304.html) that includes the `ImageEmbeddingExtraction` operator. This allows the operation to return image content when the query you input matches the image content, thereby achieving intelligent image retrieval.``
        
        @param tmp_req: SemanticQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SemanticQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SemanticQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.media_types):
            request.media_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.media_types, 'MediaTypes', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.media_types_shrink):
            query['MediaTypes'] = request.media_types_shrink
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SemanticQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SemanticQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def semantic_query(
        self,
        request: imm_20200930_models.SemanticQueryRequest,
    ) -> imm_20200930_models.SemanticQueryResponse:
        """
        @summary Queries metadata in a dataset by inputting natural language.
        
        @description ### [](#)Precautions
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**** Each time you call this operation, you are charged for semantic understanding and query fees.
        Before you call this operation, make sure that the file that you want to use is indexed into the dataset that you use. To index a file into a dataset, you can call one of the following operations: [CreateBinding](https://help.aliyun.com/document_detail/478202.html), [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html), and [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html).
        The response provided in this example is for reference only. The categories and content of metadata vary based on configurations of [workflow templates](https://help.aliyun.com/document_detail/466304.html). If you have questions, search for and join the DingTalk group numbered 21714099.
        ### [](#)Usage limits
        Each time you call this operation, up to 1,000 metadata files are returned.
        Pagination is not supported.
        The natural language processing capability may not always produce completely accurate results.
        ### [](#)Usage methods
        You can query files within a dataset by using natural language keywords. Key information supported for understanding includes labels (Labels.LabelName), time (ProduceTime), and location (Address.AddressLine). For example, if you use `2023 Hangzhou scenery` as the query criterion, the operation intelligently breaks the query criterion down into the following sub-criteria, and returns the files that meet all the sub-criteria:
        ProduceTime: 00:00 on January 1, 2023 to 00:00 on December 31, 2023.
        Address.AddressLine: `Hangzhou`
        Labels.LabelName: `scenery`.
        When you call this operation, you can configure a [workflow template](https://help.aliyun.com/document_detail/466304.html) that includes the `ImageEmbeddingExtraction` operator. This allows the operation to return image content when the query you input matches the image content, thereby achieving intelligent image retrieval.``
        
        @param request: SemanticQueryRequest
        @return: SemanticQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.semantic_query_with_options(request, runtime)

    async def semantic_query_async(
        self,
        request: imm_20200930_models.SemanticQueryRequest,
    ) -> imm_20200930_models.SemanticQueryResponse:
        """
        @summary Queries metadata in a dataset by inputting natural language.
        
        @description ### [](#)Precautions
        Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).**** Each time you call this operation, you are charged for semantic understanding and query fees.
        Before you call this operation, make sure that the file that you want to use is indexed into the dataset that you use. To index a file into a dataset, you can call one of the following operations: [CreateBinding](https://help.aliyun.com/document_detail/478202.html), [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html), and [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html).
        The response provided in this example is for reference only. The categories and content of metadata vary based on configurations of [workflow templates](https://help.aliyun.com/document_detail/466304.html). If you have questions, search for and join the DingTalk group numbered 21714099.
        ### [](#)Usage limits
        Each time you call this operation, up to 1,000 metadata files are returned.
        Pagination is not supported.
        The natural language processing capability may not always produce completely accurate results.
        ### [](#)Usage methods
        You can query files within a dataset by using natural language keywords. Key information supported for understanding includes labels (Labels.LabelName), time (ProduceTime), and location (Address.AddressLine). For example, if you use `2023 Hangzhou scenery` as the query criterion, the operation intelligently breaks the query criterion down into the following sub-criteria, and returns the files that meet all the sub-criteria:
        ProduceTime: 00:00 on January 1, 2023 to 00:00 on December 31, 2023.
        Address.AddressLine: `Hangzhou`
        Labels.LabelName: `scenery`.
        When you call this operation, you can configure a [workflow template](https://help.aliyun.com/document_detail/466304.html) that includes the `ImageEmbeddingExtraction` operator. This allows the operation to return image content when the query you input matches the image content, thereby achieving intelligent image retrieval.``
        
        @param request: SemanticQueryRequest
        @return: SemanticQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.semantic_query_with_options_async(request, runtime)

    def simple_query_with_options(
        self,
        tmp_req: imm_20200930_models.SimpleQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SimpleQueryResponse:
        """
        @summary Queries files in a dataset by performing a simple query operation. The operation supports logical expressions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        *Limits**\
        Each query returns information about up to 100 files.
        Each query returns up to 2,000 aggregations.
        A subquery supports up to 100 conditions.
        A subquery can have a maximum nesting depth of 5 levels.
        *Example query conditions**\
        Retrieve JPEG images larger than 1,000 pixels:
        <!---->
        {
        "SubQueries":[
        {
        "Field":"ContentType",
        "Value": "image/jpeg",
        "Operation":"eq"
        },
        {
        "Field":"ImageWidth",
        "Value":"1000",
        "Operation":"gt"
        }
        ],
        "Operation":"and"
        }
        Search `oss://examplebucket/path/` for objects that have the `TV` or `Stereo` label and are larger than 10 MB in size:
        >  This query requires matching files to have the `TV` or `Stereo` label. The two labels are specified as separate objects in the `Labels` fields.
        ```
        {
        "SubQueries": [
        {
        "Field": "URI",
        "Value": "oss://examplebucket/path/",
        "Operation": "prefix"
        },
        {
        "Field": "Size",
        "Value": "1048576",
        "Operation": "gt"
        },
        {
        "SubQueries": [
        {
        "Field": "Labels.LabelName",
        "Value": "TV",
        "Operation": "eq"
        },
        {
        "Field": "Labels.LabelName",
        "Value": "Stereo",
        "Operation": "eq"
        }
        ],
        "Operation": "or"
        }
        ],
        "Operation": "and"
        }
        
        ```
        Exclude images that contain a face of a male over the age of 36:
        >  In this example query, an image will be excluded from the query results if it contains a face of a male over the age of 36. This query is different from excluding an image that contains a male face or a face of a person over the age of 36. In this query, you need to use the `nested` operator to specify that the conditions are met on the same element.
        {
        "Operation": "not",
        "SubQueries": [{
        "Operation": "nested",
        "SubQueries": [{
        "Operation": "and",
        "SubQueries": [{
        "Field": "Figures.Age",
        "Operation": "gt",
        "Value": "36"
        }, {
        "Field": "Figures.Gender",
        "Operation": "eq",
        "Value": "male"
        }]
        }]
        }]
        }
        Query JPEG images that have both custom labels and system labels:
        <!---->
        {
        "SubQueries":[
        {
        "Field":"ContentType",
        "Value": "image/jpeg",
        "Operation":"eq"
        },
        {
        "Field":"CustomLabels.test",
        "Operation":"exist"
        },
        {
        "Field":"Labels.LabelName",
        "Operation":"exist"
        }
        ],
        "Operation":"and"
        }
        You can also perform aggregate operations to collect and analyze different data based on the specified conditions. For example, you can calculate the sum, count, average value, or maximum value of all files that meet the query conditions. You can also calculate the size distribution of images that meet the query conditions.
        
        @param tmp_req: SimpleQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SimpleQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SimpleQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aggregations):
            request.aggregations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.aggregations_shrink):
            query['Aggregations'] = request.aggregations_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query_shrink):
            query['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        if not UtilClient.is_unset(request.without_total_hits):
            query['WithoutTotalHits'] = request.without_total_hits
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SimpleQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SimpleQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def simple_query_with_options_async(
        self,
        tmp_req: imm_20200930_models.SimpleQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SimpleQueryResponse:
        """
        @summary Queries files in a dataset by performing a simple query operation. The operation supports logical expressions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        *Limits**\
        Each query returns information about up to 100 files.
        Each query returns up to 2,000 aggregations.
        A subquery supports up to 100 conditions.
        A subquery can have a maximum nesting depth of 5 levels.
        *Example query conditions**\
        Retrieve JPEG images larger than 1,000 pixels:
        <!---->
        {
        "SubQueries":[
        {
        "Field":"ContentType",
        "Value": "image/jpeg",
        "Operation":"eq"
        },
        {
        "Field":"ImageWidth",
        "Value":"1000",
        "Operation":"gt"
        }
        ],
        "Operation":"and"
        }
        Search `oss://examplebucket/path/` for objects that have the `TV` or `Stereo` label and are larger than 10 MB in size:
        >  This query requires matching files to have the `TV` or `Stereo` label. The two labels are specified as separate objects in the `Labels` fields.
        ```
        {
        "SubQueries": [
        {
        "Field": "URI",
        "Value": "oss://examplebucket/path/",
        "Operation": "prefix"
        },
        {
        "Field": "Size",
        "Value": "1048576",
        "Operation": "gt"
        },
        {
        "SubQueries": [
        {
        "Field": "Labels.LabelName",
        "Value": "TV",
        "Operation": "eq"
        },
        {
        "Field": "Labels.LabelName",
        "Value": "Stereo",
        "Operation": "eq"
        }
        ],
        "Operation": "or"
        }
        ],
        "Operation": "and"
        }
        
        ```
        Exclude images that contain a face of a male over the age of 36:
        >  In this example query, an image will be excluded from the query results if it contains a face of a male over the age of 36. This query is different from excluding an image that contains a male face or a face of a person over the age of 36. In this query, you need to use the `nested` operator to specify that the conditions are met on the same element.
        {
        "Operation": "not",
        "SubQueries": [{
        "Operation": "nested",
        "SubQueries": [{
        "Operation": "and",
        "SubQueries": [{
        "Field": "Figures.Age",
        "Operation": "gt",
        "Value": "36"
        }, {
        "Field": "Figures.Gender",
        "Operation": "eq",
        "Value": "male"
        }]
        }]
        }]
        }
        Query JPEG images that have both custom labels and system labels:
        <!---->
        {
        "SubQueries":[
        {
        "Field":"ContentType",
        "Value": "image/jpeg",
        "Operation":"eq"
        },
        {
        "Field":"CustomLabels.test",
        "Operation":"exist"
        },
        {
        "Field":"Labels.LabelName",
        "Operation":"exist"
        }
        ],
        "Operation":"and"
        }
        You can also perform aggregate operations to collect and analyze different data based on the specified conditions. For example, you can calculate the sum, count, average value, or maximum value of all files that meet the query conditions. You can also calculate the size distribution of images that meet the query conditions.
        
        @param tmp_req: SimpleQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SimpleQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SimpleQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aggregations):
            request.aggregations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.aggregations_shrink):
            query['Aggregations'] = request.aggregations_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query_shrink):
            query['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        if not UtilClient.is_unset(request.without_total_hits):
            query['WithoutTotalHits'] = request.without_total_hits
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SimpleQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SimpleQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def simple_query(
        self,
        request: imm_20200930_models.SimpleQueryRequest,
    ) -> imm_20200930_models.SimpleQueryResponse:
        """
        @summary Queries files in a dataset by performing a simple query operation. The operation supports logical expressions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        *Limits**\
        Each query returns information about up to 100 files.
        Each query returns up to 2,000 aggregations.
        A subquery supports up to 100 conditions.
        A subquery can have a maximum nesting depth of 5 levels.
        *Example query conditions**\
        Retrieve JPEG images larger than 1,000 pixels:
        <!---->
        {
        "SubQueries":[
        {
        "Field":"ContentType",
        "Value": "image/jpeg",
        "Operation":"eq"
        },
        {
        "Field":"ImageWidth",
        "Value":"1000",
        "Operation":"gt"
        }
        ],
        "Operation":"and"
        }
        Search `oss://examplebucket/path/` for objects that have the `TV` or `Stereo` label and are larger than 10 MB in size:
        >  This query requires matching files to have the `TV` or `Stereo` label. The two labels are specified as separate objects in the `Labels` fields.
        ```
        {
        "SubQueries": [
        {
        "Field": "URI",
        "Value": "oss://examplebucket/path/",
        "Operation": "prefix"
        },
        {
        "Field": "Size",
        "Value": "1048576",
        "Operation": "gt"
        },
        {
        "SubQueries": [
        {
        "Field": "Labels.LabelName",
        "Value": "TV",
        "Operation": "eq"
        },
        {
        "Field": "Labels.LabelName",
        "Value": "Stereo",
        "Operation": "eq"
        }
        ],
        "Operation": "or"
        }
        ],
        "Operation": "and"
        }
        
        ```
        Exclude images that contain a face of a male over the age of 36:
        >  In this example query, an image will be excluded from the query results if it contains a face of a male over the age of 36. This query is different from excluding an image that contains a male face or a face of a person over the age of 36. In this query, you need to use the `nested` operator to specify that the conditions are met on the same element.
        {
        "Operation": "not",
        "SubQueries": [{
        "Operation": "nested",
        "SubQueries": [{
        "Operation": "and",
        "SubQueries": [{
        "Field": "Figures.Age",
        "Operation": "gt",
        "Value": "36"
        }, {
        "Field": "Figures.Gender",
        "Operation": "eq",
        "Value": "male"
        }]
        }]
        }]
        }
        Query JPEG images that have both custom labels and system labels:
        <!---->
        {
        "SubQueries":[
        {
        "Field":"ContentType",
        "Value": "image/jpeg",
        "Operation":"eq"
        },
        {
        "Field":"CustomLabels.test",
        "Operation":"exist"
        },
        {
        "Field":"Labels.LabelName",
        "Operation":"exist"
        }
        ],
        "Operation":"and"
        }
        You can also perform aggregate operations to collect and analyze different data based on the specified conditions. For example, you can calculate the sum, count, average value, or maximum value of all files that meet the query conditions. You can also calculate the size distribution of images that meet the query conditions.
        
        @param request: SimpleQueryRequest
        @return: SimpleQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.simple_query_with_options(request, runtime)

    async def simple_query_async(
        self,
        request: imm_20200930_models.SimpleQueryRequest,
    ) -> imm_20200930_models.SimpleQueryResponse:
        """
        @summary Queries files in a dataset by performing a simple query operation. The operation supports logical expressions.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have indexed file metadata into the dataset automatically by calling the [CreateBinding](https://help.aliyun.com/document_detail/478202.html) operation or manually by calling the [IndexFileMeta](https://help.aliyun.com/document_detail/478166.html) or [BatchIndexFileMeta](https://help.aliyun.com/document_detail/478167.html) operation.
        The sample response is provided for reference only. The metadata type and content in your response may differ based on factors such as the [workflow template configurations](https://help.aliyun.com/document_detail/466304.html). For any inquiries, join the DingTalk chat group (ID: 31690030817) and share your questions with us.
        *Limits**\
        Each query returns information about up to 100 files.
        Each query returns up to 2,000 aggregations.
        A subquery supports up to 100 conditions.
        A subquery can have a maximum nesting depth of 5 levels.
        *Example query conditions**\
        Retrieve JPEG images larger than 1,000 pixels:
        <!---->
        {
        "SubQueries":[
        {
        "Field":"ContentType",
        "Value": "image/jpeg",
        "Operation":"eq"
        },
        {
        "Field":"ImageWidth",
        "Value":"1000",
        "Operation":"gt"
        }
        ],
        "Operation":"and"
        }
        Search `oss://examplebucket/path/` for objects that have the `TV` or `Stereo` label and are larger than 10 MB in size:
        >  This query requires matching files to have the `TV` or `Stereo` label. The two labels are specified as separate objects in the `Labels` fields.
        ```
        {
        "SubQueries": [
        {
        "Field": "URI",
        "Value": "oss://examplebucket/path/",
        "Operation": "prefix"
        },
        {
        "Field": "Size",
        "Value": "1048576",
        "Operation": "gt"
        },
        {
        "SubQueries": [
        {
        "Field": "Labels.LabelName",
        "Value": "TV",
        "Operation": "eq"
        },
        {
        "Field": "Labels.LabelName",
        "Value": "Stereo",
        "Operation": "eq"
        }
        ],
        "Operation": "or"
        }
        ],
        "Operation": "and"
        }
        
        ```
        Exclude images that contain a face of a male over the age of 36:
        >  In this example query, an image will be excluded from the query results if it contains a face of a male over the age of 36. This query is different from excluding an image that contains a male face or a face of a person over the age of 36. In this query, you need to use the `nested` operator to specify that the conditions are met on the same element.
        {
        "Operation": "not",
        "SubQueries": [{
        "Operation": "nested",
        "SubQueries": [{
        "Operation": "and",
        "SubQueries": [{
        "Field": "Figures.Age",
        "Operation": "gt",
        "Value": "36"
        }, {
        "Field": "Figures.Gender",
        "Operation": "eq",
        "Value": "male"
        }]
        }]
        }]
        }
        Query JPEG images that have both custom labels and system labels:
        <!---->
        {
        "SubQueries":[
        {
        "Field":"ContentType",
        "Value": "image/jpeg",
        "Operation":"eq"
        },
        {
        "Field":"CustomLabels.test",
        "Operation":"exist"
        },
        {
        "Field":"Labels.LabelName",
        "Operation":"exist"
        }
        ],
        "Operation":"and"
        }
        You can also perform aggregate operations to collect and analyze different data based on the specified conditions. For example, you can calculate the sum, count, average value, or maximum value of all files that meet the query conditions. You can also calculate the size distribution of images that meet the query conditions.
        
        @param request: SimpleQueryRequest
        @return: SimpleQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.simple_query_with_options_async(request, runtime)

    def suspend_batch_with_options(
        self,
        request: imm_20200930_models.SuspendBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SuspendBatchResponse:
        """
        @summary Suspends a batch processing task.
        
        @description You can suspend a batch processing task that is in the Running state. You can call the [ResumeBatch](https://help.aliyun.com/document_detail/479914.html) operation to resume a batch processing task that is suspended.
        
        @param request: SuspendBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SuspendBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_batch_with_options_async(
        self,
        request: imm_20200930_models.SuspendBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SuspendBatchResponse:
        """
        @summary Suspends a batch processing task.
        
        @description You can suspend a batch processing task that is in the Running state. You can call the [ResumeBatch](https://help.aliyun.com/document_detail/479914.html) operation to resume a batch processing task that is suspended.
        
        @param request: SuspendBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SuspendBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_batch(
        self,
        request: imm_20200930_models.SuspendBatchRequest,
    ) -> imm_20200930_models.SuspendBatchResponse:
        """
        @summary Suspends a batch processing task.
        
        @description You can suspend a batch processing task that is in the Running state. You can call the [ResumeBatch](https://help.aliyun.com/document_detail/479914.html) operation to resume a batch processing task that is suspended.
        
        @param request: SuspendBatchRequest
        @return: SuspendBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_batch_with_options(request, runtime)

    async def suspend_batch_async(
        self,
        request: imm_20200930_models.SuspendBatchRequest,
    ) -> imm_20200930_models.SuspendBatchResponse:
        """
        @summary Suspends a batch processing task.
        
        @description You can suspend a batch processing task that is in the Running state. You can call the [ResumeBatch](https://help.aliyun.com/document_detail/479914.html) operation to resume a batch processing task that is suspended.
        
        @param request: SuspendBatchRequest
        @return: SuspendBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_batch_with_options_async(request, runtime)

    def suspend_trigger_with_options(
        self,
        request: imm_20200930_models.SuspendTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SuspendTriggerResponse:
        """
        @summary Suspends a running trigger.
        
        @description The operation can be used to suspend a trigger only in the Running state. If you want to resume a suspended trigger, call the [ResumeTrigger](https://help.aliyun.com/document_detail/479919.html) operation.
        
        @param request: SuspendTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SuspendTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_trigger_with_options_async(
        self,
        request: imm_20200930_models.SuspendTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SuspendTriggerResponse:
        """
        @summary Suspends a running trigger.
        
        @description The operation can be used to suspend a trigger only in the Running state. If you want to resume a suspended trigger, call the [ResumeTrigger](https://help.aliyun.com/document_detail/479919.html) operation.
        
        @param request: SuspendTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SuspendTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_trigger(
        self,
        request: imm_20200930_models.SuspendTriggerRequest,
    ) -> imm_20200930_models.SuspendTriggerResponse:
        """
        @summary Suspends a running trigger.
        
        @description The operation can be used to suspend a trigger only in the Running state. If you want to resume a suspended trigger, call the [ResumeTrigger](https://help.aliyun.com/document_detail/479919.html) operation.
        
        @param request: SuspendTriggerRequest
        @return: SuspendTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_trigger_with_options(request, runtime)

    async def suspend_trigger_async(
        self,
        request: imm_20200930_models.SuspendTriggerRequest,
    ) -> imm_20200930_models.SuspendTriggerResponse:
        """
        @summary Suspends a running trigger.
        
        @description The operation can be used to suspend a trigger only in the Running state. If you want to resume a suspended trigger, call the [ResumeTrigger](https://help.aliyun.com/document_detail/479919.html) operation.
        
        @param request: SuspendTriggerRequest
        @return: SuspendTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_trigger_with_options_async(request, runtime)

    def update_batch_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateBatchResponse:
        """
        @summary Updates information about a batch processing task, including the input data source, data processing settings, and tags.
        
        @description    You can update only a batch processing task that is in the Ready or Failed state. The update operation does not change the status of the batch processing task.
        If you update a batch processing task that is in progress, the task is not automatically resumed after the update is complete. You must call the [ResumeBatch](https://help.aliyun.com/document_detail/479914.html) operation to resume the task.
        
        @param tmp_req: UpdateBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_batch_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateBatchResponse:
        """
        @summary Updates information about a batch processing task, including the input data source, data processing settings, and tags.
        
        @description    You can update only a batch processing task that is in the Ready or Failed state. The update operation does not change the status of the batch processing task.
        If you update a batch processing task that is in progress, the task is not automatically resumed after the update is complete. You must call the [ResumeBatch](https://help.aliyun.com/document_detail/479914.html) operation to resume the task.
        
        @param tmp_req: UpdateBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_batch(
        self,
        request: imm_20200930_models.UpdateBatchRequest,
    ) -> imm_20200930_models.UpdateBatchResponse:
        """
        @summary Updates information about a batch processing task, including the input data source, data processing settings, and tags.
        
        @description    You can update only a batch processing task that is in the Ready or Failed state. The update operation does not change the status of the batch processing task.
        If you update a batch processing task that is in progress, the task is not automatically resumed after the update is complete. You must call the [ResumeBatch](https://help.aliyun.com/document_detail/479914.html) operation to resume the task.
        
        @param request: UpdateBatchRequest
        @return: UpdateBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_batch_with_options(request, runtime)

    async def update_batch_async(
        self,
        request: imm_20200930_models.UpdateBatchRequest,
    ) -> imm_20200930_models.UpdateBatchResponse:
        """
        @summary Updates information about a batch processing task, including the input data source, data processing settings, and tags.
        
        @description    You can update only a batch processing task that is in the Ready or Failed state. The update operation does not change the status of the batch processing task.
        If you update a batch processing task that is in progress, the task is not automatically resumed after the update is complete. You must call the [ResumeBatch](https://help.aliyun.com/document_detail/479914.html) operation to resume the task.
        
        @param request: UpdateBatchRequest
        @return: UpdateBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_batch_with_options_async(request, runtime)

    def update_dataset_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateDatasetResponse:
        """
        @summary Updates a dataset.
        
        @param tmp_req: UpdateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_parameters):
            request.workflow_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_parameters, 'WorkflowParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.workflow_parameters_shrink):
            query['WorkflowParameters'] = request.workflow_parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateDatasetResponse:
        """
        @summary Updates a dataset.
        
        @param tmp_req: UpdateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_parameters):
            request.workflow_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_parameters, 'WorkflowParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.workflow_parameters_shrink):
            query['WorkflowParameters'] = request.workflow_parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset(
        self,
        request: imm_20200930_models.UpdateDatasetRequest,
    ) -> imm_20200930_models.UpdateDatasetResponse:
        """
        @summary Updates a dataset.
        
        @param request: UpdateDatasetRequest
        @return: UpdateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dataset_with_options(request, runtime)

    async def update_dataset_async(
        self,
        request: imm_20200930_models.UpdateDatasetRequest,
    ) -> imm_20200930_models.UpdateDatasetResponse:
        """
        @summary Updates a dataset.
        
        @param request: UpdateDatasetRequest
        @return: UpdateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dataset_with_options_async(request, runtime)

    def update_figure_cluster_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateFigureClusterResponse:
        """
        @summary Updates information about a face cluster, such as the cluster name and labels.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        The operation updates only the cover image, cluster name, and tags.
        After the operation is successful, you can call the [GetFigureCluster](https://help.aliyun.com/document_detail/478182.html) or [BatchGetFigureCluster](https://help.aliyun.com/document_detail/2248450.html) operation to query the updated cluster.
        
        @param tmp_req: UpdateFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.figure_cluster):
            request.figure_cluster_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster, 'FigureCluster', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_cluster_shrink):
            query['FigureCluster'] = request.figure_cluster_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_figure_cluster_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateFigureClusterResponse:
        """
        @summary Updates information about a face cluster, such as the cluster name and labels.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        The operation updates only the cover image, cluster name, and tags.
        After the operation is successful, you can call the [GetFigureCluster](https://help.aliyun.com/document_detail/478182.html) or [BatchGetFigureCluster](https://help.aliyun.com/document_detail/2248450.html) operation to query the updated cluster.
        
        @param tmp_req: UpdateFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.figure_cluster):
            request.figure_cluster_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster, 'FigureCluster', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_cluster_shrink):
            query['FigureCluster'] = request.figure_cluster_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_figure_cluster(
        self,
        request: imm_20200930_models.UpdateFigureClusterRequest,
    ) -> imm_20200930_models.UpdateFigureClusterResponse:
        """
        @summary Updates information about a face cluster, such as the cluster name and labels.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        The operation updates only the cover image, cluster name, and tags.
        After the operation is successful, you can call the [GetFigureCluster](https://help.aliyun.com/document_detail/478182.html) or [BatchGetFigureCluster](https://help.aliyun.com/document_detail/2248450.html) operation to query the updated cluster.
        
        @param request: UpdateFigureClusterRequest
        @return: UpdateFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_figure_cluster_with_options(request, runtime)

    async def update_figure_cluster_async(
        self,
        request: imm_20200930_models.UpdateFigureClusterRequest,
    ) -> imm_20200930_models.UpdateFigureClusterResponse:
        """
        @summary Updates information about a face cluster, such as the cluster name and labels.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateFigureClusteringTask](https://help.aliyun.com/document_detail/478180.html) operation to cluster all faces in the dataset.
        The operation updates only the cover image, cluster name, and tags.
        After the operation is successful, you can call the [GetFigureCluster](https://help.aliyun.com/document_detail/478182.html) or [BatchGetFigureCluster](https://help.aliyun.com/document_detail/2248450.html) operation to query the updated cluster.
        
        @param request: UpdateFigureClusterRequest
        @return: UpdateFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_figure_cluster_with_options_async(request, runtime)

    def update_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateFileMetaResponse:
        """
        @summary Updates the partial metadata of the indexed files in a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        You cannot call this operation to update all metadata. You can update only metadata specified by CustomLabels, CustomId, and Figures. For more information, see the "Request parameters" section of this topic.
        
        @param tmp_req: UpdateFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateFileMetaResponse:
        """
        @summary Updates the partial metadata of the indexed files in a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        You cannot call this operation to update all metadata. You can update only metadata specified by CustomLabels, CustomId, and Figures. For more information, see the "Request parameters" section of this topic.
        
        @param tmp_req: UpdateFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file_meta(
        self,
        request: imm_20200930_models.UpdateFileMetaRequest,
    ) -> imm_20200930_models.UpdateFileMetaResponse:
        """
        @summary Updates the partial metadata of the indexed files in a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        You cannot call this operation to update all metadata. You can update only metadata specified by CustomLabels, CustomId, and Figures. For more information, see the "Request parameters" section of this topic.
        
        @param request: UpdateFileMetaRequest
        @return: UpdateFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_file_meta_with_options(request, runtime)

    async def update_file_meta_async(
        self,
        request: imm_20200930_models.UpdateFileMetaRequest,
    ) -> imm_20200930_models.UpdateFileMetaResponse:
        """
        @summary Updates the partial metadata of the indexed files in a dataset.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        You cannot call this operation to update all metadata. You can update only metadata specified by CustomLabels, CustomId, and Figures. For more information, see the "Request parameters" section of this topic.
        
        @param request: UpdateFileMetaRequest
        @return: UpdateFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_file_meta_with_options_async(request, runtime)

    def update_location_date_cluster_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateLocationDateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateLocationDateClusterResponse:
        """
        @summary Updates a spatiotemporal cluster.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to create spatiotemporal clusters in the project.
        
        @param tmp_req: UpdateLocationDateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLocationDateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateLocationDateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_id):
            query['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            query['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLocationDateCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateLocationDateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_location_date_cluster_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateLocationDateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateLocationDateClusterResponse:
        """
        @summary Updates a spatiotemporal cluster.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to create spatiotemporal clusters in the project.
        
        @param tmp_req: UpdateLocationDateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLocationDateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateLocationDateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_id):
            query['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            query['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLocationDateCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateLocationDateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_location_date_cluster(
        self,
        request: imm_20200930_models.UpdateLocationDateClusterRequest,
    ) -> imm_20200930_models.UpdateLocationDateClusterResponse:
        """
        @summary Updates a spatiotemporal cluster.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to create spatiotemporal clusters in the project.
        
        @param request: UpdateLocationDateClusterRequest
        @return: UpdateLocationDateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_location_date_cluster_with_options(request, runtime)

    async def update_location_date_cluster_async(
        self,
        request: imm_20200930_models.UpdateLocationDateClusterRequest,
    ) -> imm_20200930_models.UpdateLocationDateClusterResponse:
        """
        @summary Updates a spatiotemporal cluster.
        
        @description    Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/477042.html) of Intelligent Media Management (IMM).****\
        Before you call this operation, make sure that you have called the [CreateLocationDateClusteringTask](https://help.aliyun.com/document_detail/478188.html) operation to create spatiotemporal clusters in the project.
        
        @param request: UpdateLocationDateClusterRequest
        @return: UpdateLocationDateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_location_date_cluster_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateProjectResponse:
        """
        @summary Updates information about a project.
        
        @description    Before you call this operation, make sure that the project exists. For information about how to create a project, see "CreateProject".
        When you call this operation, you need to specify only the parameters that you want to update. The parameters that you do not specify remain unchanged after you call this operation.
        Wait for up to 5 minutes for the update to take effect.
        
        @param tmp_req: UpdateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateProjectResponse:
        """
        @summary Updates information about a project.
        
        @description    Before you call this operation, make sure that the project exists. For information about how to create a project, see "CreateProject".
        When you call this operation, you need to specify only the parameters that you want to update. The parameters that you do not specify remain unchanged after you call this operation.
        Wait for up to 5 minutes for the update to take effect.
        
        @param tmp_req: UpdateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        request: imm_20200930_models.UpdateProjectRequest,
    ) -> imm_20200930_models.UpdateProjectResponse:
        """
        @summary Updates information about a project.
        
        @description    Before you call this operation, make sure that the project exists. For information about how to create a project, see "CreateProject".
        When you call this operation, you need to specify only the parameters that you want to update. The parameters that you do not specify remain unchanged after you call this operation.
        Wait for up to 5 minutes for the update to take effect.
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: imm_20200930_models.UpdateProjectRequest,
    ) -> imm_20200930_models.UpdateProjectResponse:
        """
        @summary Updates information about a project.
        
        @description    Before you call this operation, make sure that the project exists. For information about how to create a project, see "CreateProject".
        When you call this operation, you need to specify only the parameters that you want to update. The parameters that you do not specify remain unchanged after you call this operation.
        Wait for up to 5 minutes for the update to take effect.
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_story_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateStoryResponse:
        """
        @summary Updates the information about a story, such as the story name and cover image.
        
        @param tmp_req: UpdateStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_story_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateStoryResponse:
        """
        @summary Updates the information about a story, such as the story name and cover image.
        
        @param tmp_req: UpdateStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_story(
        self,
        request: imm_20200930_models.UpdateStoryRequest,
    ) -> imm_20200930_models.UpdateStoryResponse:
        """
        @summary Updates the information about a story, such as the story name and cover image.
        
        @param request: UpdateStoryRequest
        @return: UpdateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_story_with_options(request, runtime)

    async def update_story_async(
        self,
        request: imm_20200930_models.UpdateStoryRequest,
    ) -> imm_20200930_models.UpdateStoryResponse:
        """
        @summary Updates the information about a story, such as the story name and cover image.
        
        @param request: UpdateStoryRequest
        @return: UpdateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_story_with_options_async(request, runtime)

    def update_trigger_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateTriggerResponse:
        """
        @summary Updates information about a trigger, such as the input data source, data processing settings, and tags.
        
        @description    You can update only a trigger that is in the Ready or Failed state. The update operation does not change the trigger status.
        After you update a trigger, the uncompleted tasks under the original trigger are no longer executed. You can call the [ResumeTrigger](https://help.aliyun.com/document_detail/479916.html) operation to resume the execution of the trigger.
        
        @param tmp_req: UpdateTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTriggerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateTriggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_trigger_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateTriggerResponse:
        """
        @summary Updates information about a trigger, such as the input data source, data processing settings, and tags.
        
        @description    You can update only a trigger that is in the Ready or Failed state. The update operation does not change the trigger status.
        After you update a trigger, the uncompleted tasks under the original trigger are no longer executed. You can call the [ResumeTrigger](https://help.aliyun.com/document_detail/479916.html) operation to resume the execution of the trigger.
        
        @param tmp_req: UpdateTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTriggerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateTriggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_trigger(
        self,
        request: imm_20200930_models.UpdateTriggerRequest,
    ) -> imm_20200930_models.UpdateTriggerResponse:
        """
        @summary Updates information about a trigger, such as the input data source, data processing settings, and tags.
        
        @description    You can update only a trigger that is in the Ready or Failed state. The update operation does not change the trigger status.
        After you update a trigger, the uncompleted tasks under the original trigger are no longer executed. You can call the [ResumeTrigger](https://help.aliyun.com/document_detail/479916.html) operation to resume the execution of the trigger.
        
        @param request: UpdateTriggerRequest
        @return: UpdateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_trigger_with_options(request, runtime)

    async def update_trigger_async(
        self,
        request: imm_20200930_models.UpdateTriggerRequest,
    ) -> imm_20200930_models.UpdateTriggerResponse:
        """
        @summary Updates information about a trigger, such as the input data source, data processing settings, and tags.
        
        @description    You can update only a trigger that is in the Ready or Failed state. The update operation does not change the trigger status.
        After you update a trigger, the uncompleted tasks under the original trigger are no longer executed. You can call the [ResumeTrigger](https://help.aliyun.com/document_detail/479916.html) operation to resume the execution of the trigger.
        
        @param request: UpdateTriggerRequest
        @return: UpdateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_trigger_with_options_async(request, runtime)
