# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dt_oc_info20220829 import models as dt_oc_info_20220829_models
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
        self._endpoint = self.get_endpoint('dt-oc-info', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_oc_competitors_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcCompetitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcCompetitorsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcCompetitors',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcCompetitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_competitors_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcCompetitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcCompetitorsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcCompetitors',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcCompetitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_competitors(
        self,
        request: dt_oc_info_20220829_models.GetOcCompetitorsRequest,
    ) -> dt_oc_info_20220829_models.GetOcCompetitorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_competitors_with_options(request, runtime)

    async def get_oc_competitors_async(
        self,
        request: dt_oc_info_20220829_models.GetOcCompetitorsRequest,
    ) -> dt_oc_info_20220829_models.GetOcCompetitorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_competitors_with_options_async(request, runtime)

    def get_oc_core_teams_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcCoreTeamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcCoreTeamsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcCoreTeams',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcCoreTeamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_core_teams_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcCoreTeamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcCoreTeamsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcCoreTeams',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcCoreTeamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_core_teams(
        self,
        request: dt_oc_info_20220829_models.GetOcCoreTeamsRequest,
    ) -> dt_oc_info_20220829_models.GetOcCoreTeamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_core_teams_with_options(request, runtime)

    async def get_oc_core_teams_async(
        self,
        request: dt_oc_info_20220829_models.GetOcCoreTeamsRequest,
    ) -> dt_oc_info_20220829_models.GetOcCoreTeamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_core_teams_with_options_async(request, runtime)

    def get_oc_financing_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcFinancingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcFinancingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcFinancing',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcFinancingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_financing_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcFinancingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcFinancingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcFinancing',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcFinancingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_financing(
        self,
        request: dt_oc_info_20220829_models.GetOcFinancingRequest,
    ) -> dt_oc_info_20220829_models.GetOcFinancingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_financing_with_options(request, runtime)

    async def get_oc_financing_async(
        self,
        request: dt_oc_info_20220829_models.GetOcFinancingRequest,
    ) -> dt_oc_info_20220829_models.GetOcFinancingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_financing_with_options_async(request, runtime)

    def get_oc_fuzz_search_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcFuzzSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcFuzzSearchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcFuzzSearch',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcFuzzSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_fuzz_search_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcFuzzSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcFuzzSearchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcFuzzSearch',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcFuzzSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_fuzz_search(
        self,
        request: dt_oc_info_20220829_models.GetOcFuzzSearchRequest,
    ) -> dt_oc_info_20220829_models.GetOcFuzzSearchResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_fuzz_search_with_options(request, runtime)

    async def get_oc_fuzz_search_async(
        self,
        request: dt_oc_info_20220829_models.GetOcFuzzSearchRequest,
    ) -> dt_oc_info_20220829_models.GetOcFuzzSearchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_fuzz_search_with_options_async(request, runtime)

    def get_oc_ic_abnormal_operation_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcAbnormalOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcAbnormalOperationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcAbnormalOperation',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcAbnormalOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_abnormal_operation_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcAbnormalOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcAbnormalOperationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcAbnormalOperation',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcAbnormalOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_abnormal_operation(
        self,
        request: dt_oc_info_20220829_models.GetOcIcAbnormalOperationRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcAbnormalOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_abnormal_operation_with_options(request, runtime)

    async def get_oc_ic_abnormal_operation_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcAbnormalOperationRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcAbnormalOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_abnormal_operation_with_options_async(request, runtime)

    def get_oc_ic_admin_license_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcAdminLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcAdminLicenseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcAdminLicense',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcAdminLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_admin_license_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcAdminLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcAdminLicenseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcAdminLicense',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcAdminLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_admin_license(
        self,
        request: dt_oc_info_20220829_models.GetOcIcAdminLicenseRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcAdminLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_admin_license_with_options(request, runtime)

    async def get_oc_ic_admin_license_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcAdminLicenseRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcAdminLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_admin_license_with_options_async(request, runtime)

    def get_oc_ic_basic_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcBasicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcBasicResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcBasic',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcBasicResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_basic_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcBasicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcBasicResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcBasic',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcBasicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_basic(
        self,
        request: dt_oc_info_20220829_models.GetOcIcBasicRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcBasicResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_basic_with_options(request, runtime)

    async def get_oc_ic_basic_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcBasicRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcBasicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_basic_with_options_async(request, runtime)

    def get_oc_ic_branch_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcBranchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcBranchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcBranch',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcBranchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_branch_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcBranchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcBranchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcBranch',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcBranchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_branch(
        self,
        request: dt_oc_info_20220829_models.GetOcIcBranchRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcBranchResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_branch_with_options(request, runtime)

    async def get_oc_ic_branch_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcBranchRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcBranchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_branch_with_options_async(request, runtime)

    def get_oc_ic_change_record_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcChangeRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcChangeRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcChangeRecord',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcChangeRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_change_record_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcChangeRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcChangeRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcChangeRecord',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcChangeRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_change_record(
        self,
        request: dt_oc_info_20220829_models.GetOcIcChangeRecordRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcChangeRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_change_record_with_options(request, runtime)

    async def get_oc_ic_change_record_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcChangeRecordRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcChangeRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_change_record_with_options_async(request, runtime)

    def get_oc_ic_checkup_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcCheckupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcCheckupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcCheckup',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcCheckupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_checkup_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcCheckupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcCheckupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcCheckup',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcCheckupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_checkup(
        self,
        request: dt_oc_info_20220829_models.GetOcIcCheckupRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcCheckupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_checkup_with_options(request, runtime)

    async def get_oc_ic_checkup_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcCheckupRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcCheckupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_checkup_with_options_async(request, runtime)

    def get_oc_ic_clear_account_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcClearAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcClearAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcClearAccount',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcClearAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_clear_account_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcClearAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcClearAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcClearAccount',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcClearAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_clear_account(
        self,
        request: dt_oc_info_20220829_models.GetOcIcClearAccountRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcClearAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_clear_account_with_options(request, runtime)

    async def get_oc_ic_clear_account_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcClearAccountRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcClearAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_clear_account_with_options_async(request, runtime)

    def get_oc_ic_double_checkup_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcDoubleCheckupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcDoubleCheckupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcDoubleCheckup',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcDoubleCheckupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_double_checkup_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcDoubleCheckupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcDoubleCheckupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcDoubleCheckup',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcDoubleCheckupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_double_checkup(
        self,
        request: dt_oc_info_20220829_models.GetOcIcDoubleCheckupRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcDoubleCheckupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_double_checkup_with_options(request, runtime)

    async def get_oc_ic_double_checkup_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcDoubleCheckupRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcDoubleCheckupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_double_checkup_with_options_async(request, runtime)

    def get_oc_ic_employee_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEmployeeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcEmployeeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcEmployee',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcEmployeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_employee_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEmployeeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcEmployeeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcEmployee',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcEmployeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_employee(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEmployeeRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcEmployeeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_employee_with_options(request, runtime)

    async def get_oc_ic_employee_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEmployeeRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcEmployeeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_employee_with_options_async(request, runtime)

    def get_oc_ic_equity_frozen_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEquityFrozenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcEquityFrozenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcEquityFrozen',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcEquityFrozenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_equity_frozen_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEquityFrozenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcEquityFrozenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcEquityFrozen',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcEquityFrozenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_equity_frozen(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEquityFrozenRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcEquityFrozenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_equity_frozen_with_options(request, runtime)

    async def get_oc_ic_equity_frozen_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEquityFrozenRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcEquityFrozenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_equity_frozen_with_options_async(request, runtime)

    def get_oc_ic_equity_pledge_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEquityPledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcEquityPledgeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcEquityPledge',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcEquityPledgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_equity_pledge_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEquityPledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcEquityPledgeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcEquityPledge',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcEquityPledgeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_equity_pledge(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEquityPledgeRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcEquityPledgeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_equity_pledge_with_options(request, runtime)

    async def get_oc_ic_equity_pledge_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcEquityPledgeRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcEquityPledgeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_equity_pledge_with_options_async(request, runtime)

    def get_oc_ic_investment_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcInvestmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcInvestmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcInvestment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcInvestmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_investment_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcInvestmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcInvestmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcInvestment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcInvestmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_investment(
        self,
        request: dt_oc_info_20220829_models.GetOcIcInvestmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcInvestmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_investment_with_options(request, runtime)

    async def get_oc_ic_investment_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcInvestmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcInvestmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_investment_with_options_async(request, runtime)

    def get_oc_ic_knowledge_property_pledge_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcKnowledgePropertyPledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcKnowledgePropertyPledgeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcKnowledgePropertyPledge',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcKnowledgePropertyPledgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_knowledge_property_pledge_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcKnowledgePropertyPledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcKnowledgePropertyPledgeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcKnowledgePropertyPledge',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcKnowledgePropertyPledgeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_knowledge_property_pledge(
        self,
        request: dt_oc_info_20220829_models.GetOcIcKnowledgePropertyPledgeRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcKnowledgePropertyPledgeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_knowledge_property_pledge_with_options(request, runtime)

    async def get_oc_ic_knowledge_property_pledge_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcKnowledgePropertyPledgeRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcKnowledgePropertyPledgeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_knowledge_property_pledge_with_options_async(request, runtime)

    def get_oc_ic_mortgage_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcMortgageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcMortgageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcMortgage',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcMortgageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_mortgage_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcMortgageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcMortgageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcMortgage',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcMortgageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_mortgage(
        self,
        request: dt_oc_info_20220829_models.GetOcIcMortgageRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcMortgageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_mortgage_with_options(request, runtime)

    async def get_oc_ic_mortgage_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcMortgageRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcMortgageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_mortgage_with_options_async(request, runtime)

    def get_oc_ic_serious_offense_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcSeriousOffenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcSeriousOffenseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcSeriousOffense',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcSeriousOffenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_serious_offense_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcSeriousOffenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcSeriousOffenseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcSeriousOffense',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcSeriousOffenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_serious_offense(
        self,
        request: dt_oc_info_20220829_models.GetOcIcSeriousOffenseRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcSeriousOffenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_serious_offense_with_options(request, runtime)

    async def get_oc_ic_serious_offense_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcSeriousOffenseRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcSeriousOffenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_serious_offense_with_options_async(request, runtime)

    def get_oc_ic_shareholder_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcShareholderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcShareholderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcShareholder',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcShareholderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_shareholder_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcShareholderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcShareholderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcShareholder',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcShareholderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_shareholder(
        self,
        request: dt_oc_info_20220829_models.GetOcIcShareholderRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcShareholderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_shareholder_with_options(request, runtime)

    async def get_oc_ic_shareholder_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcShareholderRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcShareholderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_shareholder_with_options_async(request, runtime)

    def get_oc_ic_simple_cancel_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIcSimpleCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcSimpleCancelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcSimpleCancel',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcSimpleCancelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ic_simple_cancel_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcSimpleCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIcSimpleCancelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcSimpleCancel',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcSimpleCancelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ic_simple_cancel(
        self,
        request: dt_oc_info_20220829_models.GetOcIcSimpleCancelRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcSimpleCancelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_simple_cancel_with_options(request, runtime)

    async def get_oc_ic_simple_cancel_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIcSimpleCancelRequest,
    ) -> dt_oc_info_20220829_models.GetOcIcSimpleCancelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ic_simple_cancel_with_options_async(request, runtime)

    def get_oc_ip_certificate_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIpCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpCertificate',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ip_certificate_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpCertificate',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ip_certificate(
        self,
        request: dt_oc_info_20220829_models.GetOcIpCertificateRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_certificate_with_options(request, runtime)

    async def get_oc_ip_certificate_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpCertificateRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ip_certificate_with_options_async(request, runtime)

    def get_oc_ip_domain_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIpDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpDomain',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ip_domain_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpDomain',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ip_domain(
        self,
        request: dt_oc_info_20220829_models.GetOcIpDomainRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_domain_with_options(request, runtime)

    async def get_oc_ip_domain_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpDomainRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ip_domain_with_options_async(request, runtime)

    def get_oc_ip_patent_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIpPatentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpPatentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpPatent',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpPatentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ip_patent_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpPatentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpPatentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpPatent',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpPatentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ip_patent(
        self,
        request: dt_oc_info_20220829_models.GetOcIpPatentRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpPatentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_patent_with_options(request, runtime)

    async def get_oc_ip_patent_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpPatentRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpPatentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ip_patent_with_options_async(request, runtime)

    def get_oc_ip_software_copyright_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIpSoftwareCopyrightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpSoftwareCopyrightResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpSoftwareCopyright',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpSoftwareCopyrightResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ip_software_copyright_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpSoftwareCopyrightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpSoftwareCopyrightResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpSoftwareCopyright',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpSoftwareCopyrightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ip_software_copyright(
        self,
        request: dt_oc_info_20220829_models.GetOcIpSoftwareCopyrightRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpSoftwareCopyrightResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_software_copyright_with_options(request, runtime)

    async def get_oc_ip_software_copyright_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpSoftwareCopyrightRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpSoftwareCopyrightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ip_software_copyright_with_options_async(request, runtime)

    def get_oc_ip_trademark_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIpTrademarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpTrademarkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpTrademark',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpTrademarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ip_trademark_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpTrademarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpTrademarkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpTrademark',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpTrademarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ip_trademark(
        self,
        request: dt_oc_info_20220829_models.GetOcIpTrademarkRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpTrademarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_trademark_with_options(request, runtime)

    async def get_oc_ip_trademark_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpTrademarkRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpTrademarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ip_trademark_with_options_async(request, runtime)

    def get_oc_ip_works_copyright_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcIpWorksCopyrightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpWorksCopyrightResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpWorksCopyright',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpWorksCopyrightResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_ip_works_copyright_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpWorksCopyrightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcIpWorksCopyrightResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpWorksCopyright',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpWorksCopyrightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_ip_works_copyright(
        self,
        request: dt_oc_info_20220829_models.GetOcIpWorksCopyrightRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpWorksCopyrightResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_works_copyright_with_options(request, runtime)

    async def get_oc_ip_works_copyright_async(
        self,
        request: dt_oc_info_20220829_models.GetOcIpWorksCopyrightRequest,
    ) -> dt_oc_info_20220829_models.GetOcIpWorksCopyrightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_ip_works_copyright_with_options_async(request, runtime)

    def get_oc_justice_auction_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeAuctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeAuctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeAuction',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeAuctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_justice_auction_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeAuctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeAuctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeAuction',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeAuctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_justice_auction(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeAuctionRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeAuctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_auction_with_options(request, runtime)

    async def get_oc_justice_auction_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeAuctionRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeAuctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_justice_auction_with_options_async(request, runtime)

    def get_oc_justice_case_filing_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCaseFilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCaseFilingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeCaseFiling',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeCaseFilingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_justice_case_filing_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCaseFilingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCaseFilingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeCaseFiling',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeCaseFilingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_justice_case_filing(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCaseFilingRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCaseFilingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_case_filing_with_options(request, runtime)

    async def get_oc_justice_case_filing_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCaseFilingRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCaseFilingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_justice_case_filing_with_options_async(request, runtime)

    def get_oc_justice_court_announcement_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCourtAnnouncementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCourtAnnouncementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeCourtAnnouncement',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeCourtAnnouncementResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_justice_court_announcement_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCourtAnnouncementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCourtAnnouncementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeCourtAnnouncement',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeCourtAnnouncementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_justice_court_announcement(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCourtAnnouncementRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCourtAnnouncementResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_court_announcement_with_options(request, runtime)

    async def get_oc_justice_court_announcement_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCourtAnnouncementRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCourtAnnouncementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_justice_court_announcement_with_options_async(request, runtime)

    def get_oc_justice_court_notice_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCourtNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCourtNoticeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeCourtNotice',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeCourtNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_justice_court_notice_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCourtNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCourtNoticeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeCourtNotice',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeCourtNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_justice_court_notice(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCourtNoticeRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCourtNoticeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_court_notice_with_options(request, runtime)

    async def get_oc_justice_court_notice_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeCourtNoticeRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeCourtNoticeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_justice_court_notice_with_options_async(request, runtime)

    def get_oc_justice_dishonesty_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeDishonestyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeDishonestyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeDishonesty',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeDishonestyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_justice_dishonesty_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeDishonestyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeDishonestyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeDishonesty',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeDishonestyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_justice_dishonesty(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeDishonestyRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeDishonestyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_dishonesty_with_options(request, runtime)

    async def get_oc_justice_dishonesty_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeDishonestyRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeDishonestyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_justice_dishonesty_with_options_async(request, runtime)

    def get_oc_justice_executed_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeExecutedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeExecutedResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeExecuted',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeExecutedResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_justice_executed_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeExecutedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeExecutedResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeExecuted',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeExecutedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_justice_executed(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeExecutedRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeExecutedResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_executed_with_options(request, runtime)

    async def get_oc_justice_executed_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeExecutedRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeExecutedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_justice_executed_with_options_async(request, runtime)

    def get_oc_justice_judgement_doc_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeJudgementDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeJudgementDocResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeJudgementDoc',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeJudgementDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_justice_judgement_doc_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeJudgementDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeJudgementDocResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeJudgementDoc',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeJudgementDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_justice_judgement_doc(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeJudgementDocRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeJudgementDocResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_judgement_doc_with_options(request, runtime)

    async def get_oc_justice_judgement_doc_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeJudgementDocRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeJudgementDocResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_justice_judgement_doc_with_options_async(request, runtime)

    def get_oc_justice_limit_high_consume_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeLimitHighConsumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeLimitHighConsumeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeLimitHighConsume',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeLimitHighConsumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_justice_limit_high_consume_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeLimitHighConsumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeLimitHighConsumeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeLimitHighConsume',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeLimitHighConsumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_justice_limit_high_consume(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeLimitHighConsumeRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeLimitHighConsumeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_limit_high_consume_with_options(request, runtime)

    async def get_oc_justice_limit_high_consume_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeLimitHighConsumeRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeLimitHighConsumeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_justice_limit_high_consume_with_options_async(request, runtime)

    def get_oc_justice_terminal_case_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeTerminalCaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeTerminalCaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeTerminalCase',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeTerminalCaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_justice_terminal_case_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeTerminalCaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcJusticeTerminalCaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeTerminalCase',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeTerminalCaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_justice_terminal_case(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeTerminalCaseRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeTerminalCaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_terminal_case_with_options(request, runtime)

    async def get_oc_justice_terminal_case_async(
        self,
        request: dt_oc_info_20220829_models.GetOcJusticeTerminalCaseRequest,
    ) -> dt_oc_info_20220829_models.GetOcJusticeTerminalCaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_justice_terminal_case_with_options_async(request, runtime)

    def get_oc_listed_company_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcListedCompanyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcListedCompanyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcListedCompany',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcListedCompanyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_listed_company_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcListedCompanyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcListedCompanyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcListedCompany',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcListedCompanyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_listed_company(
        self,
        request: dt_oc_info_20220829_models.GetOcListedCompanyRequest,
    ) -> dt_oc_info_20220829_models.GetOcListedCompanyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_listed_company_with_options(request, runtime)

    async def get_oc_listed_company_async(
        self,
        request: dt_oc_info_20220829_models.GetOcListedCompanyRequest,
    ) -> dt_oc_info_20220829_models.GetOcListedCompanyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_listed_company_with_options_async(request, runtime)

    def get_oc_negative_admin_punishment_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeAdminPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcNegativeAdminPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeAdminPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeAdminPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_negative_admin_punishment_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeAdminPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcNegativeAdminPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeAdminPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeAdminPunishmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_negative_admin_punishment(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeAdminPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcNegativeAdminPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_negative_admin_punishment_with_options(request, runtime)

    async def get_oc_negative_admin_punishment_async(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeAdminPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcNegativeAdminPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_negative_admin_punishment_with_options_async(request, runtime)

    def get_oc_negative_customs_punishment_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeCustomsPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcNegativeCustomsPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeCustomsPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeCustomsPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_negative_customs_punishment_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeCustomsPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcNegativeCustomsPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeCustomsPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeCustomsPunishmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_negative_customs_punishment(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeCustomsPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcNegativeCustomsPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_negative_customs_punishment_with_options(request, runtime)

    async def get_oc_negative_customs_punishment_async(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeCustomsPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcNegativeCustomsPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_negative_customs_punishment_with_options_async(request, runtime)

    def get_oc_negative_environment_punishment_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeEnvironmentPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcNegativeEnvironmentPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeEnvironmentPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeEnvironmentPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_negative_environment_punishment_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeEnvironmentPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcNegativeEnvironmentPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeEnvironmentPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeEnvironmentPunishmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_negative_environment_punishment(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeEnvironmentPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcNegativeEnvironmentPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_negative_environment_punishment_with_options(request, runtime)

    async def get_oc_negative_environment_punishment_async(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeEnvironmentPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcNegativeEnvironmentPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_negative_environment_punishment_with_options_async(request, runtime)

    def get_oc_negative_food_drug_punishment_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeFoodDrugPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcNegativeFoodDrugPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeFoodDrugPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeFoodDrugPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_negative_food_drug_punishment_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeFoodDrugPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcNegativeFoodDrugPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeFoodDrugPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeFoodDrugPunishmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_negative_food_drug_punishment(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeFoodDrugPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcNegativeFoodDrugPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_negative_food_drug_punishment_with_options(request, runtime)

    async def get_oc_negative_food_drug_punishment_async(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeFoodDrugPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcNegativeFoodDrugPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_negative_food_drug_punishment_with_options_async(request, runtime)

    def get_oc_negative_quality_punishment_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeQualityPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcNegativeQualityPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeQualityPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeQualityPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_negative_quality_punishment_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeQualityPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcNegativeQualityPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeQualityPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeQualityPunishmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_negative_quality_punishment(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeQualityPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcNegativeQualityPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_negative_quality_punishment_with_options(request, runtime)

    async def get_oc_negative_quality_punishment_async(
        self,
        request: dt_oc_info_20220829_models.GetOcNegativeQualityPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcNegativeQualityPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_negative_quality_punishment_with_options_async(request, runtime)

    def get_oc_operation_bidding_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationBiddingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcOperationBiddingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationBidding',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationBiddingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_operation_bidding_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationBiddingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcOperationBiddingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationBidding',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationBiddingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_operation_bidding(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationBiddingRequest,
    ) -> dt_oc_info_20220829_models.GetOcOperationBiddingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_operation_bidding_with_options(request, runtime)

    async def get_oc_operation_bidding_async(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationBiddingRequest,
    ) -> dt_oc_info_20220829_models.GetOcOperationBiddingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_operation_bidding_with_options_async(request, runtime)

    def get_oc_operation_customs_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationCustomsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcOperationCustomsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationCustoms',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationCustomsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_operation_customs_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationCustomsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcOperationCustomsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationCustoms',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationCustomsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_operation_customs(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationCustomsRequest,
    ) -> dt_oc_info_20220829_models.GetOcOperationCustomsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_operation_customs_with_options(request, runtime)

    async def get_oc_operation_customs_async(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationCustomsRequest,
    ) -> dt_oc_info_20220829_models.GetOcOperationCustomsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_operation_customs_with_options_async(request, runtime)

    def get_oc_operation_purchase_land_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationPurchaseLandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcOperationPurchaseLandResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationPurchaseLand',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationPurchaseLandResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_operation_purchase_land_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationPurchaseLandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcOperationPurchaseLandResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationPurchaseLand',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationPurchaseLandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_operation_purchase_land(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationPurchaseLandRequest,
    ) -> dt_oc_info_20220829_models.GetOcOperationPurchaseLandResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_operation_purchase_land_with_options(request, runtime)

    async def get_oc_operation_purchase_land_async(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationPurchaseLandRequest,
    ) -> dt_oc_info_20220829_models.GetOcOperationPurchaseLandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_operation_purchase_land_with_options_async(request, runtime)

    def get_oc_operation_recruitment_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationRecruitmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcOperationRecruitmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationRecruitment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationRecruitmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_operation_recruitment_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationRecruitmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcOperationRecruitmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationRecruitment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationRecruitmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_operation_recruitment(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationRecruitmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcOperationRecruitmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_operation_recruitment_with_options(request, runtime)

    async def get_oc_operation_recruitment_async(
        self,
        request: dt_oc_info_20220829_models.GetOcOperationRecruitmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcOperationRecruitmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_operation_recruitment_with_options_async(request, runtime)

    def get_oc_product_band_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcProductBandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcProductBandResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcProductBand',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcProductBandResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_product_band_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcProductBandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcProductBandResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcProductBand',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcProductBandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_product_band(
        self,
        request: dt_oc_info_20220829_models.GetOcProductBandRequest,
    ) -> dt_oc_info_20220829_models.GetOcProductBandResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_product_band_with_options(request, runtime)

    async def get_oc_product_band_async(
        self,
        request: dt_oc_info_20220829_models.GetOcProductBandRequest,
    ) -> dt_oc_info_20220829_models.GetOcProductBandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_product_band_with_options_async(request, runtime)

    def get_oc_tax_abnormal_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxAbnormalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxAbnormalResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxAbnormal',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxAbnormalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_tax_abnormal_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxAbnormalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxAbnormalResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxAbnormal',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxAbnormalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_tax_abnormal(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxAbnormalRequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxAbnormalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_abnormal_with_options(request, runtime)

    async def get_oc_tax_abnormal_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxAbnormalRequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxAbnormalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_tax_abnormal_with_options_async(request, runtime)

    def get_oc_tax_class_awith_options(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxClassARequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxClassAResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxClassA',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxClassAResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_tax_class_awith_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxClassARequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxClassAResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxClassA',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxClassAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_tax_class_a(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxClassARequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxClassAResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_class_awith_options(request, runtime)

    async def get_oc_tax_class_a_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxClassARequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxClassAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_tax_class_awith_options_async(request, runtime)

    def get_oc_tax_general_taxpayer_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxGeneralTaxpayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxGeneralTaxpayerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxGeneralTaxpayer',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxGeneralTaxpayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_tax_general_taxpayer_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxGeneralTaxpayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxGeneralTaxpayerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxGeneralTaxpayer',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxGeneralTaxpayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_tax_general_taxpayer(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxGeneralTaxpayerRequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxGeneralTaxpayerResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_general_taxpayer_with_options(request, runtime)

    async def get_oc_tax_general_taxpayer_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxGeneralTaxpayerRequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxGeneralTaxpayerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_tax_general_taxpayer_with_options_async(request, runtime)

    def get_oc_tax_illegal_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxIllegalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxIllegalResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxIllegal',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxIllegalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_tax_illegal_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxIllegalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxIllegalResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxIllegal',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxIllegalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_tax_illegal(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxIllegalRequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxIllegalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_illegal_with_options(request, runtime)

    async def get_oc_tax_illegal_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxIllegalRequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxIllegalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_tax_illegal_with_options_async(request, runtime)

    def get_oc_tax_overdue_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxOverdueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxOverdueResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxOverdue',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxOverdueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_tax_overdue_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxOverdueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxOverdueResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxOverdue',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxOverdueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_tax_overdue(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxOverdueRequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxOverdueResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_overdue_with_options(request, runtime)

    async def get_oc_tax_overdue_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxOverdueRequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxOverdueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_tax_overdue_with_options_async(request, runtime)

    def get_oc_tax_punishment_with_options(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oc_tax_punishment_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxPunishmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetOcTaxPunishmentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxPunishmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oc_tax_punishment(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_punishment_with_options(request, runtime)

    async def get_oc_tax_punishment_async(
        self,
        request: dt_oc_info_20220829_models.GetOcTaxPunishmentRequest,
    ) -> dt_oc_info_20220829_models.GetOcTaxPunishmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oc_tax_punishment_with_options_async(request, runtime)

    def get_qcc_certification_detail_by_id_with_options(
        self,
        request: dt_oc_info_20220829_models.GetQccCertificationDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetQccCertificationDetailByIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_id):
            body['CertId'] = request.cert_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQccCertificationDetailById',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetQccCertificationDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qcc_certification_detail_by_id_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetQccCertificationDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetQccCertificationDetailByIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_id):
            body['CertId'] = request.cert_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQccCertificationDetailById',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetQccCertificationDetailByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qcc_certification_detail_by_id(
        self,
        request: dt_oc_info_20220829_models.GetQccCertificationDetailByIdRequest,
    ) -> dt_oc_info_20220829_models.GetQccCertificationDetailByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_qcc_certification_detail_by_id_with_options(request, runtime)

    async def get_qcc_certification_detail_by_id_async(
        self,
        request: dt_oc_info_20220829_models.GetQccCertificationDetailByIdRequest,
    ) -> dt_oc_info_20220829_models.GetQccCertificationDetailByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_qcc_certification_detail_by_id_with_options_async(request, runtime)

    def get_qcc_search_certification_with_options(
        self,
        request: dt_oc_info_20220829_models.GetQccSearchCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetQccSearchCertificationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_category):
            body['CertCategory'] = request.cert_category
        if not UtilClient.is_unset(request.ent_name):
            body['EntName'] = request.ent_name
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQccSearchCertification',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetQccSearchCertificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qcc_search_certification_with_options_async(
        self,
        request: dt_oc_info_20220829_models.GetQccSearchCertificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dt_oc_info_20220829_models.GetQccSearchCertificationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_category):
            body['CertCategory'] = request.cert_category
        if not UtilClient.is_unset(request.ent_name):
            body['EntName'] = request.ent_name
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQccSearchCertification',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetQccSearchCertificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qcc_search_certification(
        self,
        request: dt_oc_info_20220829_models.GetQccSearchCertificationRequest,
    ) -> dt_oc_info_20220829_models.GetQccSearchCertificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_qcc_search_certification_with_options(request, runtime)

    async def get_qcc_search_certification_async(
        self,
        request: dt_oc_info_20220829_models.GetQccSearchCertificationRequest,
    ) -> dt_oc_info_20220829_models.GetQccSearchCertificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_qcc_search_certification_with_options_async(request, runtime)
