# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sgx_dcap_server20200726 import models as sgx_dcap_server_20200726_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('sgx-dcap-server', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_qe_identity_with_options(
        self,
        request: sgx_dcap_server_20200726_models.GetQeIdentityRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.GetQeIdentityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQeIdentity',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/qe/identity',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.GetQeIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qe_identity_with_options_async(
        self,
        request: sgx_dcap_server_20200726_models.GetQeIdentityRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.GetQeIdentityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQeIdentity',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/qe/identity',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.GetQeIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qe_identity(
        self,
        request: sgx_dcap_server_20200726_models.GetQeIdentityRequest,
    ) -> sgx_dcap_server_20200726_models.GetQeIdentityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_qe_identity_with_options(request, headers, runtime)

    async def get_qe_identity_async(
        self,
        request: sgx_dcap_server_20200726_models.GetQeIdentityRequest,
    ) -> sgx_dcap_server_20200726_models.GetQeIdentityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_qe_identity_with_options_async(request, headers, runtime)

    def get_qve_identity_with_options(
        self,
        request: sgx_dcap_server_20200726_models.GetQveIdentityRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.GetQveIdentityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQveIdentity',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/qve/identity',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.GetQveIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qve_identity_with_options_async(
        self,
        request: sgx_dcap_server_20200726_models.GetQveIdentityRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.GetQveIdentityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQveIdentity',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/qve/identity',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.GetQveIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qve_identity(
        self,
        request: sgx_dcap_server_20200726_models.GetQveIdentityRequest,
    ) -> sgx_dcap_server_20200726_models.GetQveIdentityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_qve_identity_with_options(request, headers, runtime)

    async def get_qve_identity_async(
        self,
        request: sgx_dcap_server_20200726_models.GetQveIdentityRequest,
    ) -> sgx_dcap_server_20200726_models.GetQveIdentityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_qve_identity_with_options_async(request, headers, runtime)

    def get_tcb_info_with_options(
        self,
        request: sgx_dcap_server_20200726_models.GetTcbInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.GetTcbInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        if not UtilClient.is_unset(request.fmspc):
            query['fmspc'] = request.fmspc
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTcbInfo',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/tcb',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.GetTcbInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tcb_info_with_options_async(
        self,
        request: sgx_dcap_server_20200726_models.GetTcbInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.GetTcbInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        if not UtilClient.is_unset(request.fmspc):
            query['fmspc'] = request.fmspc
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTcbInfo',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/tcb',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.GetTcbInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tcb_info(
        self,
        request: sgx_dcap_server_20200726_models.GetTcbInfoRequest,
    ) -> sgx_dcap_server_20200726_models.GetTcbInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tcb_info_with_options(request, headers, runtime)

    async def get_tcb_info_async(
        self,
        request: sgx_dcap_server_20200726_models.GetTcbInfoRequest,
    ) -> sgx_dcap_server_20200726_models.GetTcbInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_tcb_info_with_options_async(request, headers, runtime)

    def pck_crl_with_options(
        self,
        request: sgx_dcap_server_20200726_models.PckCrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.PckCrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        if not UtilClient.is_unset(request.ca):
            query['ca'] = request.ca
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PckCrl',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/pckcrl',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.PckCrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def pck_crl_with_options_async(
        self,
        request: sgx_dcap_server_20200726_models.PckCrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.PckCrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        if not UtilClient.is_unset(request.ca):
            query['ca'] = request.ca
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PckCrl',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/pckcrl',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.PckCrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pck_crl(
        self,
        request: sgx_dcap_server_20200726_models.PckCrlRequest,
    ) -> sgx_dcap_server_20200726_models.PckCrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pck_crl_with_options(request, headers, runtime)

    async def pck_crl_async(
        self,
        request: sgx_dcap_server_20200726_models.PckCrlRequest,
    ) -> sgx_dcap_server_20200726_models.PckCrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.pck_crl_with_options_async(request, headers, runtime)

    def root_ca_crl_with_options(
        self,
        request: sgx_dcap_server_20200726_models.RootCaCrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.RootCaCrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RootCaCrl',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/rootcacrl',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.RootCaCrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def root_ca_crl_with_options_async(
        self,
        request: sgx_dcap_server_20200726_models.RootCaCrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.RootCaCrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RootCaCrl',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/rootcacrl',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.RootCaCrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def root_ca_crl(
        self,
        request: sgx_dcap_server_20200726_models.RootCaCrlRequest,
    ) -> sgx_dcap_server_20200726_models.RootCaCrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.root_ca_crl_with_options(request, headers, runtime)

    async def root_ca_crl_async(
        self,
        request: sgx_dcap_server_20200726_models.RootCaCrlRequest,
    ) -> sgx_dcap_server_20200726_models.RootCaCrlResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.root_ca_crl_with_options_async(request, headers, runtime)

    def simple_package_pck_cert_with_options(
        self,
        request: sgx_dcap_server_20200726_models.SimplePackagePckCertRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.SimplePackagePckCertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        if not UtilClient.is_unset(request.cpusvn):
            query['cpusvn'] = request.cpusvn
        if not UtilClient.is_unset(request.encrypted_ppid):
            query['encrypted_ppid'] = request.encrypted_ppid
        if not UtilClient.is_unset(request.pceid):
            query['pceid'] = request.pceid
        if not UtilClient.is_unset(request.pcesvn):
            query['pcesvn'] = request.pcesvn
        if not UtilClient.is_unset(request.qeid):
            query['qeid'] = request.qeid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SimplePackagePckCert',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/pckcert',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.SimplePackagePckCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def simple_package_pck_cert_with_options_async(
        self,
        request: sgx_dcap_server_20200726_models.SimplePackagePckCertRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sgx_dcap_server_20200726_models.SimplePackagePckCertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acs_host):
            query['AcsHost'] = request.acs_host
        if not UtilClient.is_unset(request.client_vpc_id):
            query['ClientVpcId'] = request.client_vpc_id
        if not UtilClient.is_unset(request.cpusvn):
            query['cpusvn'] = request.cpusvn
        if not UtilClient.is_unset(request.encrypted_ppid):
            query['encrypted_ppid'] = request.encrypted_ppid
        if not UtilClient.is_unset(request.pceid):
            query['pceid'] = request.pceid
        if not UtilClient.is_unset(request.pcesvn):
            query['pcesvn'] = request.pcesvn
        if not UtilClient.is_unset(request.qeid):
            query['qeid'] = request.qeid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SimplePackagePckCert',
            version='2020-07-26',
            protocol='HTTPS',
            pathname=f'/sgx/certification/v3/pckcert',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sgx_dcap_server_20200726_models.SimplePackagePckCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def simple_package_pck_cert(
        self,
        request: sgx_dcap_server_20200726_models.SimplePackagePckCertRequest,
    ) -> sgx_dcap_server_20200726_models.SimplePackagePckCertResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.simple_package_pck_cert_with_options(request, headers, runtime)

    async def simple_package_pck_cert_async(
        self,
        request: sgx_dcap_server_20200726_models.SimplePackagePckCertRequest,
    ) -> sgx_dcap_server_20200726_models.SimplePackagePckCertResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.simple_package_pck_cert_with_options_async(request, headers, runtime)
