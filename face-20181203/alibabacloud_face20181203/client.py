# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_face20181203 import models as face_20181203_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('face', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_face_with_options(
        self,
        request: face_20181203_models.AddFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.AddFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.AddFaceResponse().from_map(
            self.do_rpcrequest('AddFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_face_with_options_async(
        self,
        request: face_20181203_models.AddFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.AddFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.AddFaceResponse().from_map(
            await self.do_rpcrequest_async('AddFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_face(
        self,
        request: face_20181203_models.AddFaceRequest,
    ) -> face_20181203_models.AddFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_with_options(request, runtime)

    async def add_face_async(
        self,
        request: face_20181203_models.AddFaceRequest,
    ) -> face_20181203_models.AddFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_with_options_async(request, runtime)

    def delete_face_with_options(
        self,
        request: face_20181203_models.DeleteFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.DeleteFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.DeleteFaceResponse().from_map(
            self.do_rpcrequest('DeleteFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_with_options_async(
        self,
        request: face_20181203_models.DeleteFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.DeleteFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.DeleteFaceResponse().from_map(
            await self.do_rpcrequest_async('DeleteFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face(
        self,
        request: face_20181203_models.DeleteFaceRequest,
    ) -> face_20181203_models.DeleteFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_with_options(request, runtime)

    async def delete_face_async(
        self,
        request: face_20181203_models.DeleteFaceRequest,
    ) -> face_20181203_models.DeleteFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_with_options_async(request, runtime)

    def detect_face_with_options(
        self,
        request: face_20181203_models.DetectFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.DetectFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.DetectFaceResponse().from_map(
            self.do_rpcrequest('DetectFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_face_with_options_async(
        self,
        request: face_20181203_models.DetectFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.DetectFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.DetectFaceResponse().from_map(
            await self.do_rpcrequest_async('DetectFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_face(
        self,
        request: face_20181203_models.DetectFaceRequest,
    ) -> face_20181203_models.DetectFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_face_with_options(request, runtime)

    async def detect_face_async(
        self,
        request: face_20181203_models.DetectFaceRequest,
    ) -> face_20181203_models.DetectFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_face_with_options_async(request, runtime)

    def get_face_attribute_with_options(
        self,
        request: face_20181203_models.GetFaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.GetFaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.GetFaceAttributeResponse().from_map(
            self.do_rpcrequest('GetFaceAttribute', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_face_attribute_with_options_async(
        self,
        request: face_20181203_models.GetFaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.GetFaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.GetFaceAttributeResponse().from_map(
            await self.do_rpcrequest_async('GetFaceAttribute', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_face_attribute(
        self,
        request: face_20181203_models.GetFaceAttributeRequest,
    ) -> face_20181203_models.GetFaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_face_attribute_with_options(request, runtime)

    async def get_face_attribute_async(
        self,
        request: face_20181203_models.GetFaceAttributeRequest,
    ) -> face_20181203_models.GetFaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_face_attribute_with_options_async(request, runtime)

    def list_face_with_options(
        self,
        request: face_20181203_models.ListFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.ListFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.ListFaceResponse().from_map(
            self.do_rpcrequest('ListFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_face_with_options_async(
        self,
        request: face_20181203_models.ListFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.ListFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.ListFaceResponse().from_map(
            await self.do_rpcrequest_async('ListFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_face(
        self,
        request: face_20181203_models.ListFaceRequest,
    ) -> face_20181203_models.ListFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_face_with_options(request, runtime)

    async def list_face_async(
        self,
        request: face_20181203_models.ListFaceRequest,
    ) -> face_20181203_models.ListFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_face_with_options_async(request, runtime)

    def list_group_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.ListGroupResponse:
        req = open_api_models.OpenApiRequest()
        return face_20181203_models.ListGroupResponse().from_map(
            self.do_rpcrequest('ListGroup', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_group_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.ListGroupResponse:
        req = open_api_models.OpenApiRequest()
        return face_20181203_models.ListGroupResponse().from_map(
            await self.do_rpcrequest_async('ListGroup', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_group(self) -> face_20181203_models.ListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_group_with_options(runtime)

    async def list_group_async(self) -> face_20181203_models.ListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_group_with_options_async(runtime)

    def recognize_face_with_options(
        self,
        request: face_20181203_models.RecognizeFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.RecognizeFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.RecognizeFaceResponse().from_map(
            self.do_rpcrequest('RecognizeFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_face_with_options_async(
        self,
        request: face_20181203_models.RecognizeFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.RecognizeFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.RecognizeFaceResponse().from_map(
            await self.do_rpcrequest_async('RecognizeFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_face(
        self,
        request: face_20181203_models.RecognizeFaceRequest,
    ) -> face_20181203_models.RecognizeFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_face_with_options(request, runtime)

    async def recognize_face_async(
        self,
        request: face_20181203_models.RecognizeFaceRequest,
    ) -> face_20181203_models.RecognizeFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_face_with_options_async(request, runtime)

    def verify_face_with_options(
        self,
        request: face_20181203_models.VerifyFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.VerifyFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.VerifyFaceResponse().from_map(
            self.do_rpcrequest('VerifyFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_face_with_options_async(
        self,
        request: face_20181203_models.VerifyFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> face_20181203_models.VerifyFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return face_20181203_models.VerifyFaceResponse().from_map(
            await self.do_rpcrequest_async('VerifyFace', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_face(
        self,
        request: face_20181203_models.VerifyFaceRequest,
    ) -> face_20181203_models.VerifyFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_face_with_options(request, runtime)

    async def verify_face_async(
        self,
        request: face_20181203_models.VerifyFaceRequest,
    ) -> face_20181203_models.VerifyFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_face_with_options_async(request, runtime)
