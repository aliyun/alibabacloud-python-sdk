# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth_console20190403 import models as cloudauth_console_20190403_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('cloudauth-console', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def retrieve_face_with_options(
        self,
        request: cloudauth_console_20190403_models.RetrieveFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190403_models.RetrieveFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190403_models.RetrieveFaceResponse().from_map(
            self.do_rpcrequest('RetrieveFace', '2019-04-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def retrieve_face_with_options_async(
        self,
        request: cloudauth_console_20190403_models.RetrieveFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190403_models.RetrieveFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190403_models.RetrieveFaceResponse().from_map(
            await self.do_rpcrequest_async('RetrieveFace', '2019-04-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def retrieve_face(
        self,
        request: cloudauth_console_20190403_models.RetrieveFaceRequest,
    ) -> cloudauth_console_20190403_models.RetrieveFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.retrieve_face_with_options(request, runtime)

    async def retrieve_face_async(
        self,
        request: cloudauth_console_20190403_models.RetrieveFaceRequest,
    ) -> cloudauth_console_20190403_models.RetrieveFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retrieve_face_with_options_async(request, runtime)

    def upload_identify_record_with_options(
        self,
        request: cloudauth_console_20190403_models.UploadIdentifyRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190403_models.UploadIdentifyRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190403_models.UploadIdentifyRecordResponse().from_map(
            self.do_rpcrequest('UploadIdentifyRecord', '2019-04-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_identify_record_with_options_async(
        self,
        request: cloudauth_console_20190403_models.UploadIdentifyRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_console_20190403_models.UploadIdentifyRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloudauth_console_20190403_models.UploadIdentifyRecordResponse().from_map(
            await self.do_rpcrequest_async('UploadIdentifyRecord', '2019-04-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_identify_record(
        self,
        request: cloudauth_console_20190403_models.UploadIdentifyRecordRequest,
    ) -> cloudauth_console_20190403_models.UploadIdentifyRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_identify_record_with_options(request, runtime)

    async def upload_identify_record_async(
        self,
        request: cloudauth_console_20190403_models.UploadIdentifyRecordRequest,
    ) -> cloudauth_console_20190403_models.UploadIdentifyRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_identify_record_with_options_async(request, runtime)
