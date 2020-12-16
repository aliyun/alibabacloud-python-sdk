# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_address_purification20191118 import models as address_purification_20191118_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('address-purification', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_address_geocode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return address_purification_20191118_models.GetAddressGeocodeResponse().from_map(self.do_request('GetAddressGeocode', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def get_address_geocode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_address_geocode_with_options(request, runtime)

    def complete_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return address_purification_20191118_models.CompleteAddressResponse().from_map(self.do_request('CompleteAddress', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def complete_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.complete_address_with_options(request, runtime)

    def get_zipcode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return address_purification_20191118_models.GetZipcodeResponse().from_map(self.do_request('GetZipcode', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def get_zipcode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_zipcode_with_options(request, runtime)

    def extract_phone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return address_purification_20191118_models.ExtractPhoneResponse().from_map(self.do_request('ExtractPhone', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def extract_phone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.extract_phone_with_options(request, runtime)

    def extract_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return address_purification_20191118_models.ExtractNameResponse().from_map(self.do_request('ExtractName', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def extract_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.extract_name_with_options(request, runtime)

    def get_address_division_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return address_purification_20191118_models.GetAddressDivisionCodeResponse().from_map(self.do_request('GetAddressDivisionCode', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def get_address_division_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_address_division_code_with_options(request, runtime)

    def classify_poiwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return address_purification_20191118_models.ClassifyPOIResponse().from_map(self.do_request('ClassifyPOI', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def classify_poi(self, request):
        runtime = util_models.RuntimeOptions()
        return self.classify_poiwith_options(request, runtime)

    def structure_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return address_purification_20191118_models.StructureAddressResponse().from_map(self.do_request('StructureAddress', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def structure_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.structure_address_with_options(request, runtime)

    def extract_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return address_purification_20191118_models.ExtractAddressResponse().from_map(self.do_request('ExtractAddress', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def extract_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.extract_address_with_options(request, runtime)

    def update_project_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = address_purification_20191118_models.UpdateProjectShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.parameters):
            request.parameters_shrink = UtilClient.to_jsonstring(tmp.parameters)
        return address_purification_20191118_models.UpdateProjectResponse().from_map(self.do_request('UpdateProject', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def update_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    def correct_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return address_purification_20191118_models.CorrectAddressResponse().from_map(self.do_request('CorrectAddress', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def correct_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.correct_address_with_options(request, runtime)

    def get_address_similarity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return address_purification_20191118_models.GetAddressSimilarityResponse().from_map(self.do_request('GetAddressSimilarity', 'HTTPS', 'POST', '2019-11-18', 'AK', None, TeaCore.to_map(request), runtime))

    def get_address_similarity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_address_similarity_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
