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
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
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
        """
        @summary 主动脉瘤肺动脉高压检测
        
        @param request: AnalyzeChestVesselRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnalyzeChestVesselResponse
        """
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
        """
        @summary 主动脉瘤肺动脉高压检测
        
        @param request: AnalyzeChestVesselRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnalyzeChestVesselResponse
        """
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
        """
        @summary 主动脉瘤肺动脉高压检测
        
        @param request: AnalyzeChestVesselRequest
        @return: AnalyzeChestVesselResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.analyze_chest_vessel_with_options(request, runtime)

    async def analyze_chest_vessel_async(
        self,
        request: imageprocess_20200320_models.AnalyzeChestVesselRequest,
    ) -> imageprocess_20200320_models.AnalyzeChestVesselResponse:
        """
        @summary 主动脉瘤肺动脉高压检测
        
        @param request: AnalyzeChestVesselRequest
        @return: AnalyzeChestVesselResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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

    def calc_bmdwith_options(
        self,
        request: imageprocess_20200320_models.CalcBMDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.CalcBMDResponse:
        """
        @summary 骨密度估计
        
        @param request: CalcBMDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CalcBMDResponse
        """
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
            action='CalcBMD',
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
            imageprocess_20200320_models.CalcBMDResponse(),
            self.call_api(params, req, runtime)
        )

    async def calc_bmdwith_options_async(
        self,
        request: imageprocess_20200320_models.CalcBMDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.CalcBMDResponse:
        """
        @summary 骨密度估计
        
        @param request: CalcBMDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CalcBMDResponse
        """
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
            action='CalcBMD',
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
            imageprocess_20200320_models.CalcBMDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def calc_bmd(
        self,
        request: imageprocess_20200320_models.CalcBMDRequest,
    ) -> imageprocess_20200320_models.CalcBMDResponse:
        """
        @summary 骨密度估计
        
        @param request: CalcBMDRequest
        @return: CalcBMDResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.calc_bmdwith_options(request, runtime)

    async def calc_bmd_async(
        self,
        request: imageprocess_20200320_models.CalcBMDRequest,
    ) -> imageprocess_20200320_models.CalcBMDResponse:
        """
        @summary 骨密度估计
        
        @param request: CalcBMDRequest
        @return: CalcBMDResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.calc_bmdwith_options_async(request, runtime)

    def calc_bmdadvance(
        self,
        request: imageprocess_20200320_models.CalcBMDAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.CalcBMDResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        calc_bmdreq = imageprocess_20200320_models.CalcBMDRequest()
        OpenApiUtilClient.convert(request, calc_bmdreq)
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
                    tmp = calc_bmdreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        calc_bmdresp = self.calc_bmdwith_options(calc_bmdreq, runtime)
        return calc_bmdresp

    async def calc_bmdadvance_async(
        self,
        request: imageprocess_20200320_models.CalcBMDAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.CalcBMDResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        calc_bmdreq = imageprocess_20200320_models.CalcBMDRequest()
        OpenApiUtilClient.convert(request, calc_bmdreq)
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
                    tmp = calc_bmdreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        calc_bmdresp = await self.calc_bmdwith_options_async(calc_bmdreq, runtime)
        return calc_bmdresp

    def calc_cacswith_options(
        self,
        request: imageprocess_20200320_models.CalcCACSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        """
        @param request: CalcCACSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CalcCACSResponse
        """
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
        """
        @param request: CalcCACSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CalcCACSResponse
        """
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
        """
        @param request: CalcCACSRequest
        @return: CalcCACSResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.calc_cacswith_options(request, runtime)

    async def calc_cacs_async(
        self,
        request: imageprocess_20200320_models.CalcCACSRequest,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        """
        @param request: CalcCACSRequest
        @return: CalcCACSResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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

    def detect_covid_19cad_with_options(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        """
        @param request: DetectCovid19CadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectCovid19CadResponse
        """
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
        """
        @param request: DetectCovid19CadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectCovid19CadResponse
        """
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
        """
        @param request: DetectCovid19CadRequest
        @return: DetectCovid19CadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_covid_19cad_with_options(request, runtime)

    async def detect_covid_19cad_async(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadRequest,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        """
        @param request: DetectCovid19CadRequest
        @return: DetectCovid19CadResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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

    def detect_liver_steatosis_with_options(
        self,
        request: imageprocess_20200320_models.DetectLiverSteatosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLiverSteatosisResponse:
        """
        @summary 脂肪肝检测
        
        @param request: DetectLiverSteatosisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectLiverSteatosisResponse
        """
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
            action='DetectLiverSteatosis',
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
            imageprocess_20200320_models.DetectLiverSteatosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_liver_steatosis_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectLiverSteatosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLiverSteatosisResponse:
        """
        @summary 脂肪肝检测
        
        @param request: DetectLiverSteatosisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectLiverSteatosisResponse
        """
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
            action='DetectLiverSteatosis',
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
            imageprocess_20200320_models.DetectLiverSteatosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_liver_steatosis(
        self,
        request: imageprocess_20200320_models.DetectLiverSteatosisRequest,
    ) -> imageprocess_20200320_models.DetectLiverSteatosisResponse:
        """
        @summary 脂肪肝检测
        
        @param request: DetectLiverSteatosisRequest
        @return: DetectLiverSteatosisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_liver_steatosis_with_options(request, runtime)

    async def detect_liver_steatosis_async(
        self,
        request: imageprocess_20200320_models.DetectLiverSteatosisRequest,
    ) -> imageprocess_20200320_models.DetectLiverSteatosisResponse:
        """
        @summary 脂肪肝检测
        
        @param request: DetectLiverSteatosisRequest
        @return: DetectLiverSteatosisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_liver_steatosis_with_options_async(request, runtime)

    def detect_liver_steatosis_advance(
        self,
        request: imageprocess_20200320_models.DetectLiverSteatosisAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLiverSteatosisResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_liver_steatosis_req = imageprocess_20200320_models.DetectLiverSteatosisRequest()
        OpenApiUtilClient.convert(request, detect_liver_steatosis_req)
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
                    tmp = detect_liver_steatosis_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_liver_steatosis_resp = self.detect_liver_steatosis_with_options(detect_liver_steatosis_req, runtime)
        return detect_liver_steatosis_resp

    async def detect_liver_steatosis_advance_async(
        self,
        request: imageprocess_20200320_models.DetectLiverSteatosisAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLiverSteatosisResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        detect_liver_steatosis_req = imageprocess_20200320_models.DetectLiverSteatosisRequest()
        OpenApiUtilClient.convert(request, detect_liver_steatosis_req)
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
                    tmp = detect_liver_steatosis_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_liver_steatosis_resp = await self.detect_liver_steatosis_with_options_async(detect_liver_steatosis_req, runtime)
        return detect_liver_steatosis_resp

    def detect_lung_nodule_with_options(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        """
        @param request: DetectLungNoduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectLungNoduleResponse
        """
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
        """
        @param request: DetectLungNoduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectLungNoduleResponse
        """
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
        """
        @param request: DetectLungNoduleRequest
        @return: DetectLungNoduleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_lung_nodule_with_options(request, runtime)

    async def detect_lung_nodule_async(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleRequest,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        """
        @param request: DetectLungNoduleRequest
        @return: DetectLungNoduleResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        """
        @summary 淋巴结检测
        
        @param request: DetectLymphRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectLymphResponse
        """
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
        """
        @summary 淋巴结检测
        
        @param request: DetectLymphRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectLymphResponse
        """
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
        """
        @summary 淋巴结检测
        
        @param request: DetectLymphRequest
        @return: DetectLymphResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_lymph_with_options(request, runtime)

    async def detect_lymph_async(
        self,
        request: imageprocess_20200320_models.DetectLymphRequest,
    ) -> imageprocess_20200320_models.DetectLymphResponse:
        """
        @summary 淋巴结检测
        
        @param request: DetectLymphRequest
        @return: DetectLymphResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        """
        @summary 胰腺癌检测
        
        @param request: DetectPancRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectPancResponse
        """
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
        """
        @summary 胰腺癌检测
        
        @param request: DetectPancRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectPancResponse
        """
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
        """
        @summary 胰腺癌检测
        
        @param request: DetectPancRequest
        @return: DetectPancResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_panc_with_options(request, runtime)

    async def detect_panc_async(
        self,
        request: imageprocess_20200320_models.DetectPancRequest,
    ) -> imageprocess_20200320_models.DetectPancResponse:
        """
        @summary 胰腺癌检测
        
        @param request: DetectPancRequest
        @return: DetectPancResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        """
        @param request: DetectRibFractureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectRibFractureResponse
        """
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
        """
        @param request: DetectRibFractureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectRibFractureResponse
        """
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
        """
        @param request: DetectRibFractureRequest
        @return: DetectRibFractureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_rib_fracture_with_options(request, runtime)

    async def detect_rib_fracture_async(
        self,
        request: imageprocess_20200320_models.DetectRibFractureRequest,
    ) -> imageprocess_20200320_models.DetectRibFractureResponse:
        """
        @param request: DetectRibFractureRequest
        @return: DetectRibFractureResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        """
        @param request: DetectSkinDiseaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectSkinDiseaseResponse
        """
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
        """
        @param request: DetectSkinDiseaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectSkinDiseaseResponse
        """
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
        """
        @param request: DetectSkinDiseaseRequest
        @return: DetectSkinDiseaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_skin_disease_with_options(request, runtime)

    async def detect_skin_disease_async(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseRequest,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        """
        @param request: DetectSkinDiseaseRequest
        @return: DetectSkinDiseaseResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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

    def feedback_session_with_options(
        self,
        request: imageprocess_20200320_models.FeedbackSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.FeedbackSessionResponse:
        """
        @summary 会话反馈
        
        @param request: FeedbackSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FeedbackSessionResponse
        """
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
        """
        @summary 会话反馈
        
        @param request: FeedbackSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FeedbackSessionResponse
        """
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
        """
        @summary 会话反馈
        
        @param request: FeedbackSessionRequest
        @return: FeedbackSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.feedback_session_with_options(request, runtime)

    async def feedback_session_async(
        self,
        request: imageprocess_20200320_models.FeedbackSessionRequest,
    ) -> imageprocess_20200320_models.FeedbackSessionResponse:
        """
        @summary 会话反馈
        
        @param request: FeedbackSessionRequest
        @return: FeedbackSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.feedback_session_with_options_async(request, runtime)

    def generate_report_with_options(
        self,
        tmp_req: imageprocess_20200320_models.GenerateReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.GenerateReportResponse:
        """
        @summary 胸部CT平扫筛查结果报告生成
        
        @param tmp_req: GenerateReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateReportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imageprocess_20200320_models.GenerateReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.report_configs):
            request.report_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.report_configs, 'ReportConfigs', 'json')
        body = {}
        if not UtilClient.is_unset(request.report_configs_shrink):
            body['ReportConfigs'] = request.report_configs_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateReport',
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
            imageprocess_20200320_models.GenerateReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_report_with_options_async(
        self,
        tmp_req: imageprocess_20200320_models.GenerateReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.GenerateReportResponse:
        """
        @summary 胸部CT平扫筛查结果报告生成
        
        @param tmp_req: GenerateReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateReportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imageprocess_20200320_models.GenerateReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.report_configs):
            request.report_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.report_configs, 'ReportConfigs', 'json')
        body = {}
        if not UtilClient.is_unset(request.report_configs_shrink):
            body['ReportConfigs'] = request.report_configs_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateReport',
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
            imageprocess_20200320_models.GenerateReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_report(
        self,
        request: imageprocess_20200320_models.GenerateReportRequest,
    ) -> imageprocess_20200320_models.GenerateReportResponse:
        """
        @summary 胸部CT平扫筛查结果报告生成
        
        @param request: GenerateReportRequest
        @return: GenerateReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_report_with_options(request, runtime)

    async def generate_report_async(
        self,
        request: imageprocess_20200320_models.GenerateReportRequest,
    ) -> imageprocess_20200320_models.GenerateReportResponse:
        """
        @summary 胸部CT平扫筛查结果报告生成
        
        @param request: GenerateReportRequest
        @return: GenerateReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_report_with_options_async(request, runtime)

    def get_async_job_result_with_options(
        self,
        request: imageprocess_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.GetAsyncJobResultResponse:
        """
        @param request: GetAsyncJobResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncJobResultResponse
        """
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
        """
        @param request: GetAsyncJobResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncJobResultResponse
        """
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
        """
        @param request: GetAsyncJobResultRequest
        @return: GetAsyncJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: imageprocess_20200320_models.GetAsyncJobResultRequest,
    ) -> imageprocess_20200320_models.GetAsyncJobResultResponse:
        """
        @param request: GetAsyncJobResultRequest
        @return: GetAsyncJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def predict_cvdwith_options(
        self,
        request: imageprocess_20200320_models.PredictCVDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.PredictCVDResponse:
        """
        @summary CVD心血管不良事件预测
        
        @param request: PredictCVDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PredictCVDResponse
        """
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
            action='PredictCVD',
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
            imageprocess_20200320_models.PredictCVDResponse(),
            self.call_api(params, req, runtime)
        )

    async def predict_cvdwith_options_async(
        self,
        request: imageprocess_20200320_models.PredictCVDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.PredictCVDResponse:
        """
        @summary CVD心血管不良事件预测
        
        @param request: PredictCVDRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PredictCVDResponse
        """
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
            action='PredictCVD',
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
            imageprocess_20200320_models.PredictCVDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def predict_cvd(
        self,
        request: imageprocess_20200320_models.PredictCVDRequest,
    ) -> imageprocess_20200320_models.PredictCVDResponse:
        """
        @summary CVD心血管不良事件预测
        
        @param request: PredictCVDRequest
        @return: PredictCVDResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.predict_cvdwith_options(request, runtime)

    async def predict_cvd_async(
        self,
        request: imageprocess_20200320_models.PredictCVDRequest,
    ) -> imageprocess_20200320_models.PredictCVDResponse:
        """
        @summary CVD心血管不良事件预测
        
        @param request: PredictCVDRequest
        @return: PredictCVDResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.predict_cvdwith_options_async(request, runtime)

    def predict_cvdadvance(
        self,
        request: imageprocess_20200320_models.PredictCVDAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.PredictCVDResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        predict_cvdreq = imageprocess_20200320_models.PredictCVDRequest()
        OpenApiUtilClient.convert(request, predict_cvdreq)
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
                    tmp = predict_cvdreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        predict_cvdresp = self.predict_cvdwith_options(predict_cvdreq, runtime)
        return predict_cvdresp

    async def predict_cvdadvance_async(
        self,
        request: imageprocess_20200320_models.PredictCVDAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.PredictCVDResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        predict_cvdreq = imageprocess_20200320_models.PredictCVDRequest()
        OpenApiUtilClient.convert(request, predict_cvdreq)
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
                    tmp = predict_cvdreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        predict_cvdresp = await self.predict_cvdwith_options_async(predict_cvdreq, runtime)
        return predict_cvdresp

    def run_ctregistration_with_options(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        """
        @param request: RunCTRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCTRegistrationResponse
        """
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
        """
        @param request: RunCTRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCTRegistrationResponse
        """
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
        """
        @param request: RunCTRegistrationRequest
        @return: RunCTRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_ctregistration_with_options(request, runtime)

    async def run_ctregistration_async(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationRequest,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        """
        @param request: RunCTRegistrationRequest
        @return: RunCTRegistrationResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        """
        @param request: RunMedQARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunMedQAResponse
        """
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
        """
        @param request: RunMedQARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunMedQAResponse
        """
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
        """
        @param request: RunMedQARequest
        @return: RunMedQAResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_med_qawith_options(request, runtime)

    async def run_med_qa_async(
        self,
        request: imageprocess_20200320_models.RunMedQARequest,
    ) -> imageprocess_20200320_models.RunMedQAResponse:
        """
        @param request: RunMedQARequest
        @return: RunMedQAResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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

    def screen_crcwith_options(
        self,
        request: imageprocess_20200320_models.ScreenCRCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenCRCResponse:
        """
        @summary 结直肠癌筛查
        
        @param request: ScreenCRCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScreenCRCResponse
        """
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
            action='ScreenCRC',
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
            imageprocess_20200320_models.ScreenCRCResponse(),
            self.call_api(params, req, runtime)
        )

    async def screen_crcwith_options_async(
        self,
        request: imageprocess_20200320_models.ScreenCRCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenCRCResponse:
        """
        @summary 结直肠癌筛查
        
        @param request: ScreenCRCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScreenCRCResponse
        """
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
            action='ScreenCRC',
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
            imageprocess_20200320_models.ScreenCRCResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def screen_crc(
        self,
        request: imageprocess_20200320_models.ScreenCRCRequest,
    ) -> imageprocess_20200320_models.ScreenCRCResponse:
        """
        @summary 结直肠癌筛查
        
        @param request: ScreenCRCRequest
        @return: ScreenCRCResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.screen_crcwith_options(request, runtime)

    async def screen_crc_async(
        self,
        request: imageprocess_20200320_models.ScreenCRCRequest,
    ) -> imageprocess_20200320_models.ScreenCRCResponse:
        """
        @summary 结直肠癌筛查
        
        @param request: ScreenCRCRequest
        @return: ScreenCRCResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.screen_crcwith_options_async(request, runtime)

    def screen_crcadvance(
        self,
        request: imageprocess_20200320_models.ScreenCRCAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenCRCResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        screen_crcreq = imageprocess_20200320_models.ScreenCRCRequest()
        OpenApiUtilClient.convert(request, screen_crcreq)
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
                    tmp = screen_crcreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        screen_crcresp = self.screen_crcwith_options(screen_crcreq, runtime)
        return screen_crcresp

    async def screen_crcadvance_async(
        self,
        request: imageprocess_20200320_models.ScreenCRCAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenCRCResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        screen_crcreq = imageprocess_20200320_models.ScreenCRCRequest()
        OpenApiUtilClient.convert(request, screen_crcreq)
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
                    tmp = screen_crcreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        screen_crcresp = await self.screen_crcwith_options_async(screen_crcreq, runtime)
        return screen_crcresp

    def screen_chest_ctwith_options(
        self,
        request: imageprocess_20200320_models.ScreenChestCTRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        """
        @summary 胸部CT平扫
        
        @param request: ScreenChestCTRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScreenChestCTResponse
        """
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
        """
        @summary 胸部CT平扫
        
        @param request: ScreenChestCTRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScreenChestCTResponse
        """
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
        """
        @summary 胸部CT平扫
        
        @param request: ScreenChestCTRequest
        @return: ScreenChestCTResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.screen_chest_ctwith_options(request, runtime)

    async def screen_chest_ct_async(
        self,
        request: imageprocess_20200320_models.ScreenChestCTRequest,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        """
        @summary 胸部CT平扫
        
        @param request: ScreenChestCTRequest
        @return: ScreenChestCTResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        """
        @summary 食管癌筛查
        
        @param request: ScreenECRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScreenECResponse
        """
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
        """
        @summary 食管癌筛查
        
        @param request: ScreenECRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScreenECResponse
        """
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
        """
        @summary 食管癌筛查
        
        @param request: ScreenECRequest
        @return: ScreenECResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.screen_ecwith_options(request, runtime)

    async def screen_ec_async(
        self,
        request: imageprocess_20200320_models.ScreenECRequest,
    ) -> imageprocess_20200320_models.ScreenECResponse:
        """
        @summary 食管癌筛查
        
        @param request: ScreenECRequest
        @return: ScreenECResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.screen_ecwith_options_async(request, runtime)

    def screen_ecadvance(
        self,
        request: imageprocess_20200320_models.ScreenECAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenECResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        screen_ecreq = imageprocess_20200320_models.ScreenECRequest()
        OpenApiUtilClient.convert(request, screen_ecreq)
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
                    tmp = screen_ecreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        screen_ecresp = self.screen_ecwith_options(screen_ecreq, runtime)
        return screen_ecresp

    async def screen_ecadvance_async(
        self,
        request: imageprocess_20200320_models.ScreenECAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenECResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        screen_ecreq = imageprocess_20200320_models.ScreenECRequest()
        OpenApiUtilClient.convert(request, screen_ecreq)
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
                    tmp = screen_ecreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        screen_ecresp = await self.screen_ecwith_options_async(screen_ecreq, runtime)
        return screen_ecresp

    def screen_gcwith_options(
        self,
        request: imageprocess_20200320_models.ScreenGCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenGCResponse:
        """
        @summary 胃癌筛查
        
        @param request: ScreenGCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScreenGCResponse
        """
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
            action='ScreenGC',
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
            imageprocess_20200320_models.ScreenGCResponse(),
            self.call_api(params, req, runtime)
        )

    async def screen_gcwith_options_async(
        self,
        request: imageprocess_20200320_models.ScreenGCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenGCResponse:
        """
        @summary 胃癌筛查
        
        @param request: ScreenGCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScreenGCResponse
        """
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
            action='ScreenGC',
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
            imageprocess_20200320_models.ScreenGCResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def screen_gc(
        self,
        request: imageprocess_20200320_models.ScreenGCRequest,
    ) -> imageprocess_20200320_models.ScreenGCResponse:
        """
        @summary 胃癌筛查
        
        @param request: ScreenGCRequest
        @return: ScreenGCResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.screen_gcwith_options(request, runtime)

    async def screen_gc_async(
        self,
        request: imageprocess_20200320_models.ScreenGCRequest,
    ) -> imageprocess_20200320_models.ScreenGCResponse:
        """
        @summary 胃癌筛查
        
        @param request: ScreenGCRequest
        @return: ScreenGCResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.screen_gcwith_options_async(request, runtime)

    def screen_gcadvance(
        self,
        request: imageprocess_20200320_models.ScreenGCAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenGCResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        screen_gcreq = imageprocess_20200320_models.ScreenGCRequest()
        OpenApiUtilClient.convert(request, screen_gcreq)
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
                    tmp = screen_gcreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        screen_gcresp = self.screen_gcwith_options(screen_gcreq, runtime)
        return screen_gcresp

    async def screen_gcadvance_async(
        self,
        request: imageprocess_20200320_models.ScreenGCAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenGCResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        screen_gcreq = imageprocess_20200320_models.ScreenGCRequest()
        OpenApiUtilClient.convert(request, screen_gcreq)
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
                    tmp = screen_gcreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        screen_gcresp = await self.screen_gcwith_options_async(screen_gcreq, runtime)
        return screen_gcresp

    def screen_lcwith_options(
        self,
        request: imageprocess_20200320_models.ScreenLCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenLCResponse:
        """
        @summary 肝癌筛查
        
        @param request: ScreenLCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScreenLCResponse
        """
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
            action='ScreenLC',
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
            imageprocess_20200320_models.ScreenLCResponse(),
            self.call_api(params, req, runtime)
        )

    async def screen_lcwith_options_async(
        self,
        request: imageprocess_20200320_models.ScreenLCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenLCResponse:
        """
        @summary 肝癌筛查
        
        @param request: ScreenLCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScreenLCResponse
        """
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
            action='ScreenLC',
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
            imageprocess_20200320_models.ScreenLCResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def screen_lc(
        self,
        request: imageprocess_20200320_models.ScreenLCRequest,
    ) -> imageprocess_20200320_models.ScreenLCResponse:
        """
        @summary 肝癌筛查
        
        @param request: ScreenLCRequest
        @return: ScreenLCResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.screen_lcwith_options(request, runtime)

    async def screen_lc_async(
        self,
        request: imageprocess_20200320_models.ScreenLCRequest,
    ) -> imageprocess_20200320_models.ScreenLCResponse:
        """
        @summary 肝癌筛查
        
        @param request: ScreenLCRequest
        @return: ScreenLCResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.screen_lcwith_options_async(request, runtime)

    def screen_lcadvance(
        self,
        request: imageprocess_20200320_models.ScreenLCAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenLCResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        screen_lcreq = imageprocess_20200320_models.ScreenLCRequest()
        OpenApiUtilClient.convert(request, screen_lcreq)
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
                    tmp = screen_lcreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        screen_lcresp = self.screen_lcwith_options(screen_lcreq, runtime)
        return screen_lcresp

    async def screen_lcadvance_async(
        self,
        request: imageprocess_20200320_models.ScreenLCAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenLCResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        screen_lcreq = imageprocess_20200320_models.ScreenLCRequest()
        OpenApiUtilClient.convert(request, screen_lcreq)
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
                    tmp = screen_lcreq.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        screen_lcresp = await self.screen_lcwith_options_async(screen_lcreq, runtime)
        return screen_lcresp

    def segment_lymph_node_with_options(
        self,
        request: imageprocess_20200320_models.SegmentLymphNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.SegmentLymphNodeResponse:
        """
        @summary 放疗淋巴站分割
        
        @param request: SegmentLymphNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SegmentLymphNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body_part):
            body['BodyPart'] = request.body_part
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
            action='SegmentLymphNode',
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
            imageprocess_20200320_models.SegmentLymphNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def segment_lymph_node_with_options_async(
        self,
        request: imageprocess_20200320_models.SegmentLymphNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.SegmentLymphNodeResponse:
        """
        @summary 放疗淋巴站分割
        
        @param request: SegmentLymphNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SegmentLymphNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body_part):
            body['BodyPart'] = request.body_part
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
            action='SegmentLymphNode',
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
            imageprocess_20200320_models.SegmentLymphNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def segment_lymph_node(
        self,
        request: imageprocess_20200320_models.SegmentLymphNodeRequest,
    ) -> imageprocess_20200320_models.SegmentLymphNodeResponse:
        """
        @summary 放疗淋巴站分割
        
        @param request: SegmentLymphNodeRequest
        @return: SegmentLymphNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.segment_lymph_node_with_options(request, runtime)

    async def segment_lymph_node_async(
        self,
        request: imageprocess_20200320_models.SegmentLymphNodeRequest,
    ) -> imageprocess_20200320_models.SegmentLymphNodeResponse:
        """
        @summary 放疗淋巴站分割
        
        @param request: SegmentLymphNodeRequest
        @return: SegmentLymphNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.segment_lymph_node_with_options_async(request, runtime)

    def segment_lymph_node_advance(
        self,
        request: imageprocess_20200320_models.SegmentLymphNodeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.SegmentLymphNodeResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        segment_lymph_node_req = imageprocess_20200320_models.SegmentLymphNodeRequest()
        OpenApiUtilClient.convert(request, segment_lymph_node_req)
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
                    tmp = segment_lymph_node_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        segment_lymph_node_resp = self.segment_lymph_node_with_options(segment_lymph_node_req, runtime)
        return segment_lymph_node_resp

    async def segment_lymph_node_advance_async(
        self,
        request: imageprocess_20200320_models.SegmentLymphNodeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.SegmentLymphNodeResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        segment_lymph_node_req = imageprocess_20200320_models.SegmentLymphNodeRequest()
        OpenApiUtilClient.convert(request, segment_lymph_node_req)
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
                    tmp = segment_lymph_node_req.urllist[i_0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        segment_lymph_node_resp = await self.segment_lymph_node_with_options_async(segment_lymph_node_req, runtime)
        return segment_lymph_node_resp

    def segment_oarwith_options(
        self,
        request: imageprocess_20200320_models.SegmentOARRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.SegmentOARResponse:
        """
        @summary 多器官分割
        
        @param request: SegmentOARRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SegmentOARResponse
        """
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
        """
        @summary 多器官分割
        
        @param request: SegmentOARRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SegmentOARResponse
        """
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
        """
        @summary 多器官分割
        
        @param request: SegmentOARRequest
        @return: SegmentOARResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.segment_oarwith_options(request, runtime)

    async def segment_oar_async(
        self,
        request: imageprocess_20200320_models.SegmentOARRequest,
    ) -> imageprocess_20200320_models.SegmentOARResponse:
        """
        @summary 多器官分割
        
        @param request: SegmentOARRequest
        @return: SegmentOARResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        """
        @summary 放疗靶区勾画算法
        
        @param request: TargetVolumeSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TargetVolumeSegmentResponse
        """
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
        """
        @summary 放疗靶区勾画算法
        
        @param request: TargetVolumeSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TargetVolumeSegmentResponse
        """
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
        """
        @summary 放疗靶区勾画算法
        
        @param request: TargetVolumeSegmentRequest
        @return: TargetVolumeSegmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.target_volume_segment_with_options(request, runtime)

    async def target_volume_segment_async(
        self,
        request: imageprocess_20200320_models.TargetVolumeSegmentRequest,
    ) -> imageprocess_20200320_models.TargetVolumeSegmentResponse:
        """
        @summary 放疗靶区勾画算法
        
        @param request: TargetVolumeSegmentRequest
        @return: TargetVolumeSegmentResponse
        """
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
        if UtilClient.empty(open_platform_endpoint):
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
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
