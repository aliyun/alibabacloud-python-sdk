# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_dataworks_public20200518 import models as dataworks_public_20200518_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "ap-northeast-1": "dataworks.ap-northeast-1.aliyuncs.com",
            "ap-south-1": "dataworks.ap-south-1.aliyuncs.com",
            "ap-southeast-1": "dataworks.ap-southeast-1.aliyuncs.com",
            "ap-southeast-2": "dataworks.ap-southeast-2.aliyuncs.com",
            "ap-southeast-3": "dataworks.ap-southeast-3.aliyuncs.com",
            "ap-southeast-5": "dataworks.ap-southeast-5.aliyuncs.com",
            "cn-beijing": "dataworks.cn-beijing.aliyuncs.com",
            "cn-chengdu": "dataworks.cn-chengdu.aliyuncs.com",
            "cn-hangzhou": "dataworks.cn-hangzhou.aliyuncs.com",
            "cn-hongkong": "dataworks.cn-hongkong.aliyuncs.com",
            "cn-huhehaote": "dataworks.aliyuncs.com",
            "cn-qingdao": "dataworks.aliyuncs.com",
            "cn-shanghai": "dataworks.cn-shanghai.aliyuncs.com",
            "cn-shenzhen": "dataworks.cn-shenzhen.aliyuncs.com",
            "cn-zhangjiakou": "dataworks.aliyuncs.com",
            "eu-central-1": "dataworks.eu-central-1.aliyuncs.com",
            "eu-west-1": "dataworks.eu-west-1.aliyuncs.com",
            "me-east-1": "dataworks.me-east-1.aliyuncs.com",
            "us-east-1": "dataworks.us-east-1.aliyuncs.com",
            "us-west-1": "dataworks.us-west-1.aliyuncs.com",
            "cn-hangzhou-finance": "dataworks.aliyuncs.com",
            "cn-shenzhen-finance-1": "dataworks.aliyuncs.com",
            "cn-shanghai-finance-1": "dataworks.aliyuncs.com",
            "cn-north-2-gov-1": "dataworks.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("dataworks-public", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def list_quality_results_by_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListQualityResultsByEntityResponse().from_map(self.do_request("ListQualityResultsByEntity", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_quality_results_by_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quality_results_by_entity_with_options(request, runtime)

    def get_node_type_list_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetNodeTypeListInfoResponse().from_map(self.do_request("GetNodeTypeListInfo", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_node_type_list_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_type_list_info_with_options(request, runtime)

    def get_instance_status_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetInstanceStatusCountResponse().from_map(self.do_request("GetInstanceStatusCount", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_instance_status_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_status_count_with_options(request, runtime)

    def list_data_service_folders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListDataServiceFoldersResponse().from_map(self.do_request("ListDataServiceFolders", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_data_service_folders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_folders_with_options(request, runtime)

    def list_quality_results_by_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListQualityResultsByRuleResponse().from_map(self.do_request("ListQualityResultsByRule", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_quality_results_by_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quality_results_by_rule_with_options(request, runtime)

    def list_meta_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListMetaDBResponse().from_map(self.do_request("ListMetaDB", "HTTPS", "GET", "2020-05-18", "AK", request.to_map(), None, runtime))

    def list_meta_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_meta_dbwith_options(request, runtime)

    def create_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateTableResponse().from_map(self.do_request("CreateTable", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_table_with_options(request, runtime)

    def create_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateTableThemeResponse().from_map(self.do_request("CreateTableTheme", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_table_theme_with_options(request, runtime)

    def get_instance_error_rank_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetInstanceErrorRankResponse().from_map(self.do_request("GetInstanceErrorRank", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_instance_error_rank(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_error_rank_with_options(request, runtime)

    def get_ddljob_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetDDLJobStatusResponse().from_map(self.do_request("GetDDLJobStatus", "HTTPS", "GET", "2020-05-18", "AK", request.to_map(), None, runtime))

    def get_ddljob_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ddljob_status_with_options(request, runtime)

    def get_instance_consume_time_rank_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetInstanceConsumeTimeRankResponse().from_map(self.do_request("GetInstanceConsumeTimeRank", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_instance_consume_time_rank(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_consume_time_rank_with_options(request, runtime)

    def create_data_service_api_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateDataServiceApiAuthorityResponse().from_map(self.do_request("CreateDataServiceApiAuthority", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_data_service_api_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_api_authority_with_options(request, runtime)

    def delete_data_service_api_authority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteDataServiceApiAuthorityResponse().from_map(self.do_request("DeleteDataServiceApiAuthority", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_data_service_api_authority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_service_api_authority_with_options(request, runtime)

    def create_data_service_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateDataServiceGroupResponse().from_map(self.do_request("CreateDataServiceGroup", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_data_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_group_with_options(request, runtime)

    def update_meta_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateMetaTableResponse().from_map(self.do_request("UpdateMetaTable", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_meta_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_meta_table_with_options(request, runtime)

    def get_instance_count_trend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetInstanceCountTrendResponse().from_map(self.do_request("GetInstanceCountTrend", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_instance_count_trend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_count_trend_with_options(request, runtime)

    def delete_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteTableResponse().from_map(self.do_request("DeleteTable", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_table_with_options(request, runtime)

    def list_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListTableThemeResponse().from_map(self.do_request("ListTableTheme", "HTTPS", "GET", "2020-05-18", "AK", request.to_map(), None, runtime))

    def list_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_table_theme_with_options(request, runtime)

    def get_success_instance_trend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetSuccessInstanceTrendResponse().from_map(self.do_request("GetSuccessInstanceTrend", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_success_instance_trend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_success_instance_trend_with_options(request, runtime)

    def update_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateTableResponse().from_map(self.do_request("UpdateTable", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_with_options(request, runtime)

    def get_data_service_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetDataServiceFolderResponse().from_map(self.do_request("GetDataServiceFolder", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_data_service_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_folder_with_options(request, runtime)

    def list_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListTableLevelResponse().from_map(self.do_request("ListTableLevel", "HTTPS", "GET", "2020-05-18", "AK", request.to_map(), None, runtime))

    def list_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_table_level_with_options(request, runtime)

    def list_data_service_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListDataServiceGroupsResponse().from_map(self.do_request("ListDataServiceGroups", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_data_service_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_groups_with_options(request, runtime)

    def update_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateTableThemeResponse().from_map(self.do_request("UpdateTableTheme", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_theme_with_options(request, runtime)

    def create_data_service_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateDataServiceFolderResponse().from_map(self.do_request("CreateDataServiceFolder", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_data_service_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_folder_with_options(request, runtime)

    def get_data_service_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetDataServiceGroupResponse().from_map(self.do_request("GetDataServiceGroup", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_data_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_group_with_options(request, runtime)

    def create_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateTableLevelResponse().from_map(self.do_request("CreateTableLevel", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_table_level_with_options(request, runtime)

    def update_meta_table_intro_wiki_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateMetaTableIntroWikiResponse().from_map(self.do_request("UpdateMetaTableIntroWiki", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_meta_table_intro_wiki(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_meta_table_intro_wiki_with_options(request, runtime)

    def delete_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteTableLevelResponse().from_map(self.do_request("DeleteTableLevel", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_table_level_with_options(request, runtime)

    def update_table_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateTableLevelResponse().from_map(self.do_request("UpdateTableLevel", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_table_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_level_with_options(request, runtime)

    def delete_table_theme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteTableThemeResponse().from_map(self.do_request("DeleteTableTheme", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_table_theme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_table_theme_with_options(request, runtime)

    def list_program_type_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListProgramTypeCountResponse().from_map(self.do_request("ListProgramTypeCount", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_program_type_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_program_type_count_with_options(request, runtime)

    def update_table_model_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateTableModelInfoResponse().from_map(self.do_request("UpdateTableModelInfo", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_table_model_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_table_model_info_with_options(request, runtime)

    def list_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListProjectsResponse().from_map(self.do_request("ListProjects", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    def list_project_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListProjectMembersResponse().from_map(self.do_request("ListProjectMembers", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_project_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_members_with_options(request, runtime)

    def create_project_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateProjectMemberResponse().from_map(self.do_request("CreateProjectMember", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_project_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_project_member_with_options(request, runtime)

    def list_project_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListProjectRolesResponse().from_map(self.do_request("ListProjectRoles", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_project_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_roles_with_options(request, runtime)

    def add_project_member_to_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.AddProjectMemberToRoleResponse().from_map(self.do_request("AddProjectMemberToRole", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def add_project_member_to_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_project_member_to_role_with_options(request, runtime)

    def remove_project_member_from_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.RemoveProjectMemberFromRoleResponse().from_map(self.do_request("RemoveProjectMemberFromRole", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def remove_project_member_from_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_project_member_from_role_with_options(request, runtime)

    def delete_project_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteProjectMemberResponse().from_map(self.do_request("DeleteProjectMember", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_project_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_project_member_with_options(request, runtime)

    def create_dag_complement_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateDagComplementResponse().from_map(self.do_request("CreateDagComplement", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_dag_complement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dag_complement_with_options(request, runtime)

    def create_dag_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateDagTestResponse().from_map(self.do_request("CreateDagTest", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_dag_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dag_test_with_options(request, runtime)

    def list_calc_engines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListCalcEnginesResponse().from_map(self.do_request("ListCalcEngines", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_calc_engines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_calc_engines_with_options(request, runtime)

    def list_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListConnectionsResponse().from_map(self.do_request("ListConnections", "HTTPS", "GET", "2020-05-18", "AK", request.to_map(), None, runtime))

    def list_connections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_connections_with_options(request, runtime)

    def update_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateConnectionResponse().from_map(self.do_request("UpdateConnection", "HTTPS", "PUT", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_connection_with_options(request, runtime)

    def delete_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteConnectionResponse().from_map(self.do_request("DeleteConnection", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_connection_with_options(request, runtime)

    def get_project_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetProjectDetailResponse().from_map(self.do_request("GetProjectDetail", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_project_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_project_detail_with_options(request, runtime)

    def list_resource_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListResourceGroupsResponse().from_map(self.do_request("ListResourceGroups", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_resource_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    def create_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateConnectionResponse().from_map(self.do_request("CreateConnection", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_connection_with_options(request, runtime)

    def get_data_service_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetDataServiceApplicationResponse().from_map(self.do_request("GetDataServiceApplication", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_data_service_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_application_with_options(request, runtime)

    def list_data_service_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListDataServiceApplicationsResponse().from_map(self.do_request("ListDataServiceApplications", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_data_service_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_applications_with_options(request, runtime)

    def get_node_on_baseline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetNodeOnBaselineResponse().from_map(self.do_request("GetNodeOnBaseline", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_node_on_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_on_baseline_with_options(request, runtime)

    def list_baseline_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListBaselineConfigsResponse().from_map(self.do_request("ListBaselineConfigs", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_baseline_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_baseline_configs_with_options(request, runtime)

    def get_meta_table_change_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaTableChangeLogResponse().from_map(self.do_request("GetMetaTableChangeLog", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_meta_table_change_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_change_log_with_options(request, runtime)

    def get_meta_table_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaTableOutputResponse().from_map(self.do_request("GetMetaTableOutput", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_meta_table_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_output_with_options(request, runtime)

    def get_meta_table_partition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaTablePartitionResponse().from_map(self.do_request("GetMetaTablePartition", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_meta_table_partition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_partition_with_options(request, runtime)

    def get_meta_table_full_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaTableFullInfoResponse().from_map(self.do_request("GetMetaTableFullInfo", "HTTPS", "GET", "2020-05-18", "AK", request.to_map(), None, runtime))

    def get_meta_table_full_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_full_info_with_options(request, runtime)

    def get_file_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetFileVersionResponse().from_map(self.do_request("GetFileVersion", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_file_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_version_with_options(request, runtime)

    def get_meta_table_basic_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaTableBasicInfoResponse().from_map(self.do_request("GetMetaTableBasicInfo", "HTTPS", "GET", "2020-05-18", "AK", request.to_map(), None, runtime))

    def get_meta_table_basic_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_basic_info_with_options(request, runtime)

    def get_meta_table_column_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaTableColumnResponse().from_map(self.do_request("GetMetaTableColumn", "HTTPS", "GET", "2020-05-18", "AK", request.to_map(), None, runtime))

    def get_meta_table_column(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_column_with_options(request, runtime)

    def get_meta_dbinfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaDBInfoResponse().from_map(self.do_request("GetMetaDBInfo", "HTTPS", "GET", "2020-05-18", "AK", request.to_map(), None, runtime))

    def get_meta_dbinfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_dbinfo_with_options(request, runtime)

    def get_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaCategoryResponse().from_map(self.do_request("GetMetaCategory", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_category_with_options(request, runtime)

    def list_alert_messages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListAlertMessagesResponse().from_map(self.do_request("ListAlertMessages", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_alert_messages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alert_messages_with_options(request, runtime)

    def get_baseline_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetBaselineConfigResponse().from_map(self.do_request("GetBaselineConfig", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_baseline_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_config_with_options(request, runtime)

    def search_meta_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.SearchMetaTablesResponse().from_map(self.do_request("SearchMetaTables", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def search_meta_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_meta_tables_with_options(request, runtime)

    def get_meta_table_list_by_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaTableListByCategoryResponse().from_map(self.do_request("GetMetaTableListByCategory", "HTTPS", "GET", "2020-05-18", "AK", request.to_map(), None, runtime))

    def get_meta_table_list_by_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_list_by_category_with_options(request, runtime)

    def delete_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteMetaCategoryResponse().from_map(self.do_request("DeleteMetaCategory", "HTTPS", "GET", "2020-05-18", "AK", request.to_map(), None, runtime))

    def delete_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_meta_category_with_options(request, runtime)

    def update_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateMetaCategoryResponse().from_map(self.do_request("UpdateMetaCategory", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_meta_category_with_options(request, runtime)

    def list_topics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListTopicsResponse().from_map(self.do_request("ListTopics", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_topics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_topics_with_options(request, runtime)

    def list_file_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListFileVersionsResponse().from_map(self.do_request("ListFileVersions", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_file_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_file_versions_with_options(request, runtime)

    def create_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateMetaCategoryResponse().from_map(self.do_request("CreateMetaCategory", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_meta_category_with_options(request, runtime)

    def list_node_iowith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListNodeIOResponse().from_map(self.do_request("ListNodeIO", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_node_io(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_node_iowith_options(request, runtime)

    def get_topic_influence_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetTopicInfluenceResponse().from_map(self.do_request("GetTopicInfluence", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_topic_influence(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_topic_influence_with_options(request, runtime)

    def get_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetTopicResponse().from_map(self.do_request("GetTopic", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_topic_with_options(request, runtime)

    def delete_from_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteFromMetaCategoryResponse().from_map(self.do_request("DeleteFromMetaCategory", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_from_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_from_meta_category_with_options(request, runtime)

    def get_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetNodeResponse().from_map(self.do_request("GetNode", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_with_options(request, runtime)

    def list_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListNodesResponse().from_map(self.do_request("ListNodes", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    def get_node_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetNodeCodeResponse().from_map(self.do_request("GetNodeCode", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_node_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_node_code_with_options(request, runtime)

    def establish_relation_table_to_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.EstablishRelationTableToBusinessResponse().from_map(self.do_request("EstablishRelationTableToBusiness", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def establish_relation_table_to_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.establish_relation_table_to_business_with_options(request, runtime)

    def update_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateDataServiceApiResponse().from_map(self.do_request("UpdateDataServiceApi", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_data_service_api_with_options(request, runtime)

    def update_udf_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateUdfFileResponse().from_map(self.do_request("UpdateUdfFile", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_udf_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_udf_file_with_options(request, runtime)

    def create_udf_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateUdfFileResponse().from_map(self.do_request("CreateUdfFile", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_udf_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_udf_file_with_options(request, runtime)

    def list_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListFilesResponse().from_map(self.do_request("ListFiles", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    def list_data_service_authorized_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListDataServiceAuthorizedApisResponse().from_map(self.do_request("ListDataServiceAuthorizedApis", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_data_service_authorized_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_authorized_apis_with_options(request, runtime)

    def update_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateFileResponse().from_map(self.do_request("UpdateFile", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_file_with_options(request, runtime)

    def delete_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteFolderResponse().from_map(self.do_request("DeleteFolder", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    def list_folders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListFoldersResponse().from_map(self.do_request("ListFolders", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_folders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_folders_with_options(request, runtime)

    def check_meta_partition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CheckMetaPartitionResponse().from_map(self.do_request("CheckMetaPartition", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def check_meta_partition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_meta_partition_with_options(request, runtime)

    def update_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateFolderResponse().from_map(self.do_request("UpdateFolder", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    def delete_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteRemindResponse().from_map(self.do_request("DeleteRemind", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_remind_with_options(request, runtime)

    def add_to_meta_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.AddToMetaCategoryResponse().from_map(self.do_request("AddToMetaCategory", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def add_to_meta_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_to_meta_category_with_options(request, runtime)

    def list_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListInstancesResponse().from_map(self.do_request("ListInstances", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    def set_success_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.SetSuccessInstanceResponse().from_map(self.do_request("SetSuccessInstance", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def set_success_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_success_instance_with_options(request, runtime)

    def create_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateFileResponse().from_map(self.do_request("CreateFile", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_file_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.StopInstanceResponse().from_map(self.do_request("StopInstance", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def stop_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    def resume_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ResumeInstanceResponse().from_map(self.do_request("ResumeInstance", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def resume_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_instance_with_options(request, runtime)

    def suspend_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.SuspendInstanceResponse().from_map(self.do_request("SuspendInstance", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def suspend_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_instance_with_options(request, runtime)

    def restart_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.RestartInstanceResponse().from_map(self.do_request("RestartInstance", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def restart_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    def list_data_service_api_authorities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListDataServiceApiAuthoritiesResponse().from_map(self.do_request("ListDataServiceApiAuthorities", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_data_service_api_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_api_authorities_with_options(request, runtime)

    def list_data_service_published_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListDataServicePublishedApisResponse().from_map(self.do_request("ListDataServicePublishedApis", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_data_service_published_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_published_apis_with_options(request, runtime)

    def get_instance_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetInstanceLogResponse().from_map(self.do_request("GetInstanceLog", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_instance_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_log_with_options(request, runtime)

    def create_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateFolderResponse().from_map(self.do_request("CreateFolder", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    def get_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetBusinessResponse().from_map(self.do_request("GetBusiness", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_with_options(request, runtime)

    def get_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetInstanceResponse().from_map(self.do_request("GetInstance", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    def get_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetFileResponse().from_map(self.do_request("GetFile", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_with_options(request, runtime)

    def list_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListBusinessResponse().from_map(self.do_request("ListBusiness", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_business_with_options(request, runtime)

    def get_meta_dbtable_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaDBTableListResponse().from_map(self.do_request("GetMetaDBTableList", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_meta_dbtable_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_dbtable_list_with_options(request, runtime)

    def check_meta_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CheckMetaTableResponse().from_map(self.do_request("CheckMetaTable", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def check_meta_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_meta_table_with_options(request, runtime)

    def get_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetFolderResponse().from_map(self.do_request("GetFolder", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    def deploy_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeployFileResponse().from_map(self.do_request("DeployFile", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def deploy_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_file_with_options(request, runtime)

    def delete_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteBusinessResponse().from_map(self.do_request("DeleteBusiness", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_business_with_options(request, runtime)

    def delete_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteFileResponse().from_map(self.do_request("DeleteFile", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    def list_quality_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListQualityRulesResponse().from_map(self.do_request("ListQualityRules", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_quality_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quality_rules_with_options(request, runtime)

    def create_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateRemindResponse().from_map(self.do_request("CreateRemind", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_remind_with_options(request, runtime)

    def get_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetQualityRuleResponse().from_map(self.do_request("GetQualityRule", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_with_options(request, runtime)

    def get_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetDeploymentResponse().from_map(self.do_request("GetDeployment", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_deployment_with_options(request, runtime)

    def update_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateRemindResponse().from_map(self.do_request("UpdateRemind", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_remind_with_options(request, runtime)

    def get_meta_column_lineage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaColumnLineageResponse().from_map(self.do_request("GetMetaColumnLineage", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_meta_column_lineage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_column_lineage_with_options(request, runtime)

    def update_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateBusinessResponse().from_map(self.do_request("UpdateBusiness", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_business_with_options(request, runtime)

    def update_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateQualityRuleResponse().from_map(self.do_request("UpdateQualityRule", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_quality_rule_with_options(request, runtime)

    def delete_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteQualityRuleResponse().from_map(self.do_request("DeleteQualityRule", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_rule_with_options(request, runtime)

    def submit_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.SubmitFileResponse().from_map(self.do_request("SubmitFile", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def submit_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_file_with_options(request, runtime)

    def get_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetDataServiceApiResponse().from_map(self.do_request("GetDataServiceApi", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_api_with_options(request, runtime)

    def list_data_service_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListDataServiceApisResponse().from_map(self.do_request("ListDataServiceApis", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_data_service_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_apis_with_options(request, runtime)

    def get_data_service_published_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetDataServicePublishedApiResponse().from_map(self.do_request("GetDataServicePublishedApi", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_data_service_published_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_published_api_with_options(request, runtime)

    def get_baseline_key_path_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetBaselineKeyPathResponse().from_map(self.do_request("GetBaselineKeyPath", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_baseline_key_path(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_key_path_with_options(request, runtime)

    def get_remind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetRemindResponse().from_map(self.do_request("GetRemind", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_remind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_remind_with_options(request, runtime)

    def get_meta_table_intro_wiki_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaTableIntroWikiResponse().from_map(self.do_request("GetMetaTableIntroWiki", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_meta_table_intro_wiki(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_intro_wiki_with_options(request, runtime)

    def get_baseline_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetBaselineStatusResponse().from_map(self.do_request("GetBaselineStatus", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_baseline_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_status_with_options(request, runtime)

    def delete_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteDataServiceApiResponse().from_map(self.do_request("DeleteDataServiceApi", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_service_api_with_options(request, runtime)

    def publish_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.PublishDataServiceApiResponse().from_map(self.do_request("PublishDataServiceApi", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def publish_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_data_service_api_with_options(request, runtime)

    def get_meta_table_lineage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetMetaTableLineageResponse().from_map(self.do_request("GetMetaTableLineage", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_meta_table_lineage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_lineage_with_options(request, runtime)

    def list_baseline_statuses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListBaselineStatusesResponse().from_map(self.do_request("ListBaselineStatuses", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_baseline_statuses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_baseline_statuses_with_options(request, runtime)

    def list_reminds_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.ListRemindsResponse().from_map(self.do_request("ListReminds", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def list_reminds(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_reminds_with_options(request, runtime)

    def delete_quality_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteQualityEntityResponse().from_map(self.do_request("DeleteQualityEntity", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_quality_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_entity_with_options(request, runtime)

    def create_quality_follower_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateQualityFollowerResponse().from_map(self.do_request("CreateQualityFollower", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_quality_follower(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_follower_with_options(request, runtime)

    def create_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateDataServiceApiResponse().from_map(self.do_request("CreateDataServiceApi", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_api_with_options(request, runtime)

    def abolish_data_service_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.AbolishDataServiceApiResponse().from_map(self.do_request("AbolishDataServiceApi", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def abolish_data_service_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.abolish_data_service_api_with_options(request, runtime)

    def get_quality_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetQualityEntityResponse().from_map(self.do_request("GetQualityEntity", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_quality_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_entity_with_options(request, runtime)

    def get_quality_follower_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.GetQualityFollowerResponse().from_map(self.do_request("GetQualityFollower", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def get_quality_follower(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_follower_with_options(request, runtime)

    def delete_quality_follower_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteQualityFollowerResponse().from_map(self.do_request("DeleteQualityFollower", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_quality_follower(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_follower_with_options(request, runtime)

    def create_quality_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateQualityEntityResponse().from_map(self.do_request("CreateQualityEntity", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_quality_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_entity_with_options(request, runtime)

    def create_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateQualityRuleResponse().from_map(self.do_request("CreateQualityRule", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_rule_with_options(request, runtime)

    def update_quality_follower_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.UpdateQualityFollowerResponse().from_map(self.do_request("UpdateQualityFollower", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def update_quality_follower(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_quality_follower_with_options(request, runtime)

    def create_quality_relative_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.CreateQualityRelativeNodeResponse().from_map(self.do_request("CreateQualityRelativeNode", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def create_quality_relative_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_relative_node_with_options(request, runtime)

    def delete_quality_relative_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return dataworks_public_20200518_models.DeleteQualityRelativeNodeResponse().from_map(self.do_request("DeleteQualityRelativeNode", "HTTPS", "POST", "2020-05-18", "AK", None, request.to_map(), runtime))

    def delete_quality_relative_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_relative_node_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
