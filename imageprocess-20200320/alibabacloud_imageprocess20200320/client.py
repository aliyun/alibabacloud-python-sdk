# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imageprocess20200320 import models as imageprocess_20200320_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_darabonba_number.client import Client as NumberClient


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
        self._endpoint = self.get_endpoint('imageprocess', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def analyze_chest_vessel_with_options(
        self,
        request: imageprocess_20200320_models.AnalyzeChestVesselRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.AnalyzeChestVesselResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AnalyzeChestVessel',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.AnalyzeChestVesselResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_chest_vessel_with_options_async(
        self,
        request: imageprocess_20200320_models.AnalyzeChestVesselRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.AnalyzeChestVesselResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AnalyzeChestVessel',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.AnalyzeChestVesselResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_chest_vessel(
        self,
        request: imageprocess_20200320_models.AnalyzeChestVesselRequest,
    ) -> imageprocess_20200320_models.AnalyzeChestVesselResponse:
        runtime = util_models.RuntimeOptions()
        return self.analyze_chest_vessel_with_options(request, runtime)

    async def analyze_chest_vessel_async(
        self,
        request: imageprocess_20200320_models.AnalyzeChestVesselRequest,
    ) -> imageprocess_20200320_models.AnalyzeChestVesselResponse:
        runtime = util_models.RuntimeOptions()
        return await self.analyze_chest_vessel_with_options_async(request, runtime)

    def analyze_chest_vessel_advance(
        self,
        request: imageprocess_20200320_models.AnalyzeChestVesselAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.AnalyzeChestVesselResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        analyze_chest_vessel_req = imageprocess_20200320_models.AnalyzeChestVesselRequest()
        OpenApiUtilClient.convert(request, analyze_chest_vessel_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = analyze_chest_vessel_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        analyze_chest_vessel_resp = self.analyze_chest_vessel_with_options(analyze_chest_vessel_req, runtime)
        return analyze_chest_vessel_resp

    async def analyze_chest_vessel_advance_async(
        self,
        request: imageprocess_20200320_models.AnalyzeChestVesselAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.AnalyzeChestVesselResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        analyze_chest_vessel_req = imageprocess_20200320_models.AnalyzeChestVesselRequest()
        OpenApiUtilClient.convert(request, analyze_chest_vessel_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = analyze_chest_vessel_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        analyze_chest_vessel_resp = await self.analyze_chest_vessel_with_options_async(analyze_chest_vessel_req, runtime)
        return analyze_chest_vessel_resp

    def calc_cacswith_options(
        self,
        request: imageprocess_20200320_models.CalcCACSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CalcCACS',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.CalcCACSResponse(),
            self.call_api(params, req, runtime)
        )

    async def calc_cacswith_options_async(
        self,
        request: imageprocess_20200320_models.CalcCACSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CalcCACS',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.CalcCACSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def calc_cacs(
        self,
        request: imageprocess_20200320_models.CalcCACSRequest,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        runtime = util_models.RuntimeOptions()
        return self.calc_cacswith_options(request, runtime)

    async def calc_cacs_async(
        self,
        request: imageprocess_20200320_models.CalcCACSRequest,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.calc_cacswith_options_async(request, runtime)

    def calc_cacsadvance(
        self,
        request: imageprocess_20200320_models.CalcCACSAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        calc_cacsreq = imageprocess_20200320_models.CalcCACSRequest()
        OpenApiUtilClient.convert(request, calc_cacsreq)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = calc_cacsreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        calc_cacsresp = self.calc_cacswith_options(calc_cacsreq, runtime)
        return calc_cacsresp

    async def calc_cacsadvance_async(
        self,
        request: imageprocess_20200320_models.CalcCACSAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        calc_cacsreq = imageprocess_20200320_models.CalcCACSRequest()
        OpenApiUtilClient.convert(request, calc_cacsreq)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = calc_cacsreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        calc_cacsresp = await self.calc_cacswith_options_async(calc_cacsreq, runtime)
        return calc_cacsresp

    def classify_fnfwith_options(
        self,
        request: imageprocess_20200320_models.ClassifyFNFRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ClassifyFNF',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.ClassifyFNFResponse(),
            self.call_api(params, req, runtime)
        )

    async def classify_fnfwith_options_async(
        self,
        request: imageprocess_20200320_models.ClassifyFNFRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ClassifyFNF',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.ClassifyFNFResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def classify_fnf(
        self,
        request: imageprocess_20200320_models.ClassifyFNFRequest,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        runtime = util_models.RuntimeOptions()
        return self.classify_fnfwith_options(request, runtime)

    async def classify_fnf_async(
        self,
        request: imageprocess_20200320_models.ClassifyFNFRequest,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        runtime = util_models.RuntimeOptions()
        return await self.classify_fnfwith_options_async(request, runtime)

    def classify_fnfadvance(
        self,
        request: imageprocess_20200320_models.ClassifyFNFAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        classify_fnfreq = imageprocess_20200320_models.ClassifyFNFRequest()
        OpenApiUtilClient.convert(request, classify_fnfreq)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            classify_fnfreq.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        classify_fnfresp = self.classify_fnfwith_options(classify_fnfreq, runtime)
        return classify_fnfresp

    async def classify_fnfadvance_async(
        self,
        request: imageprocess_20200320_models.ClassifyFNFAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        classify_fnfreq = imageprocess_20200320_models.ClassifyFNFRequest()
        OpenApiUtilClient.convert(request, classify_fnfreq)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            classify_fnfreq.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        classify_fnfresp = await self.classify_fnfwith_options_async(classify_fnfreq, runtime)
        return classify_fnfresp

    def detect_covid_19cad_with_options(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectCovid19Cad',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectCovid19CadResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_covid_19cad_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectCovid19Cad',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectCovid19CadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_covid_19cad(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadRequest,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_covid_19cad_with_options(request, runtime)

    async def detect_covid_19cad_async(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadRequest,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_covid_19cad_with_options_async(request, runtime)

    def detect_covid_19cad_advance(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_covid_19cad_req = imageprocess_20200320_models.DetectCovid19CadRequest()
        OpenApiUtilClient.convert(request, detect_covid_19cad_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = detect_covid_19cad_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_covid_19cad_resp = self.detect_covid_19cad_with_options(detect_covid_19cad_req, runtime)
        return detect_covid_19cad_resp

    async def detect_covid_19cad_advance_async(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_covid_19cad_req = imageprocess_20200320_models.DetectCovid19CadRequest()
        OpenApiUtilClient.convert(request, detect_covid_19cad_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = detect_covid_19cad_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_covid_19cad_resp = await self.detect_covid_19cad_with_options_async(detect_covid_19cad_req, runtime)
        return detect_covid_19cad_resp

    def detect_hip_keypoint_xray_with_options(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectHipKeypointXRay',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectHipKeypointXRayResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_hip_keypoint_xray_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectHipKeypointXRay',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectHipKeypointXRayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_hip_keypoint_xray(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayRequest,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_hip_keypoint_xray_with_options(request, runtime)

    async def detect_hip_keypoint_xray_async(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayRequest,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_hip_keypoint_xray_with_options_async(request, runtime)

    def detect_hip_keypoint_xray_advance(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_hip_keypoint_xray_req = imageprocess_20200320_models.DetectHipKeypointXRayRequest()
        OpenApiUtilClient.convert(request, detect_hip_keypoint_xray_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_hip_keypoint_xray_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_hip_keypoint_xray_resp = self.detect_hip_keypoint_xray_with_options(detect_hip_keypoint_xray_req, runtime)
        return detect_hip_keypoint_xray_resp

    async def detect_hip_keypoint_xray_advance_async(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_hip_keypoint_xray_req = imageprocess_20200320_models.DetectHipKeypointXRayRequest()
        OpenApiUtilClient.convert(request, detect_hip_keypoint_xray_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_hip_keypoint_xray_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_hip_keypoint_xray_resp = await self.detect_hip_keypoint_xray_with_options_async(detect_hip_keypoint_xray_req, runtime)
        return detect_hip_keypoint_xray_resp

    def detect_knee_keypoint_xray_with_options(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectKneeKeypointXRay',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectKneeKeypointXRayResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_knee_keypoint_xray_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.tracer_id):
            body['TracerId'] = request.tracer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectKneeKeypointXRay',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectKneeKeypointXRayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_knee_keypoint_xray(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayRequest,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_knee_keypoint_xray_with_options(request, runtime)

    async def detect_knee_keypoint_xray_async(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayRequest,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_knee_keypoint_xray_with_options_async(request, runtime)

    def detect_knee_keypoint_xray_advance(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_knee_keypoint_xray_req = imageprocess_20200320_models.DetectKneeKeypointXRayRequest()
        OpenApiUtilClient.convert(request, detect_knee_keypoint_xray_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_knee_keypoint_xray_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_knee_keypoint_xray_resp = self.detect_knee_keypoint_xray_with_options(detect_knee_keypoint_xray_req, runtime)
        return detect_knee_keypoint_xray_resp

    async def detect_knee_keypoint_xray_advance_async(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_knee_keypoint_xray_req = imageprocess_20200320_models.DetectKneeKeypointXRayRequest()
        OpenApiUtilClient.convert(request, detect_knee_keypoint_xray_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_knee_keypoint_xray_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_knee_keypoint_xray_resp = await self.detect_knee_keypoint_xray_with_options_async(detect_knee_keypoint_xray_req, runtime)
        return detect_knee_keypoint_xray_resp

    def detect_knee_xray_with_options(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectKneeXRay',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectKneeXRayResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_knee_xray_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectKneeXRay',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectKneeXRayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_knee_xray(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayRequest,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_knee_xray_with_options(request, runtime)

    async def detect_knee_xray_async(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayRequest,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_knee_xray_with_options_async(request, runtime)

    def detect_knee_xray_advance(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_knee_xray_req = imageprocess_20200320_models.DetectKneeXRayRequest()
        OpenApiUtilClient.convert(request, detect_knee_xray_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_knee_xray_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_knee_xray_resp = self.detect_knee_xray_with_options(detect_knee_xray_req, runtime)
        return detect_knee_xray_resp

    async def detect_knee_xray_advance_async(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_knee_xray_req = imageprocess_20200320_models.DetectKneeXRayRequest()
        OpenApiUtilClient.convert(request, detect_knee_xray_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_knee_xray_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_knee_xray_resp = await self.detect_knee_xray_with_options_async(detect_knee_xray_req, runtime)
        return detect_knee_xray_resp

    def detect_lung_nodule_with_options(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.threshold):
            body['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectLungNodule',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectLungNoduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_lung_nodule_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.threshold):
            body['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectLungNodule',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectLungNoduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_lung_nodule(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleRequest,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_lung_nodule_with_options(request, runtime)

    async def detect_lung_nodule_async(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleRequest,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_lung_nodule_with_options_async(request, runtime)

    def detect_lung_nodule_advance(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_lung_nodule_req = imageprocess_20200320_models.DetectLungNoduleRequest()
        OpenApiUtilClient.convert(request, detect_lung_nodule_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = detect_lung_nodule_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_lung_nodule_resp = self.detect_lung_nodule_with_options(detect_lung_nodule_req, runtime)
        return detect_lung_nodule_resp

    async def detect_lung_nodule_advance_async(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_lung_nodule_req = imageprocess_20200320_models.DetectLungNoduleRequest()
        OpenApiUtilClient.convert(request, detect_lung_nodule_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = detect_lung_nodule_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_lung_nodule_resp = await self.detect_lung_nodule_with_options_async(detect_lung_nodule_req, runtime)
        return detect_lung_nodule_resp

    def detect_lymph_with_options(
        self,
        request: imageprocess_20200320_models.DetectLymphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLymphResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectLymph',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectLymphResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_lymph_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectLymphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLymphResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectLymph',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectLymphResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_lymph(
        self,
        request: imageprocess_20200320_models.DetectLymphRequest,
    ) -> imageprocess_20200320_models.DetectLymphResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_lymph_with_options(request, runtime)

    async def detect_lymph_async(
        self,
        request: imageprocess_20200320_models.DetectLymphRequest,
    ) -> imageprocess_20200320_models.DetectLymphResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_lymph_with_options_async(request, runtime)

    def detect_lymph_advance(
        self,
        request: imageprocess_20200320_models.DetectLymphAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLymphResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_lymph_req = imageprocess_20200320_models.DetectLymphRequest()
        OpenApiUtilClient.convert(request, detect_lymph_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = detect_lymph_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_lymph_resp = self.detect_lymph_with_options(detect_lymph_req, runtime)
        return detect_lymph_resp

    async def detect_lymph_advance_async(
        self,
        request: imageprocess_20200320_models.DetectLymphAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLymphResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_lymph_req = imageprocess_20200320_models.DetectLymphRequest()
        OpenApiUtilClient.convert(request, detect_lymph_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = detect_lymph_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_lymph_resp = await self.detect_lymph_with_options_async(detect_lymph_req, runtime)
        return detect_lymph_resp

    def detect_panc_with_options(
        self,
        request: imageprocess_20200320_models.DetectPancRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectPancResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectPanc',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectPancResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_panc_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectPancRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectPancResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectPanc',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectPancResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_panc(
        self,
        request: imageprocess_20200320_models.DetectPancRequest,
    ) -> imageprocess_20200320_models.DetectPancResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_panc_with_options(request, runtime)

    async def detect_panc_async(
        self,
        request: imageprocess_20200320_models.DetectPancRequest,
    ) -> imageprocess_20200320_models.DetectPancResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_panc_with_options_async(request, runtime)

    def detect_panc_advance(
        self,
        request: imageprocess_20200320_models.DetectPancAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectPancResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_panc_req = imageprocess_20200320_models.DetectPancRequest()
        OpenApiUtilClient.convert(request, detect_panc_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = detect_panc_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_panc_resp = self.detect_panc_with_options(detect_panc_req, runtime)
        return detect_panc_resp

    async def detect_panc_advance_async(
        self,
        request: imageprocess_20200320_models.DetectPancAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectPancResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_panc_req = imageprocess_20200320_models.DetectPancRequest()
        OpenApiUtilClient.convert(request, detect_panc_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = detect_panc_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_panc_resp = await self.detect_panc_with_options_async(detect_panc_req, runtime)
        return detect_panc_resp

    def detect_rib_fracture_with_options(
        self,
        request: imageprocess_20200320_models.DetectRibFractureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectRibFractureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectRibFracture',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectRibFractureResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_rib_fracture_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectRibFractureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectRibFractureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectRibFracture',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectRibFractureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_rib_fracture(
        self,
        request: imageprocess_20200320_models.DetectRibFractureRequest,
    ) -> imageprocess_20200320_models.DetectRibFractureResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_rib_fracture_with_options(request, runtime)

    async def detect_rib_fracture_async(
        self,
        request: imageprocess_20200320_models.DetectRibFractureRequest,
    ) -> imageprocess_20200320_models.DetectRibFractureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_rib_fracture_with_options_async(request, runtime)

    def detect_rib_fracture_advance(
        self,
        request: imageprocess_20200320_models.DetectRibFractureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectRibFractureResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_rib_fracture_req = imageprocess_20200320_models.DetectRibFractureRequest()
        OpenApiUtilClient.convert(request, detect_rib_fracture_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = detect_rib_fracture_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_rib_fracture_resp = self.detect_rib_fracture_with_options(detect_rib_fracture_req, runtime)
        return detect_rib_fracture_resp

    async def detect_rib_fracture_advance_async(
        self,
        request: imageprocess_20200320_models.DetectRibFractureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectRibFractureResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_rib_fracture_req = imageprocess_20200320_models.DetectRibFractureRequest()
        OpenApiUtilClient.convert(request, detect_rib_fracture_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = detect_rib_fracture_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_rib_fracture_resp = await self.detect_rib_fracture_with_options_async(detect_rib_fracture_req, runtime)
        return detect_rib_fracture_resp

    def detect_skin_disease_with_options(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectSkinDisease',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectSkinDiseaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_skin_disease_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectSkinDisease',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectSkinDiseaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_skin_disease(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseRequest,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_skin_disease_with_options(request, runtime)

    async def detect_skin_disease_async(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseRequest,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_skin_disease_with_options_async(request, runtime)

    def detect_skin_disease_advance(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_skin_disease_req = imageprocess_20200320_models.DetectSkinDiseaseRequest()
        OpenApiUtilClient.convert(request, detect_skin_disease_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_skin_disease_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_skin_disease_resp = self.detect_skin_disease_with_options(detect_skin_disease_req, runtime)
        return detect_skin_disease_resp

    async def detect_skin_disease_advance_async(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_skin_disease_req = imageprocess_20200320_models.DetectSkinDiseaseRequest()
        OpenApiUtilClient.convert(request, detect_skin_disease_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_skin_disease_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_skin_disease_resp = await self.detect_skin_disease_with_options_async(detect_skin_disease_req, runtime)
        return detect_skin_disease_resp

    def detect_spine_mriwith_options(
        self,
        request: imageprocess_20200320_models.DetectSpineMRIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSpineMRIResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectSpineMRI',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectSpineMRIResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_spine_mriwith_options_async(
        self,
        request: imageprocess_20200320_models.DetectSpineMRIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSpineMRIResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectSpineMRI',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectSpineMRIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_spine_mri(
        self,
        request: imageprocess_20200320_models.DetectSpineMRIRequest,
    ) -> imageprocess_20200320_models.DetectSpineMRIResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_spine_mriwith_options(request, runtime)

    async def detect_spine_mri_async(
        self,
        request: imageprocess_20200320_models.DetectSpineMRIRequest,
    ) -> imageprocess_20200320_models.DetectSpineMRIResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_spine_mriwith_options_async(request, runtime)

    def detect_spine_mriadvance(
        self,
        request: imageprocess_20200320_models.DetectSpineMRIAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSpineMRIResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_spine_mrireq = imageprocess_20200320_models.DetectSpineMRIRequest()
        OpenApiUtilClient.convert(request, detect_spine_mrireq)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = detect_spine_mrireq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_spine_mriresp = self.detect_spine_mriwith_options(detect_spine_mrireq, runtime)
        return detect_spine_mriresp

    async def detect_spine_mriadvance_async(
        self,
        request: imageprocess_20200320_models.DetectSpineMRIAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSpineMRIResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_spine_mrireq = imageprocess_20200320_models.DetectSpineMRIRequest()
        OpenApiUtilClient.convert(request, detect_spine_mrireq)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = detect_spine_mrireq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_spine_mriresp = await self.detect_spine_mriwith_options_async(detect_spine_mrireq, runtime)
        return detect_spine_mriresp

    def feedback_session_with_options(
        self,
        request: imageprocess_20200320_models.FeedbackSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.FeedbackSessionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feedback):
            body['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FeedbackSession',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.FeedbackSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def feedback_session_with_options_async(
        self,
        request: imageprocess_20200320_models.FeedbackSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.FeedbackSessionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feedback):
            body['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FeedbackSession',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.FeedbackSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def feedback_session(
        self,
        request: imageprocess_20200320_models.FeedbackSessionRequest,
    ) -> imageprocess_20200320_models.FeedbackSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.feedback_session_with_options(request, runtime)

    async def feedback_session_async(
        self,
        request: imageprocess_20200320_models.FeedbackSessionRequest,
    ) -> imageprocess_20200320_models.FeedbackSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.feedback_session_with_options_async(request, runtime)

    def get_async_job_result_with_options(
        self,
        request: imageprocess_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncJobResult',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.GetAsyncJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: imageprocess_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncJobResult',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.GetAsyncJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_job_result(
        self,
        request: imageprocess_20200320_models.GetAsyncJobResultRequest,
    ) -> imageprocess_20200320_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: imageprocess_20200320_models.GetAsyncJobResultRequest,
    ) -> imageprocess_20200320_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def run_ctregistration_with_options(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.floating_list):
            body['FloatingList'] = request.floating_list
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.reference_list):
            body['ReferenceList'] = request.reference_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCTRegistration',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.RunCTRegistrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_ctregistration_with_options_async(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.floating_list):
            body['FloatingList'] = request.floating_list
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.reference_list):
            body['ReferenceList'] = request.reference_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCTRegistration',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.RunCTRegistrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_ctregistration(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationRequest,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_ctregistration_with_options(request, runtime)

    async def run_ctregistration_async(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationRequest,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_ctregistration_with_options_async(request, runtime)

    def run_ctregistration_advance(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        run_ctregistration_req = imageprocess_20200320_models.RunCTRegistrationRequest()
        OpenApiUtilClient.convert(request, run_ctregistration_req)
        if not UtilClient.is_unset(request.floating_list):
            i_0 = 0
            for item_0 in request.floating_list:
                if not UtilClient.is_unset(item_0.floating_urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.floating_urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = run_ctregistration_req.floating_list[i_0]
                    tmp.floating_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        if not UtilClient.is_unset(request.reference_list):
            i_1 = 0
            for item_0 in request.reference_list:
                if not UtilClient.is_unset(item_0.reference_urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.reference_urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = run_ctregistration_req.reference_list[i_1]
                    tmp.reference_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_1 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_1), NumberClient.itol(1)))
        run_ctregistration_resp = self.run_ctregistration_with_options(run_ctregistration_req, runtime)
        return run_ctregistration_resp

    async def run_ctregistration_advance_async(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        run_ctregistration_req = imageprocess_20200320_models.RunCTRegistrationRequest()
        OpenApiUtilClient.convert(request, run_ctregistration_req)
        if not UtilClient.is_unset(request.floating_list):
            i_0 = 0
            for item_0 in request.floating_list:
                if not UtilClient.is_unset(item_0.floating_urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.floating_urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = run_ctregistration_req.floating_list[i_0]
                    tmp.floating_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        if not UtilClient.is_unset(request.reference_list):
            i_1 = 0
            for item_0 in request.reference_list:
                if not UtilClient.is_unset(item_0.reference_urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.reference_urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = run_ctregistration_req.reference_list[i_1]
                    tmp.reference_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_1 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_1), NumberClient.itol(1)))
        run_ctregistration_resp = await self.run_ctregistration_with_options_async(run_ctregistration_req, runtime)
        return run_ctregistration_resp

    def run_med_qawith_options(
        self,
        request: imageprocess_20200320_models.RunMedQARequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunMedQAResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.answer_image_data_list):
            body['AnswerImageDataList'] = request.answer_image_data_list
        if not UtilClient.is_unset(request.answer_image_urllist):
            body['AnswerImageURLList'] = request.answer_image_urllist
        if not UtilClient.is_unset(request.answer_text_list):
            body['AnswerTextList'] = request.answer_text_list
        if not UtilClient.is_unset(request.department):
            body['Department'] = request.department
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.question_type):
            body['QuestionType'] = request.question_type
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunMedQA',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.RunMedQAResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_med_qawith_options_async(
        self,
        request: imageprocess_20200320_models.RunMedQARequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunMedQAResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.answer_image_data_list):
            body['AnswerImageDataList'] = request.answer_image_data_list
        if not UtilClient.is_unset(request.answer_image_urllist):
            body['AnswerImageURLList'] = request.answer_image_urllist
        if not UtilClient.is_unset(request.answer_text_list):
            body['AnswerTextList'] = request.answer_text_list
        if not UtilClient.is_unset(request.department):
            body['Department'] = request.department
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.question_type):
            body['QuestionType'] = request.question_type
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunMedQA',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.RunMedQAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_med_qa(
        self,
        request: imageprocess_20200320_models.RunMedQARequest,
    ) -> imageprocess_20200320_models.RunMedQAResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_med_qawith_options(request, runtime)

    async def run_med_qa_async(
        self,
        request: imageprocess_20200320_models.RunMedQARequest,
    ) -> imageprocess_20200320_models.RunMedQAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_med_qawith_options_async(request, runtime)

    def run_med_qaadvance(
        self,
        request: imageprocess_20200320_models.RunMedQAAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunMedQAResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        run_med_qareq = imageprocess_20200320_models.RunMedQARequest()
        OpenApiUtilClient.convert(request, run_med_qareq)
        if not UtilClient.is_unset(request.answer_image_urllist):
            i_0 = 0
            for item_0 in request.answer_image_urllist:
                if not UtilClient.is_unset(item_0.answer_image_urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.answer_image_urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = run_med_qareq.answer_image_urllist[i_0]
                    tmp.answer_image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        run_med_qaresp = self.run_med_qawith_options(run_med_qareq, runtime)
        return run_med_qaresp

    async def run_med_qaadvance_async(
        self,
        request: imageprocess_20200320_models.RunMedQAAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunMedQAResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        run_med_qareq = imageprocess_20200320_models.RunMedQARequest()
        OpenApiUtilClient.convert(request, run_med_qareq)
        if not UtilClient.is_unset(request.answer_image_urllist):
            i_0 = 0
            for item_0 in request.answer_image_urllist:
                if not UtilClient.is_unset(item_0.answer_image_urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.answer_image_urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = run_med_qareq.answer_image_urllist[i_0]
                    tmp.answer_image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        run_med_qaresp = await self.run_med_qawith_options_async(run_med_qareq, runtime)
        return run_med_qaresp

    def screen_chest_ctwith_options(
        self,
        request: imageprocess_20200320_models.ScreenChestCTRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.mask):
            body['Mask'] = request.mask
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        if not UtilClient.is_unset(request.verbose):
            body['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScreenChestCT',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.ScreenChestCTResponse(),
            self.call_api(params, req, runtime)
        )

    async def screen_chest_ctwith_options_async(
        self,
        request: imageprocess_20200320_models.ScreenChestCTRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.mask):
            body['Mask'] = request.mask
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        if not UtilClient.is_unset(request.verbose):
            body['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScreenChestCT',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.ScreenChestCTResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def screen_chest_ct(
        self,
        request: imageprocess_20200320_models.ScreenChestCTRequest,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        runtime = util_models.RuntimeOptions()
        return self.screen_chest_ctwith_options(request, runtime)

    async def screen_chest_ct_async(
        self,
        request: imageprocess_20200320_models.ScreenChestCTRequest,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        runtime = util_models.RuntimeOptions()
        return await self.screen_chest_ctwith_options_async(request, runtime)

    def screen_chest_ctadvance(
        self,
        request: imageprocess_20200320_models.ScreenChestCTAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        screen_chest_ctreq = imageprocess_20200320_models.ScreenChestCTRequest()
        OpenApiUtilClient.convert(request, screen_chest_ctreq)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = screen_chest_ctreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        screen_chest_ctresp = self.screen_chest_ctwith_options(screen_chest_ctreq, runtime)
        return screen_chest_ctresp

    async def screen_chest_ctadvance_async(
        self,
        request: imageprocess_20200320_models.ScreenChestCTAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        screen_chest_ctreq = imageprocess_20200320_models.ScreenChestCTRequest()
        OpenApiUtilClient.convert(request, screen_chest_ctreq)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = screen_chest_ctreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        screen_chest_ctresp = await self.screen_chest_ctwith_options_async(screen_chest_ctreq, runtime)
        return screen_chest_ctresp

    def screen_ecwith_options(
        self,
        request: imageprocess_20200320_models.ScreenECRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenECResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScreenEC',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.ScreenECResponse(),
            self.call_api(params, req, runtime)
        )

    async def screen_ecwith_options_async(
        self,
        request: imageprocess_20200320_models.ScreenECRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenECResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScreenEC',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.ScreenECResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def screen_ec(
        self,
        request: imageprocess_20200320_models.ScreenECRequest,
    ) -> imageprocess_20200320_models.ScreenECResponse:
        runtime = util_models.RuntimeOptions()
        return self.screen_ecwith_options(request, runtime)

    async def screen_ec_async(
        self,
        request: imageprocess_20200320_models.ScreenECRequest,
    ) -> imageprocess_20200320_models.ScreenECResponse:
        runtime = util_models.RuntimeOptions()
        return await self.screen_ecwith_options_async(request, runtime)

    def segment_oarwith_options(
        self,
        request: imageprocess_20200320_models.SegmentOARRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.SegmentOARResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body_part):
            body['BodyPart'] = request.body_part
        if not UtilClient.is_unset(request.contrast):
            body['Contrast'] = request.contrast
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.mask_list):
            body['MaskList'] = request.mask_list
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SegmentOAR',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.SegmentOARResponse(),
            self.call_api(params, req, runtime)
        )

    async def segment_oarwith_options_async(
        self,
        request: imageprocess_20200320_models.SegmentOARRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.SegmentOARResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body_part):
            body['BodyPart'] = request.body_part
        if not UtilClient.is_unset(request.contrast):
            body['Contrast'] = request.contrast
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.mask_list):
            body['MaskList'] = request.mask_list
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SegmentOAR',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.SegmentOARResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def segment_oar(
        self,
        request: imageprocess_20200320_models.SegmentOARRequest,
    ) -> imageprocess_20200320_models.SegmentOARResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_oarwith_options(request, runtime)

    async def segment_oar_async(
        self,
        request: imageprocess_20200320_models.SegmentOARRequest,
    ) -> imageprocess_20200320_models.SegmentOARResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_oarwith_options_async(request, runtime)

    def segment_oaradvance(
        self,
        request: imageprocess_20200320_models.SegmentOARAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.SegmentOARResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        segment_oarreq = imageprocess_20200320_models.SegmentOARRequest()
        OpenApiUtilClient.convert(request, segment_oarreq)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = segment_oarreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        segment_oarresp = self.segment_oarwith_options(segment_oarreq, runtime)
        return segment_oarresp

    async def segment_oaradvance_async(
        self,
        request: imageprocess_20200320_models.SegmentOARAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.SegmentOARResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        segment_oarreq = imageprocess_20200320_models.SegmentOARRequest()
        OpenApiUtilClient.convert(request, segment_oarreq)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = segment_oarreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        segment_oarresp = await self.segment_oarwith_options_async(segment_oarreq, runtime)
        return segment_oarresp

    def target_volume_segment_with_options(
        self,
        request: imageprocess_20200320_models.TargetVolumeSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.TargetVolumeSegmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cancer_type):
            body['CancerType'] = request.cancer_type
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.target_volume_type):
            body['TargetVolumeType'] = request.target_volume_type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TargetVolumeSegment',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.TargetVolumeSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def target_volume_segment_with_options_async(
        self,
        request: imageprocess_20200320_models.TargetVolumeSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.TargetVolumeSegmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cancer_type):
            body['CancerType'] = request.cancer_type
        if not UtilClient.is_unset(request.data_format):
            body['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.org_name):
            body['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.target_volume_type):
            body['TargetVolumeType'] = request.target_volume_type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TargetVolumeSegment',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.TargetVolumeSegmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def target_volume_segment(
        self,
        request: imageprocess_20200320_models.TargetVolumeSegmentRequest,
    ) -> imageprocess_20200320_models.TargetVolumeSegmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.target_volume_segment_with_options(request, runtime)

    async def target_volume_segment_async(
        self,
        request: imageprocess_20200320_models.TargetVolumeSegmentRequest,
    ) -> imageprocess_20200320_models.TargetVolumeSegmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.target_volume_segment_with_options_async(request, runtime)

    def target_volume_segment_advance(
        self,
        request: imageprocess_20200320_models.TargetVolumeSegmentAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.TargetVolumeSegmentResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        target_volume_segment_req = imageprocess_20200320_models.TargetVolumeSegmentRequest()
        OpenApiUtilClient.convert(request, target_volume_segment_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    oss_client.post_object(upload_request, oss_runtime)
                    tmp = target_volume_segment_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        target_volume_segment_resp = self.target_volume_segment_with_options(target_volume_segment_req, runtime)
        return target_volume_segment_resp

    async def target_volume_segment_advance_async(
        self,
        request: imageprocess_20200320_models.TargetVolumeSegmentAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.TargetVolumeSegmentResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        target_volume_segment_req = imageprocess_20200320_models.TargetVolumeSegmentRequest()
        OpenApiUtilClient.convert(request, target_volume_segment_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
                        content_type=''
                    )
                    oss_header = oss_models.PostObjectRequestHeader(
                        access_key_id=auth_response.body.access_key_id,
                        policy=auth_response.body.encoded_policy,
                        signature=auth_response.body.signature,
                        key=auth_response.body.object_key,
                        file=file_obj,
                        success_action_status='201'
                    )
                    upload_request = oss_models.PostObjectRequest(
                        bucket_name=auth_response.body.bucket,
                        header=oss_header
                    )
                    await oss_client.post_object_async(upload_request, oss_runtime)
                    tmp = target_volume_segment_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        target_volume_segment_resp = await self.target_volume_segment_with_options_async(target_volume_segment_req, runtime)
        return target_volume_segment_resp

    def translate_med_with_options(
        self,
        request: imageprocess_20200320_models.TranslateMedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.TranslateMedResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_language):
            body['FromLanguage'] = request.from_language
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.to_language):
            body['ToLanguage'] = request.to_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateMed',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.TranslateMedResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_med_with_options_async(
        self,
        request: imageprocess_20200320_models.TranslateMedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.TranslateMedResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_language):
            body['FromLanguage'] = request.from_language
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.to_language):
            body['ToLanguage'] = request.to_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TranslateMed',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.TranslateMedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_med(
        self,
        request: imageprocess_20200320_models.TranslateMedRequest,
    ) -> imageprocess_20200320_models.TranslateMedResponse:
        runtime = util_models.RuntimeOptions()
        return self.translate_med_with_options(request, runtime)

    async def translate_med_async(
        self,
        request: imageprocess_20200320_models.TranslateMedRequest,
    ) -> imageprocess_20200320_models.TranslateMedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.translate_med_with_options_async(request, runtime)
