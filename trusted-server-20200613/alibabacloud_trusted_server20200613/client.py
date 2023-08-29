# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_trusted_server20200613 import models as trusted_server_20200613_models
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
        self._endpoint = self.get_endpoint('trusted-server', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_boot_with_options(
        self,
        request: trusted_server_20200613_models.DescribeBootRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.DescribeBootResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBoot',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.DescribeBootResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_boot_with_options_async(
        self,
        request: trusted_server_20200613_models.DescribeBootRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.DescribeBootResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBoot',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.DescribeBootResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_boot(
        self,
        request: trusted_server_20200613_models.DescribeBootRequest,
    ) -> trusted_server_20200613_models.DescribeBootResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_boot_with_options(request, runtime)

    async def describe_boot_async(
        self,
        request: trusted_server_20200613_models.DescribeBootRequest,
    ) -> trusted_server_20200613_models.DescribeBootResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_boot_with_options_async(request, runtime)

    def describe_events_with_options(
        self,
        request: trusted_server_20200613_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_date):
            query['CreateEndDate'] = request.create_end_date
        if not UtilClient.is_unset(request.create_start_date):
            query['CreateStartDate'] = request.create_start_date
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_affiliation):
            query['EventAffiliation'] = request.event_affiliation
        if not UtilClient.is_unset(request.event_level):
            query['EventLevel'] = request.event_level
        if not UtilClient.is_unset(request.event_status):
            query['EventStatus'] = request.event_status
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.handle_end_date):
            query['HandleEndDate'] = request.handle_end_date
        if not UtilClient.is_unset(request.handle_start_date):
            query['HandleStartDate'] = request.handle_start_date
        if not UtilClient.is_unset(request.handle_type):
            query['HandleType'] = request.handle_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.property_name):
            query['PropertyName'] = request.property_name
        if not UtilClient.is_unset(request.property_private_ip):
            query['PropertyPrivateIp'] = request.property_private_ip
        if not UtilClient.is_unset(request.property_public_ip):
            query['PropertyPublicIp'] = request.property_public_ip
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        if not UtilClient.is_unset(request.suspect):
            query['Suspect'] = request.suspect
        if not UtilClient.is_unset(request.suspect_sig):
            query['SuspectSig'] = request.suspect_sig
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: trusted_server_20200613_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_end_date):
            query['CreateEndDate'] = request.create_end_date
        if not UtilClient.is_unset(request.create_start_date):
            query['CreateStartDate'] = request.create_start_date
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_affiliation):
            query['EventAffiliation'] = request.event_affiliation
        if not UtilClient.is_unset(request.event_level):
            query['EventLevel'] = request.event_level
        if not UtilClient.is_unset(request.event_status):
            query['EventStatus'] = request.event_status
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.handle_end_date):
            query['HandleEndDate'] = request.handle_end_date
        if not UtilClient.is_unset(request.handle_start_date):
            query['HandleStartDate'] = request.handle_start_date
        if not UtilClient.is_unset(request.handle_type):
            query['HandleType'] = request.handle_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.property_name):
            query['PropertyName'] = request.property_name
        if not UtilClient.is_unset(request.property_private_ip):
            query['PropertyPrivateIp'] = request.property_private_ip
        if not UtilClient.is_unset(request.property_public_ip):
            query['PropertyPublicIp'] = request.property_public_ip
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        if not UtilClient.is_unset(request.suspect):
            query['Suspect'] = request.suspect
        if not UtilClient.is_unset(request.suspect_sig):
            query['SuspectSig'] = request.suspect_sig
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.DescribeEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events(
        self,
        request: trusted_server_20200613_models.DescribeEventsRequest,
    ) -> trusted_server_20200613_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    async def describe_events_async(
        self,
        request: trusted_server_20200613_models.DescribeEventsRequest,
    ) -> trusted_server_20200613_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_events_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: trusted_server_20200613_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: trusted_server_20200613_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: trusted_server_20200613_models.DescribeInstanceRequest,
    ) -> trusted_server_20200613_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: trusted_server_20200613_models.DescribeInstanceRequest,
    ) -> trusted_server_20200613_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def generate_aikcert_with_options(
        self,
        request: trusted_server_20200613_models.GenerateAikcertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.GenerateAikcertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aik_name):
            query['AikName'] = request.aik_name
        if not UtilClient.is_unset(request.aik_pub):
            query['AikPub'] = request.aik_pub
        if not UtilClient.is_unset(request.ek_cert):
            query['EkCert'] = request.ek_cert
        if not UtilClient.is_unset(request.ek_pub):
            query['EkPub'] = request.ek_pub
        if not UtilClient.is_unset(request.nonce_digest):
            query['NonceDigest'] = request.nonce_digest
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAikcert',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.GenerateAikcertResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_aikcert_with_options_async(
        self,
        request: trusted_server_20200613_models.GenerateAikcertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.GenerateAikcertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aik_name):
            query['AikName'] = request.aik_name
        if not UtilClient.is_unset(request.aik_pub):
            query['AikPub'] = request.aik_pub
        if not UtilClient.is_unset(request.ek_cert):
            query['EkCert'] = request.ek_cert
        if not UtilClient.is_unset(request.ek_pub):
            query['EkPub'] = request.ek_pub
        if not UtilClient.is_unset(request.nonce_digest):
            query['NonceDigest'] = request.nonce_digest
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAikcert',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.GenerateAikcertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_aikcert(
        self,
        request: trusted_server_20200613_models.GenerateAikcertRequest,
    ) -> trusted_server_20200613_models.GenerateAikcertResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_aikcert_with_options(request, runtime)

    async def generate_aikcert_async(
        self,
        request: trusted_server_20200613_models.GenerateAikcertRequest,
    ) -> trusted_server_20200613_models.GenerateAikcertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_aikcert_with_options_async(request, runtime)

    def generate_nonce_with_options(
        self,
        request: trusted_server_20200613_models.GenerateNonceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.GenerateNonceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aik_name):
            query['AikName'] = request.aik_name
        if not UtilClient.is_unset(request.ek_cert):
            query['EkCert'] = request.ek_cert
        if not UtilClient.is_unset(request.ek_pub):
            query['EkPub'] = request.ek_pub
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateNonce',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.GenerateNonceResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_nonce_with_options_async(
        self,
        request: trusted_server_20200613_models.GenerateNonceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.GenerateNonceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aik_name):
            query['AikName'] = request.aik_name
        if not UtilClient.is_unset(request.ek_cert):
            query['EkCert'] = request.ek_cert
        if not UtilClient.is_unset(request.ek_pub):
            query['EkPub'] = request.ek_pub
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateNonce',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.GenerateNonceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_nonce(
        self,
        request: trusted_server_20200613_models.GenerateNonceRequest,
    ) -> trusted_server_20200613_models.GenerateNonceResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_nonce_with_options(request, runtime)

    async def generate_nonce_async(
        self,
        request: trusted_server_20200613_models.GenerateNonceRequest,
    ) -> trusted_server_20200613_models.GenerateNonceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_nonce_with_options_async(request, runtime)

    def ignore_events_with_options(
        self,
        request: trusted_server_20200613_models.IgnoreEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.IgnoreEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_uuids):
            query['EventUuids'] = request.event_uuids
        if not UtilClient.is_unset(request.handle_style):
            query['HandleStyle'] = request.handle_style
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IgnoreEvents',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.IgnoreEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def ignore_events_with_options_async(
        self,
        request: trusted_server_20200613_models.IgnoreEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.IgnoreEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_uuids):
            query['EventUuids'] = request.event_uuids
        if not UtilClient.is_unset(request.handle_style):
            query['HandleStyle'] = request.handle_style
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IgnoreEvents',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.IgnoreEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ignore_events(
        self,
        request: trusted_server_20200613_models.IgnoreEventsRequest,
    ) -> trusted_server_20200613_models.IgnoreEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.ignore_events_with_options(request, runtime)

    async def ignore_events_async(
        self,
        request: trusted_server_20200613_models.IgnoreEventsRequest,
    ) -> trusted_server_20200613_models.IgnoreEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ignore_events_with_options_async(request, runtime)

    def produce_aikcert_with_options(
        self,
        request: trusted_server_20200613_models.ProduceAikcertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.ProduceAikcertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aik_name):
            query['AikName'] = request.aik_name
        if not UtilClient.is_unset(request.cert_request):
            query['CertRequest'] = request.cert_request
        if not UtilClient.is_unset(request.ek_cert):
            query['EkCert'] = request.ek_cert
        if not UtilClient.is_unset(request.ek_pub_key):
            query['EkPubKey'] = request.ek_pub_key
        if not UtilClient.is_unset(request.include_cert_chain):
            query['IncludeCertChain'] = request.include_cert_chain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProduceAikcert',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.ProduceAikcertResponse(),
            self.call_api(params, req, runtime)
        )

    async def produce_aikcert_with_options_async(
        self,
        request: trusted_server_20200613_models.ProduceAikcertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.ProduceAikcertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aik_name):
            query['AikName'] = request.aik_name
        if not UtilClient.is_unset(request.cert_request):
            query['CertRequest'] = request.cert_request
        if not UtilClient.is_unset(request.ek_cert):
            query['EkCert'] = request.ek_cert
        if not UtilClient.is_unset(request.ek_pub_key):
            query['EkPubKey'] = request.ek_pub_key
        if not UtilClient.is_unset(request.include_cert_chain):
            query['IncludeCertChain'] = request.include_cert_chain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProduceAikcert',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.ProduceAikcertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def produce_aikcert(
        self,
        request: trusted_server_20200613_models.ProduceAikcertRequest,
    ) -> trusted_server_20200613_models.ProduceAikcertResponse:
        runtime = util_models.RuntimeOptions()
        return self.produce_aikcert_with_options(request, runtime)

    async def produce_aikcert_async(
        self,
        request: trusted_server_20200613_models.ProduceAikcertRequest,
    ) -> trusted_server_20200613_models.ProduceAikcertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.produce_aikcert_with_options_async(request, runtime)

    def put_message_with_options(
        self,
        request: trusted_server_20200613_models.PutMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.PutMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_data):
            query['FileData'] = request.file_data
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMessage',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.PutMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_message_with_options_async(
        self,
        request: trusted_server_20200613_models.PutMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.PutMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_data):
            query['FileData'] = request.file_data
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMessage',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.PutMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_message(
        self,
        request: trusted_server_20200613_models.PutMessageRequest,
    ) -> trusted_server_20200613_models.PutMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_message_with_options(request, runtime)

    async def put_message_async(
        self,
        request: trusted_server_20200613_models.PutMessageRequest,
    ) -> trusted_server_20200613_models.PutMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_message_with_options_async(request, runtime)

    def register_message_with_options(
        self,
        request: trusted_server_20200613_models.RegisterMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.RegisterMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extensions):
            query['Extensions'] = request.extensions
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.property_affiliation):
            query['PropertyAffiliation'] = request.property_affiliation
        if not UtilClient.is_unset(request.property_name):
            query['PropertyName'] = request.property_name
        if not UtilClient.is_unset(request.property_private_ip):
            query['PropertyPrivateIp'] = request.property_private_ip
        if not UtilClient.is_unset(request.property_public_ip):
            query['PropertyPublicIp'] = request.property_public_ip
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterMessage',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.RegisterMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_message_with_options_async(
        self,
        request: trusted_server_20200613_models.RegisterMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.RegisterMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extensions):
            query['Extensions'] = request.extensions
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.property_affiliation):
            query['PropertyAffiliation'] = request.property_affiliation
        if not UtilClient.is_unset(request.property_name):
            query['PropertyName'] = request.property_name
        if not UtilClient.is_unset(request.property_private_ip):
            query['PropertyPrivateIp'] = request.property_private_ip
        if not UtilClient.is_unset(request.property_public_ip):
            query['PropertyPublicIp'] = request.property_public_ip
        if not UtilClient.is_unset(request.property_uuid):
            query['PropertyUuid'] = request.property_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterMessage',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.RegisterMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_message(
        self,
        request: trusted_server_20200613_models.RegisterMessageRequest,
    ) -> trusted_server_20200613_models.RegisterMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_message_with_options(request, runtime)

    async def register_message_async(
        self,
        request: trusted_server_20200613_models.RegisterMessageRequest,
    ) -> trusted_server_20200613_models.RegisterMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_message_with_options_async(request, runtime)

    def trust_events_with_options(
        self,
        request: trusted_server_20200613_models.TrustEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.TrustEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_uuids):
            query['EventUuids'] = request.event_uuids
        if not UtilClient.is_unset(request.handle_style):
            query['HandleStyle'] = request.handle_style
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrustEvents',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.TrustEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def trust_events_with_options_async(
        self,
        request: trusted_server_20200613_models.TrustEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.TrustEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_uuids):
            query['EventUuids'] = request.event_uuids
        if not UtilClient.is_unset(request.handle_style):
            query['HandleStyle'] = request.handle_style
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TrustEvents',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.TrustEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trust_events(
        self,
        request: trusted_server_20200613_models.TrustEventsRequest,
    ) -> trusted_server_20200613_models.TrustEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.trust_events_with_options(request, runtime)

    async def trust_events_async(
        self,
        request: trusted_server_20200613_models.TrustEventsRequest,
    ) -> trusted_server_20200613_models.TrustEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.trust_events_with_options_async(request, runtime)

    def unregister_message_with_options(
        self,
        request: trusted_server_20200613_models.UnregisterMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.UnregisterMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnregisterMessage',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.UnregisterMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def unregister_message_with_options_async(
        self,
        request: trusted_server_20200613_models.UnregisterMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.UnregisterMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnregisterMessage',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.UnregisterMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unregister_message(
        self,
        request: trusted_server_20200613_models.UnregisterMessageRequest,
    ) -> trusted_server_20200613_models.UnregisterMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.unregister_message_with_options(request, runtime)

    async def unregister_message_async(
        self,
        request: trusted_server_20200613_models.UnregisterMessageRequest,
    ) -> trusted_server_20200613_models.UnregisterMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unregister_message_with_options_async(request, runtime)

    def verify_message_with_options(
        self,
        request: trusted_server_20200613_models.VerifyMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.VerifyMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_data):
            body['FileData'] = request.file_data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyMessage',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.VerifyMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_message_with_options_async(
        self,
        request: trusted_server_20200613_models.VerifyMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trusted_server_20200613_models.VerifyMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_data):
            body['FileData'] = request.file_data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyMessage',
            version='2020-06-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            trusted_server_20200613_models.VerifyMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_message(
        self,
        request: trusted_server_20200613_models.VerifyMessageRequest,
    ) -> trusted_server_20200613_models.VerifyMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_message_with_options(request, runtime)

    async def verify_message_async(
        self,
        request: trusted_server_20200613_models.VerifyMessageRequest,
    ) -> trusted_server_20200613_models.VerifyMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_message_with_options_async(request, runtime)
