# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sas20181203 import models as sas_20181203_models
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
        self._endpoint_map = {
            'cn-hangzhou': 'tds.aliyuncs.com',
            'ap-southeast-3': 'tds.ap-southeast-3.aliyuncs.com',
            'ap-northeast-1': 'tds.aliyuncs.com',
            'ap-northeast-2-pop': 'tds.aliyuncs.com',
            'ap-south-1': 'tds.aliyuncs.com',
            'ap-southeast-1': 'tds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'tds.aliyuncs.com',
            'ap-southeast-5': 'tds.aliyuncs.com',
            'cn-beijing': 'tds.aliyuncs.com',
            'cn-beijing-finance-1': 'tds.aliyuncs.com',
            'cn-beijing-finance-pop': 'tds.aliyuncs.com',
            'cn-beijing-gov-1': 'tds.aliyuncs.com',
            'cn-beijing-nu16-b01': 'tds.aliyuncs.com',
            'cn-chengdu': 'tds.aliyuncs.com',
            'cn-edge-1': 'tds.aliyuncs.com',
            'cn-fujian': 'tds.aliyuncs.com',
            'cn-haidian-cm12-c01': 'tds.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'tds.aliyuncs.com',
            'cn-hangzhou-finance': 'tds.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'tds.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'tds.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'tds.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'tds.aliyuncs.com',
            'cn-hangzhou-test-306': 'tds.aliyuncs.com',
            'cn-hongkong': 'tds.aliyuncs.com',
            'cn-hongkong-finance-pop': 'tds.aliyuncs.com',
            'cn-huhehaote': 'tds.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'tds.aliyuncs.com',
            'cn-north-2-gov-1': 'tds.aliyuncs.com',
            'cn-qingdao': 'tds.aliyuncs.com',
            'cn-qingdao-nebula': 'tds.aliyuncs.com',
            'cn-shanghai': 'tds.aliyuncs.com',
            'cn-shanghai-et15-b01': 'tds.aliyuncs.com',
            'cn-shanghai-et2-b01': 'tds.aliyuncs.com',
            'cn-shanghai-finance-1': 'tds.aliyuncs.com',
            'cn-shanghai-inner': 'tds.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'tds.aliyuncs.com',
            'cn-shenzhen': 'tds.aliyuncs.com',
            'cn-shenzhen-finance-1': 'tds.aliyuncs.com',
            'cn-shenzhen-inner': 'tds.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'tds.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'tds.aliyuncs.com',
            'cn-wuhan': 'tds.aliyuncs.com',
            'cn-wulanchabu': 'tds.aliyuncs.com',
            'cn-yushanfang': 'tds.aliyuncs.com',
            'cn-zhangbei': 'tds.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'tds.aliyuncs.com',
            'cn-zhangjiakou': 'tds.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'tds.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'tds.aliyuncs.com',
            'eu-central-1': 'tds.aliyuncs.com',
            'eu-west-1': 'tds.aliyuncs.com',
            'eu-west-1-oxs': 'tds.aliyuncs.com',
            'me-east-1': 'tds.aliyuncs.com',
            'rus-west-1-pop': 'tds.aliyuncs.com',
            'us-east-1': 'tds.aliyuncs.com',
            'us-west-1': 'tds.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('sas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_vpc_honey_pot_with_options(
        self,
        request: sas_20181203_models.AddVpcHoneyPotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.AddVpcHoneyPotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_switch_id):
            query['VpcSwitchId'] = request.vpc_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVpcHoneyPot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddVpcHoneyPotResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vpc_honey_pot_with_options_async(
        self,
        request: sas_20181203_models.AddVpcHoneyPotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.AddVpcHoneyPotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_switch_id):
            query['VpcSwitchId'] = request.vpc_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVpcHoneyPot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddVpcHoneyPotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vpc_honey_pot(
        self,
        request: sas_20181203_models.AddVpcHoneyPotRequest,
    ) -> sas_20181203_models.AddVpcHoneyPotResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_vpc_honey_pot_with_options(request, runtime)

    async def add_vpc_honey_pot_async(
        self,
        request: sas_20181203_models.AddVpcHoneyPotRequest,
    ) -> sas_20181203_models.AddVpcHoneyPotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_vpc_honey_pot_with_options_async(request, runtime)

    def check_security_event_id_with_options(
        self,
        request: sas_20181203_models.CheckSecurityEventIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CheckSecurityEventIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSecurityEventId',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CheckSecurityEventIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_security_event_id_with_options_async(
        self,
        request: sas_20181203_models.CheckSecurityEventIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CheckSecurityEventIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSecurityEventId',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CheckSecurityEventIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_security_event_id(
        self,
        request: sas_20181203_models.CheckSecurityEventIdRequest,
    ) -> sas_20181203_models.CheckSecurityEventIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_security_event_id_with_options(request, runtime)

    async def check_security_event_id_async(
        self,
        request: sas_20181203_models.CheckSecurityEventIdRequest,
    ) -> sas_20181203_models.CheckSecurityEventIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_security_event_id_with_options_async(request, runtime)

    def create_anti_brute_force_rule_with_options(
        self,
        request: sas_20181203_models.CreateAntiBruteForceRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateAntiBruteForceRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.fail_count):
            query['FailCount'] = request.fail_count
        if not UtilClient.is_unset(request.forbidden_time):
            query['ForbiddenTime'] = request.forbidden_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.span):
            query['Span'] = request.span
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAntiBruteForceRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateAntiBruteForceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_anti_brute_force_rule_with_options_async(
        self,
        request: sas_20181203_models.CreateAntiBruteForceRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateAntiBruteForceRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.fail_count):
            query['FailCount'] = request.fail_count
        if not UtilClient.is_unset(request.forbidden_time):
            query['ForbiddenTime'] = request.forbidden_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.span):
            query['Span'] = request.span
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAntiBruteForceRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateAntiBruteForceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_anti_brute_force_rule(
        self,
        request: sas_20181203_models.CreateAntiBruteForceRuleRequest,
    ) -> sas_20181203_models.CreateAntiBruteForceRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_anti_brute_force_rule_with_options(request, runtime)

    async def create_anti_brute_force_rule_async(
        self,
        request: sas_20181203_models.CreateAntiBruteForceRuleRequest,
    ) -> sas_20181203_models.CreateAntiBruteForceRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_anti_brute_force_rule_with_options_async(request, runtime)

    def create_backup_policy_with_options(
        self,
        tmp_req: sas_20181203_models.CreateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateBackupPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.CreateBackupPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_shrink):
            query['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.policy_region_id):
            query['PolicyRegionId'] = request.policy_region_id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_policy_with_options_async(
        self,
        tmp_req: sas_20181203_models.CreateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateBackupPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.CreateBackupPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_shrink):
            query['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.policy_region_id):
            query['PolicyRegionId'] = request.policy_region_id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_policy(
        self,
        request: sas_20181203_models.CreateBackupPolicyRequest,
    ) -> sas_20181203_models.CreateBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_policy_with_options(request, runtime)

    async def create_backup_policy_async(
        self,
        request: sas_20181203_models.CreateBackupPolicyRequest,
    ) -> sas_20181203_models.CreateBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_policy_with_options_async(request, runtime)

    def create_or_update_asset_group_with_options(
        self,
        request: sas_20181203_models.CreateOrUpdateAssetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateOrUpdateAssetGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateAssetGroup',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateOrUpdateAssetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_asset_group_with_options_async(
        self,
        request: sas_20181203_models.CreateOrUpdateAssetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateOrUpdateAssetGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateAssetGroup',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateOrUpdateAssetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_asset_group(
        self,
        request: sas_20181203_models.CreateOrUpdateAssetGroupRequest,
    ) -> sas_20181203_models.CreateOrUpdateAssetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_asset_group_with_options(request, runtime)

    async def create_or_update_asset_group_async(
        self,
        request: sas_20181203_models.CreateOrUpdateAssetGroupRequest,
    ) -> sas_20181203_models.CreateOrUpdateAssetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_or_update_asset_group_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateServiceLinkedRoleResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateServiceLinkedRoleResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(self) -> sas_20181203_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(runtime)

    async def create_service_linked_role_async(self) -> sas_20181203_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(runtime)

    def create_similar_security_events_query_task_with_options(
        self,
        request: sas_20181203_models.CreateSimilarSecurityEventsQueryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.similar_event_scenario_code):
            query['SimilarEventScenarioCode'] = request.similar_event_scenario_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimilarSecurityEventsQueryTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_similar_security_events_query_task_with_options_async(
        self,
        request: sas_20181203_models.CreateSimilarSecurityEventsQueryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.similar_event_scenario_code):
            query['SimilarEventScenarioCode'] = request.similar_event_scenario_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimilarSecurityEventsQueryTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_similar_security_events_query_task(
        self,
        request: sas_20181203_models.CreateSimilarSecurityEventsQueryTaskRequest,
    ) -> sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_similar_security_events_query_task_with_options(request, runtime)

    async def create_similar_security_events_query_task_async(
        self,
        request: sas_20181203_models.CreateSimilarSecurityEventsQueryTaskRequest,
    ) -> sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_similar_security_events_query_task_with_options_async(request, runtime)

    def delete_backup_policy_with_options(
        self,
        request: sas_20181203_models.DeleteBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_policy_with_options_async(
        self,
        request: sas_20181203_models.DeleteBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_policy(
        self,
        request: sas_20181203_models.DeleteBackupPolicyRequest,
    ) -> sas_20181203_models.DeleteBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_policy_with_options(request, runtime)

    async def delete_backup_policy_async(
        self,
        request: sas_20181203_models.DeleteBackupPolicyRequest,
    ) -> sas_20181203_models.DeleteBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_policy_with_options_async(request, runtime)

    def delete_backup_policy_machine_with_options(
        self,
        request: sas_20181203_models.DeleteBackupPolicyMachineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteBackupPolicyMachineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPolicyMachine',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteBackupPolicyMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_policy_machine_with_options_async(
        self,
        request: sas_20181203_models.DeleteBackupPolicyMachineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteBackupPolicyMachineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPolicyMachine',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteBackupPolicyMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_policy_machine(
        self,
        request: sas_20181203_models.DeleteBackupPolicyMachineRequest,
    ) -> sas_20181203_models.DeleteBackupPolicyMachineResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_policy_machine_with_options(request, runtime)

    async def delete_backup_policy_machine_async(
        self,
        request: sas_20181203_models.DeleteBackupPolicyMachineRequest,
    ) -> sas_20181203_models.DeleteBackupPolicyMachineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_policy_machine_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: sas_20181203_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: sas_20181203_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: sas_20181203_models.DeleteGroupRequest,
    ) -> sas_20181203_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: sas_20181203_models.DeleteGroupRequest,
    ) -> sas_20181203_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_login_base_config_with_options(
        self,
        request: sas_20181203_models.DeleteLoginBaseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteLoginBaseConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoginBaseConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteLoginBaseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_login_base_config_with_options_async(
        self,
        request: sas_20181203_models.DeleteLoginBaseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteLoginBaseConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoginBaseConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteLoginBaseConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_login_base_config(
        self,
        request: sas_20181203_models.DeleteLoginBaseConfigRequest,
    ) -> sas_20181203_models.DeleteLoginBaseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_login_base_config_with_options(request, runtime)

    async def delete_login_base_config_async(
        self,
        request: sas_20181203_models.DeleteLoginBaseConfigRequest,
    ) -> sas_20181203_models.DeleteLoginBaseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_login_base_config_with_options_async(request, runtime)

    def delete_strategy_with_options(
        self,
        request: sas_20181203_models.DeleteStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_strategy_with_options_async(
        self,
        request: sas_20181203_models.DeleteStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_strategy(
        self,
        request: sas_20181203_models.DeleteStrategyRequest,
    ) -> sas_20181203_models.DeleteStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_strategy_with_options(request, runtime)

    async def delete_strategy_async(
        self,
        request: sas_20181203_models.DeleteStrategyRequest,
    ) -> sas_20181203_models.DeleteStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_strategy_with_options_async(request, runtime)

    def delete_tag_with_uuid_with_options(
        self,
        request: sas_20181203_models.DeleteTagWithUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteTagWithUuidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagWithUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteTagWithUuidResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_with_uuid_with_options_async(
        self,
        request: sas_20181203_models.DeleteTagWithUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteTagWithUuidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagWithUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteTagWithUuidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag_with_uuid(
        self,
        request: sas_20181203_models.DeleteTagWithUuidRequest,
    ) -> sas_20181203_models.DeleteTagWithUuidResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_with_uuid_with_options(request, runtime)

    async def delete_tag_with_uuid_async(
        self,
        request: sas_20181203_models.DeleteTagWithUuidRequest,
    ) -> sas_20181203_models.DeleteTagWithUuidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_with_uuid_with_options_async(request, runtime)

    def delete_vpc_honey_pot_with_options(
        self,
        request: sas_20181203_models.DeleteVpcHoneyPotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteVpcHoneyPotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcHoneyPot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteVpcHoneyPotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_honey_pot_with_options_async(
        self,
        request: sas_20181203_models.DeleteVpcHoneyPotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteVpcHoneyPotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcHoneyPot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteVpcHoneyPotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_honey_pot(
        self,
        request: sas_20181203_models.DeleteVpcHoneyPotRequest,
    ) -> sas_20181203_models.DeleteVpcHoneyPotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_honey_pot_with_options(request, runtime)

    async def delete_vpc_honey_pot_async(
        self,
        request: sas_20181203_models.DeleteVpcHoneyPotRequest,
    ) -> sas_20181203_models.DeleteVpcHoneyPotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_honey_pot_with_options_async(request, runtime)

    def describe_accesskey_leak_list_with_options(
        self,
        request: sas_20181203_models.DescribeAccesskeyLeakListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAccesskeyLeakListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccesskeyLeakList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAccesskeyLeakListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accesskey_leak_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeAccesskeyLeakListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAccesskeyLeakListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccesskeyLeakList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAccesskeyLeakListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accesskey_leak_list(
        self,
        request: sas_20181203_models.DescribeAccesskeyLeakListRequest,
    ) -> sas_20181203_models.DescribeAccesskeyLeakListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accesskey_leak_list_with_options(request, runtime)

    async def describe_accesskey_leak_list_async(
        self,
        request: sas_20181203_models.DescribeAccesskeyLeakListRequest,
    ) -> sas_20181203_models.DescribeAccesskeyLeakListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accesskey_leak_list_with_options_async(request, runtime)

    def describe_affected_malicious_file_images_with_options(
        self,
        request: sas_20181203_models.DescribeAffectedMaliciousFileImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAffectedMaliciousFileImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.image_layer):
            query['ImageLayer'] = request.image_layer
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.malicious_md_5):
            query['MaliciousMd5'] = request.malicious_md_5
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAffectedMaliciousFileImages',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAffectedMaliciousFileImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_affected_malicious_file_images_with_options_async(
        self,
        request: sas_20181203_models.DescribeAffectedMaliciousFileImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAffectedMaliciousFileImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.image_layer):
            query['ImageLayer'] = request.image_layer
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.malicious_md_5):
            query['MaliciousMd5'] = request.malicious_md_5
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAffectedMaliciousFileImages',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAffectedMaliciousFileImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_affected_malicious_file_images(
        self,
        request: sas_20181203_models.DescribeAffectedMaliciousFileImagesRequest,
    ) -> sas_20181203_models.DescribeAffectedMaliciousFileImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_affected_malicious_file_images_with_options(request, runtime)

    async def describe_affected_malicious_file_images_async(
        self,
        request: sas_20181203_models.DescribeAffectedMaliciousFileImagesRequest,
    ) -> sas_20181203_models.DescribeAffectedMaliciousFileImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_affected_malicious_file_images_with_options_async(request, runtime)

    def describe_alarm_event_detail_with_options(
        self,
        request: sas_20181203_models.DescribeAlarmEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAlarmEventDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarmEventDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAlarmEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarm_event_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeAlarmEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAlarmEventDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarmEventDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAlarmEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarm_event_detail(
        self,
        request: sas_20181203_models.DescribeAlarmEventDetailRequest,
    ) -> sas_20181203_models.DescribeAlarmEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_event_detail_with_options(request, runtime)

    async def describe_alarm_event_detail_async(
        self,
        request: sas_20181203_models.DescribeAlarmEventDetailRequest,
    ) -> sas_20181203_models.DescribeAlarmEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarm_event_detail_with_options_async(request, runtime)

    def describe_alarm_event_list_with_options(
        self,
        request: sas_20181203_models.DescribeAlarmEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAlarmEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_event_name):
            query['AlarmEventName'] = request.alarm_event_name
        if not UtilClient.is_unset(request.alarm_event_type):
            query['AlarmEventType'] = request.alarm_event_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.operate_error_code_list):
            query['OperateErrorCodeList'] = request.operate_error_code_list
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarmEventList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAlarmEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarm_event_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeAlarmEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAlarmEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_event_name):
            query['AlarmEventName'] = request.alarm_event_name
        if not UtilClient.is_unset(request.alarm_event_type):
            query['AlarmEventType'] = request.alarm_event_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.operate_error_code_list):
            query['OperateErrorCodeList'] = request.operate_error_code_list
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarmEventList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAlarmEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarm_event_list(
        self,
        request: sas_20181203_models.DescribeAlarmEventListRequest,
    ) -> sas_20181203_models.DescribeAlarmEventListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_event_list_with_options(request, runtime)

    async def describe_alarm_event_list_async(
        self,
        request: sas_20181203_models.DescribeAlarmEventListRequest,
    ) -> sas_20181203_models.DescribeAlarmEventListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarm_event_list_with_options_async(request, runtime)

    def describe_all_entity_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAllEntityResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAllEntity',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAllEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_entity_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAllEntityResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAllEntity',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAllEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_entity(self) -> sas_20181203_models.DescribeAllEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_entity_with_options(runtime)

    async def describe_all_entity_async(self) -> sas_20181203_models.DescribeAllEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_entity_with_options_async(runtime)

    def describe_all_groups_with_options(
        self,
        request: sas_20181203_models.DescribeAllGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAllGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllGroups',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAllGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_groups_with_options_async(
        self,
        request: sas_20181203_models.DescribeAllGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAllGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllGroups',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAllGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_groups(
        self,
        request: sas_20181203_models.DescribeAllGroupsRequest,
    ) -> sas_20181203_models.DescribeAllGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_groups_with_options(request, runtime)

    async def describe_all_groups_async(
        self,
        request: sas_20181203_models.DescribeAllGroupsRequest,
    ) -> sas_20181203_models.DescribeAllGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_groups_with_options_async(request, runtime)

    def describe_anti_brute_force_rules_with_options(
        self,
        request: sas_20181203_models.DescribeAntiBruteForceRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAntiBruteForceRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAntiBruteForceRules',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAntiBruteForceRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_anti_brute_force_rules_with_options_async(
        self,
        request: sas_20181203_models.DescribeAntiBruteForceRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAntiBruteForceRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAntiBruteForceRules',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAntiBruteForceRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_anti_brute_force_rules(
        self,
        request: sas_20181203_models.DescribeAntiBruteForceRulesRequest,
    ) -> sas_20181203_models.DescribeAntiBruteForceRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_anti_brute_force_rules_with_options(request, runtime)

    async def describe_anti_brute_force_rules_async(
        self,
        request: sas_20181203_models.DescribeAntiBruteForceRulesRequest,
    ) -> sas_20181203_models.DescribeAntiBruteForceRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_anti_brute_force_rules_with_options_async(request, runtime)

    def describe_asset_detail_by_uuid_with_options(
        self,
        request: sas_20181203_models.DescribeAssetDetailByUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAssetDetailByUuidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetDetailByUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetDetailByUuidResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_detail_by_uuid_with_options_async(
        self,
        request: sas_20181203_models.DescribeAssetDetailByUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAssetDetailByUuidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetDetailByUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetDetailByUuidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_detail_by_uuid(
        self,
        request: sas_20181203_models.DescribeAssetDetailByUuidRequest,
    ) -> sas_20181203_models.DescribeAssetDetailByUuidResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_detail_by_uuid_with_options(request, runtime)

    async def describe_asset_detail_by_uuid_async(
        self,
        request: sas_20181203_models.DescribeAssetDetailByUuidRequest,
    ) -> sas_20181203_models.DescribeAssetDetailByUuidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_asset_detail_by_uuid_with_options_async(request, runtime)

    def describe_asset_detail_by_uuids_with_options(
        self,
        request: sas_20181203_models.DescribeAssetDetailByUuidsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAssetDetailByUuidsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetDetailByUuids',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetDetailByUuidsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_detail_by_uuids_with_options_async(
        self,
        request: sas_20181203_models.DescribeAssetDetailByUuidsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAssetDetailByUuidsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetDetailByUuids',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetDetailByUuidsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_detail_by_uuids(
        self,
        request: sas_20181203_models.DescribeAssetDetailByUuidsRequest,
    ) -> sas_20181203_models.DescribeAssetDetailByUuidsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_detail_by_uuids_with_options(request, runtime)

    async def describe_asset_detail_by_uuids_async(
        self,
        request: sas_20181203_models.DescribeAssetDetailByUuidsRequest,
    ) -> sas_20181203_models.DescribeAssetDetailByUuidsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_asset_detail_by_uuids_with_options_async(request, runtime)

    def describe_asset_summary_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAssetSummaryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAssetSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_summary_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAssetSummaryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAssetSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_summary(self) -> sas_20181203_models.DescribeAssetSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_summary_with_options(runtime)

    async def describe_asset_summary_async(self) -> sas_20181203_models.DescribeAssetSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_asset_summary_with_options_async(runtime)

    def describe_attack_analysis_data_with_options(
        self,
        request: sas_20181203_models.DescribeAttackAnalysisDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAttackAnalysisDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_64):
            query['Base64'] = request.base_64
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackAnalysisData',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAttackAnalysisDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_attack_analysis_data_with_options_async(
        self,
        request: sas_20181203_models.DescribeAttackAnalysisDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAttackAnalysisDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_64):
            query['Base64'] = request.base_64
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackAnalysisData',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAttackAnalysisDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_attack_analysis_data(
        self,
        request: sas_20181203_models.DescribeAttackAnalysisDataRequest,
    ) -> sas_20181203_models.DescribeAttackAnalysisDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_attack_analysis_data_with_options(request, runtime)

    async def describe_attack_analysis_data_async(
        self,
        request: sas_20181203_models.DescribeAttackAnalysisDataRequest,
    ) -> sas_20181203_models.DescribeAttackAnalysisDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_attack_analysis_data_with_options_async(request, runtime)

    def describe_auto_del_config_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAutoDelConfigResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAutoDelConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAutoDelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_del_config_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAutoDelConfigResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAutoDelConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAutoDelConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_del_config(self) -> sas_20181203_models.DescribeAutoDelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_del_config_with_options(runtime)

    async def describe_auto_del_config_async(self) -> sas_20181203_models.DescribeAutoDelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_del_config_with_options_async(runtime)

    def describe_backup_clients_with_options(
        self,
        request: sas_20181203_models.DescribeBackupClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBackupClientsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.support_region_id):
            query['SupportRegionId'] = request.support_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupClients',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_clients_with_options_async(
        self,
        request: sas_20181203_models.DescribeBackupClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBackupClientsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.support_region_id):
            query['SupportRegionId'] = request.support_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupClients',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_clients(
        self,
        request: sas_20181203_models.DescribeBackupClientsRequest,
    ) -> sas_20181203_models.DescribeBackupClientsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_clients_with_options(request, runtime)

    async def describe_backup_clients_async(
        self,
        request: sas_20181203_models.DescribeBackupClientsRequest,
    ) -> sas_20181203_models.DescribeBackupClientsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_clients_with_options_async(request, runtime)

    def describe_backup_files_with_options(
        self,
        request: sas_20181203_models.DescribeBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBackupFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.snapshot_hash):
            query['SnapshotHash'] = request.snapshot_hash
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupFiles',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_files_with_options_async(
        self,
        request: sas_20181203_models.DescribeBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBackupFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.snapshot_hash):
            query['SnapshotHash'] = request.snapshot_hash
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupFiles',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_files(
        self,
        request: sas_20181203_models.DescribeBackupFilesRequest,
    ) -> sas_20181203_models.DescribeBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_files_with_options(request, runtime)

    async def describe_backup_files_async(
        self,
        request: sas_20181203_models.DescribeBackupFilesRequest,
    ) -> sas_20181203_models.DescribeBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_files_with_options_async(request, runtime)

    def describe_backup_policies_with_options(
        self,
        request: sas_20181203_models.DescribeBackupPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBackupPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.machine_remark):
            query['MachineRemark'] = request.machine_remark
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicies',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policies_with_options_async(
        self,
        request: sas_20181203_models.DescribeBackupPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBackupPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.machine_remark):
            query['MachineRemark'] = request.machine_remark
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicies',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policies(
        self,
        request: sas_20181203_models.DescribeBackupPoliciesRequest,
    ) -> sas_20181203_models.DescribeBackupPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policies_with_options(request, runtime)

    async def describe_backup_policies_async(
        self,
        request: sas_20181203_models.DescribeBackupPoliciesRequest,
    ) -> sas_20181203_models.DescribeBackupPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policies_with_options_async(request, runtime)

    def describe_backup_restore_count_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBackupRestoreCountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeBackupRestoreCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupRestoreCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_restore_count_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBackupRestoreCountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeBackupRestoreCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupRestoreCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_restore_count(self) -> sas_20181203_models.DescribeBackupRestoreCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_restore_count_with_options(runtime)

    async def describe_backup_restore_count_async(self) -> sas_20181203_models.DescribeBackupRestoreCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_restore_count_with_options_async(runtime)

    def describe_brute_force_summary_with_options(
        self,
        request: sas_20181203_models.DescribeBruteForceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBruteForceSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBruteForceSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBruteForceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_brute_force_summary_with_options_async(
        self,
        request: sas_20181203_models.DescribeBruteForceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBruteForceSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBruteForceSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBruteForceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_brute_force_summary(
        self,
        request: sas_20181203_models.DescribeBruteForceSummaryRequest,
    ) -> sas_20181203_models.DescribeBruteForceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_brute_force_summary_with_options(request, runtime)

    async def describe_brute_force_summary_async(
        self,
        request: sas_20181203_models.DescribeBruteForceSummaryRequest,
    ) -> sas_20181203_models.DescribeBruteForceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_brute_force_summary_with_options_async(request, runtime)

    def describe_check_ecs_warnings_with_options(
        self,
        request: sas_20181203_models.DescribeCheckEcsWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckEcsWarningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckEcsWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckEcsWarningsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_check_ecs_warnings_with_options_async(
        self,
        request: sas_20181203_models.DescribeCheckEcsWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckEcsWarningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckEcsWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckEcsWarningsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_check_ecs_warnings(
        self,
        request: sas_20181203_models.DescribeCheckEcsWarningsRequest,
    ) -> sas_20181203_models.DescribeCheckEcsWarningsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_check_ecs_warnings_with_options(request, runtime)

    async def describe_check_ecs_warnings_async(
        self,
        request: sas_20181203_models.DescribeCheckEcsWarningsRequest,
    ) -> sas_20181203_models.DescribeCheckEcsWarningsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_check_ecs_warnings_with_options_async(request, runtime)

    def describe_check_warning_detail_with_options(
        self,
        request: sas_20181203_models.DescribeCheckWarningDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckWarningDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_warning_id):
            query['CheckWarningId'] = request.check_warning_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckWarningDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_check_warning_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeCheckWarningDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckWarningDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_warning_id):
            query['CheckWarningId'] = request.check_warning_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckWarningDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_check_warning_detail(
        self,
        request: sas_20181203_models.DescribeCheckWarningDetailRequest,
    ) -> sas_20181203_models.DescribeCheckWarningDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_check_warning_detail_with_options(request, runtime)

    async def describe_check_warning_detail_async(
        self,
        request: sas_20181203_models.DescribeCheckWarningDetailRequest,
    ) -> sas_20181203_models.DescribeCheckWarningDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_check_warning_detail_with_options_async(request, runtime)

    def describe_check_warning_summary_with_options(
        self,
        request: sas_20181203_models.DescribeCheckWarningSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckWarningSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_name):
            query['RiskName'] = request.risk_name
        if not UtilClient.is_unset(request.risk_status):
            query['RiskStatus'] = request.risk_status
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.type_name):
            query['TypeName'] = request.type_name
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckWarningSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_check_warning_summary_with_options_async(
        self,
        request: sas_20181203_models.DescribeCheckWarningSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckWarningSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_name):
            query['RiskName'] = request.risk_name
        if not UtilClient.is_unset(request.risk_status):
            query['RiskStatus'] = request.risk_status
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.type_name):
            query['TypeName'] = request.type_name
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckWarningSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_check_warning_summary(
        self,
        request: sas_20181203_models.DescribeCheckWarningSummaryRequest,
    ) -> sas_20181203_models.DescribeCheckWarningSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_check_warning_summary_with_options(request, runtime)

    async def describe_check_warning_summary_async(
        self,
        request: sas_20181203_models.DescribeCheckWarningSummaryRequest,
    ) -> sas_20181203_models.DescribeCheckWarningSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_check_warning_summary_with_options_async(request, runtime)

    def describe_check_warnings_with_options(
        self,
        request: sas_20181203_models.DescribeCheckWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckWarningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_check_warnings_with_options_async(
        self,
        request: sas_20181203_models.DescribeCheckWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckWarningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_check_warnings(
        self,
        request: sas_20181203_models.DescribeCheckWarningsRequest,
    ) -> sas_20181203_models.DescribeCheckWarningsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_check_warnings_with_options(request, runtime)

    async def describe_check_warnings_async(
        self,
        request: sas_20181203_models.DescribeCheckWarningsRequest,
    ) -> sas_20181203_models.DescribeCheckWarningsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_check_warnings_with_options_async(request, runtime)

    def describe_cloud_center_instances_with_options(
        self,
        request: sas_20181203_models.DescribeCloudCenterInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCloudCenterInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.importance):
            query['Importance'] = request.importance
        if not UtilClient.is_unset(request.logical_exp):
            query['LogicalExp'] = request.logical_exp
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.no_group_trace):
            query['NoGroupTrace'] = request.no_group_trace
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudCenterInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCloudCenterInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_center_instances_with_options_async(
        self,
        request: sas_20181203_models.DescribeCloudCenterInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCloudCenterInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.importance):
            query['Importance'] = request.importance
        if not UtilClient.is_unset(request.logical_exp):
            query['LogicalExp'] = request.logical_exp
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.no_group_trace):
            query['NoGroupTrace'] = request.no_group_trace
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudCenterInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCloudCenterInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_center_instances(
        self,
        request: sas_20181203_models.DescribeCloudCenterInstancesRequest,
    ) -> sas_20181203_models.DescribeCloudCenterInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_center_instances_with_options(request, runtime)

    async def describe_cloud_center_instances_async(
        self,
        request: sas_20181203_models.DescribeCloudCenterInstancesRequest,
    ) -> sas_20181203_models.DescribeCloudCenterInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_center_instances_with_options_async(request, runtime)

    def describe_cloud_product_field_statistics_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCloudProductFieldStatisticsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCloudProductFieldStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCloudProductFieldStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_product_field_statistics_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCloudProductFieldStatisticsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCloudProductFieldStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCloudProductFieldStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_product_field_statistics(self) -> sas_20181203_models.DescribeCloudProductFieldStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_product_field_statistics_with_options(runtime)

    async def describe_cloud_product_field_statistics_async(self) -> sas_20181203_models.DescribeCloudProductFieldStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_product_field_statistics_with_options_async(runtime)

    def describe_concern_necessity_with_options(
        self,
        request: sas_20181203_models.DescribeConcernNecessityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeConcernNecessityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConcernNecessity',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeConcernNecessityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_concern_necessity_with_options_async(
        self,
        request: sas_20181203_models.DescribeConcernNecessityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeConcernNecessityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConcernNecessity',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeConcernNecessityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_concern_necessity(
        self,
        request: sas_20181203_models.DescribeConcernNecessityRequest,
    ) -> sas_20181203_models.DescribeConcernNecessityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_concern_necessity_with_options(request, runtime)

    async def describe_concern_necessity_async(
        self,
        request: sas_20181203_models.DescribeConcernNecessityRequest,
    ) -> sas_20181203_models.DescribeConcernNecessityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_concern_necessity_with_options_async(request, runtime)

    def describe_container_statistics_with_options(
        self,
        request: sas_20181203_models.DescribeContainerStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeContainerStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeContainerStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_container_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeContainerStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeContainerStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeContainerStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_container_statistics(
        self,
        request: sas_20181203_models.DescribeContainerStatisticsRequest,
    ) -> sas_20181203_models.DescribeContainerStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_container_statistics_with_options(request, runtime)

    async def describe_container_statistics_async(
        self,
        request: sas_20181203_models.DescribeContainerStatisticsRequest,
    ) -> sas_20181203_models.DescribeContainerStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_statistics_with_options_async(request, runtime)

    def describe_criteria_with_options(
        self,
        request: sas_20181203_models.DescribeCriteriaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCriteriaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.support_auto_tag):
            query['SupportAutoTag'] = request.support_auto_tag
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCriteriaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_criteria_with_options_async(
        self,
        request: sas_20181203_models.DescribeCriteriaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCriteriaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.support_auto_tag):
            query['SupportAutoTag'] = request.support_auto_tag
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCriteriaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_criteria(
        self,
        request: sas_20181203_models.DescribeCriteriaRequest,
    ) -> sas_20181203_models.DescribeCriteriaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_criteria_with_options(request, runtime)

    async def describe_criteria_async(
        self,
        request: sas_20181203_models.DescribeCriteriaRequest,
    ) -> sas_20181203_models.DescribeCriteriaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_criteria_with_options_async(request, runtime)

    def describe_dialog_messages_with_options(
        self,
        request: sas_20181203_models.DescribeDialogMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDialogMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDialogMessages',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDialogMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dialog_messages_with_options_async(
        self,
        request: sas_20181203_models.DescribeDialogMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDialogMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDialogMessages',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDialogMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dialog_messages(
        self,
        request: sas_20181203_models.DescribeDialogMessagesRequest,
    ) -> sas_20181203_models.DescribeDialogMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dialog_messages_with_options(request, runtime)

    async def describe_dialog_messages_async(
        self,
        request: sas_20181203_models.DescribeDialogMessagesRequest,
    ) -> sas_20181203_models.DescribeDialogMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dialog_messages_with_options_async(request, runtime)

    def describe_ding_talk_with_options(
        self,
        request: sas_20181203_models.DescribeDingTalkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDingTalkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_action_name):
            query['RuleActionName'] = request.rule_action_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDingTalk',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDingTalkResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ding_talk_with_options_async(
        self,
        request: sas_20181203_models.DescribeDingTalkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDingTalkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_action_name):
            query['RuleActionName'] = request.rule_action_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDingTalk',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDingTalkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ding_talk(
        self,
        request: sas_20181203_models.DescribeDingTalkRequest,
    ) -> sas_20181203_models.DescribeDingTalkResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ding_talk_with_options(request, runtime)

    async def describe_ding_talk_async(
        self,
        request: sas_20181203_models.DescribeDingTalkRequest,
    ) -> sas_20181203_models.DescribeDingTalkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ding_talk_with_options_async(request, runtime)

    def describe_domain_count_with_options(
        self,
        request: sas_20181203_models.DescribeDomainCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDomainCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_count_with_options_async(
        self,
        request: sas_20181203_models.DescribeDomainCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDomainCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_count(
        self,
        request: sas_20181203_models.DescribeDomainCountRequest,
    ) -> sas_20181203_models.DescribeDomainCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_count_with_options(request, runtime)

    async def describe_domain_count_async(
        self,
        request: sas_20181203_models.DescribeDomainCountRequest,
    ) -> sas_20181203_models.DescribeDomainCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_count_with_options_async(request, runtime)

    def describe_domain_detail_with_options(
        self,
        request: sas_20181203_models.DescribeDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDomainDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDomainDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_detail(
        self,
        request: sas_20181203_models.DescribeDomainDetailRequest,
    ) -> sas_20181203_models.DescribeDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_detail_with_options(request, runtime)

    async def describe_domain_detail_async(
        self,
        request: sas_20181203_models.DescribeDomainDetailRequest,
    ) -> sas_20181203_models.DescribeDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_detail_with_options_async(request, runtime)

    def describe_domain_list_with_options(
        self,
        request: sas_20181203_models.DescribeDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDomainListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.fuzzy_domain):
            query['FuzzyDomain'] = request.fuzzy_domain
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDomainListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.fuzzy_domain):
            query['FuzzyDomain'] = request.fuzzy_domain
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_list(
        self,
        request: sas_20181203_models.DescribeDomainListRequest,
    ) -> sas_20181203_models.DescribeDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_list_with_options(request, runtime)

    async def describe_domain_list_async(
        self,
        request: sas_20181203_models.DescribeDomainListRequest,
    ) -> sas_20181203_models.DescribeDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_list_with_options_async(request, runtime)

    def describe_emg_vul_item_with_options(
        self,
        request: sas_20181203_models.DescribeEmgVulItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeEmgVulItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_status):
            query['RiskStatus'] = request.risk_status
        if not UtilClient.is_unset(request.scan_type):
            query['ScanType'] = request.scan_type
        if not UtilClient.is_unset(request.vul_name):
            query['VulName'] = request.vul_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEmgVulItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeEmgVulItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_emg_vul_item_with_options_async(
        self,
        request: sas_20181203_models.DescribeEmgVulItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeEmgVulItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_status):
            query['RiskStatus'] = request.risk_status
        if not UtilClient.is_unset(request.scan_type):
            query['ScanType'] = request.scan_type
        if not UtilClient.is_unset(request.vul_name):
            query['VulName'] = request.vul_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEmgVulItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeEmgVulItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_emg_vul_item(
        self,
        request: sas_20181203_models.DescribeEmgVulItemRequest,
    ) -> sas_20181203_models.DescribeEmgVulItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_emg_vul_item_with_options(request, runtime)

    async def describe_emg_vul_item_async(
        self,
        request: sas_20181203_models.DescribeEmgVulItemRequest,
    ) -> sas_20181203_models.DescribeEmgVulItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_emg_vul_item_with_options_async(request, runtime)

    def describe_export_info_with_options(
        self,
        request: sas_20181203_models.DescribeExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExportInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_export_info_with_options_async(
        self,
        request: sas_20181203_models.DescribeExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExportInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExportInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_export_info(
        self,
        request: sas_20181203_models.DescribeExportInfoRequest,
    ) -> sas_20181203_models.DescribeExportInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_export_info_with_options(request, runtime)

    async def describe_export_info_async(
        self,
        request: sas_20181203_models.DescribeExportInfoRequest,
    ) -> sas_20181203_models.DescribeExportInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_export_info_with_options_async(request, runtime)

    def describe_exposed_instance_criteria_with_options(
        self,
        request: sas_20181203_models.DescribeExposedInstanceCriteriaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedInstanceCriteriaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedInstanceCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceCriteriaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exposed_instance_criteria_with_options_async(
        self,
        request: sas_20181203_models.DescribeExposedInstanceCriteriaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedInstanceCriteriaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedInstanceCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceCriteriaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exposed_instance_criteria(
        self,
        request: sas_20181203_models.DescribeExposedInstanceCriteriaRequest,
    ) -> sas_20181203_models.DescribeExposedInstanceCriteriaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_instance_criteria_with_options(request, runtime)

    async def describe_exposed_instance_criteria_async(
        self,
        request: sas_20181203_models.DescribeExposedInstanceCriteriaRequest,
    ) -> sas_20181203_models.DescribeExposedInstanceCriteriaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_exposed_instance_criteria_with_options_async(request, runtime)

    def describe_exposed_instance_detail_with_options(
        self,
        request: sas_20181203_models.DescribeExposedInstanceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedInstanceDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedInstanceDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exposed_instance_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeExposedInstanceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedInstanceDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedInstanceDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exposed_instance_detail(
        self,
        request: sas_20181203_models.DescribeExposedInstanceDetailRequest,
    ) -> sas_20181203_models.DescribeExposedInstanceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_instance_detail_with_options(request, runtime)

    async def describe_exposed_instance_detail_async(
        self,
        request: sas_20181203_models.DescribeExposedInstanceDetailRequest,
    ) -> sas_20181203_models.DescribeExposedInstanceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_exposed_instance_detail_with_options_async(request, runtime)

    def describe_exposed_instance_list_with_options(
        self,
        request: sas_20181203_models.DescribeExposedInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedInstanceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.exposure_component):
            query['ExposureComponent'] = request.exposure_component
        if not UtilClient.is_unset(request.exposure_ip):
            query['ExposureIp'] = request.exposure_ip
        if not UtilClient.is_unset(request.exposure_port):
            query['ExposurePort'] = request.exposure_port
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vul_status):
            query['VulStatus'] = request.vul_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedInstanceList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exposed_instance_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeExposedInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedInstanceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.exposure_component):
            query['ExposureComponent'] = request.exposure_component
        if not UtilClient.is_unset(request.exposure_ip):
            query['ExposureIp'] = request.exposure_ip
        if not UtilClient.is_unset(request.exposure_port):
            query['ExposurePort'] = request.exposure_port
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vul_status):
            query['VulStatus'] = request.vul_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedInstanceList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exposed_instance_list(
        self,
        request: sas_20181203_models.DescribeExposedInstanceListRequest,
    ) -> sas_20181203_models.DescribeExposedInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_instance_list_with_options(request, runtime)

    async def describe_exposed_instance_list_async(
        self,
        request: sas_20181203_models.DescribeExposedInstanceListRequest,
    ) -> sas_20181203_models.DescribeExposedInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_exposed_instance_list_with_options_async(request, runtime)

    def describe_exposed_statistics_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedStatisticsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeExposedStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exposed_statistics_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedStatisticsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeExposedStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exposed_statistics(self) -> sas_20181203_models.DescribeExposedStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_statistics_with_options(runtime)

    async def describe_exposed_statistics_async(self) -> sas_20181203_models.DescribeExposedStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_exposed_statistics_with_options_async(runtime)

    def describe_exposed_statistics_detail_with_options(
        self,
        request: sas_20181203_models.DescribeExposedStatisticsDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedStatisticsDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.statistics_type):
            query['StatisticsType'] = request.statistics_type
        if not UtilClient.is_unset(request.statistics_type_gateway_type):
            query['StatisticsTypeGatewayType'] = request.statistics_type_gateway_type
        if not UtilClient.is_unset(request.statistics_type_instance_value):
            query['StatisticsTypeInstanceValue'] = request.statistics_type_instance_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedStatisticsDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedStatisticsDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exposed_statistics_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeExposedStatisticsDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedStatisticsDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.statistics_type):
            query['StatisticsType'] = request.statistics_type
        if not UtilClient.is_unset(request.statistics_type_gateway_type):
            query['StatisticsTypeGatewayType'] = request.statistics_type_gateway_type
        if not UtilClient.is_unset(request.statistics_type_instance_value):
            query['StatisticsTypeInstanceValue'] = request.statistics_type_instance_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedStatisticsDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedStatisticsDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exposed_statistics_detail(
        self,
        request: sas_20181203_models.DescribeExposedStatisticsDetailRequest,
    ) -> sas_20181203_models.DescribeExposedStatisticsDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_statistics_detail_with_options(request, runtime)

    async def describe_exposed_statistics_detail_async(
        self,
        request: sas_20181203_models.DescribeExposedStatisticsDetailRequest,
    ) -> sas_20181203_models.DescribeExposedStatisticsDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_exposed_statistics_detail_with_options_async(request, runtime)

    def describe_field_statistics_with_options(
        self,
        request: sas_20181203_models.DescribeFieldStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeFieldStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFieldStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeFieldStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_field_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeFieldStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeFieldStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFieldStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeFieldStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_field_statistics(
        self,
        request: sas_20181203_models.DescribeFieldStatisticsRequest,
    ) -> sas_20181203_models.DescribeFieldStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_field_statistics_with_options(request, runtime)

    async def describe_field_statistics_async(
        self,
        request: sas_20181203_models.DescribeFieldStatisticsRequest,
    ) -> sas_20181203_models.DescribeFieldStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_field_statistics_with_options_async(request, runtime)

    def describe_grouped_container_instances_with_options(
        self,
        request: sas_20181203_models.DescribeGroupedContainerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedContainerInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.group_field):
            query['GroupField'] = request.group_field
        if not UtilClient.is_unset(request.logical_exp):
            query['LogicalExp'] = request.logical_exp
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedContainerInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedContainerInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grouped_container_instances_with_options_async(
        self,
        request: sas_20181203_models.DescribeGroupedContainerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedContainerInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.group_field):
            query['GroupField'] = request.group_field
        if not UtilClient.is_unset(request.logical_exp):
            query['LogicalExp'] = request.logical_exp
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedContainerInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedContainerInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grouped_container_instances(
        self,
        request: sas_20181203_models.DescribeGroupedContainerInstancesRequest,
    ) -> sas_20181203_models.DescribeGroupedContainerInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_container_instances_with_options(request, runtime)

    async def describe_grouped_container_instances_async(
        self,
        request: sas_20181203_models.DescribeGroupedContainerInstancesRequest,
    ) -> sas_20181203_models.DescribeGroupedContainerInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grouped_container_instances_with_options_async(request, runtime)

    def describe_grouped_instances_with_options(
        self,
        request: sas_20181203_models.DescribeGroupedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.group_field):
            query['GroupField'] = request.group_field
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.no_page):
            query['NoPage'] = request.no_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grouped_instances_with_options_async(
        self,
        request: sas_20181203_models.DescribeGroupedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.group_field):
            query['GroupField'] = request.group_field
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.no_page):
            query['NoPage'] = request.no_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grouped_instances(
        self,
        request: sas_20181203_models.DescribeGroupedInstancesRequest,
    ) -> sas_20181203_models.DescribeGroupedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_instances_with_options(request, runtime)

    async def describe_grouped_instances_async(
        self,
        request: sas_20181203_models.DescribeGroupedInstancesRequest,
    ) -> sas_20181203_models.DescribeGroupedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grouped_instances_with_options_async(request, runtime)

    def describe_grouped_malicious_files_with_options(
        self,
        request: sas_20181203_models.DescribeGroupedMaliciousFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedMaliciousFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.fuzzy_malicious_name):
            query['FuzzyMaliciousName'] = request.fuzzy_malicious_name
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.image_layer):
            query['ImageLayer'] = request.image_layer
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedMaliciousFiles',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedMaliciousFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grouped_malicious_files_with_options_async(
        self,
        request: sas_20181203_models.DescribeGroupedMaliciousFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedMaliciousFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.fuzzy_malicious_name):
            query['FuzzyMaliciousName'] = request.fuzzy_malicious_name
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.image_layer):
            query['ImageLayer'] = request.image_layer
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedMaliciousFiles',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedMaliciousFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grouped_malicious_files(
        self,
        request: sas_20181203_models.DescribeGroupedMaliciousFilesRequest,
    ) -> sas_20181203_models.DescribeGroupedMaliciousFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_malicious_files_with_options(request, runtime)

    async def describe_grouped_malicious_files_async(
        self,
        request: sas_20181203_models.DescribeGroupedMaliciousFilesRequest,
    ) -> sas_20181203_models.DescribeGroupedMaliciousFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grouped_malicious_files_with_options_async(request, runtime)

    def describe_grouped_tags_with_options(
        self,
        request: sas_20181203_models.DescribeGroupedTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedTags',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grouped_tags_with_options_async(
        self,
        request: sas_20181203_models.DescribeGroupedTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedTags',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grouped_tags(
        self,
        request: sas_20181203_models.DescribeGroupedTagsRequest,
    ) -> sas_20181203_models.DescribeGroupedTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_tags_with_options(request, runtime)

    async def describe_grouped_tags_async(
        self,
        request: sas_20181203_models.DescribeGroupedTagsRequest,
    ) -> sas_20181203_models.DescribeGroupedTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grouped_tags_with_options_async(request, runtime)

    def describe_grouped_vul_with_options(
        self,
        request: sas_20181203_models.DescribeGroupedVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedVulResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_tags):
            query['SearchTags'] = request.search_tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedVul',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedVulResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grouped_vul_with_options_async(
        self,
        request: sas_20181203_models.DescribeGroupedVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedVulResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_tags):
            query['SearchTags'] = request.search_tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedVul',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedVulResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grouped_vul(
        self,
        request: sas_20181203_models.DescribeGroupedVulRequest,
    ) -> sas_20181203_models.DescribeGroupedVulResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_vul_with_options(request, runtime)

    async def describe_grouped_vul_async(
        self,
        request: sas_20181203_models.DescribeGroupedVulRequest,
    ) -> sas_20181203_models.DescribeGroupedVulResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grouped_vul_with_options_async(request, runtime)

    def describe_honey_pot_auth_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeHoneyPotAuthResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeHoneyPotAuth',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeHoneyPotAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_honey_pot_auth_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeHoneyPotAuthResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeHoneyPotAuth',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeHoneyPotAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_honey_pot_auth(self) -> sas_20181203_models.DescribeHoneyPotAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_honey_pot_auth_with_options(runtime)

    async def describe_honey_pot_auth_async(self) -> sas_20181203_models.DescribeHoneyPotAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_honey_pot_auth_with_options_async(runtime)

    def describe_honey_pot_susp_statistics_with_options(
        self,
        request: sas_20181203_models.DescribeHoneyPotSuspStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.statistics_days):
            query['StatisticsDays'] = request.statistics_days
        if not UtilClient.is_unset(request.statistics_key_type):
            query['StatisticsKeyType'] = request.statistics_key_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHoneyPotSuspStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_honey_pot_susp_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeHoneyPotSuspStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.statistics_days):
            query['StatisticsDays'] = request.statistics_days
        if not UtilClient.is_unset(request.statistics_key_type):
            query['StatisticsKeyType'] = request.statistics_key_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHoneyPotSuspStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_honey_pot_susp_statistics(
        self,
        request: sas_20181203_models.DescribeHoneyPotSuspStatisticsRequest,
    ) -> sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_honey_pot_susp_statistics_with_options(request, runtime)

    async def describe_honey_pot_susp_statistics_async(
        self,
        request: sas_20181203_models.DescribeHoneyPotSuspStatisticsRequest,
    ) -> sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_honey_pot_susp_statistics_with_options_async(request, runtime)

    def describe_image_baseline_check_summary_with_options(
        self,
        request: sas_20181203_models.DescribeImageBaselineCheckSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageBaselineCheckSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.criteria_type):
            query['CriteriaType'] = request.criteria_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageBaselineCheckSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageBaselineCheckSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_baseline_check_summary_with_options_async(
        self,
        request: sas_20181203_models.DescribeImageBaselineCheckSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageBaselineCheckSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.criteria_type):
            query['CriteriaType'] = request.criteria_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageBaselineCheckSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageBaselineCheckSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_baseline_check_summary(
        self,
        request: sas_20181203_models.DescribeImageBaselineCheckSummaryRequest,
    ) -> sas_20181203_models.DescribeImageBaselineCheckSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_baseline_check_summary_with_options(request, runtime)

    async def describe_image_baseline_check_summary_async(
        self,
        request: sas_20181203_models.DescribeImageBaselineCheckSummaryRequest,
    ) -> sas_20181203_models.DescribeImageBaselineCheckSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_baseline_check_summary_with_options_async(request, runtime)

    def describe_image_fix_task_with_options(
        self,
        request: sas_20181203_models.DescribeImageFixTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageFixTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageFixTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageFixTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_fix_task_with_options_async(
        self,
        request: sas_20181203_models.DescribeImageFixTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageFixTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageFixTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageFixTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_fix_task(
        self,
        request: sas_20181203_models.DescribeImageFixTaskRequest,
    ) -> sas_20181203_models.DescribeImageFixTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_fix_task_with_options(request, runtime)

    async def describe_image_fix_task_async(
        self,
        request: sas_20181203_models.DescribeImageFixTaskRequest,
    ) -> sas_20181203_models.DescribeImageFixTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_fix_task_with_options_async(request, runtime)

    def describe_image_grouped_vul_list_with_options(
        self,
        request: sas_20181203_models.DescribeImageGroupedVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageGroupedVulListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.cve_id):
            query['CveId'] = request.cve_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.image_layer):
            query['ImageLayer'] = request.image_layer
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.is_latest):
            query['IsLatest'] = request.is_latest
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.patch_id):
            query['PatchId'] = request.patch_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageGroupedVulList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageGroupedVulListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_grouped_vul_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeImageGroupedVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageGroupedVulListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.cve_id):
            query['CveId'] = request.cve_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.image_layer):
            query['ImageLayer'] = request.image_layer
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.is_latest):
            query['IsLatest'] = request.is_latest
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.patch_id):
            query['PatchId'] = request.patch_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageGroupedVulList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageGroupedVulListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_grouped_vul_list(
        self,
        request: sas_20181203_models.DescribeImageGroupedVulListRequest,
    ) -> sas_20181203_models.DescribeImageGroupedVulListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_grouped_vul_list_with_options(request, runtime)

    async def describe_image_grouped_vul_list_async(
        self,
        request: sas_20181203_models.DescribeImageGroupedVulListRequest,
    ) -> sas_20181203_models.DescribeImageGroupedVulListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_grouped_vul_list_with_options_async(request, runtime)

    def describe_image_list_with_baseline_name_with_options(
        self,
        request: sas_20181203_models.DescribeImageListWithBaselineNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageListWithBaselineNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_name_key):
            query['BaselineNameKey'] = request.baseline_name_key
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.criteria_type):
            query['CriteriaType'] = request.criteria_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageListWithBaselineName',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageListWithBaselineNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_list_with_baseline_name_with_options_async(
        self,
        request: sas_20181203_models.DescribeImageListWithBaselineNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageListWithBaselineNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_name_key):
            query['BaselineNameKey'] = request.baseline_name_key
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.criteria_type):
            query['CriteriaType'] = request.criteria_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageListWithBaselineName',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageListWithBaselineNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_list_with_baseline_name(
        self,
        request: sas_20181203_models.DescribeImageListWithBaselineNameRequest,
    ) -> sas_20181203_models.DescribeImageListWithBaselineNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_list_with_baseline_name_with_options(request, runtime)

    async def describe_image_list_with_baseline_name_async(
        self,
        request: sas_20181203_models.DescribeImageListWithBaselineNameRequest,
    ) -> sas_20181203_models.DescribeImageListWithBaselineNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_list_with_baseline_name_with_options_async(request, runtime)

    def describe_image_scan_auth_count_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageScanAuthCountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeImageScanAuthCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageScanAuthCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_scan_auth_count_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageScanAuthCountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeImageScanAuthCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageScanAuthCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_scan_auth_count(self) -> sas_20181203_models.DescribeImageScanAuthCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_scan_auth_count_with_options(runtime)

    async def describe_image_scan_auth_count_async(self) -> sas_20181203_models.DescribeImageScanAuthCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_scan_auth_count_with_options_async(runtime)

    def describe_image_statistics_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageStatisticsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeImageStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_statistics_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageStatisticsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeImageStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_statistics(self) -> sas_20181203_models.DescribeImageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_statistics_with_options(runtime)

    async def describe_image_statistics_async(self) -> sas_20181203_models.DescribeImageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_statistics_with_options_async(runtime)

    def describe_image_vul_list_with_options(
        self,
        request: sas_20181203_models.DescribeImageVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageVulListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageVulList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageVulListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_vul_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeImageVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageVulListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageVulList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageVulListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_vul_list(
        self,
        request: sas_20181203_models.DescribeImageVulListRequest,
    ) -> sas_20181203_models.DescribeImageVulListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_vul_list_with_options(request, runtime)

    async def describe_image_vul_list_async(
        self,
        request: sas_20181203_models.DescribeImageVulListRequest,
    ) -> sas_20181203_models.DescribeImageVulListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_vul_list_with_options_async(request, runtime)

    def describe_install_captcha_with_options(
        self,
        request: sas_20181203_models.DescribeInstallCaptchaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstallCaptchaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deadline):
            query['Deadline'] = request.deadline
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstallCaptcha',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstallCaptchaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_install_captcha_with_options_async(
        self,
        request: sas_20181203_models.DescribeInstallCaptchaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstallCaptchaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deadline):
            query['Deadline'] = request.deadline
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstallCaptcha',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstallCaptchaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_install_captcha(
        self,
        request: sas_20181203_models.DescribeInstallCaptchaRequest,
    ) -> sas_20181203_models.DescribeInstallCaptchaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_install_captcha_with_options(request, runtime)

    async def describe_install_captcha_async(
        self,
        request: sas_20181203_models.DescribeInstallCaptchaRequest,
    ) -> sas_20181203_models.DescribeInstallCaptchaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_install_captcha_with_options_async(request, runtime)

    def describe_install_codes_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstallCodesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeInstallCodes',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstallCodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_install_codes_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstallCodesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeInstallCodes',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstallCodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_install_codes(self) -> sas_20181203_models.DescribeInstallCodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_install_codes_with_options(runtime)

    async def describe_install_codes_async(self) -> sas_20181203_models.DescribeInstallCodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_install_codes_with_options_async(runtime)

    def describe_instance_anti_brute_force_rules_with_options(
        self,
        request: sas_20181203_models.DescribeInstanceAntiBruteForceRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAntiBruteForceRules',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_anti_brute_force_rules_with_options_async(
        self,
        request: sas_20181203_models.DescribeInstanceAntiBruteForceRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAntiBruteForceRules',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_anti_brute_force_rules(
        self,
        request: sas_20181203_models.DescribeInstanceAntiBruteForceRulesRequest,
    ) -> sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_anti_brute_force_rules_with_options(request, runtime)

    async def describe_instance_anti_brute_force_rules_async(
        self,
        request: sas_20181203_models.DescribeInstanceAntiBruteForceRulesRequest,
    ) -> sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_anti_brute_force_rules_with_options_async(request, runtime)

    def describe_instance_statistics_with_options(
        self,
        request: sas_20181203_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstanceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstanceStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_statistics(
        self,
        request: sas_20181203_models.DescribeInstanceStatisticsRequest,
    ) -> sas_20181203_models.DescribeInstanceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    async def describe_instance_statistics_async(
        self,
        request: sas_20181203_models.DescribeInstanceStatisticsRequest,
    ) -> sas_20181203_models.DescribeInstanceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_statistics_with_options_async(request, runtime)

    def describe_ip_info_with_options(
        self,
        request: sas_20181203_models.DescribeIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeIpInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeIpInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_info_with_options_async(
        self,
        request: sas_20181203_models.DescribeIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeIpInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeIpInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_info(
        self,
        request: sas_20181203_models.DescribeIpInfoRequest,
    ) -> sas_20181203_models.DescribeIpInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_info_with_options(request, runtime)

    async def describe_ip_info_async(
        self,
        request: sas_20181203_models.DescribeIpInfoRequest,
    ) -> sas_20181203_models.DescribeIpInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_info_with_options_async(request, runtime)

    def describe_logstore_storage_with_options(
        self,
        request: sas_20181203_models.DescribeLogstoreStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeLogstoreStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogstoreStorage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeLogstoreStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_logstore_storage_with_options_async(
        self,
        request: sas_20181203_models.DescribeLogstoreStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeLogstoreStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogstoreStorage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeLogstoreStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_logstore_storage(
        self,
        request: sas_20181203_models.DescribeLogstoreStorageRequest,
    ) -> sas_20181203_models.DescribeLogstoreStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_logstore_storage_with_options(request, runtime)

    async def describe_logstore_storage_async(
        self,
        request: sas_20181203_models.DescribeLogstoreStorageRequest,
    ) -> sas_20181203_models.DescribeLogstoreStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_logstore_storage_with_options_async(request, runtime)

    def describe_module_config_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeModuleConfigResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeModuleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeModuleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_module_config_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeModuleConfigResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeModuleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeModuleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_module_config(self) -> sas_20181203_models.DescribeModuleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_module_config_with_options(runtime)

    async def describe_module_config_async(self) -> sas_20181203_models.DescribeModuleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_module_config_with_options_async(runtime)

    def describe_notice_config_with_options(
        self,
        request: sas_20181203_models.DescribeNoticeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeNoticeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNoticeConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeNoticeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_notice_config_with_options_async(
        self,
        request: sas_20181203_models.DescribeNoticeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeNoticeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNoticeConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeNoticeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_notice_config(
        self,
        request: sas_20181203_models.DescribeNoticeConfigRequest,
    ) -> sas_20181203_models.DescribeNoticeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_notice_config_with_options(request, runtime)

    async def describe_notice_config_async(
        self,
        request: sas_20181203_models.DescribeNoticeConfigRequest,
    ) -> sas_20181203_models.DescribeNoticeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_notice_config_with_options_async(request, runtime)

    def describe_property_count_with_options(
        self,
        request: sas_20181203_models.DescribePropertyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_count_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_count(
        self,
        request: sas_20181203_models.DescribePropertyCountRequest,
    ) -> sas_20181203_models.DescribePropertyCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_count_with_options(request, runtime)

    async def describe_property_count_async(
        self,
        request: sas_20181203_models.DescribePropertyCountRequest,
    ) -> sas_20181203_models.DescribePropertyCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_count_with_options_async(request, runtime)

    def describe_property_cron_detail_with_options(
        self,
        request: sas_20181203_models.DescribePropertyCronDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyCronDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyCronDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyCronDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_cron_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyCronDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyCronDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyCronDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyCronDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_cron_detail(
        self,
        request: sas_20181203_models.DescribePropertyCronDetailRequest,
    ) -> sas_20181203_models.DescribePropertyCronDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_cron_detail_with_options(request, runtime)

    async def describe_property_cron_detail_async(
        self,
        request: sas_20181203_models.DescribePropertyCronDetailRequest,
    ) -> sas_20181203_models.DescribePropertyCronDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_cron_detail_with_options_async(request, runtime)

    def describe_property_port_detail_with_options(
        self,
        request: sas_20181203_models.DescribePropertyPortDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyPortDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_ip):
            query['BindIp'] = request.bind_ip
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.proc_name):
            query['ProcName'] = request.proc_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyPortDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyPortDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_port_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyPortDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyPortDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_ip):
            query['BindIp'] = request.bind_ip
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.proc_name):
            query['ProcName'] = request.proc_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyPortDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyPortDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_port_detail(
        self,
        request: sas_20181203_models.DescribePropertyPortDetailRequest,
    ) -> sas_20181203_models.DescribePropertyPortDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_port_detail_with_options(request, runtime)

    async def describe_property_port_detail_async(
        self,
        request: sas_20181203_models.DescribePropertyPortDetailRequest,
    ) -> sas_20181203_models.DescribePropertyPortDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_port_detail_with_options_async(request, runtime)

    def describe_property_port_item_with_options(
        self,
        request: sas_20181203_models.DescribePropertyPortItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyPortItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyPortItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyPortItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_port_item_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyPortItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyPortItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyPortItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyPortItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_port_item(
        self,
        request: sas_20181203_models.DescribePropertyPortItemRequest,
    ) -> sas_20181203_models.DescribePropertyPortItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_port_item_with_options(request, runtime)

    async def describe_property_port_item_async(
        self,
        request: sas_20181203_models.DescribePropertyPortItemRequest,
    ) -> sas_20181203_models.DescribePropertyPortItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_port_item_with_options_async(request, runtime)

    def describe_property_proc_detail_with_options(
        self,
        request: sas_20181203_models.DescribePropertyProcDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyProcDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cmdline):
            query['Cmdline'] = request.cmdline
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proc_time_end):
            query['ProcTimeEnd'] = request.proc_time_end
        if not UtilClient.is_unset(request.proc_time_start):
            query['ProcTimeStart'] = request.proc_time_start
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyProcDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyProcDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_proc_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyProcDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyProcDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cmdline):
            query['Cmdline'] = request.cmdline
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proc_time_end):
            query['ProcTimeEnd'] = request.proc_time_end
        if not UtilClient.is_unset(request.proc_time_start):
            query['ProcTimeStart'] = request.proc_time_start
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyProcDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyProcDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_proc_detail(
        self,
        request: sas_20181203_models.DescribePropertyProcDetailRequest,
    ) -> sas_20181203_models.DescribePropertyProcDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_proc_detail_with_options(request, runtime)

    async def describe_property_proc_detail_async(
        self,
        request: sas_20181203_models.DescribePropertyProcDetailRequest,
    ) -> sas_20181203_models.DescribePropertyProcDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_proc_detail_with_options_async(request, runtime)

    def describe_property_proc_item_with_options(
        self,
        request: sas_20181203_models.DescribePropertyProcItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyProcItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyProcItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyProcItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_proc_item_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyProcItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyProcItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyProcItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyProcItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_proc_item(
        self,
        request: sas_20181203_models.DescribePropertyProcItemRequest,
    ) -> sas_20181203_models.DescribePropertyProcItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_proc_item_with_options(request, runtime)

    async def describe_property_proc_item_async(
        self,
        request: sas_20181203_models.DescribePropertyProcItemRequest,
    ) -> sas_20181203_models.DescribePropertyProcItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_proc_item_with_options_async(request, runtime)

    def describe_property_sca_detail_with_options(
        self,
        request: sas_20181203_models.DescribePropertyScaDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyScaDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz):
            query['Biz'] = request.biz
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.process_started_end):
            query['ProcessStartedEnd'] = request.process_started_end
        if not UtilClient.is_unset(request.process_started_start):
            query['ProcessStartedStart'] = request.process_started_start
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.sca_name):
            query['ScaName'] = request.sca_name
        if not UtilClient.is_unset(request.sca_name_pattern):
            query['ScaNamePattern'] = request.sca_name_pattern
        if not UtilClient.is_unset(request.sca_version):
            query['ScaVersion'] = request.sca_version
        if not UtilClient.is_unset(request.search_info):
            query['SearchInfo'] = request.search_info
        if not UtilClient.is_unset(request.search_info_sub):
            query['SearchInfoSub'] = request.search_info_sub
        if not UtilClient.is_unset(request.search_item):
            query['SearchItem'] = request.search_item
        if not UtilClient.is_unset(request.search_item_sub):
            query['SearchItemSub'] = request.search_item_sub
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyScaDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyScaDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_sca_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyScaDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyScaDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz):
            query['Biz'] = request.biz
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.process_started_end):
            query['ProcessStartedEnd'] = request.process_started_end
        if not UtilClient.is_unset(request.process_started_start):
            query['ProcessStartedStart'] = request.process_started_start
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.sca_name):
            query['ScaName'] = request.sca_name
        if not UtilClient.is_unset(request.sca_name_pattern):
            query['ScaNamePattern'] = request.sca_name_pattern
        if not UtilClient.is_unset(request.sca_version):
            query['ScaVersion'] = request.sca_version
        if not UtilClient.is_unset(request.search_info):
            query['SearchInfo'] = request.search_info
        if not UtilClient.is_unset(request.search_info_sub):
            query['SearchInfoSub'] = request.search_info_sub
        if not UtilClient.is_unset(request.search_item):
            query['SearchItem'] = request.search_item
        if not UtilClient.is_unset(request.search_item_sub):
            query['SearchItemSub'] = request.search_item_sub
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyScaDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyScaDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_sca_detail(
        self,
        request: sas_20181203_models.DescribePropertyScaDetailRequest,
    ) -> sas_20181203_models.DescribePropertyScaDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_sca_detail_with_options(request, runtime)

    async def describe_property_sca_detail_async(
        self,
        request: sas_20181203_models.DescribePropertyScaDetailRequest,
    ) -> sas_20181203_models.DescribePropertyScaDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_sca_detail_with_options_async(request, runtime)

    def describe_property_software_detail_with_options(
        self,
        request: sas_20181203_models.DescribePropertySoftwareDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertySoftwareDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.install_time_end):
            query['InstallTimeEnd'] = request.install_time_end
        if not UtilClient.is_unset(request.install_time_start):
            query['InstallTimeStart'] = request.install_time_start
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.software_version):
            query['SoftwareVersion'] = request.software_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertySoftwareDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertySoftwareDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_software_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertySoftwareDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertySoftwareDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.install_time_end):
            query['InstallTimeEnd'] = request.install_time_end
        if not UtilClient.is_unset(request.install_time_start):
            query['InstallTimeStart'] = request.install_time_start
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.software_version):
            query['SoftwareVersion'] = request.software_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertySoftwareDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertySoftwareDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_software_detail(
        self,
        request: sas_20181203_models.DescribePropertySoftwareDetailRequest,
    ) -> sas_20181203_models.DescribePropertySoftwareDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_software_detail_with_options(request, runtime)

    async def describe_property_software_detail_async(
        self,
        request: sas_20181203_models.DescribePropertySoftwareDetailRequest,
    ) -> sas_20181203_models.DescribePropertySoftwareDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_software_detail_with_options_async(request, runtime)

    def describe_property_software_item_with_options(
        self,
        request: sas_20181203_models.DescribePropertySoftwareItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertySoftwareItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertySoftwareItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertySoftwareItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_software_item_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertySoftwareItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertySoftwareItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertySoftwareItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertySoftwareItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_software_item(
        self,
        request: sas_20181203_models.DescribePropertySoftwareItemRequest,
    ) -> sas_20181203_models.DescribePropertySoftwareItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_software_item_with_options(request, runtime)

    async def describe_property_software_item_async(
        self,
        request: sas_20181203_models.DescribePropertySoftwareItemRequest,
    ) -> sas_20181203_models.DescribePropertySoftwareItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_software_item_with_options_async(request, runtime)

    def describe_property_usage_newest_with_options(
        self,
        request: sas_20181203_models.DescribePropertyUsageNewestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyUsageNewestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyUsageNewest',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUsageNewestResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_usage_newest_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyUsageNewestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyUsageNewestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyUsageNewest',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUsageNewestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_usage_newest(
        self,
        request: sas_20181203_models.DescribePropertyUsageNewestRequest,
    ) -> sas_20181203_models.DescribePropertyUsageNewestResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_usage_newest_with_options(request, runtime)

    async def describe_property_usage_newest_async(
        self,
        request: sas_20181203_models.DescribePropertyUsageNewestRequest,
    ) -> sas_20181203_models.DescribePropertyUsageNewestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_usage_newest_with_options_async(request, runtime)

    def describe_property_user_detail_with_options(
        self,
        request: sas_20181203_models.DescribePropertyUserDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyUserDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.is_root):
            query['IsRoot'] = request.is_root
        if not UtilClient.is_unset(request.last_login_time_end):
            query['LastLoginTimeEnd'] = request.last_login_time_end
        if not UtilClient.is_unset(request.last_login_time_start):
            query['LastLoginTimeStart'] = request.last_login_time_start
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyUserDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUserDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_user_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyUserDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyUserDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.is_root):
            query['IsRoot'] = request.is_root
        if not UtilClient.is_unset(request.last_login_time_end):
            query['LastLoginTimeEnd'] = request.last_login_time_end
        if not UtilClient.is_unset(request.last_login_time_start):
            query['LastLoginTimeStart'] = request.last_login_time_start
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyUserDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUserDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_user_detail(
        self,
        request: sas_20181203_models.DescribePropertyUserDetailRequest,
    ) -> sas_20181203_models.DescribePropertyUserDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_user_detail_with_options(request, runtime)

    async def describe_property_user_detail_async(
        self,
        request: sas_20181203_models.DescribePropertyUserDetailRequest,
    ) -> sas_20181203_models.DescribePropertyUserDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_user_detail_with_options_async(request, runtime)

    def describe_property_user_item_with_options(
        self,
        request: sas_20181203_models.DescribePropertyUserItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyUserItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyUserItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUserItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_property_user_item_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyUserItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyUserItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyUserItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUserItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_property_user_item(
        self,
        request: sas_20181203_models.DescribePropertyUserItemRequest,
    ) -> sas_20181203_models.DescribePropertyUserItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_property_user_item_with_options(request, runtime)

    async def describe_property_user_item_async(
        self,
        request: sas_20181203_models.DescribePropertyUserItemRequest,
    ) -> sas_20181203_models.DescribePropertyUserItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_property_user_item_with_options_async(request, runtime)

    def describe_restore_jobs_with_options(
        self,
        request: sas_20181203_models.DescribeRestoreJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRestoreJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.machine_remark):
            query['MachineRemark'] = request.machine_remark
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreJobs',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRestoreJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_jobs_with_options_async(
        self,
        request: sas_20181203_models.DescribeRestoreJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRestoreJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.machine_remark):
            query['MachineRemark'] = request.machine_remark
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreJobs',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRestoreJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_jobs(
        self,
        request: sas_20181203_models.DescribeRestoreJobsRequest,
    ) -> sas_20181203_models.DescribeRestoreJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_jobs_with_options(request, runtime)

    async def describe_restore_jobs_async(
        self,
        request: sas_20181203_models.DescribeRestoreJobsRequest,
    ) -> sas_20181203_models.DescribeRestoreJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_jobs_with_options_async(request, runtime)

    def describe_risk_check_item_result_with_options(
        self,
        request: sas_20181203_models.DescribeRiskCheckItemResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskCheckItemResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskCheckItemResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckItemResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_check_item_result_with_options_async(
        self,
        request: sas_20181203_models.DescribeRiskCheckItemResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskCheckItemResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskCheckItemResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckItemResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_check_item_result(
        self,
        request: sas_20181203_models.DescribeRiskCheckItemResultRequest,
    ) -> sas_20181203_models.DescribeRiskCheckItemResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_check_item_result_with_options(request, runtime)

    async def describe_risk_check_item_result_async(
        self,
        request: sas_20181203_models.DescribeRiskCheckItemResultRequest,
    ) -> sas_20181203_models.DescribeRiskCheckItemResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_check_item_result_with_options_async(request, runtime)

    def describe_risk_check_result_with_options(
        self,
        request: sas_20181203_models.DescribeRiskCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskCheckResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.item_ids):
            query['ItemIds'] = request.item_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_flag):
            query['QueryFlag'] = request.query_flag
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskCheckResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_check_result_with_options_async(
        self,
        request: sas_20181203_models.DescribeRiskCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskCheckResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.item_ids):
            query['ItemIds'] = request.item_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_flag):
            query['QueryFlag'] = request.query_flag
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskCheckResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_check_result(
        self,
        request: sas_20181203_models.DescribeRiskCheckResultRequest,
    ) -> sas_20181203_models.DescribeRiskCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_check_result_with_options(request, runtime)

    async def describe_risk_check_result_async(
        self,
        request: sas_20181203_models.DescribeRiskCheckResultRequest,
    ) -> sas_20181203_models.DescribeRiskCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_check_result_with_options_async(request, runtime)

    def describe_risk_check_summary_with_options(
        self,
        request: sas_20181203_models.DescribeRiskCheckSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskCheckSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskCheckSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_check_summary_with_options_async(
        self,
        request: sas_20181203_models.DescribeRiskCheckSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskCheckSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskCheckSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_check_summary(
        self,
        request: sas_20181203_models.DescribeRiskCheckSummaryRequest,
    ) -> sas_20181203_models.DescribeRiskCheckSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_check_summary_with_options(request, runtime)

    async def describe_risk_check_summary_async(
        self,
        request: sas_20181203_models.DescribeRiskCheckSummaryRequest,
    ) -> sas_20181203_models.DescribeRiskCheckSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_check_summary_with_options_async(request, runtime)

    def describe_risk_item_type_with_options(
        self,
        request: sas_20181203_models.DescribeRiskItemTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskItemTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskItemType',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskItemTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_item_type_with_options_async(
        self,
        request: sas_20181203_models.DescribeRiskItemTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskItemTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskItemType',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskItemTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_item_type(
        self,
        request: sas_20181203_models.DescribeRiskItemTypeRequest,
    ) -> sas_20181203_models.DescribeRiskItemTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_item_type_with_options(request, runtime)

    async def describe_risk_item_type_async(
        self,
        request: sas_20181203_models.DescribeRiskItemTypeRequest,
    ) -> sas_20181203_models.DescribeRiskItemTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_item_type_with_options_async(request, runtime)

    def describe_risk_list_check_result_with_options(
        self,
        request: sas_20181203_models.DescribeRiskListCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskListCheckResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskListCheckResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskListCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_list_check_result_with_options_async(
        self,
        request: sas_20181203_models.DescribeRiskListCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskListCheckResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskListCheckResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskListCheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_list_check_result(
        self,
        request: sas_20181203_models.DescribeRiskListCheckResultRequest,
    ) -> sas_20181203_models.DescribeRiskListCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_list_check_result_with_options(request, runtime)

    async def describe_risk_list_check_result_async(
        self,
        request: sas_20181203_models.DescribeRiskListCheckResultRequest,
    ) -> sas_20181203_models.DescribeRiskListCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_list_check_result_with_options_async(request, runtime)

    def describe_scan_task_progress_with_options(
        self,
        request: sas_20181203_models.DescribeScanTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeScanTaskProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScanTaskProgress',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeScanTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scan_task_progress_with_options_async(
        self,
        request: sas_20181203_models.DescribeScanTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeScanTaskProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScanTaskProgress',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeScanTaskProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scan_task_progress(
        self,
        request: sas_20181203_models.DescribeScanTaskProgressRequest,
    ) -> sas_20181203_models.DescribeScanTaskProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scan_task_progress_with_options(request, runtime)

    async def describe_scan_task_progress_async(
        self,
        request: sas_20181203_models.DescribeScanTaskProgressRequest,
    ) -> sas_20181203_models.DescribeScanTaskProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scan_task_progress_with_options_async(request, runtime)

    def describe_search_condition_with_options(
        self,
        request: sas_20181203_models.DescribeSearchConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSearchConditionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSearchCondition',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSearchConditionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_search_condition_with_options_async(
        self,
        request: sas_20181203_models.DescribeSearchConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSearchConditionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSearchCondition',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSearchConditionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_search_condition(
        self,
        request: sas_20181203_models.DescribeSearchConditionRequest,
    ) -> sas_20181203_models.DescribeSearchConditionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_search_condition_with_options(request, runtime)

    async def describe_search_condition_async(
        self,
        request: sas_20181203_models.DescribeSearchConditionRequest,
    ) -> sas_20181203_models.DescribeSearchConditionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_search_condition_with_options_async(request, runtime)

    def describe_secure_suggestion_with_options(
        self,
        request: sas_20181203_models.DescribeSecureSuggestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecureSuggestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecureSuggestion',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecureSuggestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_secure_suggestion_with_options_async(
        self,
        request: sas_20181203_models.DescribeSecureSuggestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecureSuggestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecureSuggestion',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecureSuggestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_secure_suggestion(
        self,
        request: sas_20181203_models.DescribeSecureSuggestionRequest,
    ) -> sas_20181203_models.DescribeSecureSuggestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_secure_suggestion_with_options(request, runtime)

    async def describe_secure_suggestion_async(
        self,
        request: sas_20181203_models.DescribeSecureSuggestionRequest,
    ) -> sas_20181203_models.DescribeSecureSuggestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_secure_suggestion_with_options_async(request, runtime)

    def describe_security_check_schedule_config_with_options(
        self,
        request: sas_20181203_models.DescribeSecurityCheckScheduleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityCheckScheduleConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityCheckScheduleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityCheckScheduleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_check_schedule_config_with_options_async(
        self,
        request: sas_20181203_models.DescribeSecurityCheckScheduleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityCheckScheduleConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityCheckScheduleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityCheckScheduleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_check_schedule_config(
        self,
        request: sas_20181203_models.DescribeSecurityCheckScheduleConfigRequest,
    ) -> sas_20181203_models.DescribeSecurityCheckScheduleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_check_schedule_config_with_options(request, runtime)

    async def describe_security_check_schedule_config_async(
        self,
        request: sas_20181203_models.DescribeSecurityCheckScheduleConfigRequest,
    ) -> sas_20181203_models.DescribeSecurityCheckScheduleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_check_schedule_config_with_options_async(request, runtime)

    def describe_security_event_operation_status_with_options(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityEventOperationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperationStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityEventOperationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_event_operation_status_with_options_async(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityEventOperationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperationStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityEventOperationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_event_operation_status(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationStatusRequest,
    ) -> sas_20181203_models.DescribeSecurityEventOperationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operation_status_with_options(request, runtime)

    async def describe_security_event_operation_status_async(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationStatusRequest,
    ) -> sas_20181203_models.DescribeSecurityEventOperationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_event_operation_status_with_options_async(request, runtime)

    def describe_security_event_operations_with_options(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityEventOperationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperations',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityEventOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_event_operations_with_options_async(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityEventOperationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperations',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityEventOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_event_operations(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationsRequest,
    ) -> sas_20181203_models.DescribeSecurityEventOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operations_with_options(request, runtime)

    async def describe_security_event_operations_async(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationsRequest,
    ) -> sas_20181203_models.DescribeSecurityEventOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_event_operations_with_options_async(request, runtime)

    def describe_security_stat_info_with_options(
        self,
        request: sas_20181203_models.DescribeSecurityStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityStatInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityStatInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityStatInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_stat_info_with_options_async(
        self,
        request: sas_20181203_models.DescribeSecurityStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityStatInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityStatInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityStatInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_stat_info(
        self,
        request: sas_20181203_models.DescribeSecurityStatInfoRequest,
    ) -> sas_20181203_models.DescribeSecurityStatInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_stat_info_with_options(request, runtime)

    async def describe_security_stat_info_async(
        self,
        request: sas_20181203_models.DescribeSecurityStatInfoRequest,
    ) -> sas_20181203_models.DescribeSecurityStatInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_stat_info_with_options_async(request, runtime)

    def describe_service_linked_role_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeServiceLinkedRoleStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeServiceLinkedRoleStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeServiceLinkedRoleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_linked_role_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeServiceLinkedRoleStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeServiceLinkedRoleStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeServiceLinkedRoleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_linked_role_status(self) -> sas_20181203_models.DescribeServiceLinkedRoleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_linked_role_status_with_options(runtime)

    async def describe_service_linked_role_status_async(self) -> sas_20181203_models.DescribeServiceLinkedRoleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_linked_role_status_with_options_async(runtime)

    def describe_similar_event_scenarios_with_options(
        self,
        request: sas_20181203_models.DescribeSimilarEventScenariosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSimilarEventScenariosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSimilarEventScenarios',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSimilarEventScenariosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_similar_event_scenarios_with_options_async(
        self,
        request: sas_20181203_models.DescribeSimilarEventScenariosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSimilarEventScenariosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSimilarEventScenarios',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSimilarEventScenariosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_similar_event_scenarios(
        self,
        request: sas_20181203_models.DescribeSimilarEventScenariosRequest,
    ) -> sas_20181203_models.DescribeSimilarEventScenariosResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_similar_event_scenarios_with_options(request, runtime)

    async def describe_similar_event_scenarios_async(
        self,
        request: sas_20181203_models.DescribeSimilarEventScenariosRequest,
    ) -> sas_20181203_models.DescribeSimilarEventScenariosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_similar_event_scenarios_with_options_async(request, runtime)

    def describe_similar_security_events_with_options(
        self,
        request: sas_20181203_models.DescribeSimilarSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSimilarSecurityEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSimilarSecurityEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSimilarSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_similar_security_events_with_options_async(
        self,
        request: sas_20181203_models.DescribeSimilarSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSimilarSecurityEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSimilarSecurityEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSimilarSecurityEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_similar_security_events(
        self,
        request: sas_20181203_models.DescribeSimilarSecurityEventsRequest,
    ) -> sas_20181203_models.DescribeSimilarSecurityEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_similar_security_events_with_options(request, runtime)

    async def describe_similar_security_events_async(
        self,
        request: sas_20181203_models.DescribeSimilarSecurityEventsRequest,
    ) -> sas_20181203_models.DescribeSimilarSecurityEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_similar_security_events_with_options_async(request, runtime)

    def describe_strategy_with_options(
        self,
        request: sas_20181203_models.DescribeStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_type):
            query['CustomType'] = request.custom_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.strategy_ids):
            query['StrategyIds'] = request.strategy_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_strategy_with_options_async(
        self,
        request: sas_20181203_models.DescribeStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeStrategyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_type):
            query['CustomType'] = request.custom_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.strategy_ids):
            query['StrategyIds'] = request.strategy_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_strategy(
        self,
        request: sas_20181203_models.DescribeStrategyRequest,
    ) -> sas_20181203_models.DescribeStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_with_options(request, runtime)

    async def describe_strategy_async(
        self,
        request: sas_20181203_models.DescribeStrategyRequest,
    ) -> sas_20181203_models.DescribeStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_strategy_with_options_async(request, runtime)

    def describe_strategy_exec_detail_with_options(
        self,
        request: sas_20181203_models.DescribeStrategyExecDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeStrategyExecDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStrategyExecDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyExecDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_strategy_exec_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeStrategyExecDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeStrategyExecDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStrategyExecDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyExecDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_strategy_exec_detail(
        self,
        request: sas_20181203_models.DescribeStrategyExecDetailRequest,
    ) -> sas_20181203_models.DescribeStrategyExecDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_exec_detail_with_options(request, runtime)

    async def describe_strategy_exec_detail_async(
        self,
        request: sas_20181203_models.DescribeStrategyExecDetailRequest,
    ) -> sas_20181203_models.DescribeStrategyExecDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_strategy_exec_detail_with_options_async(request, runtime)

    def describe_strategy_target_with_options(
        self,
        request: sas_20181203_models.DescribeStrategyTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeStrategyTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStrategyTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_strategy_target_with_options_async(
        self,
        request: sas_20181203_models.DescribeStrategyTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeStrategyTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStrategyTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_strategy_target(
        self,
        request: sas_20181203_models.DescribeStrategyTargetRequest,
    ) -> sas_20181203_models.DescribeStrategyTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_target_with_options(request, runtime)

    async def describe_strategy_target_async(
        self,
        request: sas_20181203_models.DescribeStrategyTargetRequest,
    ) -> sas_20181203_models.DescribeStrategyTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_strategy_target_with_options_async(request, runtime)

    def describe_summary_info_with_options(
        self,
        request: sas_20181203_models.DescribeSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSummaryInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSummaryInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_summary_info_with_options_async(
        self,
        request: sas_20181203_models.DescribeSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSummaryInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSummaryInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSummaryInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_summary_info(
        self,
        request: sas_20181203_models.DescribeSummaryInfoRequest,
    ) -> sas_20181203_models.DescribeSummaryInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_summary_info_with_options(request, runtime)

    async def describe_summary_info_async(
        self,
        request: sas_20181203_models.DescribeSummaryInfoRequest,
    ) -> sas_20181203_models.DescribeSummaryInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_summary_info_with_options_async(request, runtime)

    def describe_support_region_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSupportRegionResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSupportRegion',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSupportRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_support_region_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSupportRegionResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSupportRegion',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSupportRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_support_region(self) -> sas_20181203_models.DescribeSupportRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_support_region_with_options(runtime)

    async def describe_support_region_async(self) -> sas_20181203_models.DescribeSupportRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_support_region_with_options_async(runtime)

    def describe_susp_event_detail_with_options(
        self,
        request: sas_20181203_models.DescribeSuspEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspEventDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.suspicious_event_id):
            query['SuspiciousEventId'] = request.suspicious_event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_susp_event_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeSuspEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspEventDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.suspicious_event_id):
            query['SuspiciousEventId'] = request.suspicious_event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_susp_event_detail(
        self,
        request: sas_20181203_models.DescribeSuspEventDetailRequest,
    ) -> sas_20181203_models.DescribeSuspEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_detail_with_options(request, runtime)

    async def describe_susp_event_detail_async(
        self,
        request: sas_20181203_models.DescribeSuspEventDetailRequest,
    ) -> sas_20181203_models.DescribeSuspEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_susp_event_detail_with_options_async(request, runtime)

    def describe_susp_event_quara_files_with_options(
        self,
        request: sas_20181203_models.DescribeSuspEventQuaraFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspEventQuaraFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.grouping_id):
            query['GroupingId'] = request.grouping_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.quara_tag):
            query['QuaraTag'] = request.quara_tag
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventQuaraFiles',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventQuaraFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_susp_event_quara_files_with_options_async(
        self,
        request: sas_20181203_models.DescribeSuspEventQuaraFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspEventQuaraFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.grouping_id):
            query['GroupingId'] = request.grouping_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.quara_tag):
            query['QuaraTag'] = request.quara_tag
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventQuaraFiles',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventQuaraFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_susp_event_quara_files(
        self,
        request: sas_20181203_models.DescribeSuspEventQuaraFilesRequest,
    ) -> sas_20181203_models.DescribeSuspEventQuaraFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_quara_files_with_options(request, runtime)

    async def describe_susp_event_quara_files_async(
        self,
        request: sas_20181203_models.DescribeSuspEventQuaraFilesRequest,
    ) -> sas_20181203_models.DescribeSuspEventQuaraFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_susp_event_quara_files_with_options_async(request, runtime)

    def describe_susp_events_with_options(
        self,
        request: sas_20181203_models.DescribeSuspEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.event_names):
            query['EventNames'] = request.event_names
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operate_error_code_list):
            query['OperateErrorCodeList'] = request.operate_error_code_list
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_event_types):
            query['ParentEventTypes'] = request.parent_event_types
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_susp_events_with_options_async(
        self,
        request: sas_20181203_models.DescribeSuspEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.event_names):
            query['EventNames'] = request.event_names
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operate_error_code_list):
            query['OperateErrorCodeList'] = request.operate_error_code_list
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_event_types):
            query['ParentEventTypes'] = request.parent_event_types
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_susp_events(
        self,
        request: sas_20181203_models.DescribeSuspEventsRequest,
    ) -> sas_20181203_models.DescribeSuspEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_events_with_options(request, runtime)

    async def describe_susp_events_async(
        self,
        request: sas_20181203_models.DescribeSuspEventsRequest,
    ) -> sas_20181203_models.DescribeSuspEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_susp_events_with_options_async(request, runtime)

    def describe_suspicious_uuidconfig_with_options(
        self,
        request: sas_20181203_models.DescribeSuspiciousUUIDConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspiciousUUIDConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspiciousUUIDConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspiciousUUIDConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_suspicious_uuidconfig_with_options_async(
        self,
        request: sas_20181203_models.DescribeSuspiciousUUIDConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspiciousUUIDConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspiciousUUIDConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspiciousUUIDConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_suspicious_uuidconfig(
        self,
        request: sas_20181203_models.DescribeSuspiciousUUIDConfigRequest,
    ) -> sas_20181203_models.DescribeSuspiciousUUIDConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_suspicious_uuidconfig_with_options(request, runtime)

    async def describe_suspicious_uuidconfig_async(
        self,
        request: sas_20181203_models.DescribeSuspiciousUUIDConfigRequest,
    ) -> sas_20181203_models.DescribeSuspiciousUUIDConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_suspicious_uuidconfig_with_options_async(request, runtime)

    def describe_user_backup_machines_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeUserBackupMachinesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeUserBackupMachines',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserBackupMachinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_backup_machines_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeUserBackupMachinesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeUserBackupMachines',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserBackupMachinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_backup_machines(self) -> sas_20181203_models.DescribeUserBackupMachinesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_backup_machines_with_options(runtime)

    async def describe_user_backup_machines_async(self) -> sas_20181203_models.DescribeUserBackupMachinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_backup_machines_with_options_async(runtime)

    def describe_user_baseline_authorization_with_options(
        self,
        request: sas_20181203_models.DescribeUserBaselineAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeUserBaselineAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBaselineAuthorization',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserBaselineAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_baseline_authorization_with_options_async(
        self,
        request: sas_20181203_models.DescribeUserBaselineAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeUserBaselineAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBaselineAuthorization',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserBaselineAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_baseline_authorization(
        self,
        request: sas_20181203_models.DescribeUserBaselineAuthorizationRequest,
    ) -> sas_20181203_models.DescribeUserBaselineAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_baseline_authorization_with_options(request, runtime)

    async def describe_user_baseline_authorization_async(
        self,
        request: sas_20181203_models.DescribeUserBaselineAuthorizationRequest,
    ) -> sas_20181203_models.DescribeUserBaselineAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_baseline_authorization_with_options_async(request, runtime)

    def describe_user_layout_authorization_with_options(
        self,
        request: sas_20181203_models.DescribeUserLayoutAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeUserLayoutAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserLayoutAuthorization',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserLayoutAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_layout_authorization_with_options_async(
        self,
        request: sas_20181203_models.DescribeUserLayoutAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeUserLayoutAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserLayoutAuthorization',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserLayoutAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_layout_authorization(
        self,
        request: sas_20181203_models.DescribeUserLayoutAuthorizationRequest,
    ) -> sas_20181203_models.DescribeUserLayoutAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_layout_authorization_with_options(request, runtime)

    async def describe_user_layout_authorization_async(
        self,
        request: sas_20181203_models.DescribeUserLayoutAuthorizationRequest,
    ) -> sas_20181203_models.DescribeUserLayoutAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_layout_authorization_with_options_async(request, runtime)

    def describe_version_config_with_options(
        self,
        request: sas_20181203_models.DescribeVersionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVersionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVersionConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_version_config_with_options_async(
        self,
        request: sas_20181203_models.DescribeVersionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVersionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVersionConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVersionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_version_config(
        self,
        request: sas_20181203_models.DescribeVersionConfigRequest,
    ) -> sas_20181203_models.DescribeVersionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_version_config_with_options(request, runtime)

    async def describe_version_config_async(
        self,
        request: sas_20181203_models.DescribeVersionConfigRequest,
    ) -> sas_20181203_models.DescribeVersionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_version_config_with_options_async(request, runtime)

    def describe_vol_dingding_message_with_options(
        self,
        request: sas_20181203_models.DescribeVolDingdingMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVolDingdingMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVolDingdingMessage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVolDingdingMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vol_dingding_message_with_options_async(
        self,
        request: sas_20181203_models.DescribeVolDingdingMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVolDingdingMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVolDingdingMessage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVolDingdingMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vol_dingding_message(
        self,
        request: sas_20181203_models.DescribeVolDingdingMessageRequest,
    ) -> sas_20181203_models.DescribeVolDingdingMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vol_dingding_message_with_options(request, runtime)

    async def describe_vol_dingding_message_async(
        self,
        request: sas_20181203_models.DescribeVolDingdingMessageRequest,
    ) -> sas_20181203_models.DescribeVolDingdingMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vol_dingding_message_with_options_async(request, runtime)

    def describe_vpc_honey_pot_criteria_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVpcHoneyPotCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_honey_pot_criteria_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVpcHoneyPotCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_honey_pot_criteria(self) -> sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_honey_pot_criteria_with_options(runtime)

    async def describe_vpc_honey_pot_criteria_async(self) -> sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_honey_pot_criteria_with_options_async(runtime)

    def describe_vpc_honey_pot_list_with_options(
        self,
        request: sas_20181203_models.DescribeVpcHoneyPotListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcHoneyPotListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.honey_pot_existence):
            query['HoneyPotExistence'] = request.honey_pot_existence
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_name):
            query['VpcName'] = request.vpc_name
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcHoneyPotList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcHoneyPotListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_honey_pot_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeVpcHoneyPotListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcHoneyPotListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.honey_pot_existence):
            query['HoneyPotExistence'] = request.honey_pot_existence
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_name):
            query['VpcName'] = request.vpc_name
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcHoneyPotList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcHoneyPotListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_honey_pot_list(
        self,
        request: sas_20181203_models.DescribeVpcHoneyPotListRequest,
    ) -> sas_20181203_models.DescribeVpcHoneyPotListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_honey_pot_list_with_options(request, runtime)

    async def describe_vpc_honey_pot_list_async(
        self,
        request: sas_20181203_models.DescribeVpcHoneyPotListRequest,
    ) -> sas_20181203_models.DescribeVpcHoneyPotListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_honey_pot_list_with_options_async(request, runtime)

    def describe_vpc_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVpcList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVpcList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_list(self) -> sas_20181203_models.DescribeVpcListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_list_with_options(runtime)

    async def describe_vpc_list_async(self) -> sas_20181203_models.DescribeVpcListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_list_with_options_async(runtime)

    def describe_vul_details_with_options(
        self,
        request: sas_20181203_models.DescribeVulDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulDetails',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vul_details_with_options_async(
        self,
        request: sas_20181203_models.DescribeVulDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulDetails',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vul_details(
        self,
        request: sas_20181203_models.DescribeVulDetailsRequest,
    ) -> sas_20181203_models.DescribeVulDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_details_with_options(request, runtime)

    async def describe_vul_details_async(
        self,
        request: sas_20181203_models.DescribeVulDetailsRequest,
    ) -> sas_20181203_models.DescribeVulDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vul_details_with_options_async(request, runtime)

    def describe_vul_export_info_with_options(
        self,
        request: sas_20181203_models.DescribeVulExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulExportInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulExportInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vul_export_info_with_options_async(
        self,
        request: sas_20181203_models.DescribeVulExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulExportInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulExportInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulExportInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vul_export_info(
        self,
        request: sas_20181203_models.DescribeVulExportInfoRequest,
    ) -> sas_20181203_models.DescribeVulExportInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_export_info_with_options(request, runtime)

    async def describe_vul_export_info_async(
        self,
        request: sas_20181203_models.DescribeVulExportInfoRequest,
    ) -> sas_20181203_models.DescribeVulExportInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vul_export_info_with_options_async(request, runtime)

    def describe_vul_list_with_options(
        self,
        request: sas_20181203_models.DescribeVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.attach_types):
            query['AttachTypes'] = request.attach_types
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.vpc_instance_ids):
            query['VpcInstanceIds'] = request.vpc_instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vul_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.attach_types):
            query['AttachTypes'] = request.attach_types
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.vpc_instance_ids):
            query['VpcInstanceIds'] = request.vpc_instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vul_list(
        self,
        request: sas_20181203_models.DescribeVulListRequest,
    ) -> sas_20181203_models.DescribeVulListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_list_with_options(request, runtime)

    async def describe_vul_list_async(
        self,
        request: sas_20181203_models.DescribeVulListRequest,
    ) -> sas_20181203_models.DescribeVulListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vul_list_with_options_async(request, runtime)

    def describe_vul_whitelist_with_options(
        self,
        request: sas_20181203_models.DescribeVulWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulWhitelist',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vul_whitelist_with_options_async(
        self,
        request: sas_20181203_models.DescribeVulWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulWhitelist',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vul_whitelist(
        self,
        request: sas_20181203_models.DescribeVulWhitelistRequest,
    ) -> sas_20181203_models.DescribeVulWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_whitelist_with_options(request, runtime)

    async def describe_vul_whitelist_async(
        self,
        request: sas_20181203_models.DescribeVulWhitelistRequest,
    ) -> sas_20181203_models.DescribeVulWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vul_whitelist_with_options_async(request, runtime)

    def describe_warning_machines_with_options(
        self,
        request: sas_20181203_models.DescribeWarningMachinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeWarningMachinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.machine_name):
            query['MachineName'] = request.machine_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWarningMachines',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWarningMachinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_warning_machines_with_options_async(
        self,
        request: sas_20181203_models.DescribeWarningMachinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeWarningMachinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.machine_name):
            query['MachineName'] = request.machine_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWarningMachines',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWarningMachinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_warning_machines(
        self,
        request: sas_20181203_models.DescribeWarningMachinesRequest,
    ) -> sas_20181203_models.DescribeWarningMachinesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_warning_machines_with_options(request, runtime)

    async def describe_warning_machines_async(
        self,
        request: sas_20181203_models.DescribeWarningMachinesRequest,
    ) -> sas_20181203_models.DescribeWarningMachinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_warning_machines_with_options_async(request, runtime)

    def describe_web_lock_bind_list_with_options(
        self,
        request: sas_20181203_models.DescribeWebLockBindListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeWebLockBindListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebLockBindList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockBindListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_lock_bind_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeWebLockBindListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeWebLockBindListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebLockBindList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockBindListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_lock_bind_list(
        self,
        request: sas_20181203_models.DescribeWebLockBindListRequest,
    ) -> sas_20181203_models.DescribeWebLockBindListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_bind_list_with_options(request, runtime)

    async def describe_web_lock_bind_list_async(
        self,
        request: sas_20181203_models.DescribeWebLockBindListRequest,
    ) -> sas_20181203_models.DescribeWebLockBindListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_lock_bind_list_with_options_async(request, runtime)

    def describe_web_lock_config_list_with_options(
        self,
        request: sas_20181203_models.DescribeWebLockConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeWebLockConfigListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebLockConfigList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_lock_config_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeWebLockConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeWebLockConfigListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebLockConfigList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockConfigListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_lock_config_list(
        self,
        request: sas_20181203_models.DescribeWebLockConfigListRequest,
    ) -> sas_20181203_models.DescribeWebLockConfigListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_config_list_with_options(request, runtime)

    async def describe_web_lock_config_list_async(
        self,
        request: sas_20181203_models.DescribeWebLockConfigListRequest,
    ) -> sas_20181203_models.DescribeWebLockConfigListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_lock_config_list_with_options_async(request, runtime)

    def export_record_with_options(
        self,
        request: sas_20181203_models.ExportRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ExportRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportRecord',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ExportRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_record_with_options_async(
        self,
        request: sas_20181203_models.ExportRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ExportRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportRecord',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ExportRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_record(
        self,
        request: sas_20181203_models.ExportRecordRequest,
    ) -> sas_20181203_models.ExportRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_record_with_options(request, runtime)

    async def export_record_async(
        self,
        request: sas_20181203_models.ExportRecordRequest,
    ) -> sas_20181203_models.ExportRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_record_with_options_async(request, runtime)

    def export_vul_with_options(
        self,
        request: sas_20181203_models.ExportVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ExportVulResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.attach_types):
            query['AttachTypes'] = request.attach_types
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.search_tags):
            query['SearchTags'] = request.search_tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.vpc_instance_ids):
            query['VpcInstanceIds'] = request.vpc_instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportVul',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ExportVulResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_vul_with_options_async(
        self,
        request: sas_20181203_models.ExportVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ExportVulResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.attach_types):
            query['AttachTypes'] = request.attach_types
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.search_tags):
            query['SearchTags'] = request.search_tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.vpc_instance_ids):
            query['VpcInstanceIds'] = request.vpc_instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportVul',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ExportVulResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_vul(
        self,
        request: sas_20181203_models.ExportVulRequest,
    ) -> sas_20181203_models.ExportVulResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_vul_with_options(request, runtime)

    async def export_vul_async(
        self,
        request: sas_20181203_models.ExportVulRequest,
    ) -> sas_20181203_models.ExportVulResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_vul_with_options_async(request, runtime)

    def fix_check_warnings_with_options(
        self,
        request: sas_20181203_models.FixCheckWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.FixCheckWarningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_params):
            query['CheckParams'] = request.check_params
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FixCheckWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.FixCheckWarningsResponse(),
            self.call_api(params, req, runtime)
        )

    async def fix_check_warnings_with_options_async(
        self,
        request: sas_20181203_models.FixCheckWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.FixCheckWarningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_params):
            query['CheckParams'] = request.check_params
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FixCheckWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.FixCheckWarningsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fix_check_warnings(
        self,
        request: sas_20181203_models.FixCheckWarningsRequest,
    ) -> sas_20181203_models.FixCheckWarningsResponse:
        runtime = util_models.RuntimeOptions()
        return self.fix_check_warnings_with_options(request, runtime)

    async def fix_check_warnings_async(
        self,
        request: sas_20181203_models.FixCheckWarningsRequest,
    ) -> sas_20181203_models.FixCheckWarningsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fix_check_warnings_with_options_async(request, runtime)

    def get_backup_storage_count_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.GetBackupStorageCountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetBackupStorageCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetBackupStorageCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_backup_storage_count_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.GetBackupStorageCountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetBackupStorageCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetBackupStorageCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_backup_storage_count(self) -> sas_20181203_models.GetBackupStorageCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_backup_storage_count_with_options(runtime)

    async def get_backup_storage_count_async(self) -> sas_20181203_models.GetBackupStorageCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_backup_storage_count_with_options_async(runtime)

    def get_suspicious_statistics_with_options(
        self,
        request: sas_20181203_models.GetSuspiciousStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.GetSuspiciousStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSuspiciousStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetSuspiciousStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_suspicious_statistics_with_options_async(
        self,
        request: sas_20181203_models.GetSuspiciousStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.GetSuspiciousStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSuspiciousStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetSuspiciousStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_suspicious_statistics(
        self,
        request: sas_20181203_models.GetSuspiciousStatisticsRequest,
    ) -> sas_20181203_models.GetSuspiciousStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_suspicious_statistics_with_options(request, runtime)

    async def get_suspicious_statistics_async(
        self,
        request: sas_20181203_models.GetSuspiciousStatisticsRequest,
    ) -> sas_20181203_models.GetSuspiciousStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_suspicious_statistics_with_options_async(request, runtime)

    def get_vul_statistics_with_options(
        self,
        request: sas_20181203_models.GetVulStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.GetVulStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type_list):
            query['TypeList'] = request.type_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVulStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetVulStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vul_statistics_with_options_async(
        self,
        request: sas_20181203_models.GetVulStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.GetVulStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type_list):
            query['TypeList'] = request.type_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVulStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetVulStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vul_statistics(
        self,
        request: sas_20181203_models.GetVulStatisticsRequest,
    ) -> sas_20181203_models.GetVulStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vul_statistics_with_options(request, runtime)

    async def get_vul_statistics_async(
        self,
        request: sas_20181203_models.GetVulStatisticsRequest,
    ) -> sas_20181203_models.GetVulStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vul_statistics_with_options_async(request, runtime)

    def handle_security_events_with_options(
        self,
        request: sas_20181203_models.HandleSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.HandleSecurityEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mark_batch):
            query['MarkBatch'] = request.mark_batch
        if not UtilClient.is_unset(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not UtilClient.is_unset(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not UtilClient.is_unset(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleSecurityEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.HandleSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def handle_security_events_with_options_async(
        self,
        request: sas_20181203_models.HandleSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.HandleSecurityEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mark_batch):
            query['MarkBatch'] = request.mark_batch
        if not UtilClient.is_unset(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not UtilClient.is_unset(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not UtilClient.is_unset(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleSecurityEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.HandleSecurityEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def handle_security_events(
        self,
        request: sas_20181203_models.HandleSecurityEventsRequest,
    ) -> sas_20181203_models.HandleSecurityEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.handle_security_events_with_options(request, runtime)

    async def handle_security_events_async(
        self,
        request: sas_20181203_models.HandleSecurityEventsRequest,
    ) -> sas_20181203_models.HandleSecurityEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.handle_security_events_with_options_async(request, runtime)

    def handle_similar_security_events_with_options(
        self,
        request: sas_20181203_models.HandleSimilarSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.HandleSimilarSecurityEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not UtilClient.is_unset(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleSimilarSecurityEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.HandleSimilarSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def handle_similar_security_events_with_options_async(
        self,
        request: sas_20181203_models.HandleSimilarSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.HandleSimilarSecurityEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not UtilClient.is_unset(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleSimilarSecurityEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.HandleSimilarSecurityEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def handle_similar_security_events(
        self,
        request: sas_20181203_models.HandleSimilarSecurityEventsRequest,
    ) -> sas_20181203_models.HandleSimilarSecurityEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.handle_similar_security_events_with_options(request, runtime)

    async def handle_similar_security_events_async(
        self,
        request: sas_20181203_models.HandleSimilarSecurityEventsRequest,
    ) -> sas_20181203_models.HandleSimilarSecurityEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.handle_similar_security_events_with_options_async(request, runtime)

    def ignore_hc_check_warnings_with_options(
        self,
        request: sas_20181203_models.IgnoreHcCheckWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.IgnoreHcCheckWarningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_ids):
            query['CheckIds'] = request.check_ids
        if not UtilClient.is_unset(request.check_warning_ids):
            query['CheckWarningIds'] = request.check_warning_ids
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IgnoreHcCheckWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.IgnoreHcCheckWarningsResponse(),
            self.call_api(params, req, runtime)
        )

    async def ignore_hc_check_warnings_with_options_async(
        self,
        request: sas_20181203_models.IgnoreHcCheckWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.IgnoreHcCheckWarningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_ids):
            query['CheckIds'] = request.check_ids
        if not UtilClient.is_unset(request.check_warning_ids):
            query['CheckWarningIds'] = request.check_warning_ids
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IgnoreHcCheckWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.IgnoreHcCheckWarningsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ignore_hc_check_warnings(
        self,
        request: sas_20181203_models.IgnoreHcCheckWarningsRequest,
    ) -> sas_20181203_models.IgnoreHcCheckWarningsResponse:
        runtime = util_models.RuntimeOptions()
        return self.ignore_hc_check_warnings_with_options(request, runtime)

    async def ignore_hc_check_warnings_async(
        self,
        request: sas_20181203_models.IgnoreHcCheckWarningsRequest,
    ) -> sas_20181203_models.IgnoreHcCheckWarningsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ignore_hc_check_warnings_with_options_async(request, runtime)

    def install_backup_client_with_options(
        self,
        request: sas_20181203_models.InstallBackupClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.InstallBackupClientResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallBackupClient',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.InstallBackupClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_backup_client_with_options_async(
        self,
        request: sas_20181203_models.InstallBackupClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.InstallBackupClientResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallBackupClient',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.InstallBackupClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_backup_client(
        self,
        request: sas_20181203_models.InstallBackupClientRequest,
    ) -> sas_20181203_models.InstallBackupClientResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_backup_client_with_options(request, runtime)

    async def install_backup_client_async(
        self,
        request: sas_20181203_models.InstallBackupClientRequest,
    ) -> sas_20181203_models.InstallBackupClientResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_backup_client_with_options_async(request, runtime)

    def modify_anti_brute_force_rule_with_options(
        self,
        request: sas_20181203_models.ModifyAntiBruteForceRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyAntiBruteForceRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.fail_count):
            query['FailCount'] = request.fail_count
        if not UtilClient.is_unset(request.forbidden_time):
            query['ForbiddenTime'] = request.forbidden_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.span):
            query['Span'] = request.span
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAntiBruteForceRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAntiBruteForceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_anti_brute_force_rule_with_options_async(
        self,
        request: sas_20181203_models.ModifyAntiBruteForceRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyAntiBruteForceRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.fail_count):
            query['FailCount'] = request.fail_count
        if not UtilClient.is_unset(request.forbidden_time):
            query['ForbiddenTime'] = request.forbidden_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.span):
            query['Span'] = request.span
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAntiBruteForceRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAntiBruteForceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_anti_brute_force_rule(
        self,
        request: sas_20181203_models.ModifyAntiBruteForceRuleRequest,
    ) -> sas_20181203_models.ModifyAntiBruteForceRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_anti_brute_force_rule_with_options(request, runtime)

    async def modify_anti_brute_force_rule_async(
        self,
        request: sas_20181203_models.ModifyAntiBruteForceRuleRequest,
    ) -> sas_20181203_models.ModifyAntiBruteForceRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_anti_brute_force_rule_with_options_async(request, runtime)

    def modify_asset_group_with_options(
        self,
        request: sas_20181203_models.ModifyAssetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyAssetGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAssetGroup',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAssetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_asset_group_with_options_async(
        self,
        request: sas_20181203_models.ModifyAssetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyAssetGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAssetGroup',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAssetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_asset_group(
        self,
        request: sas_20181203_models.ModifyAssetGroupRequest,
    ) -> sas_20181203_models.ModifyAssetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_asset_group_with_options(request, runtime)

    async def modify_asset_group_async(
        self,
        request: sas_20181203_models.ModifyAssetGroupRequest,
    ) -> sas_20181203_models.ModifyAssetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_asset_group_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        tmp_req: sas_20181203_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.ModifyBackupPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_shrink):
            query['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.policy_region_id):
            query['PolicyRegionId'] = request.policy_region_id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        tmp_req: sas_20181203_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.ModifyBackupPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_shrink):
            query['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.policy_region_id):
            query['PolicyRegionId'] = request.policy_region_id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: sas_20181203_models.ModifyBackupPolicyRequest,
    ) -> sas_20181203_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: sas_20181203_models.ModifyBackupPolicyRequest,
    ) -> sas_20181203_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_backup_policy_status_with_options(
        self,
        request: sas_20181203_models.ModifyBackupPolicyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyBackupPolicyStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicyStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyBackupPolicyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_status_with_options_async(
        self,
        request: sas_20181203_models.ModifyBackupPolicyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyBackupPolicyStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicyStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyBackupPolicyStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy_status(
        self,
        request: sas_20181203_models.ModifyBackupPolicyStatusRequest,
    ) -> sas_20181203_models.ModifyBackupPolicyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_status_with_options(request, runtime)

    async def modify_backup_policy_status_async(
        self,
        request: sas_20181203_models.ModifyBackupPolicyStatusRequest,
    ) -> sas_20181203_models.ModifyBackupPolicyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_status_with_options_async(request, runtime)

    def modify_create_vul_whitelist_with_options(
        self,
        request: sas_20181203_models.ModifyCreateVulWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyCreateVulWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.target_info):
            query['TargetInfo'] = request.target_info
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCreateVulWhitelist',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyCreateVulWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_create_vul_whitelist_with_options_async(
        self,
        request: sas_20181203_models.ModifyCreateVulWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyCreateVulWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.target_info):
            query['TargetInfo'] = request.target_info
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCreateVulWhitelist',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyCreateVulWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_create_vul_whitelist(
        self,
        request: sas_20181203_models.ModifyCreateVulWhitelistRequest,
    ) -> sas_20181203_models.ModifyCreateVulWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_create_vul_whitelist_with_options(request, runtime)

    async def modify_create_vul_whitelist_async(
        self,
        request: sas_20181203_models.ModifyCreateVulWhitelistRequest,
    ) -> sas_20181203_models.ModifyCreateVulWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_create_vul_whitelist_with_options_async(request, runtime)

    def modify_emg_vul_submit_with_options(
        self,
        request: sas_20181203_models.ModifyEmgVulSubmitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyEmgVulSubmitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.user_agreement):
            query['UserAgreement'] = request.user_agreement
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEmgVulSubmit',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyEmgVulSubmitResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_emg_vul_submit_with_options_async(
        self,
        request: sas_20181203_models.ModifyEmgVulSubmitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyEmgVulSubmitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.user_agreement):
            query['UserAgreement'] = request.user_agreement
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEmgVulSubmit',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyEmgVulSubmitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_emg_vul_submit(
        self,
        request: sas_20181203_models.ModifyEmgVulSubmitRequest,
    ) -> sas_20181203_models.ModifyEmgVulSubmitResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_emg_vul_submit_with_options(request, runtime)

    async def modify_emg_vul_submit_async(
        self,
        request: sas_20181203_models.ModifyEmgVulSubmitRequest,
    ) -> sas_20181203_models.ModifyEmgVulSubmitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_emg_vul_submit_with_options_async(request, runtime)

    def modify_group_property_with_options(
        self,
        request: sas_20181203_models.ModifyGroupPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyGroupPropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGroupProperty',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyGroupPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_group_property_with_options_async(
        self,
        request: sas_20181203_models.ModifyGroupPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyGroupPropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGroupProperty',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyGroupPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_group_property(
        self,
        request: sas_20181203_models.ModifyGroupPropertyRequest,
    ) -> sas_20181203_models.ModifyGroupPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_group_property_with_options(request, runtime)

    async def modify_group_property_async(
        self,
        request: sas_20181203_models.ModifyGroupPropertyRequest,
    ) -> sas_20181203_models.ModifyGroupPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_group_property_with_options_async(request, runtime)

    def modify_instance_anti_brute_force_rule_with_options(
        self,
        request: sas_20181203_models.ModifyInstanceAntiBruteForceRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyInstanceAntiBruteForceRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_rule_id):
            query['NewRuleId'] = request.new_rule_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAntiBruteForceRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyInstanceAntiBruteForceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_anti_brute_force_rule_with_options_async(
        self,
        request: sas_20181203_models.ModifyInstanceAntiBruteForceRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyInstanceAntiBruteForceRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_rule_id):
            query['NewRuleId'] = request.new_rule_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAntiBruteForceRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyInstanceAntiBruteForceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_anti_brute_force_rule(
        self,
        request: sas_20181203_models.ModifyInstanceAntiBruteForceRuleRequest,
    ) -> sas_20181203_models.ModifyInstanceAntiBruteForceRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_anti_brute_force_rule_with_options(request, runtime)

    async def modify_instance_anti_brute_force_rule_async(
        self,
        request: sas_20181203_models.ModifyInstanceAntiBruteForceRuleRequest,
    ) -> sas_20181203_models.ModifyInstanceAntiBruteForceRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_anti_brute_force_rule_with_options_async(request, runtime)

    def modify_login_base_config_with_options(
        self,
        request: sas_20181203_models.ModifyLoginBaseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyLoginBaseConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoginBaseConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyLoginBaseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_login_base_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyLoginBaseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyLoginBaseConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoginBaseConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyLoginBaseConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_login_base_config(
        self,
        request: sas_20181203_models.ModifyLoginBaseConfigRequest,
    ) -> sas_20181203_models.ModifyLoginBaseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_login_base_config_with_options(request, runtime)

    async def modify_login_base_config_async(
        self,
        request: sas_20181203_models.ModifyLoginBaseConfigRequest,
    ) -> sas_20181203_models.ModifyLoginBaseConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_login_base_config_with_options_async(request, runtime)

    def modify_login_switch_config_with_options(
        self,
        request: sas_20181203_models.ModifyLoginSwitchConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyLoginSwitchConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item):
            query['Item'] = request.item
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoginSwitchConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyLoginSwitchConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_login_switch_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyLoginSwitchConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyLoginSwitchConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item):
            query['Item'] = request.item
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoginSwitchConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyLoginSwitchConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_login_switch_config(
        self,
        request: sas_20181203_models.ModifyLoginSwitchConfigRequest,
    ) -> sas_20181203_models.ModifyLoginSwitchConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_login_switch_config_with_options(request, runtime)

    async def modify_login_switch_config_async(
        self,
        request: sas_20181203_models.ModifyLoginSwitchConfigRequest,
    ) -> sas_20181203_models.ModifyLoginSwitchConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_login_switch_config_with_options_async(request, runtime)

    def modify_open_log_shipper_with_options(
        self,
        request: sas_20181203_models.ModifyOpenLogShipperRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyOpenLogShipperResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOpenLogShipper',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyOpenLogShipperResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_open_log_shipper_with_options_async(
        self,
        request: sas_20181203_models.ModifyOpenLogShipperRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyOpenLogShipperResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOpenLogShipper',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyOpenLogShipperResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_open_log_shipper(
        self,
        request: sas_20181203_models.ModifyOpenLogShipperRequest,
    ) -> sas_20181203_models.ModifyOpenLogShipperResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_open_log_shipper_with_options(request, runtime)

    async def modify_open_log_shipper_async(
        self,
        request: sas_20181203_models.ModifyOpenLogShipperRequest,
    ) -> sas_20181203_models.ModifyOpenLogShipperResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_open_log_shipper_with_options_async(request, runtime)

    def modify_operate_vul_with_options(
        self,
        request: sas_20181203_models.ModifyOperateVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyOperateVulResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.info):
            query['Info'] = request.info
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOperateVul',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyOperateVulResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_operate_vul_with_options_async(
        self,
        request: sas_20181203_models.ModifyOperateVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyOperateVulResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.info):
            query['Info'] = request.info
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOperateVul',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyOperateVulResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_operate_vul(
        self,
        request: sas_20181203_models.ModifyOperateVulRequest,
    ) -> sas_20181203_models.ModifyOperateVulResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_operate_vul_with_options(request, runtime)

    async def modify_operate_vul_async(
        self,
        request: sas_20181203_models.ModifyOperateVulRequest,
    ) -> sas_20181203_models.ModifyOperateVulResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_operate_vul_with_options_async(request, runtime)

    def modify_push_all_task_with_options(
        self,
        request: sas_20181203_models.ModifyPushAllTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyPushAllTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.tasks):
            query['Tasks'] = request.tasks
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPushAllTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyPushAllTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_push_all_task_with_options_async(
        self,
        request: sas_20181203_models.ModifyPushAllTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyPushAllTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.tasks):
            query['Tasks'] = request.tasks
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPushAllTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyPushAllTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_push_all_task(
        self,
        request: sas_20181203_models.ModifyPushAllTaskRequest,
    ) -> sas_20181203_models.ModifyPushAllTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_push_all_task_with_options(request, runtime)

    async def modify_push_all_task_async(
        self,
        request: sas_20181203_models.ModifyPushAllTaskRequest,
    ) -> sas_20181203_models.ModifyPushAllTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_push_all_task_with_options_async(request, runtime)

    def modify_risk_check_status_with_options(
        self,
        request: sas_20181203_models.ModifyRiskCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyRiskCheckStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRiskCheckStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyRiskCheckStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_risk_check_status_with_options_async(
        self,
        request: sas_20181203_models.ModifyRiskCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyRiskCheckStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRiskCheckStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyRiskCheckStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_risk_check_status(
        self,
        request: sas_20181203_models.ModifyRiskCheckStatusRequest,
    ) -> sas_20181203_models.ModifyRiskCheckStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_risk_check_status_with_options(request, runtime)

    async def modify_risk_check_status_async(
        self,
        request: sas_20181203_models.ModifyRiskCheckStatusRequest,
    ) -> sas_20181203_models.ModifyRiskCheckStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_risk_check_status_with_options_async(request, runtime)

    def modify_risk_single_result_status_with_options(
        self,
        request: sas_20181203_models.ModifyRiskSingleResultStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyRiskSingleResultStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRiskSingleResultStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyRiskSingleResultStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_risk_single_result_status_with_options_async(
        self,
        request: sas_20181203_models.ModifyRiskSingleResultStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyRiskSingleResultStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRiskSingleResultStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyRiskSingleResultStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_risk_single_result_status(
        self,
        request: sas_20181203_models.ModifyRiskSingleResultStatusRequest,
    ) -> sas_20181203_models.ModifyRiskSingleResultStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_risk_single_result_status_with_options(request, runtime)

    async def modify_risk_single_result_status_async(
        self,
        request: sas_20181203_models.ModifyRiskSingleResultStatusRequest,
    ) -> sas_20181203_models.ModifyRiskSingleResultStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_risk_single_result_status_with_options_async(request, runtime)

    def modify_security_check_schedule_config_with_options(
        self,
        request: sas_20181203_models.ModifySecurityCheckScheduleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifySecurityCheckScheduleConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.days_of_week):
            query['DaysOfWeek'] = request.days_of_week
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityCheckScheduleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifySecurityCheckScheduleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_check_schedule_config_with_options_async(
        self,
        request: sas_20181203_models.ModifySecurityCheckScheduleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifySecurityCheckScheduleConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.days_of_week):
            query['DaysOfWeek'] = request.days_of_week
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityCheckScheduleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifySecurityCheckScheduleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_check_schedule_config(
        self,
        request: sas_20181203_models.ModifySecurityCheckScheduleConfigRequest,
    ) -> sas_20181203_models.ModifySecurityCheckScheduleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_check_schedule_config_with_options(request, runtime)

    async def modify_security_check_schedule_config_async(
        self,
        request: sas_20181203_models.ModifySecurityCheckScheduleConfigRequest,
    ) -> sas_20181203_models.ModifySecurityCheckScheduleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_check_schedule_config_with_options_async(request, runtime)

    def modify_start_vul_scan_with_options(
        self,
        request: sas_20181203_models.ModifyStartVulScanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyStartVulScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStartVulScan',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyStartVulScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_start_vul_scan_with_options_async(
        self,
        request: sas_20181203_models.ModifyStartVulScanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyStartVulScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStartVulScan',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyStartVulScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_start_vul_scan(
        self,
        request: sas_20181203_models.ModifyStartVulScanRequest,
    ) -> sas_20181203_models.ModifyStartVulScanResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_start_vul_scan_with_options(request, runtime)

    async def modify_start_vul_scan_async(
        self,
        request: sas_20181203_models.ModifyStartVulScanRequest,
    ) -> sas_20181203_models.ModifyStartVulScanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_start_vul_scan_with_options_async(request, runtime)

    def modify_tag_with_uuid_with_options(
        self,
        request: sas_20181203_models.ModifyTagWithUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyTagWithUuidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTagWithUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyTagWithUuidResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tag_with_uuid_with_options_async(
        self,
        request: sas_20181203_models.ModifyTagWithUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyTagWithUuidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTagWithUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyTagWithUuidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tag_with_uuid(
        self,
        request: sas_20181203_models.ModifyTagWithUuidRequest,
    ) -> sas_20181203_models.ModifyTagWithUuidResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tag_with_uuid_with_options(request, runtime)

    async def modify_tag_with_uuid_async(
        self,
        request: sas_20181203_models.ModifyTagWithUuidRequest,
    ) -> sas_20181203_models.ModifyTagWithUuidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tag_with_uuid_with_options_async(request, runtime)

    def modify_vpc_honey_pot_with_options(
        self,
        request: sas_20181203_models.ModifyVpcHoneyPotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyVpcHoneyPotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.honey_pot_action):
            query['HoneyPotAction'] = request.honey_pot_action
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcHoneyPot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyVpcHoneyPotResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_honey_pot_with_options_async(
        self,
        request: sas_20181203_models.ModifyVpcHoneyPotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyVpcHoneyPotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.honey_pot_action):
            query['HoneyPotAction'] = request.honey_pot_action
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcHoneyPot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyVpcHoneyPotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_honey_pot(
        self,
        request: sas_20181203_models.ModifyVpcHoneyPotRequest,
    ) -> sas_20181203_models.ModifyVpcHoneyPotResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_honey_pot_with_options(request, runtime)

    async def modify_vpc_honey_pot_async(
        self,
        request: sas_20181203_models.ModifyVpcHoneyPotRequest,
    ) -> sas_20181203_models.ModifyVpcHoneyPotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_honey_pot_with_options_async(request, runtime)

    def modify_vul_target_config_with_options(
        self,
        request: sas_20181203_models.ModifyVulTargetConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyVulTargetConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVulTargetConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyVulTargetConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vul_target_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyVulTargetConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyVulTargetConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVulTargetConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyVulTargetConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vul_target_config(
        self,
        request: sas_20181203_models.ModifyVulTargetConfigRequest,
    ) -> sas_20181203_models.ModifyVulTargetConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vul_target_config_with_options(request, runtime)

    async def modify_vul_target_config_async(
        self,
        request: sas_20181203_models.ModifyVulTargetConfigRequest,
    ) -> sas_20181203_models.ModifyVulTargetConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vul_target_config_with_options_async(request, runtime)

    def modify_web_lock_create_config_with_options(
        self,
        request: sas_20181203_models.ModifyWebLockCreateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockCreateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defence_mode):
            query['DefenceMode'] = request.defence_mode
        if not UtilClient.is_unset(request.dir):
            query['Dir'] = request.dir
        if not UtilClient.is_unset(request.exclusive_dir):
            query['ExclusiveDir'] = request.exclusive_dir
        if not UtilClient.is_unset(request.exclusive_file):
            query['ExclusiveFile'] = request.exclusive_file
        if not UtilClient.is_unset(request.exclusive_file_type):
            query['ExclusiveFileType'] = request.exclusive_file_type
        if not UtilClient.is_unset(request.inclusive_file):
            query['InclusiveFile'] = request.inclusive_file
        if not UtilClient.is_unset(request.inclusive_file_type):
            query['InclusiveFileType'] = request.inclusive_file_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_backup_dir):
            query['LocalBackupDir'] = request.local_backup_dir
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockCreateConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockCreateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_lock_create_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyWebLockCreateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockCreateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defence_mode):
            query['DefenceMode'] = request.defence_mode
        if not UtilClient.is_unset(request.dir):
            query['Dir'] = request.dir
        if not UtilClient.is_unset(request.exclusive_dir):
            query['ExclusiveDir'] = request.exclusive_dir
        if not UtilClient.is_unset(request.exclusive_file):
            query['ExclusiveFile'] = request.exclusive_file
        if not UtilClient.is_unset(request.exclusive_file_type):
            query['ExclusiveFileType'] = request.exclusive_file_type
        if not UtilClient.is_unset(request.inclusive_file):
            query['InclusiveFile'] = request.inclusive_file
        if not UtilClient.is_unset(request.inclusive_file_type):
            query['InclusiveFileType'] = request.inclusive_file_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_backup_dir):
            query['LocalBackupDir'] = request.local_backup_dir
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockCreateConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockCreateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_lock_create_config(
        self,
        request: sas_20181203_models.ModifyWebLockCreateConfigRequest,
    ) -> sas_20181203_models.ModifyWebLockCreateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_create_config_with_options(request, runtime)

    async def modify_web_lock_create_config_async(
        self,
        request: sas_20181203_models.ModifyWebLockCreateConfigRequest,
    ) -> sas_20181203_models.ModifyWebLockCreateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_lock_create_config_with_options_async(request, runtime)

    def modify_web_lock_delete_config_with_options(
        self,
        request: sas_20181203_models.ModifyWebLockDeleteConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockDeleteConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockDeleteConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockDeleteConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_lock_delete_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyWebLockDeleteConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockDeleteConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockDeleteConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockDeleteConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_lock_delete_config(
        self,
        request: sas_20181203_models.ModifyWebLockDeleteConfigRequest,
    ) -> sas_20181203_models.ModifyWebLockDeleteConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_delete_config_with_options(request, runtime)

    async def modify_web_lock_delete_config_async(
        self,
        request: sas_20181203_models.ModifyWebLockDeleteConfigRequest,
    ) -> sas_20181203_models.ModifyWebLockDeleteConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_lock_delete_config_with_options_async(request, runtime)

    def modify_web_lock_start_with_options(
        self,
        request: sas_20181203_models.ModifyWebLockStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockStartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defence_mode):
            query['DefenceMode'] = request.defence_mode
        if not UtilClient.is_unset(request.dir):
            query['Dir'] = request.dir
        if not UtilClient.is_unset(request.exclusive_dir):
            query['ExclusiveDir'] = request.exclusive_dir
        if not UtilClient.is_unset(request.exclusive_file):
            query['ExclusiveFile'] = request.exclusive_file
        if not UtilClient.is_unset(request.exclusive_file_type):
            query['ExclusiveFileType'] = request.exclusive_file_type
        if not UtilClient.is_unset(request.inclusive_file_type):
            query['InclusiveFileType'] = request.inclusive_file_type
        if not UtilClient.is_unset(request.local_backup_dir):
            query['LocalBackupDir'] = request.local_backup_dir
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockStart',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockStartResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_lock_start_with_options_async(
        self,
        request: sas_20181203_models.ModifyWebLockStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockStartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defence_mode):
            query['DefenceMode'] = request.defence_mode
        if not UtilClient.is_unset(request.dir):
            query['Dir'] = request.dir
        if not UtilClient.is_unset(request.exclusive_dir):
            query['ExclusiveDir'] = request.exclusive_dir
        if not UtilClient.is_unset(request.exclusive_file):
            query['ExclusiveFile'] = request.exclusive_file
        if not UtilClient.is_unset(request.exclusive_file_type):
            query['ExclusiveFileType'] = request.exclusive_file_type
        if not UtilClient.is_unset(request.inclusive_file_type):
            query['InclusiveFileType'] = request.inclusive_file_type
        if not UtilClient.is_unset(request.local_backup_dir):
            query['LocalBackupDir'] = request.local_backup_dir
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockStart',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockStartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_lock_start(
        self,
        request: sas_20181203_models.ModifyWebLockStartRequest,
    ) -> sas_20181203_models.ModifyWebLockStartResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_start_with_options(request, runtime)

    async def modify_web_lock_start_async(
        self,
        request: sas_20181203_models.ModifyWebLockStartRequest,
    ) -> sas_20181203_models.ModifyWebLockStartResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_lock_start_with_options_async(request, runtime)

    def modify_web_lock_status_with_options(
        self,
        request: sas_20181203_models.ModifyWebLockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_lock_status_with_options_async(
        self,
        request: sas_20181203_models.ModifyWebLockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_lock_status(
        self,
        request: sas_20181203_models.ModifyWebLockStatusRequest,
    ) -> sas_20181203_models.ModifyWebLockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_status_with_options(request, runtime)

    async def modify_web_lock_status_async(
        self,
        request: sas_20181203_models.ModifyWebLockStatusRequest,
    ) -> sas_20181203_models.ModifyWebLockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_lock_status_with_options_async(request, runtime)

    def modify_web_lock_update_config_with_options(
        self,
        request: sas_20181203_models.ModifyWebLockUpdateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockUpdateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defence_mode):
            query['DefenceMode'] = request.defence_mode
        if not UtilClient.is_unset(request.dir):
            query['Dir'] = request.dir
        if not UtilClient.is_unset(request.exclusive_dir):
            query['ExclusiveDir'] = request.exclusive_dir
        if not UtilClient.is_unset(request.exclusive_file):
            query['ExclusiveFile'] = request.exclusive_file
        if not UtilClient.is_unset(request.exclusive_file_type):
            query['ExclusiveFileType'] = request.exclusive_file_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.inclusive_file):
            query['InclusiveFile'] = request.inclusive_file
        if not UtilClient.is_unset(request.inclusive_file_type):
            query['InclusiveFileType'] = request.inclusive_file_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_backup_dir):
            query['LocalBackupDir'] = request.local_backup_dir
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockUpdateConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockUpdateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_web_lock_update_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyWebLockUpdateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockUpdateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defence_mode):
            query['DefenceMode'] = request.defence_mode
        if not UtilClient.is_unset(request.dir):
            query['Dir'] = request.dir
        if not UtilClient.is_unset(request.exclusive_dir):
            query['ExclusiveDir'] = request.exclusive_dir
        if not UtilClient.is_unset(request.exclusive_file):
            query['ExclusiveFile'] = request.exclusive_file
        if not UtilClient.is_unset(request.exclusive_file_type):
            query['ExclusiveFileType'] = request.exclusive_file_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.inclusive_file):
            query['InclusiveFile'] = request.inclusive_file
        if not UtilClient.is_unset(request.inclusive_file_type):
            query['InclusiveFileType'] = request.inclusive_file_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_backup_dir):
            query['LocalBackupDir'] = request.local_backup_dir
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockUpdateConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockUpdateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_web_lock_update_config(
        self,
        request: sas_20181203_models.ModifyWebLockUpdateConfigRequest,
    ) -> sas_20181203_models.ModifyWebLockUpdateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_update_config_with_options(request, runtime)

    async def modify_web_lock_update_config_async(
        self,
        request: sas_20181203_models.ModifyWebLockUpdateConfigRequest,
    ) -> sas_20181203_models.ModifyWebLockUpdateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_lock_update_config_with_options_async(request, runtime)

    def operate_agent_client_install_with_options(
        self,
        request: sas_20181203_models.OperateAgentClientInstallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperateAgentClientInstallResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateAgentClientInstall',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateAgentClientInstallResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_agent_client_install_with_options_async(
        self,
        request: sas_20181203_models.OperateAgentClientInstallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperateAgentClientInstallResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateAgentClientInstall',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateAgentClientInstallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_agent_client_install(
        self,
        request: sas_20181203_models.OperateAgentClientInstallRequest,
    ) -> sas_20181203_models.OperateAgentClientInstallResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_agent_client_install_with_options(request, runtime)

    async def operate_agent_client_install_async(
        self,
        request: sas_20181203_models.OperateAgentClientInstallRequest,
    ) -> sas_20181203_models.OperateAgentClientInstallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_agent_client_install_with_options_async(request, runtime)

    def operate_suspicious_target_config_with_options(
        self,
        request: sas_20181203_models.OperateSuspiciousTargetConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperateSuspiciousTargetConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.target_operations):
            query['TargetOperations'] = request.target_operations
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateSuspiciousTargetConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateSuspiciousTargetConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_suspicious_target_config_with_options_async(
        self,
        request: sas_20181203_models.OperateSuspiciousTargetConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperateSuspiciousTargetConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.target_operations):
            query['TargetOperations'] = request.target_operations
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateSuspiciousTargetConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateSuspiciousTargetConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_suspicious_target_config(
        self,
        request: sas_20181203_models.OperateSuspiciousTargetConfigRequest,
    ) -> sas_20181203_models.OperateSuspiciousTargetConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_suspicious_target_config_with_options(request, runtime)

    async def operate_suspicious_target_config_async(
        self,
        request: sas_20181203_models.OperateSuspiciousTargetConfigRequest,
    ) -> sas_20181203_models.OperateSuspiciousTargetConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_suspicious_target_config_with_options_async(request, runtime)

    def operate_vuls_with_options(
        self,
        request: sas_20181203_models.OperateVulsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperateVulsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.vul_names):
            query['VulNames'] = request.vul_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateVuls',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateVulsResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_vuls_with_options_async(
        self,
        request: sas_20181203_models.OperateVulsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperateVulsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.vul_names):
            query['VulNames'] = request.vul_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateVuls',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateVulsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_vuls(
        self,
        request: sas_20181203_models.OperateVulsRequest,
    ) -> sas_20181203_models.OperateVulsResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_vuls_with_options(request, runtime)

    async def operate_vuls_async(
        self,
        request: sas_20181203_models.OperateVulsRequest,
    ) -> sas_20181203_models.OperateVulsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_vuls_with_options_async(request, runtime)

    def operation_susp_events_with_options(
        self,
        request: sas_20181203_models.OperationSuspEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperationSuspEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.sub_operation):
            query['SubOperation'] = request.sub_operation
        if not UtilClient.is_unset(request.suspicious_event_ids):
            query['SuspiciousEventIds'] = request.suspicious_event_ids
        if not UtilClient.is_unset(request.warn_type):
            query['WarnType'] = request.warn_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperationSuspEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperationSuspEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def operation_susp_events_with_options_async(
        self,
        request: sas_20181203_models.OperationSuspEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperationSuspEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.sub_operation):
            query['SubOperation'] = request.sub_operation
        if not UtilClient.is_unset(request.suspicious_event_ids):
            query['SuspiciousEventIds'] = request.suspicious_event_ids
        if not UtilClient.is_unset(request.warn_type):
            query['WarnType'] = request.warn_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperationSuspEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperationSuspEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operation_susp_events(
        self,
        request: sas_20181203_models.OperationSuspEventsRequest,
    ) -> sas_20181203_models.OperationSuspEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.operation_susp_events_with_options(request, runtime)

    async def operation_susp_events_async(
        self,
        request: sas_20181203_models.OperationSuspEventsRequest,
    ) -> sas_20181203_models.OperationSuspEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operation_susp_events_with_options_async(request, runtime)

    def pause_client_with_options(
        self,
        request: sas_20181203_models.PauseClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.PauseClientResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseClient',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.PauseClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_client_with_options_async(
        self,
        request: sas_20181203_models.PauseClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.PauseClientResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseClient',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.PauseClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_client(
        self,
        request: sas_20181203_models.PauseClientRequest,
    ) -> sas_20181203_models.PauseClientResponse:
        runtime = util_models.RuntimeOptions()
        return self.pause_client_with_options(request, runtime)

    async def pause_client_async(
        self,
        request: sas_20181203_models.PauseClientRequest,
    ) -> sas_20181203_models.PauseClientResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pause_client_with_options_async(request, runtime)

    def query_group_id_by_group_name_with_options(
        self,
        request: sas_20181203_models.QueryGroupIdByGroupNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.QueryGroupIdByGroupNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGroupIdByGroupName',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.QueryGroupIdByGroupNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_group_id_by_group_name_with_options_async(
        self,
        request: sas_20181203_models.QueryGroupIdByGroupNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.QueryGroupIdByGroupNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGroupIdByGroupName',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.QueryGroupIdByGroupNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_group_id_by_group_name(
        self,
        request: sas_20181203_models.QueryGroupIdByGroupNameRequest,
    ) -> sas_20181203_models.QueryGroupIdByGroupNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_group_id_by_group_name_with_options(request, runtime)

    async def query_group_id_by_group_name_async(
        self,
        request: sas_20181203_models.QueryGroupIdByGroupNameRequest,
    ) -> sas_20181203_models.QueryGroupIdByGroupNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_group_id_by_group_name_with_options_async(request, runtime)

    def refresh_assets_with_options(
        self,
        request: sas_20181203_models.RefreshAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.RefreshAssetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshAssets',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RefreshAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_assets_with_options_async(
        self,
        request: sas_20181203_models.RefreshAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.RefreshAssetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshAssets',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RefreshAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_assets(
        self,
        request: sas_20181203_models.RefreshAssetsRequest,
    ) -> sas_20181203_models.RefreshAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_assets_with_options(request, runtime)

    async def refresh_assets_async(
        self,
        request: sas_20181203_models.RefreshAssetsRequest,
    ) -> sas_20181203_models.RefreshAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_assets_with_options_async(request, runtime)

    def refresh_container_assets_with_options(
        self,
        request: sas_20181203_models.RefreshContainerAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.RefreshContainerAssetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshContainerAssets',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RefreshContainerAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_container_assets_with_options_async(
        self,
        request: sas_20181203_models.RefreshContainerAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.RefreshContainerAssetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshContainerAssets',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RefreshContainerAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_container_assets(
        self,
        request: sas_20181203_models.RefreshContainerAssetsRequest,
    ) -> sas_20181203_models.RefreshContainerAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_container_assets_with_options(request, runtime)

    async def refresh_container_assets_async(
        self,
        request: sas_20181203_models.RefreshContainerAssetsRequest,
    ) -> sas_20181203_models.RefreshContainerAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_container_assets_with_options_async(request, runtime)

    def rollback_susp_event_quara_file_with_options(
        self,
        request: sas_20181203_models.RollbackSuspEventQuaraFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.RollbackSuspEventQuaraFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.quara_file_id):
            query['QuaraFileId'] = request.quara_file_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackSuspEventQuaraFile',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RollbackSuspEventQuaraFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_susp_event_quara_file_with_options_async(
        self,
        request: sas_20181203_models.RollbackSuspEventQuaraFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.RollbackSuspEventQuaraFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.quara_file_id):
            query['QuaraFileId'] = request.quara_file_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackSuspEventQuaraFile',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RollbackSuspEventQuaraFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_susp_event_quara_file(
        self,
        request: sas_20181203_models.RollbackSuspEventQuaraFileRequest,
    ) -> sas_20181203_models.RollbackSuspEventQuaraFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_susp_event_quara_file_with_options(request, runtime)

    async def rollback_susp_event_quara_file_async(
        self,
        request: sas_20181203_models.RollbackSuspEventQuaraFileRequest,
    ) -> sas_20181203_models.RollbackSuspEventQuaraFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_susp_event_quara_file_with_options_async(request, runtime)

    def sas_install_code_with_options(
        self,
        request: sas_20181203_models.SasInstallCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.SasInstallCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SasInstallCode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.SasInstallCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def sas_install_code_with_options_async(
        self,
        request: sas_20181203_models.SasInstallCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.SasInstallCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SasInstallCode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.SasInstallCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sas_install_code(
        self,
        request: sas_20181203_models.SasInstallCodeRequest,
    ) -> sas_20181203_models.SasInstallCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.sas_install_code_with_options(request, runtime)

    async def sas_install_code_async(
        self,
        request: sas_20181203_models.SasInstallCodeRequest,
    ) -> sas_20181203_models.SasInstallCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sas_install_code_with_options_async(request, runtime)

    def start_baseline_security_check_with_options(
        self,
        request: sas_20181203_models.StartBaselineSecurityCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.StartBaselineSecurityCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_ids):
            query['ItemIds'] = request.item_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBaselineSecurityCheck',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.StartBaselineSecurityCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_baseline_security_check_with_options_async(
        self,
        request: sas_20181203_models.StartBaselineSecurityCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.StartBaselineSecurityCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_ids):
            query['ItemIds'] = request.item_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBaselineSecurityCheck',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.StartBaselineSecurityCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_baseline_security_check(
        self,
        request: sas_20181203_models.StartBaselineSecurityCheckRequest,
    ) -> sas_20181203_models.StartBaselineSecurityCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_baseline_security_check_with_options(request, runtime)

    async def start_baseline_security_check_async(
        self,
        request: sas_20181203_models.StartBaselineSecurityCheckRequest,
    ) -> sas_20181203_models.StartBaselineSecurityCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_baseline_security_check_with_options_async(request, runtime)

    def start_image_vul_scan_with_options(
        self,
        request: sas_20181203_models.StartImageVulScanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.StartImageVulScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.image_layer):
            query['ImageLayer'] = request.image_layer
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registry_types):
            query['RegistryTypes'] = request.registry_types
        if not UtilClient.is_unset(request.rep_name):
            query['RepName'] = request.rep_name
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartImageVulScan',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.StartImageVulScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_image_vul_scan_with_options_async(
        self,
        request: sas_20181203_models.StartImageVulScanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.StartImageVulScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.image_layer):
            query['ImageLayer'] = request.image_layer
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registry_types):
            query['RegistryTypes'] = request.registry_types
        if not UtilClient.is_unset(request.rep_name):
            query['RepName'] = request.rep_name
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartImageVulScan',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.StartImageVulScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_image_vul_scan(
        self,
        request: sas_20181203_models.StartImageVulScanRequest,
    ) -> sas_20181203_models.StartImageVulScanResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_image_vul_scan_with_options(request, runtime)

    async def start_image_vul_scan_async(
        self,
        request: sas_20181203_models.StartImageVulScanRequest,
    ) -> sas_20181203_models.StartImageVulScanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_image_vul_scan_with_options_async(request, runtime)

    def start_virus_scan_task_with_options(
        self,
        request: sas_20181203_models.StartVirusScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.StartVirusScanTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_info):
            query['TargetInfo'] = request.target_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartVirusScanTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.StartVirusScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_virus_scan_task_with_options_async(
        self,
        request: sas_20181203_models.StartVirusScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.StartVirusScanTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_info):
            query['TargetInfo'] = request.target_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartVirusScanTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.StartVirusScanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_virus_scan_task(
        self,
        request: sas_20181203_models.StartVirusScanTaskRequest,
    ) -> sas_20181203_models.StartVirusScanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_virus_scan_task_with_options(request, runtime)

    async def start_virus_scan_task_async(
        self,
        request: sas_20181203_models.StartVirusScanTaskRequest,
    ) -> sas_20181203_models.StartVirusScanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_virus_scan_task_with_options_async(request, runtime)

    def unbind_aegis_with_options(
        self,
        request: sas_20181203_models.UnbindAegisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.UnbindAegisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAegis',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UnbindAegisResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_aegis_with_options_async(
        self,
        request: sas_20181203_models.UnbindAegisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.UnbindAegisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAegis',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UnbindAegisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_aegis(
        self,
        request: sas_20181203_models.UnbindAegisRequest,
    ) -> sas_20181203_models.UnbindAegisResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_aegis_with_options(request, runtime)

    async def unbind_aegis_async(
        self,
        request: sas_20181203_models.UnbindAegisRequest,
    ) -> sas_20181203_models.UnbindAegisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_aegis_with_options_async(request, runtime)

    def uninstall_backup_client_with_options(
        self,
        request: sas_20181203_models.UninstallBackupClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.UninstallBackupClientResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallBackupClient',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UninstallBackupClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_backup_client_with_options_async(
        self,
        request: sas_20181203_models.UninstallBackupClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.UninstallBackupClientResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallBackupClient',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UninstallBackupClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_backup_client(
        self,
        request: sas_20181203_models.UninstallBackupClientRequest,
    ) -> sas_20181203_models.UninstallBackupClientResponse:
        runtime = util_models.RuntimeOptions()
        return self.uninstall_backup_client_with_options(request, runtime)

    async def uninstall_backup_client_async(
        self,
        request: sas_20181203_models.UninstallBackupClientRequest,
    ) -> sas_20181203_models.UninstallBackupClientResponse:
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_backup_client_with_options_async(request, runtime)

    def validate_hc_warnings_with_options(
        self,
        request: sas_20181203_models.ValidateHcWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ValidateHcWarningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.risk_ids):
            query['RiskIds'] = request.risk_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateHcWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ValidateHcWarningsResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_hc_warnings_with_options_async(
        self,
        request: sas_20181203_models.ValidateHcWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ValidateHcWarningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.risk_ids):
            query['RiskIds'] = request.risk_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateHcWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ValidateHcWarningsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_hc_warnings(
        self,
        request: sas_20181203_models.ValidateHcWarningsRequest,
    ) -> sas_20181203_models.ValidateHcWarningsResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_hc_warnings_with_options(request, runtime)

    async def validate_hc_warnings_async(
        self,
        request: sas_20181203_models.ValidateHcWarningsRequest,
    ) -> sas_20181203_models.ValidateHcWarningsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_hc_warnings_with_options_async(request, runtime)
