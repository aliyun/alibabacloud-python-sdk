# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_address_purification20191118 import models as address_purification_20191118_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('address-purification', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_address_division_code_with_options(
        self,
        request: address_purification_20191118_models.GetAddressDivisionCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressDivisionCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressDivisionCodeResponse(),
            self.do_rpcrequest('GetAddressDivisionCode', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_address_division_code_with_options_async(
        self,
        request: address_purification_20191118_models.GetAddressDivisionCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressDivisionCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressDivisionCodeResponse(),
            await self.do_rpcrequest_async('GetAddressDivisionCode', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_division_code(
        self,
        request: address_purification_20191118_models.GetAddressDivisionCodeRequest,
    ) -> address_purification_20191118_models.GetAddressDivisionCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_address_division_code_with_options(request, runtime)

    async def get_address_division_code_async(
        self,
        request: address_purification_20191118_models.GetAddressDivisionCodeRequest,
    ) -> address_purification_20191118_models.GetAddressDivisionCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_address_division_code_with_options_async(request, runtime)

    def structure_address_with_options(
        self,
        request: address_purification_20191118_models.StructureAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.StructureAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.StructureAddressResponse(),
            self.do_rpcrequest('StructureAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def structure_address_with_options_async(
        self,
        request: address_purification_20191118_models.StructureAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.StructureAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.StructureAddressResponse(),
            await self.do_rpcrequest_async('StructureAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def structure_address(
        self,
        request: address_purification_20191118_models.StructureAddressRequest,
    ) -> address_purification_20191118_models.StructureAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.structure_address_with_options(request, runtime)

    async def structure_address_async(
        self,
        request: address_purification_20191118_models.StructureAddressRequest,
    ) -> address_purification_20191118_models.StructureAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.structure_address_with_options_async(request, runtime)

    def extract_express_with_options(
        self,
        request: address_purification_20191118_models.ExtractExpressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractExpressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractExpressResponse(),
            self.do_rpcrequest('ExtractExpress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def extract_express_with_options_async(
        self,
        request: address_purification_20191118_models.ExtractExpressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractExpressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractExpressResponse(),
            await self.do_rpcrequest_async('ExtractExpress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def extract_express(
        self,
        request: address_purification_20191118_models.ExtractExpressRequest,
    ) -> address_purification_20191118_models.ExtractExpressResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_express_with_options(request, runtime)

    async def extract_express_async(
        self,
        request: address_purification_20191118_models.ExtractExpressRequest,
    ) -> address_purification_20191118_models.ExtractExpressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_express_with_options_async(request, runtime)

    def extract_name_with_options(
        self,
        request: address_purification_20191118_models.ExtractNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractNameResponse(),
            self.do_rpcrequest('ExtractName', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def extract_name_with_options_async(
        self,
        request: address_purification_20191118_models.ExtractNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractNameResponse(),
            await self.do_rpcrequest_async('ExtractName', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def extract_name(
        self,
        request: address_purification_20191118_models.ExtractNameRequest,
    ) -> address_purification_20191118_models.ExtractNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_name_with_options(request, runtime)

    async def extract_name_async(
        self,
        request: address_purification_20191118_models.ExtractNameRequest,
    ) -> address_purification_20191118_models.ExtractNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_name_with_options_async(request, runtime)

    def get_address_block_mapping_with_options(
        self,
        request: address_purification_20191118_models.GetAddressBlockMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressBlockMappingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressBlockMappingResponse(),
            self.do_rpcrequest('GetAddressBlockMapping', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_address_block_mapping_with_options_async(
        self,
        request: address_purification_20191118_models.GetAddressBlockMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressBlockMappingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressBlockMappingResponse(),
            await self.do_rpcrequest_async('GetAddressBlockMapping', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_block_mapping(
        self,
        request: address_purification_20191118_models.GetAddressBlockMappingRequest,
    ) -> address_purification_20191118_models.GetAddressBlockMappingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_address_block_mapping_with_options(request, runtime)

    async def get_address_block_mapping_async(
        self,
        request: address_purification_20191118_models.GetAddressBlockMappingRequest,
    ) -> address_purification_20191118_models.GetAddressBlockMappingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_address_block_mapping_with_options_async(request, runtime)

    def get_address_search_with_options(
        self,
        request: address_purification_20191118_models.GetAddressSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressSearchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressSearchResponse(),
            self.do_rpcrequest('GetAddressSearch', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_address_search_with_options_async(
        self,
        request: address_purification_20191118_models.GetAddressSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressSearchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressSearchResponse(),
            await self.do_rpcrequest_async('GetAddressSearch', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_search(
        self,
        request: address_purification_20191118_models.GetAddressSearchRequest,
    ) -> address_purification_20191118_models.GetAddressSearchResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_address_search_with_options(request, runtime)

    async def get_address_search_async(
        self,
        request: address_purification_20191118_models.GetAddressSearchRequest,
    ) -> address_purification_20191118_models.GetAddressSearchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_address_search_with_options_async(request, runtime)

    def predict_poiwith_options(
        self,
        request: address_purification_20191118_models.PredictPOIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.PredictPOIResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.PredictPOIResponse(),
            self.do_rpcrequest('PredictPOI', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def predict_poiwith_options_async(
        self,
        request: address_purification_20191118_models.PredictPOIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.PredictPOIResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.PredictPOIResponse(),
            await self.do_rpcrequest_async('PredictPOI', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def predict_poi(
        self,
        request: address_purification_20191118_models.PredictPOIRequest,
    ) -> address_purification_20191118_models.PredictPOIResponse:
        runtime = util_models.RuntimeOptions()
        return self.predict_poiwith_options(request, runtime)

    async def predict_poi_async(
        self,
        request: address_purification_20191118_models.PredictPOIRequest,
    ) -> address_purification_20191118_models.PredictPOIResponse:
        runtime = util_models.RuntimeOptions()
        return await self.predict_poiwith_options_async(request, runtime)

    def classify_poiwith_options(
        self,
        request: address_purification_20191118_models.ClassifyPOIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ClassifyPOIResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ClassifyPOIResponse(),
            self.do_rpcrequest('ClassifyPOI', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def classify_poiwith_options_async(
        self,
        request: address_purification_20191118_models.ClassifyPOIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ClassifyPOIResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ClassifyPOIResponse(),
            await self.do_rpcrequest_async('ClassifyPOI', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def classify_poi(
        self,
        request: address_purification_20191118_models.ClassifyPOIRequest,
    ) -> address_purification_20191118_models.ClassifyPOIResponse:
        runtime = util_models.RuntimeOptions()
        return self.classify_poiwith_options(request, runtime)

    async def classify_poi_async(
        self,
        request: address_purification_20191118_models.ClassifyPOIRequest,
    ) -> address_purification_20191118_models.ClassifyPOIResponse:
        runtime = util_models.RuntimeOptions()
        return await self.classify_poiwith_options_async(request, runtime)

    def correct_address_with_options(
        self,
        request: address_purification_20191118_models.CorrectAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.CorrectAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.CorrectAddressResponse(),
            self.do_rpcrequest('CorrectAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def correct_address_with_options_async(
        self,
        request: address_purification_20191118_models.CorrectAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.CorrectAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.CorrectAddressResponse(),
            await self.do_rpcrequest_async('CorrectAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def correct_address(
        self,
        request: address_purification_20191118_models.CorrectAddressRequest,
    ) -> address_purification_20191118_models.CorrectAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.correct_address_with_options(request, runtime)

    async def correct_address_async(
        self,
        request: address_purification_20191118_models.CorrectAddressRequest,
    ) -> address_purification_20191118_models.CorrectAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.correct_address_with_options_async(request, runtime)

    def get_zipcode_with_options(
        self,
        request: address_purification_20191118_models.GetZipcodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetZipcodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetZipcodeResponse(),
            self.do_rpcrequest('GetZipcode', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_zipcode_with_options_async(
        self,
        request: address_purification_20191118_models.GetZipcodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetZipcodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetZipcodeResponse(),
            await self.do_rpcrequest_async('GetZipcode', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_zipcode(
        self,
        request: address_purification_20191118_models.GetZipcodeRequest,
    ) -> address_purification_20191118_models.GetZipcodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_zipcode_with_options(request, runtime)

    async def get_zipcode_async(
        self,
        request: address_purification_20191118_models.GetZipcodeRequest,
    ) -> address_purification_20191118_models.GetZipcodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_zipcode_with_options_async(request, runtime)

    def complete_address_with_options(
        self,
        request: address_purification_20191118_models.CompleteAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.CompleteAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.CompleteAddressResponse(),
            self.do_rpcrequest('CompleteAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def complete_address_with_options_async(
        self,
        request: address_purification_20191118_models.CompleteAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.CompleteAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.CompleteAddressResponse(),
            await self.do_rpcrequest_async('CompleteAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def complete_address(
        self,
        request: address_purification_20191118_models.CompleteAddressRequest,
    ) -> address_purification_20191118_models.CompleteAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.complete_address_with_options(request, runtime)

    async def complete_address_async(
        self,
        request: address_purification_20191118_models.CompleteAddressRequest,
    ) -> address_purification_20191118_models.CompleteAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.complete_address_with_options_async(request, runtime)

    def get_address_similarity_with_options(
        self,
        request: address_purification_20191118_models.GetAddressSimilarityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressSimilarityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressSimilarityResponse(),
            self.do_rpcrequest('GetAddressSimilarity', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_address_similarity_with_options_async(
        self,
        request: address_purification_20191118_models.GetAddressSimilarityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressSimilarityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressSimilarityResponse(),
            await self.do_rpcrequest_async('GetAddressSimilarity', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_similarity(
        self,
        request: address_purification_20191118_models.GetAddressSimilarityRequest,
    ) -> address_purification_20191118_models.GetAddressSimilarityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_address_similarity_with_options(request, runtime)

    async def get_address_similarity_async(
        self,
        request: address_purification_20191118_models.GetAddressSimilarityRequest,
    ) -> address_purification_20191118_models.GetAddressSimilarityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_address_similarity_with_options_async(request, runtime)

    def get_address_geocode_with_options(
        self,
        request: address_purification_20191118_models.GetAddressGeocodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressGeocodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressGeocodeResponse(),
            self.do_rpcrequest('GetAddressGeocode', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_address_geocode_with_options_async(
        self,
        request: address_purification_20191118_models.GetAddressGeocodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressGeocodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressGeocodeResponse(),
            await self.do_rpcrequest_async('GetAddressGeocode', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_geocode(
        self,
        request: address_purification_20191118_models.GetAddressGeocodeRequest,
    ) -> address_purification_20191118_models.GetAddressGeocodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_address_geocode_with_options(request, runtime)

    async def get_address_geocode_async(
        self,
        request: address_purification_20191118_models.GetAddressGeocodeRequest,
    ) -> address_purification_20191118_models.GetAddressGeocodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_address_geocode_with_options_async(request, runtime)

    def transfer_coord_with_options(
        self,
        request: address_purification_20191118_models.TransferCoordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.TransferCoordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.TransferCoordResponse(),
            self.do_rpcrequest('TransferCoord', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transfer_coord_with_options_async(
        self,
        request: address_purification_20191118_models.TransferCoordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.TransferCoordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.TransferCoordResponse(),
            await self.do_rpcrequest_async('TransferCoord', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transfer_coord(
        self,
        request: address_purification_20191118_models.TransferCoordRequest,
    ) -> address_purification_20191118_models.TransferCoordResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_coord_with_options(request, runtime)

    async def transfer_coord_async(
        self,
        request: address_purification_20191118_models.TransferCoordRequest,
    ) -> address_purification_20191118_models.TransferCoordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_coord_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        tmp_req: address_purification_20191118_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.UpdateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = address_purification_20191118_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.UpdateProjectResponse(),
            self.do_rpcrequest('UpdateProject', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_with_options_async(
        self,
        tmp_req: address_purification_20191118_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.UpdateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = address_purification_20191118_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.UpdateProjectResponse(),
            await self.do_rpcrequest_async('UpdateProject', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(
        self,
        request: address_purification_20191118_models.UpdateProjectRequest,
    ) -> address_purification_20191118_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: address_purification_20191118_models.UpdateProjectRequest,
    ) -> address_purification_20191118_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def extract_phone_with_options(
        self,
        request: address_purification_20191118_models.ExtractPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractPhoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractPhoneResponse(),
            self.do_rpcrequest('ExtractPhone', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def extract_phone_with_options_async(
        self,
        request: address_purification_20191118_models.ExtractPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractPhoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractPhoneResponse(),
            await self.do_rpcrequest_async('ExtractPhone', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def extract_phone(
        self,
        request: address_purification_20191118_models.ExtractPhoneRequest,
    ) -> address_purification_20191118_models.ExtractPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_phone_with_options(request, runtime)

    async def extract_phone_async(
        self,
        request: address_purification_20191118_models.ExtractPhoneRequest,
    ) -> address_purification_20191118_models.ExtractPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_phone_with_options_async(request, runtime)

    def get_input_search_with_options(
        self,
        request: address_purification_20191118_models.GetInputSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetInputSearchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetInputSearchResponse(),
            self.do_rpcrequest('GetInputSearch', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_input_search_with_options_async(
        self,
        request: address_purification_20191118_models.GetInputSearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetInputSearchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetInputSearchResponse(),
            await self.do_rpcrequest_async('GetInputSearch', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_input_search(
        self,
        request: address_purification_20191118_models.GetInputSearchRequest,
    ) -> address_purification_20191118_models.GetInputSearchResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_input_search_with_options(request, runtime)

    async def get_input_search_async(
        self,
        request: address_purification_20191118_models.GetInputSearchRequest,
    ) -> address_purification_20191118_models.GetInputSearchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_input_search_with_options_async(request, runtime)

    def get_address_evaluate_with_options(
        self,
        request: address_purification_20191118_models.GetAddressEvaluateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressEvaluateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressEvaluateResponse(),
            self.do_rpcrequest('GetAddressEvaluate', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_address_evaluate_with_options_async(
        self,
        request: address_purification_20191118_models.GetAddressEvaluateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.GetAddressEvaluateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressEvaluateResponse(),
            await self.do_rpcrequest_async('GetAddressEvaluate', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_evaluate(
        self,
        request: address_purification_20191118_models.GetAddressEvaluateRequest,
    ) -> address_purification_20191118_models.GetAddressEvaluateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_address_evaluate_with_options(request, runtime)

    async def get_address_evaluate_async(
        self,
        request: address_purification_20191118_models.GetAddressEvaluateRequest,
    ) -> address_purification_20191118_models.GetAddressEvaluateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_address_evaluate_with_options_async(request, runtime)

    def extract_address_with_options(
        self,
        request: address_purification_20191118_models.ExtractAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractAddressResponse(),
            self.do_rpcrequest('ExtractAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def extract_address_with_options_async(
        self,
        request: address_purification_20191118_models.ExtractAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> address_purification_20191118_models.ExtractAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractAddressResponse(),
            await self.do_rpcrequest_async('ExtractAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def extract_address(
        self,
        request: address_purification_20191118_models.ExtractAddressRequest,
    ) -> address_purification_20191118_models.ExtractAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_address_with_options(request, runtime)

    async def extract_address_async(
        self,
        request: address_purification_20191118_models.ExtractAddressRequest,
    ) -> address_purification_20191118_models.ExtractAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_address_with_options_async(request, runtime)
