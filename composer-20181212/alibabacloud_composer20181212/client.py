# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_composer20181212 import models as composer_20181212_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self.check_config(config)
        self._endpoint = self.get_endpoint("composer", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def list_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.ListTemplatesResponse().from_map(self.do_request("ListTemplates", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def list_templates(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.list_templates_with_options(request, runtime)

    def get_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.GetTemplateResponse().from_map(self.do_request("GetTemplate", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def get_template(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_template_with_options(request, runtime)

    def group_invoke_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.GroupInvokeFlowResponse().from_map(self.do_request("GroupInvokeFlow", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def group_invoke_flow(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.group_invoke_flow_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.ListTagResourcesResponse().from_map(self.do_request("ListTagResources", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.list_tag_resources_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.TagResourcesResponse().from_map(self.do_request("TagResources", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.UntagResourcesResponse().from_map(self.do_request("UntagResources", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.untag_resources_with_options(request, runtime)

    def get_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.GetVersionResponse().from_map(self.do_request("GetVersion", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def get_version(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_version_with_options(request, runtime)

    def list_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.ListVersionsResponse().from_map(self.do_request("ListVersions", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def list_versions(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.list_versions_with_options(request, runtime)

    def update_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.UpdateFlowResponse().from_map(self.do_request("UpdateFlow", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def update_flow(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.update_flow_with_options(request, runtime)

    def clone_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.CloneFlowResponse().from_map(self.do_request("CloneFlow", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def clone_flow(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.clone_flow_with_options(request, runtime)

    def get_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.GetFlowResponse().from_map(self.do_request("GetFlow", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def get_flow(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_flow_with_options(request, runtime)

    def list_flows_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.ListFlowsResponse().from_map(self.do_request("ListFlows", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def list_flows(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.list_flows_with_options(request, runtime)

    def delete_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.DeleteFlowResponse().from_map(self.do_request("DeleteFlow", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def delete_flow(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_flow_with_options(request, runtime)

    def disable_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.DisableFlowResponse().from_map(self.do_request("DisableFlow", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def disable_flow(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.disable_flow_with_options(request, runtime)

    def enable_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.EnableFlowResponse().from_map(self.do_request("EnableFlow", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def enable_flow(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.enable_flow_with_options(request, runtime)

    def create_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.CreateFlowResponse().from_map(self.do_request("CreateFlow", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def create_flow(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_flow_with_options(request, runtime)

    def invoke_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return composer_20181212_models.InvokeFlowResponse().from_map(self.do_request("InvokeFlow", "HTTPS", "POST", "2018-12-12", "AK", None, request.to_map(), runtime))

    def invoke_flow(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.invoke_flow_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
