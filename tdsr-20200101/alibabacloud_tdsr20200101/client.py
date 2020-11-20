# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tdsr20200101 import models as tdsr_20200101_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "cn-hangzhou": "lyj.cn-hangzhou.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("tdsr", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def save_hotspot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.SaveHotspotConfigResponse().from_map(self.do_request("SaveHotspotConfig", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def save_hotspot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_hotspot_config_with_options(request, runtime)

    def get_hotspot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.GetHotspotConfigResponse().from_map(self.do_request("GetHotspotConfig", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def get_hotspot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_config_with_options(request, runtime)

    def list_main_scenes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.ListMainScenesResponse().from_map(self.do_request("ListMainScenes", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def list_main_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_main_scenes_with_options(request, runtime)

    def save_hotspot_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.SaveHotspotTagResponse().from_map(self.do_request("SaveHotspotTag", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def save_hotspot_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_hotspot_tag_with_options(request, runtime)

    def get_scene_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.GetSceneListResponse().from_map(self.do_request("GetSceneList", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def get_scene_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_list_with_options(request, runtime)

    def save_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.SaveFileResponse().from_map(self.do_request("SaveFile", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def save_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_file_with_options(request, runtime)

    def delete_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.DeleteFileResponse().from_map(self.do_request("DeleteFile", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def delete_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    def get_hotspot_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.GetHotspotTagResponse().from_map(self.do_request("GetHotspotTag", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def get_hotspot_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_tag_with_options(request, runtime)

    def get_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.GetPolicyResponse().from_map(self.do_request("GetPolicy", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def get_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    def publish_hotspot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.PublishHotspotResponse().from_map(self.do_request("PublishHotspot", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def publish_hotspot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_hotspot_with_options(request, runtime)

    def get_window_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.GetWindowConfigResponse().from_map(self.do_request("GetWindowConfig", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def get_window_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_window_config_with_options(request, runtime)

    def get_scene_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.GetSceneDataResponse().from_map(self.do_request("GetSceneData", "HTTPS", "POST", "2020-01-01", "AK,APP,PrivateKey,BearerToken", None, request.to_map(), runtime))

    def get_scene_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_data_with_options(request, runtime)

    def check_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.CheckPermissionResponse().from_map(self.do_request("CheckPermission", "HTTPS", "POST", "2020-01-01", "AK", None, request.to_map(), runtime))

    def check_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_permission_with_options(request, runtime)

    def check_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.CheckResourceResponse().from_map(self.do_request("CheckResource", "HTTPS", "POST", "2020-01-01", "AK", None, request.to_map(), runtime))

    def check_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_resource_with_options(request, runtime)

    def create_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.CreateSceneResponse().from_map(self.do_request("CreateScene", "HTTPS", "POST", "2020-01-01", "AK", None, request.to_map(), runtime))

    def create_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scene_with_options(request, runtime)

    def create_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.CreateProjectResponse().from_map(self.do_request("CreateProject", "HTTPS", "POST", "2020-01-01", "AK", None, request.to_map(), runtime))

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    def delete_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.DeleteProjectResponse().from_map(self.do_request("DeleteProject", "HTTPS", "POST", "2020-01-01", "AK", None, request.to_map(), runtime))

    def delete_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    def list_scenes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return tdsr_20200101_models.ListScenesResponse().from_map(self.do_request("ListScenes", "HTTPS", "POST", "2020-01-01", "AK", None, request.to_map(), runtime))

    def list_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_scenes_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
