# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_gateway_spi.client import Client as SPIClient
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_oss.client import Client as GatewayClientClient
from alibabacloud_oss20190517 import models as oss_20190517_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    _client: SPIClient = None

    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._client = GatewayClientClient()
        self._spi = self._client
        self._endpoint_rule = ''

    def abort_bucket_worm(
        self,
        bucket: str,
    ) -> oss_20190517_models.AbortBucketWormResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_bucket_worm_with_options(bucket, headers, runtime)

    async def abort_bucket_worm_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.AbortBucketWormResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.abort_bucket_worm_with_options_async(bucket, headers, runtime)

    def abort_bucket_worm_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.AbortBucketWormResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='AbortBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?worm',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.AbortBucketWormResponse(),
            self.execute(params, req, runtime)
        )

    async def abort_bucket_worm_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.AbortBucketWormResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='AbortBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?worm',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.AbortBucketWormResponse(),
            await self.execute_async(params, req, runtime)
        )

    def abort_multipart_upload(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.AbortMultipartUploadRequest,
    ) -> oss_20190517_models.AbortMultipartUploadResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_multipart_upload_with_options(bucket, key, request, headers, runtime)

    async def abort_multipart_upload_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.AbortMultipartUploadRequest,
    ) -> oss_20190517_models.AbortMultipartUploadResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.abort_multipart_upload_with_options_async(bucket, key, request, headers, runtime)

    def abort_multipart_upload_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.AbortMultipartUploadRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.AbortMultipartUploadResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortMultipartUpload',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.AbortMultipartUploadResponse(),
            self.execute(params, req, runtime)
        )

    async def abort_multipart_upload_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.AbortMultipartUploadRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.AbortMultipartUploadResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortMultipartUpload',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.AbortMultipartUploadResponse(),
            await self.execute_async(params, req, runtime)
        )

    def append_object(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.AppendObjectRequest,
    ) -> oss_20190517_models.AppendObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.AppendObjectHeaders()
        return self.append_object_with_options(bucket, key, request, headers, runtime)

    async def append_object_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.AppendObjectRequest,
    ) -> oss_20190517_models.AppendObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.AppendObjectHeaders()
        return await self.append_object_with_options_async(bucket, key, request, headers, runtime)

    def append_object_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.AppendObjectRequest,
        headers: oss_20190517_models.AppendObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.AppendObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.position):
            query['position'] = request.position
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.cache_control):
            real_headers['Cache-Control'] = UtilClient.to_jsonstring(headers.cache_control)
        if not UtilClient.is_unset(headers.content_disposition):
            real_headers['Content-Disposition'] = UtilClient.to_jsonstring(headers.content_disposition)
        if not UtilClient.is_unset(headers.content_encoding):
            real_headers['Content-Encoding'] = UtilClient.to_jsonstring(headers.content_encoding)
        if not UtilClient.is_unset(headers.content_md5):
            real_headers['Content-MD5'] = UtilClient.to_jsonstring(headers.content_md5)
        if not UtilClient.is_unset(headers.expires):
            real_headers['Expires'] = UtilClient.to_jsonstring(headers.expires)
        if not UtilClient.is_unset(headers.meta_data):
            real_headers['x-oss-meta-*'] = UtilClient.to_jsonstring(headers.meta_data)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='AppendObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?append',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='binary',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.AppendObjectResponse(),
            self.execute(params, req, runtime)
        )

    async def append_object_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.AppendObjectRequest,
        headers: oss_20190517_models.AppendObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.AppendObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.position):
            query['position'] = request.position
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.cache_control):
            real_headers['Cache-Control'] = UtilClient.to_jsonstring(headers.cache_control)
        if not UtilClient.is_unset(headers.content_disposition):
            real_headers['Content-Disposition'] = UtilClient.to_jsonstring(headers.content_disposition)
        if not UtilClient.is_unset(headers.content_encoding):
            real_headers['Content-Encoding'] = UtilClient.to_jsonstring(headers.content_encoding)
        if not UtilClient.is_unset(headers.content_md5):
            real_headers['Content-MD5'] = UtilClient.to_jsonstring(headers.content_md5)
        if not UtilClient.is_unset(headers.expires):
            real_headers['Expires'] = UtilClient.to_jsonstring(headers.expires)
        if not UtilClient.is_unset(headers.meta_data):
            real_headers['x-oss-meta-*'] = UtilClient.to_jsonstring(headers.meta_data)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='AppendObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?append',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='binary',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.AppendObjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def complete_bucket_worm(
        self,
        bucket: str,
        request: oss_20190517_models.CompleteBucketWormRequest,
    ) -> oss_20190517_models.CompleteBucketWormResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.complete_bucket_worm_with_options(bucket, request, headers, runtime)

    async def complete_bucket_worm_async(
        self,
        bucket: str,
        request: oss_20190517_models.CompleteBucketWormRequest,
    ) -> oss_20190517_models.CompleteBucketWormResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.complete_bucket_worm_with_options_async(bucket, request, headers, runtime)

    def complete_bucket_worm_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.CompleteBucketWormRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.CompleteBucketWormResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.worm_id):
            query['wormId'] = request.worm_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.CompleteBucketWormResponse(),
            self.execute(params, req, runtime)
        )

    async def complete_bucket_worm_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.CompleteBucketWormRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.CompleteBucketWormResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.worm_id):
            query['wormId'] = request.worm_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.CompleteBucketWormResponse(),
            await self.execute_async(params, req, runtime)
        )

    def complete_multipart_upload(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.CompleteMultipartUploadRequest,
    ) -> oss_20190517_models.CompleteMultipartUploadResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.CompleteMultipartUploadHeaders()
        return self.complete_multipart_upload_with_options(bucket, key, request, headers, runtime)

    async def complete_multipart_upload_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.CompleteMultipartUploadRequest,
    ) -> oss_20190517_models.CompleteMultipartUploadResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.CompleteMultipartUploadHeaders()
        return await self.complete_multipart_upload_with_options_async(bucket, key, request, headers, runtime)

    def complete_multipart_upload_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.CompleteMultipartUploadRequest,
        headers: oss_20190517_models.CompleteMultipartUploadHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.CompleteMultipartUploadResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        body = {}
        if not UtilClient.is_unset(request.complete_multipart_upload):
            body['completeMultipartUpload'] = request.complete_multipart_upload
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.complete_all):
            real_headers['x-oss-complete-all'] = UtilClient.to_jsonstring(headers.complete_all)
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompleteMultipartUpload',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.CompleteMultipartUploadResponse(),
            self.execute(params, req, runtime)
        )

    async def complete_multipart_upload_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.CompleteMultipartUploadRequest,
        headers: oss_20190517_models.CompleteMultipartUploadHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.CompleteMultipartUploadResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        body = {}
        if not UtilClient.is_unset(request.complete_multipart_upload):
            body['completeMultipartUpload'] = request.complete_multipart_upload
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.complete_all):
            real_headers['x-oss-complete-all'] = UtilClient.to_jsonstring(headers.complete_all)
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompleteMultipartUpload',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.CompleteMultipartUploadResponse(),
            await self.execute_async(params, req, runtime)
        )

    def copy_object(
        self,
        bucket: str,
        key: str,
    ) -> oss_20190517_models.CopyObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.CopyObjectHeaders()
        return self.copy_object_with_options(bucket, key, headers, runtime)

    async def copy_object_async(
        self,
        bucket: str,
        key: str,
    ) -> oss_20190517_models.CopyObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.CopyObjectHeaders()
        return await self.copy_object_with_options_async(bucket, key, headers, runtime)

    def copy_object_with_options(
        self,
        bucket: str,
        key: str,
        headers: oss_20190517_models.CopyObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.CopyObjectResponse:
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.copy_source):
            real_headers['x-oss-copy-source'] = UtilClient.to_jsonstring(headers.copy_source)
        if not UtilClient.is_unset(headers.copy_source_if_match):
            real_headers['x-oss-copy-source-if-match'] = UtilClient.to_jsonstring(headers.copy_source_if_match)
        if not UtilClient.is_unset(headers.copy_source_if_modified_since):
            real_headers['x-oss-copy-source-if-modified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_modified_since)
        if not UtilClient.is_unset(headers.copy_source_if_none_match):
            real_headers['x-oss-copy-source-if-none-match'] = UtilClient.to_jsonstring(headers.copy_source_if_none_match)
        if not UtilClient.is_unset(headers.copy_source_if_unmodified_since):
            real_headers['x-oss-copy-source-if-unmodified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_unmodified_since)
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.meta_data):
            real_headers['x-oss-meta-*'] = UtilClient.to_jsonstring(headers.meta_data)
        if not UtilClient.is_unset(headers.metadata_directive):
            real_headers['x-oss-metadata-directive'] = UtilClient.to_jsonstring(headers.metadata_directive)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.sse_key_id):
            real_headers['x-oss-server-side-encryption-key-id'] = UtilClient.to_jsonstring(headers.sse_key_id)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.tagging):
            real_headers['x-oss-tagging'] = UtilClient.to_jsonstring(headers.tagging)
        if not UtilClient.is_unset(headers.tagging_directive):
            real_headers['x-oss-tagging-directive'] = UtilClient.to_jsonstring(headers.tagging_directive)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='CopyObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.CopyObjectResponse(),
            self.execute(params, req, runtime)
        )

    async def copy_object_with_options_async(
        self,
        bucket: str,
        key: str,
        headers: oss_20190517_models.CopyObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.CopyObjectResponse:
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.copy_source):
            real_headers['x-oss-copy-source'] = UtilClient.to_jsonstring(headers.copy_source)
        if not UtilClient.is_unset(headers.copy_source_if_match):
            real_headers['x-oss-copy-source-if-match'] = UtilClient.to_jsonstring(headers.copy_source_if_match)
        if not UtilClient.is_unset(headers.copy_source_if_modified_since):
            real_headers['x-oss-copy-source-if-modified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_modified_since)
        if not UtilClient.is_unset(headers.copy_source_if_none_match):
            real_headers['x-oss-copy-source-if-none-match'] = UtilClient.to_jsonstring(headers.copy_source_if_none_match)
        if not UtilClient.is_unset(headers.copy_source_if_unmodified_since):
            real_headers['x-oss-copy-source-if-unmodified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_unmodified_since)
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.meta_data):
            real_headers['x-oss-meta-*'] = UtilClient.to_jsonstring(headers.meta_data)
        if not UtilClient.is_unset(headers.metadata_directive):
            real_headers['x-oss-metadata-directive'] = UtilClient.to_jsonstring(headers.metadata_directive)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.sse_key_id):
            real_headers['x-oss-server-side-encryption-key-id'] = UtilClient.to_jsonstring(headers.sse_key_id)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.tagging):
            real_headers['x-oss-tagging'] = UtilClient.to_jsonstring(headers.tagging)
        if not UtilClient.is_unset(headers.tagging_directive):
            real_headers['x-oss-tagging-directive'] = UtilClient.to_jsonstring(headers.tagging_directive)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='CopyObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.CopyObjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_select_object_meta(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.CreateSelectObjectMetaRequest,
    ) -> oss_20190517_models.CreateSelectObjectMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_select_object_meta_with_options(bucket, key, request, headers, runtime)

    async def create_select_object_meta_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.CreateSelectObjectMetaRequest,
    ) -> oss_20190517_models.CreateSelectObjectMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_select_object_meta_with_options_async(bucket, key, request, headers, runtime)

    def create_select_object_meta_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.CreateSelectObjectMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.CreateSelectObjectMetaResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.select_meta_request))
        )
        params = open_api_models.Params(
            action='CreateSelectObjectMeta',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_20190517_models.CreateSelectObjectMetaResponse(),
            self.execute(params, req, runtime)
        )

    async def create_select_object_meta_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.CreateSelectObjectMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.CreateSelectObjectMetaResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.select_meta_request))
        )
        params = open_api_models.Params(
            action='CreateSelectObjectMeta',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_20190517_models.CreateSelectObjectMetaResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_bucket(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_with_options(bucket, headers, runtime)

    async def delete_bucket_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_bucket_with_options_async(bucket, headers, runtime)

    def delete_bucket_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucket',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_bucket_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucket',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_bucket_cors(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketCorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_cors_with_options(bucket, headers, runtime)

    async def delete_bucket_cors_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketCorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_bucket_cors_with_options_async(bucket, headers, runtime)

    def delete_bucket_cors_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketCorsResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketCors',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?cors',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketCorsResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_bucket_cors_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketCorsResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketCors',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?cors',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketCorsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_bucket_encryption(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketEncryptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_encryption_with_options(bucket, headers, runtime)

    async def delete_bucket_encryption_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketEncryptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_bucket_encryption_with_options_async(bucket, headers, runtime)

    def delete_bucket_encryption_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketEncryptionResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketEncryption',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?encryption',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketEncryptionResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_bucket_encryption_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketEncryptionResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketEncryption',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?encryption',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketEncryptionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_bucket_inventory(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteBucketInventoryRequest,
    ) -> oss_20190517_models.DeleteBucketInventoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_inventory_with_options(bucket, request, headers, runtime)

    async def delete_bucket_inventory_async(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteBucketInventoryRequest,
    ) -> oss_20190517_models.DeleteBucketInventoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_bucket_inventory_with_options_async(bucket, request, headers, runtime)

    def delete_bucket_inventory_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteBucketInventoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketInventoryResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.inventory_id):
            query['inventoryId'] = request.inventory_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?inventory',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketInventoryResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_bucket_inventory_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteBucketInventoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketInventoryResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.inventory_id):
            query['inventoryId'] = request.inventory_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?inventory',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketInventoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_bucket_lifecycle(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketLifecycleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_lifecycle_with_options(bucket, headers, runtime)

    async def delete_bucket_lifecycle_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketLifecycleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_bucket_lifecycle_with_options_async(bucket, headers, runtime)

    def delete_bucket_lifecycle_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketLifecycleResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketLifecycle',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?lifecycle',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketLifecycleResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_bucket_lifecycle_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketLifecycleResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketLifecycle',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?lifecycle',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketLifecycleResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_bucket_logging(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketLoggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_logging_with_options(bucket, headers, runtime)

    async def delete_bucket_logging_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketLoggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_bucket_logging_with_options_async(bucket, headers, runtime)

    def delete_bucket_logging_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketLoggingResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketLogging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?logging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketLoggingResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_bucket_logging_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketLoggingResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketLogging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?logging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketLoggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_bucket_policy(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_policy_with_options(bucket, headers, runtime)

    async def delete_bucket_policy_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_bucket_policy_with_options_async(bucket, headers, runtime)

    def delete_bucket_policy_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketPolicyResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketPolicy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?policy',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_bucket_policy_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketPolicyResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketPolicy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?policy',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_bucket_replication(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteBucketReplicationRequest,
    ) -> oss_20190517_models.DeleteBucketReplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_replication_with_options(bucket, request, headers, runtime)

    async def delete_bucket_replication_async(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteBucketReplicationRequest,
    ) -> oss_20190517_models.DeleteBucketReplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_bucket_replication_with_options_async(bucket, request, headers, runtime)

    def delete_bucket_replication_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteBucketReplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketReplicationResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='DeleteBucketReplication',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?replication&comp=delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketReplicationResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_bucket_replication_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteBucketReplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketReplicationResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='DeleteBucketReplication',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?replication&comp=delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketReplicationResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_bucket_tags(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_tags_with_options(bucket, headers, runtime)

    async def delete_bucket_tags_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_bucket_tags_with_options_async(bucket, headers, runtime)

    def delete_bucket_tags_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketTagsResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketTags',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?tagging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_bucket_tags_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketTagsResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketTags',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?tagging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_bucket_website(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketWebsiteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_website_with_options(bucket, headers, runtime)

    async def delete_bucket_website_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.DeleteBucketWebsiteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_bucket_website_with_options_async(bucket, headers, runtime)

    def delete_bucket_website_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketWebsiteResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketWebsite',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?website',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketWebsiteResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_bucket_website_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteBucketWebsiteResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketWebsite',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?website',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketWebsiteResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_live_channel(
        self,
        bucket: str,
        channel: str,
    ) -> oss_20190517_models.DeleteLiveChannelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_live_channel_with_options(bucket, channel, headers, runtime)

    async def delete_live_channel_async(
        self,
        bucket: str,
        channel: str,
    ) -> oss_20190517_models.DeleteLiveChannelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_live_channel_with_options_async(bucket, channel, headers, runtime)

    def delete_live_channel_with_options(
        self,
        bucket: str,
        channel: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteLiveChannelResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLiveChannel',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteLiveChannelResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_live_channel_with_options_async(
        self,
        bucket: str,
        channel: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteLiveChannelResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLiveChannel',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteLiveChannelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_multiple_objects(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteMultipleObjectsRequest,
    ) -> oss_20190517_models.DeleteMultipleObjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_multiple_objects_with_options(bucket, request, headers, runtime)

    async def delete_multiple_objects_async(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteMultipleObjectsRequest,
    ) -> oss_20190517_models.DeleteMultipleObjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_multiple_objects_with_options_async(bucket, request, headers, runtime)

    def delete_multiple_objects_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteMultipleObjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteMultipleObjectsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.delete))
        )
        params = open_api_models.Params(
            action='DeleteMultipleObjects',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteMultipleObjectsResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_multiple_objects_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.DeleteMultipleObjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteMultipleObjectsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.delete))
        )
        params = open_api_models.Params(
            action='DeleteMultipleObjects',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteMultipleObjectsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_object(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.DeleteObjectRequest,
    ) -> oss_20190517_models.DeleteObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_object_with_options(bucket, key, request, headers, runtime)

    async def delete_object_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.DeleteObjectRequest,
    ) -> oss_20190517_models.DeleteObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_object_with_options_async(bucket, key, request, headers, runtime)

    def delete_object_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.DeleteObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteObjectResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_object_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.DeleteObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteObjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_object_tagging(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.DeleteObjectTaggingRequest,
    ) -> oss_20190517_models.DeleteObjectTaggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_object_tagging_with_options(bucket, key, request, headers, runtime)

    async def delete_object_tagging_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.DeleteObjectTaggingRequest,
    ) -> oss_20190517_models.DeleteObjectTaggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_object_tagging_with_options_async(bucket, key, request, headers, runtime)

    def delete_object_tagging_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.DeleteObjectTaggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteObjectTaggingResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteObjectTagging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?tagging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteObjectTaggingResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_object_tagging_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.DeleteObjectTaggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DeleteObjectTaggingResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteObjectTagging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?tagging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteObjectTaggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: oss_20190517_models.DescribeRegionsRequest,
    ) -> oss_20190517_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: oss_20190517_models.DescribeRegionsRequest,
    ) -> oss_20190517_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        request: oss_20190517_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.regions):
            query['regions'] = request.regions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DescribeRegionsResponse(),
            self.execute(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: oss_20190517_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.regions):
            query['regions'] = request.regions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DescribeRegionsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def extend_bucket_worm(
        self,
        bucket: str,
        request: oss_20190517_models.ExtendBucketWormRequest,
    ) -> oss_20190517_models.ExtendBucketWormResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.extend_bucket_worm_with_options(bucket, request, headers, runtime)

    async def extend_bucket_worm_async(
        self,
        bucket: str,
        request: oss_20190517_models.ExtendBucketWormRequest,
    ) -> oss_20190517_models.ExtendBucketWormResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.extend_bucket_worm_with_options_async(bucket, request, headers, runtime)

    def extend_bucket_worm_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.ExtendBucketWormRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ExtendBucketWormResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.worm_id):
            query['wormId'] = request.worm_id
        body = {}
        if not UtilClient.is_unset(request.extend_worm_configuration):
            body['extendWormConfiguration'] = request.extend_worm_configuration
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtendBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?wormExtend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ExtendBucketWormResponse(),
            self.execute(params, req, runtime)
        )

    async def extend_bucket_worm_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.ExtendBucketWormRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ExtendBucketWormResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.worm_id):
            query['wormId'] = request.worm_id
        body = {}
        if not UtilClient.is_unset(request.extend_worm_configuration):
            body['extendWormConfiguration'] = request.extend_worm_configuration
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtendBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?wormExtend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ExtendBucketWormResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_acl(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketAclResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_acl_with_options(bucket, headers, runtime)

    async def get_bucket_acl_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketAclResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_acl_with_options_async(bucket, headers, runtime)

    def get_bucket_acl_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketAclResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?acl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketAclResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_acl_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketAclResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?acl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketAclResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_cors(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketCorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_cors_with_options(bucket, headers, runtime)

    async def get_bucket_cors_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketCorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_cors_with_options_async(bucket, headers, runtime)

    def get_bucket_cors_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketCorsResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketCors',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?cors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketCorsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_cors_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketCorsResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketCors',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?cors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketCorsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_encryption(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketEncryptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_encryption_with_options(bucket, headers, runtime)

    async def get_bucket_encryption_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketEncryptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_encryption_with_options_async(bucket, headers, runtime)

    def get_bucket_encryption_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketEncryptionResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketEncryption',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?encryption',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketEncryptionResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_encryption_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketEncryptionResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketEncryption',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?encryption',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketEncryptionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_info(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_info_with_options(bucket, headers, runtime)

    async def get_bucket_info_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_info_with_options_async(bucket, headers, runtime)

    def get_bucket_info_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketInfoResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketInfo',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?bucketInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketInfoResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_info_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketInfoResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketInfo',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?bucketInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketInfoResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_inventory(
        self,
        bucket: str,
        request: oss_20190517_models.GetBucketInventoryRequest,
    ) -> oss_20190517_models.GetBucketInventoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_inventory_with_options(bucket, request, headers, runtime)

    async def get_bucket_inventory_async(
        self,
        bucket: str,
        request: oss_20190517_models.GetBucketInventoryRequest,
    ) -> oss_20190517_models.GetBucketInventoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_inventory_with_options_async(bucket, request, headers, runtime)

    def get_bucket_inventory_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.GetBucketInventoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketInventoryResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.inventory_id):
            query['inventoryId'] = request.inventory_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?inventory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketInventoryResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_inventory_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.GetBucketInventoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketInventoryResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.inventory_id):
            query['inventoryId'] = request.inventory_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?inventory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketInventoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_lifecycle(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketLifecycleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_lifecycle_with_options(bucket, headers, runtime)

    async def get_bucket_lifecycle_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketLifecycleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_lifecycle_with_options_async(bucket, headers, runtime)

    def get_bucket_lifecycle_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketLifecycleResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketLifecycle',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?lifecycle',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketLifecycleResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_lifecycle_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketLifecycleResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketLifecycle',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?lifecycle',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketLifecycleResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_location(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketLocationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_location_with_options(bucket, headers, runtime)

    async def get_bucket_location_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketLocationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_location_with_options_async(bucket, headers, runtime)

    def get_bucket_location_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketLocationResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketLocation',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?location',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketLocationResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_location_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketLocationResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketLocation',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?location',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketLocationResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_logging(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketLoggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_logging_with_options(bucket, headers, runtime)

    async def get_bucket_logging_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketLoggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_logging_with_options_async(bucket, headers, runtime)

    def get_bucket_logging_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketLoggingResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketLogging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?logging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketLoggingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_logging_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketLoggingResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketLogging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?logging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketLoggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_policy(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_policy_with_options(bucket, headers, runtime)

    async def get_bucket_policy_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_policy_with_options_async(bucket, headers, runtime)

    def get_bucket_policy_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketPolicyResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketPolicy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_policy_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketPolicyResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketPolicy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_referer(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketRefererResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_referer_with_options(bucket, headers, runtime)

    async def get_bucket_referer_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketRefererResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_referer_with_options_async(bucket, headers, runtime)

    def get_bucket_referer_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketRefererResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketReferer',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?referer',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketRefererResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_referer_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketRefererResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketReferer',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?referer',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketRefererResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_replication(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketReplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_replication_with_options(bucket, headers, runtime)

    async def get_bucket_replication_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketReplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_replication_with_options_async(bucket, headers, runtime)

    def get_bucket_replication_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketReplicationResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketReplication',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?replication',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketReplicationResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_replication_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketReplicationResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketReplication',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?replication',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketReplicationResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_replication_location(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketReplicationLocationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_replication_location_with_options(bucket, headers, runtime)

    async def get_bucket_replication_location_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketReplicationLocationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_replication_location_with_options_async(bucket, headers, runtime)

    def get_bucket_replication_location_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketReplicationLocationResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketReplicationLocation',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?replicationLocation',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketReplicationLocationResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_replication_location_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketReplicationLocationResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketReplicationLocation',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?replicationLocation',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketReplicationLocationResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_replication_progress(
        self,
        bucket: str,
        request: oss_20190517_models.GetBucketReplicationProgressRequest,
    ) -> oss_20190517_models.GetBucketReplicationProgressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_replication_progress_with_options(bucket, request, headers, runtime)

    async def get_bucket_replication_progress_async(
        self,
        bucket: str,
        request: oss_20190517_models.GetBucketReplicationProgressRequest,
    ) -> oss_20190517_models.GetBucketReplicationProgressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_replication_progress_with_options_async(bucket, request, headers, runtime)

    def get_bucket_replication_progress_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.GetBucketReplicationProgressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketReplicationProgressResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['rule-id'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketReplicationProgress',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?replicationProgress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketReplicationProgressResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_replication_progress_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.GetBucketReplicationProgressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketReplicationProgressResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['rule-id'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketReplicationProgress',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?replicationProgress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketReplicationProgressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_request_payment(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketRequestPaymentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_request_payment_with_options(bucket, headers, runtime)

    async def get_bucket_request_payment_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketRequestPaymentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_request_payment_with_options_async(bucket, headers, runtime)

    def get_bucket_request_payment_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketRequestPaymentResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketRequestPayment',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?requestPayment',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketRequestPaymentResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_request_payment_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketRequestPaymentResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketRequestPayment',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?requestPayment',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketRequestPaymentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_tags(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_tags_with_options(bucket, headers, runtime)

    async def get_bucket_tags_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_tags_with_options_async(bucket, headers, runtime)

    def get_bucket_tags_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketTagsResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketTags',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?tagging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_tags_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketTagsResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketTags',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?tagging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_transfer_acceleration(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketTransferAccelerationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_transfer_acceleration_with_options(bucket, headers, runtime)

    async def get_bucket_transfer_acceleration_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketTransferAccelerationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_transfer_acceleration_with_options_async(bucket, headers, runtime)

    def get_bucket_transfer_acceleration_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketTransferAccelerationResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketTransferAcceleration',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?transferAcceleration',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketTransferAccelerationResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_transfer_acceleration_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketTransferAccelerationResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketTransferAcceleration',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?transferAcceleration',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketTransferAccelerationResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_versioning(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketVersioningResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_versioning_with_options(bucket, headers, runtime)

    async def get_bucket_versioning_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketVersioningResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_versioning_with_options_async(bucket, headers, runtime)

    def get_bucket_versioning_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketVersioningResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketVersioning',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?versioning',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketVersioningResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_versioning_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketVersioningResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketVersioning',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?versioning',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketVersioningResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_website(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketWebsiteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_website_with_options(bucket, headers, runtime)

    async def get_bucket_website_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketWebsiteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_website_with_options_async(bucket, headers, runtime)

    def get_bucket_website_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketWebsiteResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketWebsite',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?website',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketWebsiteResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_website_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketWebsiteResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketWebsite',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?website',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketWebsiteResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_bucket_worm(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketWormResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_worm_with_options(bucket, headers, runtime)

    async def get_bucket_worm_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.GetBucketWormResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bucket_worm_with_options_async(bucket, headers, runtime)

    def get_bucket_worm_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketWormResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?worm',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketWormResponse(),
            self.execute(params, req, runtime)
        )

    async def get_bucket_worm_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetBucketWormResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?worm',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketWormResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_live_channel_history(
        self,
        bucket: str,
        channel: str,
    ) -> oss_20190517_models.GetLiveChannelHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_live_channel_history_with_options(bucket, channel, headers, runtime)

    async def get_live_channel_history_async(
        self,
        bucket: str,
        channel: str,
    ) -> oss_20190517_models.GetLiveChannelHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_live_channel_history_with_options_async(bucket, channel, headers, runtime)

    def get_live_channel_history_with_options(
        self,
        bucket: str,
        channel: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetLiveChannelHistoryResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLiveChannelHistory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live&comp=history',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetLiveChannelHistoryResponse(),
            self.execute(params, req, runtime)
        )

    async def get_live_channel_history_with_options_async(
        self,
        bucket: str,
        channel: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetLiveChannelHistoryResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLiveChannelHistory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live&comp=history',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetLiveChannelHistoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_live_channel_info(
        self,
        bucket: str,
        channel: str,
    ) -> oss_20190517_models.GetLiveChannelInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_live_channel_info_with_options(bucket, channel, headers, runtime)

    async def get_live_channel_info_async(
        self,
        bucket: str,
        channel: str,
    ) -> oss_20190517_models.GetLiveChannelInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_live_channel_info_with_options_async(bucket, channel, headers, runtime)

    def get_live_channel_info_with_options(
        self,
        bucket: str,
        channel: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetLiveChannelInfoResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLiveChannelInfo',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetLiveChannelInfoResponse(),
            self.execute(params, req, runtime)
        )

    async def get_live_channel_info_with_options_async(
        self,
        bucket: str,
        channel: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetLiveChannelInfoResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLiveChannelInfo',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetLiveChannelInfoResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_live_channel_stat(
        self,
        bucket: str,
        channel: str,
    ) -> oss_20190517_models.GetLiveChannelStatResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_live_channel_stat_with_options(bucket, channel, headers, runtime)

    async def get_live_channel_stat_async(
        self,
        bucket: str,
        channel: str,
    ) -> oss_20190517_models.GetLiveChannelStatResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_live_channel_stat_with_options_async(bucket, channel, headers, runtime)

    def get_live_channel_stat_with_options(
        self,
        bucket: str,
        channel: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetLiveChannelStatResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLiveChannelStat',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live&comp=stat',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetLiveChannelStatResponse(),
            self.execute(params, req, runtime)
        )

    async def get_live_channel_stat_with_options_async(
        self,
        bucket: str,
        channel: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetLiveChannelStatResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLiveChannelStat',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live&comp=stat',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetLiveChannelStatResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_object(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectRequest,
    ) -> oss_20190517_models.GetObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.GetObjectHeaders()
        return self.get_object_with_options(bucket, key, request, headers, runtime)

    async def get_object_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectRequest,
    ) -> oss_20190517_models.GetObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.GetObjectHeaders()
        return await self.get_object_with_options_async(bucket, key, request, headers, runtime)

    def get_object_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectRequest,
        headers: oss_20190517_models.GetObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.response_cache_control):
            query['response-cache-control'] = request.response_cache_control
        if not UtilClient.is_unset(request.response_content_disposition):
            query['response-content-disposition'] = request.response_content_disposition
        if not UtilClient.is_unset(request.response_content_encoding):
            query['response-content-encoding'] = request.response_content_encoding
        if not UtilClient.is_unset(request.response_content_language):
            query['response-content-language'] = request.response_content_language
        if not UtilClient.is_unset(request.response_content_type):
            query['response-content-type'] = request.response_content_type
        if not UtilClient.is_unset(request.response_expires):
            query['response-expires'] = request.response_expires
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.accept_encoding):
            real_headers['Accept-Encoding'] = UtilClient.to_jsonstring(headers.accept_encoding)
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.if_modified_since):
            real_headers['If-Modified-Since'] = UtilClient.to_jsonstring(headers.if_modified_since)
        if not UtilClient.is_unset(headers.if_none_match):
            real_headers['If-None-Match'] = UtilClient.to_jsonstring(headers.if_none_match)
        if not UtilClient.is_unset(headers.if_unmodified_since):
            real_headers['If-Unmodified-Since'] = UtilClient.to_jsonstring(headers.if_unmodified_since)
        if not UtilClient.is_unset(headers.range):
            real_headers['Range'] = UtilClient.to_jsonstring(headers.range)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='binary'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectResponse(),
            self.execute(params, req, runtime)
        )

    async def get_object_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectRequest,
        headers: oss_20190517_models.GetObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.response_cache_control):
            query['response-cache-control'] = request.response_cache_control
        if not UtilClient.is_unset(request.response_content_disposition):
            query['response-content-disposition'] = request.response_content_disposition
        if not UtilClient.is_unset(request.response_content_encoding):
            query['response-content-encoding'] = request.response_content_encoding
        if not UtilClient.is_unset(request.response_content_language):
            query['response-content-language'] = request.response_content_language
        if not UtilClient.is_unset(request.response_content_type):
            query['response-content-type'] = request.response_content_type
        if not UtilClient.is_unset(request.response_expires):
            query['response-expires'] = request.response_expires
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.accept_encoding):
            real_headers['Accept-Encoding'] = UtilClient.to_jsonstring(headers.accept_encoding)
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.if_modified_since):
            real_headers['If-Modified-Since'] = UtilClient.to_jsonstring(headers.if_modified_since)
        if not UtilClient.is_unset(headers.if_none_match):
            real_headers['If-None-Match'] = UtilClient.to_jsonstring(headers.if_none_match)
        if not UtilClient.is_unset(headers.if_unmodified_since):
            real_headers['If-Unmodified-Since'] = UtilClient.to_jsonstring(headers.if_unmodified_since)
        if not UtilClient.is_unset(headers.range):
            real_headers['Range'] = UtilClient.to_jsonstring(headers.range)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='binary'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_object_acl(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectAclRequest,
    ) -> oss_20190517_models.GetObjectAclResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_object_acl_with_options(bucket, key, request, headers, runtime)

    async def get_object_acl_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectAclRequest,
    ) -> oss_20190517_models.GetObjectAclResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_object_acl_with_options_async(bucket, key, request, headers, runtime)

    def get_object_acl_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectAclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetObjectAclResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObjectAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?acl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectAclResponse(),
            self.execute(params, req, runtime)
        )

    async def get_object_acl_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectAclRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetObjectAclResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObjectAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?acl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectAclResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_object_meta(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectMetaRequest,
    ) -> oss_20190517_models.GetObjectMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_object_meta_with_options(bucket, key, request, headers, runtime)

    async def get_object_meta_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectMetaRequest,
    ) -> oss_20190517_models.GetObjectMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_object_meta_with_options_async(bucket, key, request, headers, runtime)

    def get_object_meta_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetObjectMetaResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObjectMeta',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?objectMeta',
            method='HEAD',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectMetaResponse(),
            self.execute(params, req, runtime)
        )

    async def get_object_meta_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetObjectMetaResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObjectMeta',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?objectMeta',
            method='HEAD',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectMetaResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_object_tagging(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectTaggingRequest,
    ) -> oss_20190517_models.GetObjectTaggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_object_tagging_with_options(bucket, key, request, headers, runtime)

    async def get_object_tagging_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectTaggingRequest,
    ) -> oss_20190517_models.GetObjectTaggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_object_tagging_with_options_async(bucket, key, request, headers, runtime)

    def get_object_tagging_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectTaggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetObjectTaggingResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObjectTagging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?tagging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectTaggingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_object_tagging_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetObjectTaggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetObjectTaggingResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObjectTagging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?tagging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectTaggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_symlink(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetSymlinkRequest,
    ) -> oss_20190517_models.GetSymlinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_symlink_with_options(bucket, key, request, headers, runtime)

    async def get_symlink_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetSymlinkRequest,
    ) -> oss_20190517_models.GetSymlinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_symlink_with_options_async(bucket, key, request, headers, runtime)

    def get_symlink_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetSymlinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetSymlinkResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSymlink',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?symlink',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetSymlinkResponse(),
            self.execute(params, req, runtime)
        )

    async def get_symlink_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.GetSymlinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetSymlinkResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSymlink',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?symlink',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetSymlinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_vod_playlist(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.GetVodPlaylistRequest,
    ) -> oss_20190517_models.GetVodPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_vod_playlist_with_options(bucket, channel, request, headers, runtime)

    async def get_vod_playlist_async(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.GetVodPlaylistRequest,
    ) -> oss_20190517_models.GetVodPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_vod_playlist_with_options_async(bucket, channel, request, headers, runtime)

    def get_vod_playlist_with_options(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.GetVodPlaylistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetVodPlaylistResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVodPlaylist',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?vod',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='binary'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetVodPlaylistResponse(),
            self.execute(params, req, runtime)
        )

    async def get_vod_playlist_with_options_async(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.GetVodPlaylistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.GetVodPlaylistResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVodPlaylist',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?vod',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='binary'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetVodPlaylistResponse(),
            await self.execute_async(params, req, runtime)
        )

    def head_object(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.HeadObjectRequest,
    ) -> oss_20190517_models.HeadObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.HeadObjectHeaders()
        return self.head_object_with_options(bucket, key, request, headers, runtime)

    async def head_object_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.HeadObjectRequest,
    ) -> oss_20190517_models.HeadObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.HeadObjectHeaders()
        return await self.head_object_with_options_async(bucket, key, request, headers, runtime)

    def head_object_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.HeadObjectRequest,
        headers: oss_20190517_models.HeadObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.HeadObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.if_modified_since):
            real_headers['If-Modified-Since'] = UtilClient.to_jsonstring(headers.if_modified_since)
        if not UtilClient.is_unset(headers.if_none_match):
            real_headers['If-None-Match'] = UtilClient.to_jsonstring(headers.if_none_match)
        if not UtilClient.is_unset(headers.if_unmodified_since):
            real_headers['If-Unmodified-Since'] = UtilClient.to_jsonstring(headers.if_unmodified_since)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HeadObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='HEAD',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.HeadObjectResponse(),
            self.execute(params, req, runtime)
        )

    async def head_object_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.HeadObjectRequest,
        headers: oss_20190517_models.HeadObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.HeadObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.if_modified_since):
            real_headers['If-Modified-Since'] = UtilClient.to_jsonstring(headers.if_modified_since)
        if not UtilClient.is_unset(headers.if_none_match):
            real_headers['If-None-Match'] = UtilClient.to_jsonstring(headers.if_none_match)
        if not UtilClient.is_unset(headers.if_unmodified_since):
            real_headers['If-Unmodified-Since'] = UtilClient.to_jsonstring(headers.if_unmodified_since)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HeadObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='HEAD',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.HeadObjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def initiate_bucket_worm(
        self,
        bucket: str,
        request: oss_20190517_models.InitiateBucketWormRequest,
    ) -> oss_20190517_models.InitiateBucketWormResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.initiate_bucket_worm_with_options(bucket, request, headers, runtime)

    async def initiate_bucket_worm_async(
        self,
        bucket: str,
        request: oss_20190517_models.InitiateBucketWormRequest,
    ) -> oss_20190517_models.InitiateBucketWormResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.initiate_bucket_worm_with_options_async(bucket, request, headers, runtime)

    def initiate_bucket_worm_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.InitiateBucketWormRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.InitiateBucketWormResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.initiate_worm_configuration))
        )
        params = open_api_models.Params(
            action='InitiateBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?worm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.InitiateBucketWormResponse(),
            self.execute(params, req, runtime)
        )

    async def initiate_bucket_worm_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.InitiateBucketWormRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.InitiateBucketWormResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.initiate_worm_configuration))
        )
        params = open_api_models.Params(
            action='InitiateBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?worm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.InitiateBucketWormResponse(),
            await self.execute_async(params, req, runtime)
        )

    def initiate_multipart_upload(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.InitiateMultipartUploadRequest,
    ) -> oss_20190517_models.InitiateMultipartUploadResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.InitiateMultipartUploadHeaders()
        return self.initiate_multipart_upload_with_options(bucket, key, request, headers, runtime)

    async def initiate_multipart_upload_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.InitiateMultipartUploadRequest,
    ) -> oss_20190517_models.InitiateMultipartUploadResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.InitiateMultipartUploadHeaders()
        return await self.initiate_multipart_upload_with_options_async(bucket, key, request, headers, runtime)

    def initiate_multipart_upload_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.InitiateMultipartUploadRequest,
        headers: oss_20190517_models.InitiateMultipartUploadHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.InitiateMultipartUploadResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.cache_control):
            real_headers['Cache-Control'] = UtilClient.to_jsonstring(headers.cache_control)
        if not UtilClient.is_unset(headers.content_disposition):
            real_headers['Content-Disposition'] = UtilClient.to_jsonstring(headers.content_disposition)
        if not UtilClient.is_unset(headers.content_encoding):
            real_headers['Content-Encoding'] = UtilClient.to_jsonstring(headers.content_encoding)
        if not UtilClient.is_unset(headers.expires):
            real_headers['Expires'] = UtilClient.to_jsonstring(headers.expires)
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.sse_data_encryption):
            real_headers['x-oss-server-side-data-encryption'] = UtilClient.to_jsonstring(headers.sse_data_encryption)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.sse_key_id):
            real_headers['x-oss-server-side-encryption-key-id'] = UtilClient.to_jsonstring(headers.sse_key_id)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.tagging):
            real_headers['x-oss-tagging'] = UtilClient.to_jsonstring(headers.tagging)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitiateMultipartUpload',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?uploads',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.InitiateMultipartUploadResponse(),
            self.execute(params, req, runtime)
        )

    async def initiate_multipart_upload_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.InitiateMultipartUploadRequest,
        headers: oss_20190517_models.InitiateMultipartUploadHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.InitiateMultipartUploadResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.cache_control):
            real_headers['Cache-Control'] = UtilClient.to_jsonstring(headers.cache_control)
        if not UtilClient.is_unset(headers.content_disposition):
            real_headers['Content-Disposition'] = UtilClient.to_jsonstring(headers.content_disposition)
        if not UtilClient.is_unset(headers.content_encoding):
            real_headers['Content-Encoding'] = UtilClient.to_jsonstring(headers.content_encoding)
        if not UtilClient.is_unset(headers.expires):
            real_headers['Expires'] = UtilClient.to_jsonstring(headers.expires)
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.sse_data_encryption):
            real_headers['x-oss-server-side-data-encryption'] = UtilClient.to_jsonstring(headers.sse_data_encryption)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.sse_key_id):
            real_headers['x-oss-server-side-encryption-key-id'] = UtilClient.to_jsonstring(headers.sse_key_id)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.tagging):
            real_headers['x-oss-tagging'] = UtilClient.to_jsonstring(headers.tagging)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitiateMultipartUpload',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?uploads',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.InitiateMultipartUploadResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_bucket_inventory(
        self,
        bucket: str,
        request: oss_20190517_models.ListBucketInventoryRequest,
    ) -> oss_20190517_models.ListBucketInventoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_bucket_inventory_with_options(bucket, request, headers, runtime)

    async def list_bucket_inventory_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListBucketInventoryRequest,
    ) -> oss_20190517_models.ListBucketInventoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_bucket_inventory_with_options_async(bucket, request, headers, runtime)

    def list_bucket_inventory_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.ListBucketInventoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListBucketInventoryResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.continuation_token):
            query['continuation-token'] = request.continuation_token
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?inventory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListBucketInventoryResponse(),
            self.execute(params, req, runtime)
        )

    async def list_bucket_inventory_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListBucketInventoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListBucketInventoryResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.continuation_token):
            query['continuation-token'] = request.continuation_token
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?inventory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListBucketInventoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_buckets(
        self,
        request: oss_20190517_models.ListBucketsRequest,
    ) -> oss_20190517_models.ListBucketsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_buckets_with_options(request, headers, runtime)

    async def list_buckets_async(
        self,
        request: oss_20190517_models.ListBucketsRequest,
    ) -> oss_20190517_models.ListBucketsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_buckets_with_options_async(request, headers, runtime)

    def list_buckets_with_options(
        self,
        request: oss_20190517_models.ListBucketsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListBucketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBuckets',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListBucketsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_buckets_with_options_async(
        self,
        request: oss_20190517_models.ListBucketsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListBucketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBuckets',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListBucketsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_live_channel(
        self,
        bucket: str,
        request: oss_20190517_models.ListLiveChannelRequest,
    ) -> oss_20190517_models.ListLiveChannelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_live_channel_with_options(bucket, request, headers, runtime)

    async def list_live_channel_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListLiveChannelRequest,
    ) -> oss_20190517_models.ListLiveChannelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_live_channel_with_options_async(bucket, request, headers, runtime)

    def list_live_channel_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.ListLiveChannelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListLiveChannelResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveChannel',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?live',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListLiveChannelResponse(),
            self.execute(params, req, runtime)
        )

    async def list_live_channel_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListLiveChannelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListLiveChannelResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveChannel',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?live',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListLiveChannelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_multipart_uploads(
        self,
        bucket: str,
        request: oss_20190517_models.ListMultipartUploadsRequest,
    ) -> oss_20190517_models.ListMultipartUploadsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_multipart_uploads_with_options(bucket, request, headers, runtime)

    async def list_multipart_uploads_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListMultipartUploadsRequest,
    ) -> oss_20190517_models.ListMultipartUploadsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_multipart_uploads_with_options_async(bucket, request, headers, runtime)

    def list_multipart_uploads_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.ListMultipartUploadsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListMultipartUploadsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.key_marker):
            query['key-marker'] = request.key_marker
        if not UtilClient.is_unset(request.max_uploads):
            query['max-uploads'] = request.max_uploads
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.upload_id_marker):
            query['upload-id-marker'] = request.upload_id_marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultipartUploads',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?uploads',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListMultipartUploadsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_multipart_uploads_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListMultipartUploadsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListMultipartUploadsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.key_marker):
            query['key-marker'] = request.key_marker
        if not UtilClient.is_unset(request.max_uploads):
            query['max-uploads'] = request.max_uploads
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.upload_id_marker):
            query['upload-id-marker'] = request.upload_id_marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultipartUploads',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?uploads',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListMultipartUploadsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_object_versions(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectVersionsRequest,
    ) -> oss_20190517_models.ListObjectVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_object_versions_with_options(bucket, request, headers, runtime)

    async def list_object_versions_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectVersionsRequest,
    ) -> oss_20190517_models.ListObjectVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_object_versions_with_options_async(bucket, request, headers, runtime)

    def list_object_versions_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListObjectVersionsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.key_marker):
            query['key-marker'] = request.key_marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.version_id_marker):
            query['version-id-marker'] = request.version_id_marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjectVersions',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListObjectVersionsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_object_versions_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListObjectVersionsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.key_marker):
            query['key-marker'] = request.key_marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.version_id_marker):
            query['version-id-marker'] = request.version_id_marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjectVersions',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListObjectVersionsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_objects(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectsRequest,
    ) -> oss_20190517_models.ListObjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_objects_with_options(bucket, request, headers, runtime)

    async def list_objects_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectsRequest,
    ) -> oss_20190517_models.ListObjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_objects_with_options_async(bucket, request, headers, runtime)

    def list_objects_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListObjectsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjects',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListObjectsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_objects_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListObjectsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjects',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListObjectsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_objects_v2(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectsV2Request,
    ) -> oss_20190517_models.ListObjectsV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_objects_v2with_options(bucket, request, headers, runtime)

    async def list_objects_v2_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectsV2Request,
    ) -> oss_20190517_models.ListObjectsV2Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_objects_v2with_options_async(bucket, request, headers, runtime)

    def list_objects_v2with_options(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectsV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListObjectsV2Response:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.continuation_token):
            query['continuation-token'] = request.continuation_token
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.fetch_owner):
            query['fetch-owner'] = request.fetch_owner
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_after):
            query['start-after'] = request.start_after
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjectsV2',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?list-type=2',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListObjectsV2Response(),
            self.execute(params, req, runtime)
        )

    async def list_objects_v2with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.ListObjectsV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListObjectsV2Response:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.continuation_token):
            query['continuation-token'] = request.continuation_token
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.fetch_owner):
            query['fetch-owner'] = request.fetch_owner
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_after):
            query['start-after'] = request.start_after
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjectsV2',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?list-type=2',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListObjectsV2Response(),
            await self.execute_async(params, req, runtime)
        )

    def list_parts(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.ListPartsRequest,
    ) -> oss_20190517_models.ListPartsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_parts_with_options(bucket, key, request, headers, runtime)

    async def list_parts_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.ListPartsRequest,
    ) -> oss_20190517_models.ListPartsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_parts_with_options_async(bucket, key, request, headers, runtime)

    def list_parts_with_options(
        self,
        bucket: str,
        key: str,
        tmp_req: oss_20190517_models.ListPartsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListPartsResponse:
        UtilClient.validate_model(tmp_req)
        host_map = {}
        host_map['bucket'] = bucket
        request = oss_20190517_models.ListPartsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encoding_type):
            request.encoding_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encoding_type, 'encoding-type', 'json')
        query = {}
        if not UtilClient.is_unset(request.encoding_type_shrink):
            query['encoding-type'] = request.encoding_type_shrink
        if not UtilClient.is_unset(request.max_parts):
            query['max-parts'] = request.max_parts
        if not UtilClient.is_unset(request.part_number_marker):
            query['part-number-marker'] = request.part_number_marker
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParts',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListPartsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_parts_with_options_async(
        self,
        bucket: str,
        key: str,
        tmp_req: oss_20190517_models.ListPartsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.ListPartsResponse:
        UtilClient.validate_model(tmp_req)
        host_map = {}
        host_map['bucket'] = bucket
        request = oss_20190517_models.ListPartsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encoding_type):
            request.encoding_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encoding_type, 'encoding-type', 'json')
        query = {}
        if not UtilClient.is_unset(request.encoding_type_shrink):
            query['encoding-type'] = request.encoding_type_shrink
        if not UtilClient.is_unset(request.max_parts):
            query['max-parts'] = request.max_parts
        if not UtilClient.is_unset(request.part_number_marker):
            query['part-number-marker'] = request.part_number_marker
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParts',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListPartsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def option_object(
        self,
        bucket: str,
        key: str,
    ) -> oss_20190517_models.OptionObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.OptionObjectHeaders()
        return self.option_object_with_options(bucket, key, headers, runtime)

    async def option_object_async(
        self,
        bucket: str,
        key: str,
    ) -> oss_20190517_models.OptionObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.OptionObjectHeaders()
        return await self.option_object_with_options_async(bucket, key, headers, runtime)

    def option_object_with_options(
        self,
        bucket: str,
        key: str,
        headers: oss_20190517_models.OptionObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.OptionObjectResponse:
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.access_control_request_headers):
            real_headers['Access-Control-Request-Headers'] = UtilClient.to_jsonstring(headers.access_control_request_headers)
        if not UtilClient.is_unset(headers.access_control_request_method):
            real_headers['Access-Control-Request-Method'] = UtilClient.to_jsonstring(headers.access_control_request_method)
        if not UtilClient.is_unset(headers.origin):
            real_headers['Origin'] = UtilClient.to_jsonstring(headers.origin)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='OptionObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='OPTIONS',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.OptionObjectResponse(),
            self.execute(params, req, runtime)
        )

    async def option_object_with_options_async(
        self,
        bucket: str,
        key: str,
        headers: oss_20190517_models.OptionObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.OptionObjectResponse:
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.access_control_request_headers):
            real_headers['Access-Control-Request-Headers'] = UtilClient.to_jsonstring(headers.access_control_request_headers)
        if not UtilClient.is_unset(headers.access_control_request_method):
            real_headers['Access-Control-Request-Method'] = UtilClient.to_jsonstring(headers.access_control_request_method)
        if not UtilClient.is_unset(headers.origin):
            real_headers['Origin'] = UtilClient.to_jsonstring(headers.origin)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='OptionObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='OPTIONS',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.OptionObjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def post_object(
        self,
        bucket: str,
    ) -> oss_20190517_models.PostObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.post_object_with_options(bucket, headers, runtime)

    async def post_object_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.PostObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.post_object_with_options_async(bucket, headers, runtime)

    def post_object_with_options(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PostObjectResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='PostObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='multiFormData',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PostObjectResponse(),
            self.execute(params, req, runtime)
        )

    async def post_object_with_options_async(
        self,
        bucket: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PostObjectResponse:
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='PostObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='multiFormData',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PostObjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def post_vod_playlist(
        self,
        bucket: str,
        channel: str,
        playlist: str,
        request: oss_20190517_models.PostVodPlaylistRequest,
    ) -> oss_20190517_models.PostVodPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.post_vod_playlist_with_options(bucket, channel, playlist, request, headers, runtime)

    async def post_vod_playlist_async(
        self,
        bucket: str,
        channel: str,
        playlist: str,
        request: oss_20190517_models.PostVodPlaylistRequest,
    ) -> oss_20190517_models.PostVodPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.post_vod_playlist_with_options_async(bucket, channel, playlist, request, headers, runtime)

    def post_vod_playlist_with_options(
        self,
        bucket: str,
        channel: str,
        playlist: str,
        request: oss_20190517_models.PostVodPlaylistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PostVodPlaylistResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PostVodPlaylist',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}/{playlist}?vod',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PostVodPlaylistResponse(),
            self.execute(params, req, runtime)
        )

    async def post_vod_playlist_with_options_async(
        self,
        bucket: str,
        channel: str,
        playlist: str,
        request: oss_20190517_models.PostVodPlaylistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PostVodPlaylistResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PostVodPlaylist',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}/{playlist}?vod',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PostVodPlaylistResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRequest,
    ) -> oss_20190517_models.PutBucketResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutBucketHeaders()
        return self.put_bucket_with_options(bucket, request, headers, runtime)

    async def put_bucket_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRequest,
    ) -> oss_20190517_models.PutBucketResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutBucketHeaders()
        return await self.put_bucket_with_options_async(bucket, request, headers, runtime)

    def put_bucket_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRequest,
        headers: oss_20190517_models.PutBucketHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-acl'] = UtilClient.to_jsonstring(headers.acl)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.create_bucket_configuration))
        )
        params = open_api_models.Params(
            action='PutBucket',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRequest,
        headers: oss_20190517_models.PutBucketHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-acl'] = UtilClient.to_jsonstring(headers.acl)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.create_bucket_configuration))
        )
        params = open_api_models.Params(
            action='PutBucket',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_acl(
        self,
        bucket: str,
    ) -> oss_20190517_models.PutBucketAclResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutBucketAclHeaders()
        return self.put_bucket_acl_with_options(bucket, headers, runtime)

    async def put_bucket_acl_async(
        self,
        bucket: str,
    ) -> oss_20190517_models.PutBucketAclResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutBucketAclHeaders()
        return await self.put_bucket_acl_with_options_async(bucket, headers, runtime)

    def put_bucket_acl_with_options(
        self,
        bucket: str,
        headers: oss_20190517_models.PutBucketAclHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketAclResponse:
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-acl'] = UtilClient.to_jsonstring(headers.acl)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='PutBucketAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?acl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketAclResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_acl_with_options_async(
        self,
        bucket: str,
        headers: oss_20190517_models.PutBucketAclHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketAclResponse:
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-acl'] = UtilClient.to_jsonstring(headers.acl)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='PutBucketAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?acl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketAclResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_cors(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketCorsRequest,
    ) -> oss_20190517_models.PutBucketCorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_cors_with_options(bucket, request, headers, runtime)

    async def put_bucket_cors_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketCorsRequest,
    ) -> oss_20190517_models.PutBucketCorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_cors_with_options_async(bucket, request, headers, runtime)

    def put_bucket_cors_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketCorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketCorsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.c_orsconfiguration))
        )
        params = open_api_models.Params(
            action='PutBucketCors',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?cors',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketCorsResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_cors_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketCorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketCorsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.c_orsconfiguration))
        )
        params = open_api_models.Params(
            action='PutBucketCors',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?cors',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketCorsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_encryption(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketEncryptionRequest,
    ) -> oss_20190517_models.PutBucketEncryptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_encryption_with_options(bucket, request, headers, runtime)

    async def put_bucket_encryption_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketEncryptionRequest,
    ) -> oss_20190517_models.PutBucketEncryptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_encryption_with_options_async(bucket, request, headers, runtime)

    def put_bucket_encryption_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketEncryptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketEncryptionResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.server_side_encryption_rule))
        )
        params = open_api_models.Params(
            action='PutBucketEncryption',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?encryption',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketEncryptionResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_encryption_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketEncryptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketEncryptionResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.server_side_encryption_rule))
        )
        params = open_api_models.Params(
            action='PutBucketEncryption',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?encryption',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketEncryptionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_inventory(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketInventoryRequest,
    ) -> oss_20190517_models.PutBucketInventoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_inventory_with_options(bucket, request, headers, runtime)

    async def put_bucket_inventory_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketInventoryRequest,
    ) -> oss_20190517_models.PutBucketInventoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_inventory_with_options_async(bucket, request, headers, runtime)

    def put_bucket_inventory_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketInventoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketInventoryResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.inventory_id):
            query['inventoryId'] = request.inventory_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.inventory_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?inventory',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketInventoryResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_inventory_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketInventoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketInventoryResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.inventory_id):
            query['inventoryId'] = request.inventory_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.inventory_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?inventory',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketInventoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_lifecycle(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketLifecycleRequest,
    ) -> oss_20190517_models.PutBucketLifecycleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_lifecycle_with_options(bucket, request, headers, runtime)

    async def put_bucket_lifecycle_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketLifecycleRequest,
    ) -> oss_20190517_models.PutBucketLifecycleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_lifecycle_with_options_async(bucket, request, headers, runtime)

    def put_bucket_lifecycle_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketLifecycleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketLifecycleResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.lifecycle_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketLifecycle',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?lifecycle',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketLifecycleResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_lifecycle_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketLifecycleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketLifecycleResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.lifecycle_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketLifecycle',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?lifecycle',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketLifecycleResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_logging(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketLoggingRequest,
    ) -> oss_20190517_models.PutBucketLoggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_logging_with_options(bucket, request, headers, runtime)

    async def put_bucket_logging_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketLoggingRequest,
    ) -> oss_20190517_models.PutBucketLoggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_logging_with_options_async(bucket, request, headers, runtime)

    def put_bucket_logging_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketLoggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketLoggingResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.bucket_logging_status))
        )
        params = open_api_models.Params(
            action='PutBucketLogging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?logging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketLoggingResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_logging_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketLoggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketLoggingResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.bucket_logging_status))
        )
        params = open_api_models.Params(
            action='PutBucketLogging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?logging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketLoggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_policy(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketPolicyRequest,
    ) -> oss_20190517_models.PutBucketPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_policy_with_options(bucket, request, headers, runtime)

    async def put_bucket_policy_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketPolicyRequest,
    ) -> oss_20190517_models.PutBucketPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_policy_with_options_async(bucket, request, headers, runtime)

    def put_bucket_policy_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketPolicyResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=request.policy
        )
        params = open_api_models.Params(
            action='PutBucketPolicy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?policy',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_policy_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketPolicyResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=request.policy
        )
        params = open_api_models.Params(
            action='PutBucketPolicy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?policy',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_referer(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRefererRequest,
    ) -> oss_20190517_models.PutBucketRefererResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_referer_with_options(bucket, request, headers, runtime)

    async def put_bucket_referer_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRefererRequest,
    ) -> oss_20190517_models.PutBucketRefererResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_referer_with_options_async(bucket, request, headers, runtime)

    def put_bucket_referer_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRefererRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketRefererResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.referer_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketReferer',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?referer',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketRefererResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_referer_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRefererRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketRefererResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.referer_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketReferer',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?referer',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketRefererResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_replication(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketReplicationRequest,
    ) -> oss_20190517_models.PutBucketReplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_replication_with_options(bucket, request, headers, runtime)

    async def put_bucket_replication_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketReplicationRequest,
    ) -> oss_20190517_models.PutBucketReplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_replication_with_options_async(bucket, request, headers, runtime)

    def put_bucket_replication_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketReplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketReplicationResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.replication_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketReplication',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?replication&comp=add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketReplicationResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_replication_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketReplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketReplicationResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.replication_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketReplication',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?replication&comp=add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketReplicationResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_request_payment(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRequestPaymentRequest,
    ) -> oss_20190517_models.PutBucketRequestPaymentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_request_payment_with_options(bucket, request, headers, runtime)

    async def put_bucket_request_payment_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRequestPaymentRequest,
    ) -> oss_20190517_models.PutBucketRequestPaymentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_request_payment_with_options_async(bucket, request, headers, runtime)

    def put_bucket_request_payment_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRequestPaymentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketRequestPaymentResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.request_payment_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketRequestPayment',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?requestPayment',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketRequestPaymentResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_request_payment_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketRequestPaymentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketRequestPaymentResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.request_payment_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketRequestPayment',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?requestPayment',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketRequestPaymentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_tags(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketTagsRequest,
    ) -> oss_20190517_models.PutBucketTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_tags_with_options(bucket, request, headers, runtime)

    async def put_bucket_tags_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketTagsRequest,
    ) -> oss_20190517_models.PutBucketTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_tags_with_options_async(bucket, request, headers, runtime)

    def put_bucket_tags_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketTagsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.tagging))
        )
        params = open_api_models.Params(
            action='PutBucketTags',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?tagging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_tags_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketTagsResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.tagging))
        )
        params = open_api_models.Params(
            action='PutBucketTags',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?tagging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_transfer_acceleration(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketTransferAccelerationRequest,
    ) -> oss_20190517_models.PutBucketTransferAccelerationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_transfer_acceleration_with_options(bucket, request, headers, runtime)

    async def put_bucket_transfer_acceleration_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketTransferAccelerationRequest,
    ) -> oss_20190517_models.PutBucketTransferAccelerationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_transfer_acceleration_with_options_async(bucket, request, headers, runtime)

    def put_bucket_transfer_acceleration_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketTransferAccelerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketTransferAccelerationResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.transfer_acceleration_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketTransferAcceleration',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?transferAcceleration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketTransferAccelerationResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_transfer_acceleration_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketTransferAccelerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketTransferAccelerationResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.transfer_acceleration_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketTransferAcceleration',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?transferAcceleration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketTransferAccelerationResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_versioning(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketVersioningRequest,
    ) -> oss_20190517_models.PutBucketVersioningResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_versioning_with_options(bucket, request, headers, runtime)

    async def put_bucket_versioning_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketVersioningRequest,
    ) -> oss_20190517_models.PutBucketVersioningResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_versioning_with_options_async(bucket, request, headers, runtime)

    def put_bucket_versioning_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketVersioningRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketVersioningResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.versioning_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketVersioning',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?versioning',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketVersioningResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_versioning_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketVersioningRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketVersioningResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.versioning_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketVersioning',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?versioning',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketVersioningResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_bucket_website(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketWebsiteRequest,
    ) -> oss_20190517_models.PutBucketWebsiteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_website_with_options(bucket, request, headers, runtime)

    async def put_bucket_website_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketWebsiteRequest,
    ) -> oss_20190517_models.PutBucketWebsiteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_bucket_website_with_options_async(bucket, request, headers, runtime)

    def put_bucket_website_with_options(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketWebsiteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketWebsiteResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.website_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketWebsite',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?website',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketWebsiteResponse(),
            self.execute(params, req, runtime)
        )

    async def put_bucket_website_with_options_async(
        self,
        bucket: str,
        request: oss_20190517_models.PutBucketWebsiteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutBucketWebsiteResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.website_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketWebsite',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/?website',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketWebsiteResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_live_channel(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.PutLiveChannelRequest,
    ) -> oss_20190517_models.PutLiveChannelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_live_channel_with_options(bucket, channel, request, headers, runtime)

    async def put_live_channel_async(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.PutLiveChannelRequest,
    ) -> oss_20190517_models.PutLiveChannelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_live_channel_with_options_async(bucket, channel, request, headers, runtime)

    def put_live_channel_with_options(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.PutLiveChannelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutLiveChannelResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.live_channel_configuration))
        )
        params = open_api_models.Params(
            action='PutLiveChannel',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutLiveChannelResponse(),
            self.execute(params, req, runtime)
        )

    async def put_live_channel_with_options_async(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.PutLiveChannelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutLiveChannelResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.live_channel_configuration))
        )
        params = open_api_models.Params(
            action='PutLiveChannel',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutLiveChannelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_live_channel_status(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.PutLiveChannelStatusRequest,
    ) -> oss_20190517_models.PutLiveChannelStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_live_channel_status_with_options(bucket, channel, request, headers, runtime)

    async def put_live_channel_status_async(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.PutLiveChannelStatusRequest,
    ) -> oss_20190517_models.PutLiveChannelStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_live_channel_status_with_options_async(bucket, channel, request, headers, runtime)

    def put_live_channel_status_with_options(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.PutLiveChannelStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutLiveChannelStatusResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutLiveChannelStatus',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutLiveChannelStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def put_live_channel_status_with_options_async(
        self,
        bucket: str,
        channel: str,
        request: oss_20190517_models.PutLiveChannelStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutLiveChannelStatusResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutLiveChannelStatus',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{channel}?live',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutLiveChannelStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_object(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectRequest,
    ) -> oss_20190517_models.PutObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutObjectHeaders()
        return self.put_object_with_options(bucket, key, request, headers, runtime)

    async def put_object_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectRequest,
    ) -> oss_20190517_models.PutObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutObjectHeaders()
        return await self.put_object_with_options_async(bucket, key, request, headers, runtime)

    def put_object_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectRequest,
        headers: oss_20190517_models.PutObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.meta_data):
            real_headers['x-oss-meta-*'] = UtilClient.to_jsonstring(headers.meta_data)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.sse_data_encryption):
            real_headers['x-oss-server-side-data-encryption'] = UtilClient.to_jsonstring(headers.sse_data_encryption)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.sse_key_id):
            real_headers['x-oss-server-side-encryption-key-id'] = UtilClient.to_jsonstring(headers.sse_key_id)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.tagging):
            real_headers['x-oss-tagging'] = UtilClient.to_jsonstring(headers.tagging)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='PutObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='binary',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutObjectResponse(),
            self.execute(params, req, runtime)
        )

    async def put_object_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectRequest,
        headers: oss_20190517_models.PutObjectHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.meta_data):
            real_headers['x-oss-meta-*'] = UtilClient.to_jsonstring(headers.meta_data)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.sse_data_encryption):
            real_headers['x-oss-server-side-data-encryption'] = UtilClient.to_jsonstring(headers.sse_data_encryption)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.sse_key_id):
            real_headers['x-oss-server-side-encryption-key-id'] = UtilClient.to_jsonstring(headers.sse_key_id)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.tagging):
            real_headers['x-oss-tagging'] = UtilClient.to_jsonstring(headers.tagging)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='PutObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='binary',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutObjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_object_acl(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectAclRequest,
    ) -> oss_20190517_models.PutObjectAclResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutObjectAclHeaders()
        return self.put_object_acl_with_options(bucket, key, request, headers, runtime)

    async def put_object_acl_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectAclRequest,
    ) -> oss_20190517_models.PutObjectAclResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutObjectAclHeaders()
        return await self.put_object_acl_with_options_async(bucket, key, request, headers, runtime)

    def put_object_acl_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectAclRequest,
        headers: oss_20190517_models.PutObjectAclHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutObjectAclResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutObjectAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?acl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutObjectAclResponse(),
            self.execute(params, req, runtime)
        )

    async def put_object_acl_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectAclRequest,
        headers: oss_20190517_models.PutObjectAclHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutObjectAclResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutObjectAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?acl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutObjectAclResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_object_tagging(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectTaggingRequest,
    ) -> oss_20190517_models.PutObjectTaggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_object_tagging_with_options(bucket, key, request, headers, runtime)

    async def put_object_tagging_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectTaggingRequest,
    ) -> oss_20190517_models.PutObjectTaggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_object_tagging_with_options_async(bucket, key, request, headers, runtime)

    def put_object_tagging_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectTaggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutObjectTaggingResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.tagging))
        )
        params = open_api_models.Params(
            action='PutObjectTagging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?tagging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutObjectTaggingResponse(),
            self.execute(params, req, runtime)
        )

    async def put_object_tagging_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.PutObjectTaggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutObjectTaggingResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.tagging))
        )
        params = open_api_models.Params(
            action='PutObjectTagging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?tagging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutObjectTaggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_symlink(
        self,
        bucket: str,
        key: str,
    ) -> oss_20190517_models.PutSymlinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutSymlinkHeaders()
        return self.put_symlink_with_options(bucket, key, headers, runtime)

    async def put_symlink_async(
        self,
        bucket: str,
        key: str,
    ) -> oss_20190517_models.PutSymlinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutSymlinkHeaders()
        return await self.put_symlink_with_options_async(bucket, key, headers, runtime)

    def put_symlink_with_options(
        self,
        bucket: str,
        key: str,
        headers: oss_20190517_models.PutSymlinkHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutSymlinkResponse:
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.symlink_target_key):
            real_headers['x-oss-symlink-target'] = UtilClient.to_jsonstring(headers.symlink_target_key)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='PutSymlink',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?symlink',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutSymlinkResponse(),
            self.execute(params, req, runtime)
        )

    async def put_symlink_with_options_async(
        self,
        bucket: str,
        key: str,
        headers: oss_20190517_models.PutSymlinkHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.PutSymlinkResponse:
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.symlink_target_key):
            real_headers['x-oss-symlink-target'] = UtilClient.to_jsonstring(headers.symlink_target_key)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='PutSymlink',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?symlink',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutSymlinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def restore_object(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.RestoreObjectRequest,
    ) -> oss_20190517_models.RestoreObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restore_object_with_options(bucket, key, request, headers, runtime)

    async def restore_object_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.RestoreObjectRequest,
    ) -> oss_20190517_models.RestoreObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restore_object_with_options_async(bucket, key, request, headers, runtime)

    def restore_object_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.RestoreObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.RestoreObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.restore_request))
        )
        params = open_api_models.Params(
            action='RestoreObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.RestoreObjectResponse(),
            self.execute(params, req, runtime)
        )

    async def restore_object_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.RestoreObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.RestoreObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.restore_request))
        )
        params = open_api_models.Params(
            action='RestoreObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}?restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.RestoreObjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def select_object(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.SelectObjectRequest,
    ) -> oss_20190517_models.SelectObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.select_object_with_options(bucket, key, request, headers, runtime)

    async def select_object_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.SelectObjectRequest,
    ) -> oss_20190517_models.SelectObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.select_object_with_options_async(bucket, key, request, headers, runtime)

    def select_object_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.SelectObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.SelectObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.select_request))
        )
        params = open_api_models.Params(
            action='SelectObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='binary'
        )
        return TeaCore.from_map(
            oss_20190517_models.SelectObjectResponse(),
            self.execute(params, req, runtime)
        )

    async def select_object_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.SelectObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.SelectObjectResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.select_request))
        )
        params = open_api_models.Params(
            action='SelectObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='binary'
        )
        return TeaCore.from_map(
            oss_20190517_models.SelectObjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def upload_part(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.UploadPartRequest,
    ) -> oss_20190517_models.UploadPartResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_part_with_options(bucket, key, request, headers, runtime)

    async def upload_part_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.UploadPartRequest,
    ) -> oss_20190517_models.UploadPartResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_part_with_options_async(bucket, key, request, headers, runtime)

    def upload_part_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.UploadPartRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.UploadPartResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.part_number):
            query['partNumber'] = request.part_number
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='UploadPart',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='binary',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.UploadPartResponse(),
            self.execute(params, req, runtime)
        )

    async def upload_part_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.UploadPartRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.UploadPartResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.part_number):
            query['partNumber'] = request.part_number
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='UploadPart',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='binary',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.UploadPartResponse(),
            await self.execute_async(params, req, runtime)
        )

    def upload_part_copy(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.UploadPartCopyRequest,
    ) -> oss_20190517_models.UploadPartCopyResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.UploadPartCopyHeaders()
        return self.upload_part_copy_with_options(bucket, key, request, headers, runtime)

    async def upload_part_copy_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.UploadPartCopyRequest,
    ) -> oss_20190517_models.UploadPartCopyResponse:
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.UploadPartCopyHeaders()
        return await self.upload_part_copy_with_options_async(bucket, key, request, headers, runtime)

    def upload_part_copy_with_options(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.UploadPartCopyRequest,
        headers: oss_20190517_models.UploadPartCopyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.UploadPartCopyResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.part_number):
            query['partNumber'] = request.part_number
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.copy_source):
            real_headers['x-oss-copy-source'] = UtilClient.to_jsonstring(headers.copy_source)
        if not UtilClient.is_unset(headers.copy_source_if_match):
            real_headers['x-oss-copy-source-if-match'] = UtilClient.to_jsonstring(headers.copy_source_if_match)
        if not UtilClient.is_unset(headers.copy_source_if_modified_since):
            real_headers['x-oss-copy-source-if-modified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_modified_since)
        if not UtilClient.is_unset(headers.copy_source_if_none_match):
            real_headers['x-oss-copy-source-if-none-match'] = UtilClient.to_jsonstring(headers.copy_source_if_none_match)
        if not UtilClient.is_unset(headers.copy_source_if_unmodified_since):
            real_headers['x-oss-copy-source-if-unmodified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_unmodified_since)
        if not UtilClient.is_unset(headers.copy_source_range):
            real_headers['x-oss-copy-source-range'] = UtilClient.to_jsonstring(headers.copy_source_range)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadPartCopy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.UploadPartCopyResponse(),
            self.execute(params, req, runtime)
        )

    async def upload_part_copy_with_options_async(
        self,
        bucket: str,
        key: str,
        request: oss_20190517_models.UploadPartCopyRequest,
        headers: oss_20190517_models.UploadPartCopyHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> oss_20190517_models.UploadPartCopyResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.part_number):
            query['partNumber'] = request.part_number
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.copy_source):
            real_headers['x-oss-copy-source'] = UtilClient.to_jsonstring(headers.copy_source)
        if not UtilClient.is_unset(headers.copy_source_if_match):
            real_headers['x-oss-copy-source-if-match'] = UtilClient.to_jsonstring(headers.copy_source_if_match)
        if not UtilClient.is_unset(headers.copy_source_if_modified_since):
            real_headers['x-oss-copy-source-if-modified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_modified_since)
        if not UtilClient.is_unset(headers.copy_source_if_none_match):
            real_headers['x-oss-copy-source-if-none-match'] = UtilClient.to_jsonstring(headers.copy_source_if_none_match)
        if not UtilClient.is_unset(headers.copy_source_if_unmodified_since):
            real_headers['x-oss-copy-source-if-unmodified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_unmodified_since)
        if not UtilClient.is_unset(headers.copy_source_range):
            real_headers['x-oss-copy-source-range'] = UtilClient.to_jsonstring(headers.copy_source_range)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadPartCopy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname=f'/{key}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.UploadPartCopyResponse(),
            await self.execute_async(params, req, runtime)
        )
