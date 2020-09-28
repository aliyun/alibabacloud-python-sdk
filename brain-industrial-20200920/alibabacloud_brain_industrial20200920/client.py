# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_brain_industrial20200920 import models as brain_industrial_20200920_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self.check_config(config)
        self._endpoint = self.get_endpoint("brain-industrial", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_op_pv_custom_values(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetOpPvCustomValuesResponse().from_map(self.do_request("GetOpPvCustomValues", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def submit_pid_loop_evaluation(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.SubmitPidLoopEvaluationResponse().from_map(self.do_request("SubmitPidLoopEvaluation", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_default_adjust_values(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetDefaultAdjustValuesResponse().from_map(self.do_request("GetDefaultAdjustValues", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_pv_op_adjust_values(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetPvOpAdjustValuesResponse().from_map(self.do_request("GetPvOpAdjustValues", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_pv_custom_simulation_values(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetPvCustomSimulationValuesResponse().from_map(self.do_request("GetPvCustomSimulationValues", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_identificate_values(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetIdentificateValuesResponse().from_map(self.do_request("GetIdentificateValues", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_pv_ident_simulation_values(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetPvIdentSimulationValuesResponse().from_map(self.do_request("GetPvIdentSimulationValues", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_custom_ident_values(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetCustomIdentValuesResponse().from_map(self.do_request("GetCustomIdentValues", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_pid_project_report_overview(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetPidProjectReportOverviewResponse().from_map(self.do_request("GetPidProjectReportOverview", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_low_model_perform_values(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetLowModelPerformValuesResponse().from_map(self.do_request("GetLowModelPerformValues", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def list_pid_loop_evaluations(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.ListPidLoopEvaluationsResponse().from_map(self.do_request("ListPidLoopEvaluations", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def list_loop_parameter_tag_values(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.ListLoopParameterTagValuesResponse().from_map(self.do_request("ListLoopParameterTagValues", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_pid_loop_parameter(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetPidLoopParameterResponse().from_map(self.do_request("GetPidLoopParameter", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_daily_report_info(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetDailyReportInfoResponse().from_map(self.do_request("GetDailyReportInfo", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_pid_loop(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetPidLoopResponse().from_map(self.do_request("GetPidLoop", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def create_pid_project(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.CreatePidProjectResponse().from_map(self.do_request("CreatePidProject", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def list_ident_models(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.ListIdentModelsResponse().from_map(self.do_request("ListIdentModels", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def list_pid_data_process(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.ListPidDataProcessResponse().from_map(self.do_request("ListPidDataProcess", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def add_custom_ident_model(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.AddCustomIdentModelResponse().from_map(self.do_request("AddCustomIdentModel", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_loop_parameter_step(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetLoopParameterStepResponse().from_map(self.do_request("GetLoopParameterStep", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def list_pid_loops(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.ListPidLoopsResponse().from_map(self.do_request("ListPidLoops", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def move_pid_organization(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.MovePidOrganizationResponse().from_map(self.do_request("MovePidOrganization", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def update_pid_loop(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.UpdatePidLoopResponse().from_map(self.do_request("UpdatePidLoop", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def add_pid_loop_to_schedule(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.AddPidLoopToScheduleResponse().from_map(self.do_request("AddPidLoopToSchedule", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_parsing_tag_task(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetParsingTagTaskResponse().from_map(self.do_request("GetParsingTagTask", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_pid_loop_latest_task_status(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetPidLoopLatestTaskStatusResponse().from_map(self.do_request("GetPidLoopLatestTaskStatus", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def delete_pid_loop(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.DeletePidLoopResponse().from_map(self.do_request("DeletePidLoop", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_summary_report_info(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetSummaryReportInfoResponse().from_map(self.do_request("GetSummaryReportInfo", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_summary_report_data_trend(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetSummaryReportDataTrendResponse().from_map(self.do_request("GetSummaryReportDataTrend", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_summary_report_chart(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetSummaryReportChartResponse().from_map(self.do_request("GetSummaryReportChart", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_daily_report_data_trend(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetDailyReportDataTrendResponse().from_map(self.do_request("GetDailyReportDataTrend", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def list_tag_value_trend(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.ListTagValueTrendResponse().from_map(self.do_request("ListTagValueTrend", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_daily_report_chart(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetDailyReportChartResponse().from_map(self.do_request("GetDailyReportChart", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def list_pid_organizations(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.ListPidOrganizationsResponse().from_map(self.do_request("ListPidOrganizations", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def create_pid_data_processes(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.CreatePidDataProcessesResponse().from_map(self.do_request("CreatePidDataProcesses", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_daily_report_pid_param(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetDailyReportPidParamResponse().from_map(self.do_request("GetDailyReportPidParam", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def add_parameter_to_pid_loop(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.AddParameterToPidLoopResponse().from_map(self.do_request("AddParameterToPidLoop", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def list_pid_projects(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.ListPidProjectsResponse().from_map(self.do_request("ListPidProjects", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def delete_pid_organization(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.DeletePidOrganizationResponse().from_map(self.do_request("DeletePidOrganization", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def set_pid_loop_default_parameter(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.SetPidLoopDefaultParameterResponse().from_map(self.do_request("SetPidLoopDefaultParameter", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_pid_organization_parent_ids(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.GetPidOrganizationParentIdsResponse().from_map(self.do_request("GetPidOrganizationParentIds", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def create_pid_organization(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.CreatePidOrganizationResponse().from_map(self.do_request("CreatePidOrganization", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def update_pid_organization(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.UpdatePidOrganizationResponse().from_map(self.do_request("UpdatePidOrganization", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def create_pid_loop(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.CreatePidLoopResponse().from_map(self.do_request("CreatePidLoop", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def update_pid_project(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.UpdatePidProjectResponse().from_map(self.do_request("UpdatePidProject", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def list_pid_tags(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.ListPidTagsResponse().from_map(self.do_request("ListPidTags", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def delete_pid_data_process(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.DeletePidDataProcessResponse().from_map(self.do_request("DeletePidDataProcess", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def create_pid_data_source(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.CreatePidDataSourceResponse().from_map(self.do_request("CreatePidDataSource", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def create_pid_data_source_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="brain-industrial",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse(

        )
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField(

        )
        oss_header = oss_models.PostObjectRequestHeader(

        )
        upload_request = oss_models.PostObjectRequest(

        )
        oss_runtime = ossutil_models.RuntimeOptions(

        )
        RPCUtilClient.convert(runtime, oss_runtime)
        create_pid_data_sourcereq = brain_industrial_20200920_models.CreatePidDataSourceRequest(

        )
        RPCUtilClient.convert(request, create_pid_data_sourcereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.oss_path_object,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        create_pid_data_sourcereq.oss_path = "http://" + str(auth_response.bucket) + "." + str(auth_response.endpoint) + "/" + str(auth_response.object_key) + ""
        create_pid_data_source_resp = self.create_pid_data_source(create_pid_data_sourcereq, runtime)
        return create_pid_data_source_resp

    def delete_pid_project(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.DeletePidProjectResponse().from_map(self.do_request("DeletePidProject", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def delete_pid_tag(self, request, runtime):
        UtilClient.validate_model(request)
        return brain_industrial_20200920_models.DeletePidTagResponse().from_map(self.do_request("DeletePidTag", "HTTPS", "POST", "2020-09-20", "AK", None, request.to_map(), runtime))

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
