# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_nlp_automl20190701 import models as nlp_automl_20190701_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self.check_config(config)
        self._endpoint = self.get_endpoint("nlp-automl", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def predict_mtmodel_by_doc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return nlp_automl_20190701_models.PredictMTModelByDocResponse().from_map(self.do_request("PredictMTModelByDoc", "HTTPS", "POST", "2019-07-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def predict_mtmodel_by_doc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.predict_mtmodel_by_doc_with_options(request, runtime)

    def bind_intervene_package_and_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return nlp_automl_20190701_models.BindIntervenePackageAndModelResponse().from_map(self.do_request("BindIntervenePackageAndModel", "HTTPS", "POST", "2019-07-01", "AK,APP,PrivateKey", None, request.to_map(), runtime))

    def bind_intervene_package_and_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_intervene_package_and_model_with_options(request, runtime)

    def add_mt_intervene_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return nlp_automl_20190701_models.AddMtIntervenePackageResponse().from_map(self.do_request("AddMtIntervenePackage", "HTTPS", "POST", "2019-07-01", "AK,APP,PrivateKey", None, request.to_map(), runtime))

    def add_mt_intervene_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_mt_intervene_package_with_options(request, runtime)

    def get_predict_doc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return nlp_automl_20190701_models.GetPredictDocResponse().from_map(self.do_request("GetPredictDoc", "HTTPS", "POST", "2019-07-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def get_predict_doc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_predict_doc_with_options(request, runtime)

    def add_mtintervene_word_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return nlp_automl_20190701_models.AddMTInterveneWordResponse().from_map(self.do_request("AddMTInterveneWord", "HTTPS", "POST", "2019-07-01", "AK,APP,PrivateKey", None, request.to_map(), runtime))

    def add_mtintervene_word(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_mtintervene_word_with_options(request, runtime)

    def predict_mtmodel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return nlp_automl_20190701_models.PredictMTModelResponse().from_map(self.do_request("PredictMTModel", "HTTPS", "POST", "2019-07-01", "AK", None, request.to_map(), runtime))

    def predict_mtmodel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.predict_mtmodel_with_options(request, runtime)

    def invoke_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return nlp_automl_20190701_models.InvokeActionResponse().from_map(self.do_request("InvokeAction", "HTTPS", "POST", "2019-07-01", "AK", None, request.to_map(), runtime))

    def invoke_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_action_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
