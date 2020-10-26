# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_vcs20200515 import models as vcs_20200515_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self.check_config(config)
        self._endpoint = self.get_endpoint("vcs", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def unsubscribe_device_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UnsubscribeDeviceEventResponse().from_map(self.do_request("UnsubscribeDeviceEvent", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def unsubscribe_device_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unsubscribe_device_event_with_options(request, runtime)

    def list_subscribe_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListSubscribeDeviceResponse().from_map(self.do_request("ListSubscribeDevice", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def list_subscribe_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_subscribe_device_with_options(request, runtime)

    def subscribe_device_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.SubscribeDeviceEventResponse().from_map(self.do_request("SubscribeDeviceEvent", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def subscribe_device_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.subscribe_device_event_with_options(request, runtime)

    def subscribe_space_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.SubscribeSpaceEventResponse().from_map(self.do_request("SubscribeSpaceEvent", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def subscribe_space_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.subscribe_space_event_with_options(request, runtime)

    def unsubscribe_space_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UnsubscribeSpaceEventResponse().from_map(self.do_request("UnsubscribeSpaceEvent", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def unsubscribe_space_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unsubscribe_space_event_with_options(request, runtime)

    def list_person_trace_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListPersonTraceDetailsResponse().from_map(self.do_request("ListPersonTraceDetails", "HTTPS", "POST", "2020-05-15", "AK,APP", None, request.to_map(), runtime))

    def list_person_trace_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_person_trace_details_with_options(request, runtime)

    def get_monitor_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetMonitorListResponse().from_map(self.do_request("GetMonitorList", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_monitor_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_list_with_options(request, runtime)

    def list_device_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListDeviceGroupsResponse().from_map(self.do_request("ListDeviceGroups", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def list_device_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_groups_with_options(request, runtime)

    def search_object_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = vcs_20200515_models.SearchObjectShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.device_list):
            request.device_list_shrink = UtilClient.to_jsonstring(tmp.device_list)
        if not UtilClient.is_unset(tmp.conditions):
            request.conditions_shrink = UtilClient.to_jsonstring(tmp.conditions)
        if not UtilClient.is_unset(tmp.image_path):
            request.image_path_shrink = UtilClient.to_jsonstring(tmp.image_path)
        return vcs_20200515_models.SearchObjectResponse().from_map(self.do_request("SearchObject", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def search_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_object_with_options(request, runtime)

    def describe_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.DescribeDevicesResponse().from_map(self.do_request("DescribeDevices", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def describe_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_devices_with_options(request, runtime)

    def get_profile_list_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = vcs_20200515_models.GetProfileListShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.person_id_list):
            request.person_id_list_shrink = UtilClient.to_jsonstring(tmp.person_id_list)
        if not UtilClient.is_unset(tmp.profile_id_list):
            request.profile_id_list_shrink = UtilClient.to_jsonstring(tmp.profile_id_list)
        return vcs_20200515_models.GetProfileListResponse().from_map(self.do_request("GetProfileList", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_profile_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_profile_list_with_options(request, runtime)

    def get_profile_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetProfileDetailResponse().from_map(self.do_request("GetProfileDetail", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_profile_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_profile_detail_with_options(request, runtime)

    def delete_profile_catalog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.DeleteProfileCatalogResponse().from_map(self.do_request("DeleteProfileCatalog", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def delete_profile_catalog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_profile_catalog_with_options(request, runtime)

    def bind_person_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.BindPersonResponse().from_map(self.do_request("BindPerson", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def bind_person(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_person_with_options(request, runtime)

    def update_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UpdateProfileResponse().from_map(self.do_request("UpdateProfile", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def update_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_profile_with_options(request, runtime)

    def unbind_person_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UnbindPersonResponse().from_map(self.do_request("UnbindPerson", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def unbind_person(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_person_with_options(request, runtime)

    def add_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.AddProfileResponse().from_map(self.do_request("AddProfile", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def add_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_profile_with_options(request, runtime)

    def update_profile_catalog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UpdateProfileCatalogResponse().from_map(self.do_request("UpdateProfileCatalog", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def update_profile_catalog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_profile_catalog_with_options(request, runtime)

    def add_profile_catalog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.AddProfileCatalogResponse().from_map(self.do_request("AddProfileCatalog", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def add_profile_catalog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_profile_catalog_with_options(request, runtime)

    def get_catalog_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetCatalogListResponse().from_map(self.do_request("GetCatalogList", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_catalog_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_catalog_list_with_options(request, runtime)

    def delete_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.DeleteProfileResponse().from_map(self.do_request("DeleteProfile", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def delete_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_profile_with_options(request, runtime)

    def unbind_corp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UnbindCorpGroupResponse().from_map(self.do_request("UnbindCorpGroup", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def unbind_corp_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_corp_group_with_options(request, runtime)

    def bind_corp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.BindCorpGroupResponse().from_map(self.do_request("BindCorpGroup", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def bind_corp_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_corp_group_with_options(request, runtime)

    def list_user_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListUserGroupsResponse().from_map(self.do_request("ListUserGroups", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def list_user_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    def get_person_list_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = vcs_20200515_models.GetPersonListShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.corp_id_list):
            request.corp_id_list_shrink = UtilClient.to_jsonstring(tmp.corp_id_list)
        if not UtilClient.is_unset(tmp.person_id_list):
            request.person_id_list_shrink = UtilClient.to_jsonstring(tmp.person_id_list)
        return vcs_20200515_models.GetPersonListResponse().from_map(self.do_request("GetPersonList", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_person_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_person_list_with_options(request, runtime)

    def list_users_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = vcs_20200515_models.ListUsersShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.person_list):
            request.person_list_shrink = UtilClient.to_jsonstring(tmp.person_list)
        if not UtilClient.is_unset(tmp.user_list):
            request.user_list_shrink = UtilClient.to_jsonstring(tmp.user_list)
        return vcs_20200515_models.ListUsersResponse().from_map(self.do_request("ListUsers", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.CreateUserResponse().from_map(self.do_request("CreateUser", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def bind_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.BindUserResponse().from_map(self.do_request("BindUser", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def bind_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_user_with_options(request, runtime)

    def get_user_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetUserDetailResponse().from_map(self.do_request("GetUserDetail", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_user_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_detail_with_options(request, runtime)

    def upload_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UploadImageResponse().from_map(self.do_request("UploadImage", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def upload_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_image_with_options(request, runtime)

    def update_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UpdateUserGroupResponse().from_map(self.do_request("UpdateUserGroup", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def update_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    def create_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.CreateUserGroupResponse().from_map(self.do_request("CreateUserGroup", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def create_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    def unbind_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UnbindUserResponse().from_map(self.do_request("UnbindUser", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def unbind_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_user_with_options(request, runtime)

    def update_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UpdateUserResponse().from_map(self.do_request("UpdateUser", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.DeleteUserResponse().from_map(self.do_request("DeleteUser", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def delete_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.DeleteUserGroupResponse().from_map(self.do_request("DeleteUserGroup", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def delete_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    def list_person_visit_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListPersonVisitCountResponse().from_map(self.do_request("ListPersonVisitCount", "HTTPS", "POST", "2020-05-15", "AK,APP", None, request.to_map(), runtime))

    def list_person_visit_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_person_visit_count_with_options(request, runtime)

    def list_event_algorithm_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListEventAlgorithmDetailsResponse().from_map(self.do_request("ListEventAlgorithmDetails", "HTTPS", "POST", "2020-05-15", "AK,APP", None, request.to_map(), runtime))

    def list_event_algorithm_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_event_algorithm_details_with_options(request, runtime)

    def list_corp_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListCorpMetricsResponse().from_map(self.do_request("ListCorpMetrics", "HTTPS", "POST", "2020-05-15", "AK,APP", None, request.to_map(), runtime))

    def list_corp_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_corp_metrics_with_options(request, runtime)

    def list_person_trace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListPersonTraceResponse().from_map(self.do_request("ListPersonTrace", "HTTPS", "POST", "2020-05-15", "AK,APP", None, request.to_map(), runtime))

    def list_person_trace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_person_trace_with_options(request, runtime)

    def list_corp_group_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListCorpGroupMetricsResponse().from_map(self.do_request("ListCorpGroupMetrics", "HTTPS", "POST", "2020-05-15", "AK,APP", None, request.to_map(), runtime))

    def list_corp_group_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_corp_group_metrics_with_options(request, runtime)

    def get_face_model_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetFaceModelResultResponse().from_map(self.do_request("GetFaceModelResult", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_face_model_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_face_model_result_with_options(request, runtime)

    def create_corp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.CreateCorpGroupResponse().from_map(self.do_request("CreateCorpGroup", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def create_corp_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_corp_group_with_options(request, runtime)

    def list_corp_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListCorpGroupsResponse().from_map(self.do_request("ListCorpGroups", "HTTPS", "POST", "2020-05-15", "AK,APP", None, request.to_map(), runtime))

    def list_corp_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_corp_groups_with_options(request, runtime)

    def delete_corp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.DeleteCorpGroupResponse().from_map(self.do_request("DeleteCorpGroup", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def delete_corp_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_corp_group_with_options(request, runtime)

    def invoke_motor_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.InvokeMotorModelResponse().from_map(self.do_request("InvokeMotorModel", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def invoke_motor_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_motor_model_with_options(request, runtime)

    def get_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetDeviceConfigResponse().from_map(self.do_request("GetDeviceConfig", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_config_with_options(request, runtime)

    def sync_device_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.SyncDeviceTimeResponse().from_map(self.do_request("SyncDeviceTime", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def sync_device_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_device_time_with_options(request, runtime)

    def register_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.RegisterDeviceResponse().from_map(self.do_request("RegisterDevice", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def register_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    def report_device_capacity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ReportDeviceCapacityResponse().from_map(self.do_request("ReportDeviceCapacity", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def report_device_capacity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_device_capacity_with_options(request, runtime)

    def save_video_summary_task_video_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.SaveVideoSummaryTaskVideoResponse().from_map(self.do_request("SaveVideoSummaryTaskVideo", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def save_video_summary_task_video(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_video_summary_task_video_with_options(request, runtime)

    def list_body_algorithm_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListBodyAlgorithmResultsResponse().from_map(self.do_request("ListBodyAlgorithmResults", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def list_body_algorithm_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_body_algorithm_results_with_options(request, runtime)

    def add_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.AddDataSourceResponse().from_map(self.do_request("AddDataSource", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def add_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_data_source_with_options(request, runtime)

    def get_video_compose_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetVideoComposeResultResponse().from_map(self.do_request("GetVideoComposeResult", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_video_compose_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_compose_result_with_options(request, runtime)

    def create_video_compose_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.CreateVideoComposeTaskResponse().from_map(self.do_request("CreateVideoComposeTask", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def create_video_compose_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_video_compose_task_with_options(request, runtime)

    def delete_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.DeleteDataSourceResponse().from_map(self.do_request("DeleteDataSource", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def delete_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    def upload_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UploadFileResponse().from_map(self.do_request("UploadFile", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def upload_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_file_with_options(request, runtime)

    def list_event_algorithm_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListEventAlgorithmResultsResponse().from_map(self.do_request("ListEventAlgorithmResults", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def list_event_algorithm_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_event_algorithm_results_with_options(request, runtime)

    def delete_video_summary_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.DeleteVideoSummaryTaskResponse().from_map(self.do_request("DeleteVideoSummaryTask", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def delete_video_summary_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_video_summary_task_with_options(request, runtime)

    def get_video_summary_task_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetVideoSummaryTaskResultResponse().from_map(self.do_request("GetVideoSummaryTaskResult", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_video_summary_task_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_summary_task_result_with_options(request, runtime)

    def create_video_summary_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.CreateVideoSummaryTaskResponse().from_map(self.do_request("CreateVideoSummaryTask", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def create_video_summary_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_video_summary_task_with_options(request, runtime)

    def list_motor_algorithm_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListMotorAlgorithmResultsResponse().from_map(self.do_request("ListMotorAlgorithmResults", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def list_motor_algorithm_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_motor_algorithm_results_with_options(request, runtime)

    def list_face_algorithm_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListFaceAlgorithmResultsResponse().from_map(self.do_request("ListFaceAlgorithmResults", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def list_face_algorithm_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_face_algorithm_results_with_options(request, runtime)

    def list_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListMetricsResponse().from_map(self.do_request("ListMetrics", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def list_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_metrics_with_options(request, runtime)

    def delete_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.DeleteRecordsResponse().from_map(self.do_request("DeleteRecords", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def delete_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_records_with_options(request, runtime)

    def recognize_face_quality_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.RecognizeFaceQualityResponse().from_map(self.do_request("RecognizeFaceQuality", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def recognize_face_quality(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_face_quality_with_options(request, runtime)

    def list_persons_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListPersonsResponse().from_map(self.do_request("ListPersons", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def list_persons(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_persons_with_options(request, runtime)

    def get_person_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetPersonDetailResponse().from_map(self.do_request("GetPersonDetail", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_person_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_person_detail_with_options(request, runtime)

    def get_face_options_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetFaceOptionsResponse().from_map(self.do_request("GetFaceOptions", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_face_options(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_face_options_with_options(request, runtime)

    def get_body_options_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetBodyOptionsResponse().from_map(self.do_request("GetBodyOptions", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_body_options(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_body_options_with_options(request, runtime)

    def stop_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.StopMonitorResponse().from_map(self.do_request("StopMonitor", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def stop_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_monitor_with_options(request, runtime)

    def search_body_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = vcs_20200515_models.SearchBodyShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.option_list):
            request.option_list_shrink = UtilClient.to_jsonstring(tmp.option_list)
        return vcs_20200515_models.SearchBodyResponse().from_map(self.do_request("SearchBody", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def search_body(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_body_with_options(request, runtime)

    def add_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.AddMonitorResponse().from_map(self.do_request("AddMonitor", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def add_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_monitor_with_options(request, runtime)

    def get_monitor_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetMonitorResultResponse().from_map(self.do_request("GetMonitorResult", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_monitor_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_result_with_options(request, runtime)

    def update_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UpdateMonitorResponse().from_map(self.do_request("UpdateMonitor", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def update_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_monitor_with_options(request, runtime)

    def get_device_video_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetDeviceVideoUrlResponse().from_map(self.do_request("GetDeviceVideoUrl", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_device_video_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_video_url_with_options(request, runtime)

    def get_inventory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetInventoryResponse().from_map(self.do_request("GetInventory", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_inventory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_inventory_with_options(request, runtime)

    def recognize_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.RecognizeImageResponse().from_map(self.do_request("RecognizeImage", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def recognize_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_image_with_options(request, runtime)

    def list_corps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListCorpsResponse().from_map(self.do_request("ListCorps", "HTTPS", "POST", "2020-05-15", "AK,APP", None, request.to_map(), runtime))

    def list_corps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_corps_with_options(request, runtime)

    def update_corp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UpdateCorpResponse().from_map(self.do_request("UpdateCorp", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def update_corp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_corp_with_options(request, runtime)

    def update_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.UpdateDeviceResponse().from_map(self.do_request("UpdateDevice", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def update_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_with_options(request, runtime)

    def list_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.ListDevicesResponse().from_map(self.do_request("ListDevices", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def list_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    def get_device_live_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.GetDeviceLiveUrlResponse().from_map(self.do_request("GetDeviceLiveUrl", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def get_device_live_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_live_url_with_options(request, runtime)

    def search_face_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = vcs_20200515_models.SearchFaceShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.option_list):
            request.option_list_shrink = UtilClient.to_jsonstring(tmp.option_list)
        return vcs_20200515_models.SearchFaceResponse().from_map(self.do_request("SearchFace", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def search_face(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_face_with_options(request, runtime)

    def add_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.AddDeviceResponse().from_map(self.do_request("AddDevice", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def add_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_device_with_options(request, runtime)

    def create_corp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.CreateCorpResponse().from_map(self.do_request("CreateCorp", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def create_corp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_corp_with_options(request, runtime)

    def delete_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vcs_20200515_models.DeleteDeviceResponse().from_map(self.do_request("DeleteDevice", "HTTPS", "POST", "2020-05-15", "AK", None, request.to_map(), runtime))

    def delete_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
