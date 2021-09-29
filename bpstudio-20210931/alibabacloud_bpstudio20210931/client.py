# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bpstudio20210931 import models as bpstudio_20210931_models
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
        self._endpoint = self.get_endpoint('bpstudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_application_with_options(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListApplicationResponse(),
            self.do_rpcrequest('ListApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListApplicationResponse(),
            await self.do_rpcrequest_async('ListApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_application(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_application_with_options(request, runtime)

    async def list_application_async(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_application_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        tmp_req: bpstudio_20210931_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.CreateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instances):
            request.instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.CreateApplicationResponse(),
            self.do_rpcrequest('CreateApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_application_with_options_async(
        self,
        tmp_req: bpstudio_20210931_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.CreateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instances):
            request.instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.CreateApplicationResponse(),
            await self.do_rpcrequest_async('CreateApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_application(
        self,
        request: bpstudio_20210931_models.CreateApplicationRequest,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: bpstudio_20210931_models.CreateApplicationRequest,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def deploy_application_with_options(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeployApplicationResponse(),
            self.do_rpcrequest('DeployApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deploy_application_with_options_async(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeployApplicationResponse(),
            await self.do_rpcrequest_async('DeployApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_application(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_application_with_options(request, runtime)

    async def deploy_application_async(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_application_with_options_async(request, runtime)

    def list_template_with_options(
        self,
        request: bpstudio_20210931_models.ListTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListTemplateResponse(),
            self.do_rpcrequest('ListTemplate', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_template_with_options_async(
        self,
        request: bpstudio_20210931_models.ListTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListTemplateResponse(),
            await self.do_rpcrequest_async('ListTemplate', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_template(
        self,
        request: bpstudio_20210931_models.ListTemplateRequest,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_template_with_options(request, runtime)

    async def list_template_async(
        self,
        request: bpstudio_20210931_models.ListTemplateRequest,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_template_with_options_async(request, runtime)

    def validate_application_with_options(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValidateApplicationResponse(),
            self.do_rpcrequest('ValidateApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def validate_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValidateApplicationResponse(),
            await self.do_rpcrequest_async('ValidateApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def validate_application(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_application_with_options(request, runtime)

    async def validate_application_async(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_application_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeleteApplicationResponse(),
            self.do_rpcrequest('DeleteApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeleteApplicationResponse(),
            await self.do_rpcrequest_async('DeleteApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_application(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetApplicationResponse(),
            self.do_rpcrequest('GetApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetApplicationResponse(),
            await self.do_rpcrequest_async('GetApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_application(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def release_application_with_options(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ReleaseApplicationResponse(),
            self.do_rpcrequest('ReleaseApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ReleaseApplicationResponse(),
            await self.do_rpcrequest_async('ReleaseApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_application(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_application_with_options(request, runtime)

    async def release_application_async(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_application_with_options_async(request, runtime)

    def get_token_with_options(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTokenResponse(),
            self.do_rpcrequest('GetToken', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTokenResponse(),
            await self.do_rpcrequest_async('GetToken', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_token(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_token_with_options(request, runtime)

    async def get_token_async(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_token_with_options_async(request, runtime)

    def valuate_application_with_options(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValuateApplicationResponse(),
            self.do_rpcrequest('ValuateApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def valuate_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValuateApplicationResponse(),
            await self.do_rpcrequest_async('ValuateApplication', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def valuate_application(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.valuate_application_with_options(request, runtime)

    async def valuate_application_async(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.valuate_application_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTemplateResponse(),
            self.do_rpcrequest('GetTemplate', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTemplateResponse(),
            await self.do_rpcrequest_async('GetTemplate', '2021-09-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)
