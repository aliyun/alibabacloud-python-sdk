# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sas20181203 import models as sas_20181203_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-hangzhou': 'tds.aliyuncs.com',
            'ap-southeast-3': 'tds.ap-southeast-3.aliyuncs.com',
            'cn-shanghai-et2-b01': 'tds.cn-shanghai-et2-b01.aliyuncs.com'
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.AddVpcHoneyPotResponse().from_map(
            self.do_rpcrequest('AddVpcHoneyPot', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_vpc_honey_pot_with_options_async(
        self,
        request: sas_20181203_models.AddVpcHoneyPotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.AddVpcHoneyPotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.AddVpcHoneyPotResponse().from_map(
            await self.do_rpcrequest_async('AddVpcHoneyPot', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_anti_brute_force_rule_with_options(
        self,
        request: sas_20181203_models.CreateAntiBruteForceRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateAntiBruteForceRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.CreateAntiBruteForceRuleResponse().from_map(
            self.do_rpcrequest('CreateAntiBruteForceRule', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_anti_brute_force_rule_with_options_async(
        self,
        request: sas_20181203_models.CreateAntiBruteForceRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateAntiBruteForceRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.CreateAntiBruteForceRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateAntiBruteForceRule', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_or_update_asset_group_with_options(
        self,
        request: sas_20181203_models.CreateOrUpdateAssetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateOrUpdateAssetGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.CreateOrUpdateAssetGroupResponse().from_map(
            self.do_rpcrequest('CreateOrUpdateAssetGroup', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_or_update_asset_group_with_options_async(
        self,
        request: sas_20181203_models.CreateOrUpdateAssetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateOrUpdateAssetGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.CreateOrUpdateAssetGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateOrUpdateAssetGroup', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_sas_order_with_options(
        self,
        request: sas_20181203_models.CreateSasOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateSasOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.CreateSasOrderResponse().from_map(
            self.do_rpcrequest('CreateSasOrder', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sas_order_with_options_async(
        self,
        request: sas_20181203_models.CreateSasOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateSasOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.CreateSasOrderResponse().from_map(
            await self.do_rpcrequest_async('CreateSasOrder', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sas_order(
        self,
        request: sas_20181203_models.CreateSasOrderRequest,
    ) -> sas_20181203_models.CreateSasOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sas_order_with_options(request, runtime)

    async def create_sas_order_async(
        self,
        request: sas_20181203_models.CreateSasOrderRequest,
    ) -> sas_20181203_models.CreateSasOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sas_order_with_options_async(request, runtime)

    def create_similar_security_events_query_task_with_options(
        self,
        request: sas_20181203_models.CreateSimilarSecurityEventsQueryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse().from_map(
            self.do_rpcrequest('CreateSimilarSecurityEventsQueryTask', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_similar_security_events_query_task_with_options_async(
        self,
        request: sas_20181203_models.CreateSimilarSecurityEventsQueryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateSimilarSecurityEventsQueryTask', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_group_with_options(
        self,
        request: sas_20181203_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DeleteGroupResponse().from_map(
            self.do_rpcrequest('DeleteGroup', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: sas_20181203_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DeleteGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteGroup', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DeleteLoginBaseConfigResponse().from_map(
            self.do_rpcrequest('DeleteLoginBaseConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_login_base_config_with_options_async(
        self,
        request: sas_20181203_models.DeleteLoginBaseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteLoginBaseConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DeleteLoginBaseConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteLoginBaseConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_tag_with_uuid_with_options(
        self,
        request: sas_20181203_models.DeleteTagWithUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteTagWithUuidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DeleteTagWithUuidResponse().from_map(
            self.do_rpcrequest('DeleteTagWithUuid', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_tag_with_uuid_with_options_async(
        self,
        request: sas_20181203_models.DeleteTagWithUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteTagWithUuidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DeleteTagWithUuidResponse().from_map(
            await self.do_rpcrequest_async('DeleteTagWithUuid', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DeleteVpcHoneyPotResponse().from_map(
            self.do_rpcrequest('DeleteVpcHoneyPot', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vpc_honey_pot_with_options_async(
        self,
        request: sas_20181203_models.DeleteVpcHoneyPotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DeleteVpcHoneyPotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DeleteVpcHoneyPotResponse().from_map(
            await self.do_rpcrequest_async('DeleteVpcHoneyPot', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAccesskeyLeakListResponse().from_map(
            self.do_rpcrequest('DescribeAccesskeyLeakList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_accesskey_leak_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeAccesskeyLeakListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAccesskeyLeakListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAccesskeyLeakListResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccesskeyLeakList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAffectedMaliciousFileImagesResponse().from_map(
            self.do_rpcrequest('DescribeAffectedMaliciousFileImages', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_affected_malicious_file_images_with_options_async(
        self,
        request: sas_20181203_models.DescribeAffectedMaliciousFileImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAffectedMaliciousFileImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAffectedMaliciousFileImagesResponse().from_map(
            await self.do_rpcrequest_async('DescribeAffectedMaliciousFileImages', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAlarmEventDetailResponse().from_map(
            self.do_rpcrequest('DescribeAlarmEventDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_alarm_event_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeAlarmEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAlarmEventDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAlarmEventDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeAlarmEventDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAlarmEventListResponse().from_map(
            self.do_rpcrequest('DescribeAlarmEventList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_alarm_event_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeAlarmEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAlarmEventListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAlarmEventListResponse().from_map(
            await self.do_rpcrequest_async('DescribeAlarmEventList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: sas_20181203_models.DescribeAllEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAllEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAllEntityResponse().from_map(
            self.do_rpcrequest('DescribeAllEntity', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_all_entity_with_options_async(
        self,
        request: sas_20181203_models.DescribeAllEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAllEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAllEntityResponse().from_map(
            await self.do_rpcrequest_async('DescribeAllEntity', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_entity(
        self,
        request: sas_20181203_models.DescribeAllEntityRequest,
    ) -> sas_20181203_models.DescribeAllEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_entity_with_options(request, runtime)

    async def describe_all_entity_async(
        self,
        request: sas_20181203_models.DescribeAllEntityRequest,
    ) -> sas_20181203_models.DescribeAllEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_entity_with_options_async(request, runtime)

    def describe_all_groups_with_options(
        self,
        request: sas_20181203_models.DescribeAllGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAllGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAllGroupsResponse().from_map(
            self.do_rpcrequest('DescribeAllGroups', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_all_groups_with_options_async(
        self,
        request: sas_20181203_models.DescribeAllGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAllGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAllGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAllGroups', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_all_regions_statistics_with_options(
        self,
        request: sas_20181203_models.DescribeAllRegionsStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAllRegionsStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAllRegionsStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeAllRegionsStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_all_regions_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeAllRegionsStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAllRegionsStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAllRegionsStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAllRegionsStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_regions_statistics(
        self,
        request: sas_20181203_models.DescribeAllRegionsStatisticsRequest,
    ) -> sas_20181203_models.DescribeAllRegionsStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_regions_statistics_with_options(request, runtime)

    async def describe_all_regions_statistics_async(
        self,
        request: sas_20181203_models.DescribeAllRegionsStatisticsRequest,
    ) -> sas_20181203_models.DescribeAllRegionsStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_regions_statistics_with_options_async(request, runtime)

    def describe_anti_brute_force_rules_with_options(
        self,
        request: sas_20181203_models.DescribeAntiBruteForceRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAntiBruteForceRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAntiBruteForceRulesResponse().from_map(
            self.do_rpcrequest('DescribeAntiBruteForceRules', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_anti_brute_force_rules_with_options_async(
        self,
        request: sas_20181203_models.DescribeAntiBruteForceRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAntiBruteForceRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAntiBruteForceRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntiBruteForceRules', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAssetDetailByUuidResponse().from_map(
            self.do_rpcrequest('DescribeAssetDetailByUuid', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_asset_detail_by_uuid_with_options_async(
        self,
        request: sas_20181203_models.DescribeAssetDetailByUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAssetDetailByUuidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAssetDetailByUuidResponse().from_map(
            await self.do_rpcrequest_async('DescribeAssetDetailByUuid', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAssetDetailByUuidsResponse().from_map(
            self.do_rpcrequest('DescribeAssetDetailByUuids', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_asset_detail_by_uuids_with_options_async(
        self,
        request: sas_20181203_models.DescribeAssetDetailByUuidsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAssetDetailByUuidsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAssetDetailByUuidsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAssetDetailByUuids', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_auto_del_config_with_options(
        self,
        request: sas_20181203_models.DescribeAutoDelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAutoDelConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAutoDelConfigResponse().from_map(
            self.do_rpcrequest('DescribeAutoDelConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_del_config_with_options_async(
        self,
        request: sas_20181203_models.DescribeAutoDelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeAutoDelConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeAutoDelConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutoDelConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_del_config(
        self,
        request: sas_20181203_models.DescribeAutoDelConfigRequest,
    ) -> sas_20181203_models.DescribeAutoDelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_del_config_with_options(request, runtime)

    async def describe_auto_del_config_async(
        self,
        request: sas_20181203_models.DescribeAutoDelConfigRequest,
    ) -> sas_20181203_models.DescribeAutoDelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_del_config_with_options_async(request, runtime)

    def describe_brute_force_summary_with_options(
        self,
        request: sas_20181203_models.DescribeBruteForceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBruteForceSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeBruteForceSummaryResponse().from_map(
            self.do_rpcrequest('DescribeBruteForceSummary', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_brute_force_summary_with_options_async(
        self,
        request: sas_20181203_models.DescribeBruteForceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeBruteForceSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeBruteForceSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeBruteForceSummary', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCheckEcsWarningsResponse().from_map(
            self.do_rpcrequest('DescribeCheckEcsWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_check_ecs_warnings_with_options_async(
        self,
        request: sas_20181203_models.DescribeCheckEcsWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckEcsWarningsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCheckEcsWarningsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCheckEcsWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCheckWarningDetailResponse().from_map(
            self.do_rpcrequest('DescribeCheckWarningDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_check_warning_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeCheckWarningDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckWarningDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCheckWarningDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeCheckWarningDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_check_warnings_with_options(
        self,
        request: sas_20181203_models.DescribeCheckWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckWarningsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCheckWarningsResponse().from_map(
            self.do_rpcrequest('DescribeCheckWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_check_warnings_with_options_async(
        self,
        request: sas_20181203_models.DescribeCheckWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckWarningsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCheckWarningsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCheckWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_check_warning_summary_with_options(
        self,
        request: sas_20181203_models.DescribeCheckWarningSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckWarningSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCheckWarningSummaryResponse().from_map(
            self.do_rpcrequest('DescribeCheckWarningSummary', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_check_warning_summary_with_options_async(
        self,
        request: sas_20181203_models.DescribeCheckWarningSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCheckWarningSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCheckWarningSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeCheckWarningSummary', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_cloud_center_instances_with_options(
        self,
        request: sas_20181203_models.DescribeCloudCenterInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCloudCenterInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCloudCenterInstancesResponse().from_map(
            self.do_rpcrequest('DescribeCloudCenterInstances', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cloud_center_instances_with_options_async(
        self,
        request: sas_20181203_models.DescribeCloudCenterInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCloudCenterInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCloudCenterInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCloudCenterInstances', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: sas_20181203_models.DescribeCloudProductFieldStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCloudProductFieldStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCloudProductFieldStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeCloudProductFieldStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cloud_product_field_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeCloudProductFieldStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCloudProductFieldStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCloudProductFieldStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCloudProductFieldStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloud_product_field_statistics(
        self,
        request: sas_20181203_models.DescribeCloudProductFieldStatisticsRequest,
    ) -> sas_20181203_models.DescribeCloudProductFieldStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_product_field_statistics_with_options(request, runtime)

    async def describe_cloud_product_field_statistics_async(
        self,
        request: sas_20181203_models.DescribeCloudProductFieldStatisticsRequest,
    ) -> sas_20181203_models.DescribeCloudProductFieldStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_product_field_statistics_with_options_async(request, runtime)

    def describe_concern_necessity_with_options(
        self,
        request: sas_20181203_models.DescribeConcernNecessityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeConcernNecessityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeConcernNecessityResponse().from_map(
            self.do_rpcrequest('DescribeConcernNecessity', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_concern_necessity_with_options_async(
        self,
        request: sas_20181203_models.DescribeConcernNecessityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeConcernNecessityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeConcernNecessityResponse().from_map(
            await self.do_rpcrequest_async('DescribeConcernNecessity', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeContainerStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeContainerStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_container_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeContainerStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeContainerStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeContainerStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeContainerStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCriteriaResponse().from_map(
            self.do_rpcrequest('DescribeCriteria', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_criteria_with_options_async(
        self,
        request: sas_20181203_models.DescribeCriteriaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeCriteriaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeCriteriaResponse().from_map(
            await self.do_rpcrequest_async('DescribeCriteria', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeDialogMessagesResponse().from_map(
            self.do_rpcrequest('DescribeDialogMessages', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dialog_messages_with_options_async(
        self,
        request: sas_20181203_models.DescribeDialogMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDialogMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeDialogMessagesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDialogMessages', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeDingTalkResponse().from_map(
            self.do_rpcrequest('DescribeDingTalk', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ding_talk_with_options_async(
        self,
        request: sas_20181203_models.DescribeDingTalkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDingTalkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeDingTalkResponse().from_map(
            await self.do_rpcrequest_async('DescribeDingTalk', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeDomainCountResponse().from_map(
            self.do_rpcrequest('DescribeDomainCount', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_count_with_options_async(
        self,
        request: sas_20181203_models.DescribeDomainCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDomainCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeDomainCountResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainCount', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeDomainDetailResponse().from_map(
            self.do_rpcrequest('DescribeDomainDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeDomainDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeDomainListResponse().from_map(
            self.do_rpcrequest('DescribeDomainList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeDomainListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeDomainListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_emg_vul_group_with_options(
        self,
        request: sas_20181203_models.DescribeEmgVulGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeEmgVulGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeEmgVulGroupResponse().from_map(
            self.do_rpcrequest('DescribeEmgVulGroup', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_emg_vul_group_with_options_async(
        self,
        request: sas_20181203_models.DescribeEmgVulGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeEmgVulGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeEmgVulGroupResponse().from_map(
            await self.do_rpcrequest_async('DescribeEmgVulGroup', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_emg_vul_group(
        self,
        request: sas_20181203_models.DescribeEmgVulGroupRequest,
    ) -> sas_20181203_models.DescribeEmgVulGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_emg_vul_group_with_options(request, runtime)

    async def describe_emg_vul_group_async(
        self,
        request: sas_20181203_models.DescribeEmgVulGroupRequest,
    ) -> sas_20181203_models.DescribeEmgVulGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_emg_vul_group_with_options_async(request, runtime)

    def describe_export_info_with_options(
        self,
        request: sas_20181203_models.DescribeExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExportInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeExportInfoResponse().from_map(
            self.do_rpcrequest('DescribeExportInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_export_info_with_options_async(
        self,
        request: sas_20181203_models.DescribeExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExportInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeExportInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeExportInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeExposedInstanceCriteriaResponse().from_map(
            self.do_rpcrequest('DescribeExposedInstanceCriteria', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_exposed_instance_criteria_with_options_async(
        self,
        request: sas_20181203_models.DescribeExposedInstanceCriteriaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedInstanceCriteriaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeExposedInstanceCriteriaResponse().from_map(
            await self.do_rpcrequest_async('DescribeExposedInstanceCriteria', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeExposedInstanceDetailResponse().from_map(
            self.do_rpcrequest('DescribeExposedInstanceDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_exposed_instance_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeExposedInstanceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedInstanceDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeExposedInstanceDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeExposedInstanceDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeExposedInstanceListResponse().from_map(
            self.do_rpcrequest('DescribeExposedInstanceList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_exposed_instance_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeExposedInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeExposedInstanceListResponse().from_map(
            await self.do_rpcrequest_async('DescribeExposedInstanceList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: sas_20181203_models.DescribeExposedStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeExposedStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeExposedStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_exposed_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeExposedStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeExposedStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeExposedStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeExposedStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_exposed_statistics(
        self,
        request: sas_20181203_models.DescribeExposedStatisticsRequest,
    ) -> sas_20181203_models.DescribeExposedStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_statistics_with_options(request, runtime)

    async def describe_exposed_statistics_async(
        self,
        request: sas_20181203_models.DescribeExposedStatisticsRequest,
    ) -> sas_20181203_models.DescribeExposedStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_exposed_statistics_with_options_async(request, runtime)

    def describe_field_statistics_with_options(
        self,
        request: sas_20181203_models.DescribeFieldStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeFieldStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeFieldStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeFieldStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_field_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeFieldStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeFieldStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeFieldStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFieldStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_graph_4investigation_online_with_options(
        self,
        request: sas_20181203_models.DescribeGraph4InvestigationOnlineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGraph4InvestigationOnlineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeGraph4InvestigationOnlineResponse().from_map(
            self.do_rpcrequest('DescribeGraph4InvestigationOnline', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_graph_4investigation_online_with_options_async(
        self,
        request: sas_20181203_models.DescribeGraph4InvestigationOnlineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGraph4InvestigationOnlineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeGraph4InvestigationOnlineResponse().from_map(
            await self.do_rpcrequest_async('DescribeGraph4InvestigationOnline', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_graph_4investigation_online(
        self,
        request: sas_20181203_models.DescribeGraph4InvestigationOnlineRequest,
    ) -> sas_20181203_models.DescribeGraph4InvestigationOnlineResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_graph_4investigation_online_with_options(request, runtime)

    async def describe_graph_4investigation_online_async(
        self,
        request: sas_20181203_models.DescribeGraph4InvestigationOnlineRequest,
    ) -> sas_20181203_models.DescribeGraph4InvestigationOnlineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_graph_4investigation_online_with_options_async(request, runtime)

    def describe_grouped_container_instances_with_options(
        self,
        request: sas_20181203_models.DescribeGroupedContainerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedContainerInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeGroupedContainerInstancesResponse().from_map(
            self.do_rpcrequest('DescribeGroupedContainerInstances', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_grouped_container_instances_with_options_async(
        self,
        request: sas_20181203_models.DescribeGroupedContainerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedContainerInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeGroupedContainerInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeGroupedContainerInstances', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_grouped_malicious_files_with_options(
        self,
        request: sas_20181203_models.DescribeGroupedMaliciousFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedMaliciousFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeGroupedMaliciousFilesResponse().from_map(
            self.do_rpcrequest('DescribeGroupedMaliciousFiles', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_grouped_malicious_files_with_options_async(
        self,
        request: sas_20181203_models.DescribeGroupedMaliciousFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedMaliciousFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeGroupedMaliciousFilesResponse().from_map(
            await self.do_rpcrequest_async('DescribeGroupedMaliciousFiles', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeGroupedTagsResponse().from_map(
            self.do_rpcrequest('DescribeGroupedTags', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_grouped_tags_with_options_async(
        self,
        request: sas_20181203_models.DescribeGroupedTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeGroupedTagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeGroupedTags', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeGroupedVulResponse().from_map(
            self.do_rpcrequest('DescribeGroupedVul', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_grouped_vul_with_options_async(
        self,
        request: sas_20181203_models.DescribeGroupedVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeGroupedVulResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeGroupedVulResponse().from_map(
            await self.do_rpcrequest_async('DescribeGroupedVul', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: sas_20181203_models.DescribeHoneyPotAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeHoneyPotAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeHoneyPotAuthResponse().from_map(
            self.do_rpcrequest('DescribeHoneyPotAuth', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_honey_pot_auth_with_options_async(
        self,
        request: sas_20181203_models.DescribeHoneyPotAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeHoneyPotAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeHoneyPotAuthResponse().from_map(
            await self.do_rpcrequest_async('DescribeHoneyPotAuth', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_honey_pot_auth(
        self,
        request: sas_20181203_models.DescribeHoneyPotAuthRequest,
    ) -> sas_20181203_models.DescribeHoneyPotAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_honey_pot_auth_with_options(request, runtime)

    async def describe_honey_pot_auth_async(
        self,
        request: sas_20181203_models.DescribeHoneyPotAuthRequest,
    ) -> sas_20181203_models.DescribeHoneyPotAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_honey_pot_auth_with_options_async(request, runtime)

    def describe_honey_pot_susp_statistics_with_options(
        self,
        request: sas_20181203_models.DescribeHoneyPotSuspStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeHoneyPotSuspStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_honey_pot_susp_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeHoneyPotSuspStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeHoneyPotSuspStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_image_grouped_vul_list_with_options(
        self,
        request: sas_20181203_models.DescribeImageGroupedVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageGroupedVulListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeImageGroupedVulListResponse().from_map(
            self.do_rpcrequest('DescribeImageGroupedVulList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_grouped_vul_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeImageGroupedVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageGroupedVulListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeImageGroupedVulListResponse().from_map(
            await self.do_rpcrequest_async('DescribeImageGroupedVulList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_image_statistics_with_options(
        self,
        request: sas_20181203_models.DescribeImageStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeImageStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeImageStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeImageStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeImageStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeImageStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_statistics(
        self,
        request: sas_20181203_models.DescribeImageStatisticsRequest,
    ) -> sas_20181203_models.DescribeImageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_statistics_with_options(request, runtime)

    async def describe_image_statistics_async(
        self,
        request: sas_20181203_models.DescribeImageStatisticsRequest,
    ) -> sas_20181203_models.DescribeImageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_statistics_with_options_async(request, runtime)

    def describe_image_vul_list_with_options(
        self,
        request: sas_20181203_models.DescribeImageVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageVulListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeImageVulListResponse().from_map(
            self.do_rpcrequest('DescribeImageVulList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_vul_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeImageVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeImageVulListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeImageVulListResponse().from_map(
            await self.do_rpcrequest_async('DescribeImageVulList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeInstallCaptchaResponse().from_map(
            self.do_rpcrequest('DescribeInstallCaptcha', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_install_captcha_with_options_async(
        self,
        request: sas_20181203_models.DescribeInstallCaptchaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstallCaptchaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeInstallCaptchaResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstallCaptcha', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_instance_anti_brute_force_rules_with_options(
        self,
        request: sas_20181203_models.DescribeInstanceAntiBruteForceRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAntiBruteForceRules', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_anti_brute_force_rules_with_options_async(
        self,
        request: sas_20181203_models.DescribeInstanceAntiBruteForceRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceAntiBruteForceRules', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeInstanceStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_statistics_with_options_async(
        self,
        request: sas_20181203_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeInstanceStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeIpInfoResponse().from_map(
            self.do_rpcrequest('DescribeIpInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ip_info_with_options_async(
        self,
        request: sas_20181203_models.DescribeIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeIpInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeIpInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeIpInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_module_config_with_options(
        self,
        request: sas_20181203_models.DescribeModuleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeModuleConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeModuleConfigResponse().from_map(
            self.do_rpcrequest('DescribeModuleConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_module_config_with_options_async(
        self,
        request: sas_20181203_models.DescribeModuleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeModuleConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeModuleConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeModuleConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_module_config(
        self,
        request: sas_20181203_models.DescribeModuleConfigRequest,
    ) -> sas_20181203_models.DescribeModuleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_module_config_with_options(request, runtime)

    async def describe_module_config_async(
        self,
        request: sas_20181203_models.DescribeModuleConfigRequest,
    ) -> sas_20181203_models.DescribeModuleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_module_config_with_options_async(request, runtime)

    def describe_notice_config_with_options(
        self,
        request: sas_20181203_models.DescribeNoticeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeNoticeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeNoticeConfigResponse().from_map(
            self.do_rpcrequest('DescribeNoticeConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_notice_config_with_options_async(
        self,
        request: sas_20181203_models.DescribeNoticeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeNoticeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeNoticeConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeNoticeConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyCountResponse().from_map(
            self.do_rpcrequest('DescribePropertyCount', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_count_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyCountResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertyCount', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyCronDetailResponse().from_map(
            self.do_rpcrequest('DescribePropertyCronDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_cron_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyCronDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyCronDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyCronDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertyCronDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyPortDetailResponse().from_map(
            self.do_rpcrequest('DescribePropertyPortDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_port_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyPortDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyPortDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyPortDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertyPortDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyPortItemResponse().from_map(
            self.do_rpcrequest('DescribePropertyPortItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_port_item_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyPortItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyPortItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyPortItemResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertyPortItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyProcDetailResponse().from_map(
            self.do_rpcrequest('DescribePropertyProcDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_proc_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyProcDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyProcDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyProcDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertyProcDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyProcItemResponse().from_map(
            self.do_rpcrequest('DescribePropertyProcItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_proc_item_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyProcItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyProcItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyProcItemResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertyProcItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyScaDetailResponse().from_map(
            self.do_rpcrequest('DescribePropertyScaDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_sca_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyScaDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyScaDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyScaDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertyScaDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertySoftwareDetailResponse().from_map(
            self.do_rpcrequest('DescribePropertySoftwareDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_software_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertySoftwareDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertySoftwareDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertySoftwareDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertySoftwareDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertySoftwareItemResponse().from_map(
            self.do_rpcrequest('DescribePropertySoftwareItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_software_item_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertySoftwareItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertySoftwareItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertySoftwareItemResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertySoftwareItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyUsageNewestResponse().from_map(
            self.do_rpcrequest('DescribePropertyUsageNewest', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_usage_newest_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyUsageNewestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyUsageNewestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyUsageNewestResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertyUsageNewest', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyUserDetailResponse().from_map(
            self.do_rpcrequest('DescribePropertyUserDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_user_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyUserDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyUserDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyUserDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertyUserDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyUserItemResponse().from_map(
            self.do_rpcrequest('DescribePropertyUserItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_property_user_item_with_options_async(
        self,
        request: sas_20181203_models.DescribePropertyUserItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribePropertyUserItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribePropertyUserItemResponse().from_map(
            await self.do_rpcrequest_async('DescribePropertyUserItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_risk_check_item_result_with_options(
        self,
        request: sas_20181203_models.DescribeRiskCheckItemResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskCheckItemResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeRiskCheckItemResultResponse().from_map(
            self.do_rpcrequest('DescribeRiskCheckItemResult', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_risk_check_item_result_with_options_async(
        self,
        request: sas_20181203_models.DescribeRiskCheckItemResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskCheckItemResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeRiskCheckItemResultResponse().from_map(
            await self.do_rpcrequest_async('DescribeRiskCheckItemResult', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeRiskCheckResultResponse().from_map(
            self.do_rpcrequest('DescribeRiskCheckResult', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_risk_check_result_with_options_async(
        self,
        request: sas_20181203_models.DescribeRiskCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskCheckResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeRiskCheckResultResponse().from_map(
            await self.do_rpcrequest_async('DescribeRiskCheckResult', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeRiskCheckSummaryResponse().from_map(
            self.do_rpcrequest('DescribeRiskCheckSummary', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_risk_check_summary_with_options_async(
        self,
        request: sas_20181203_models.DescribeRiskCheckSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskCheckSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeRiskCheckSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeRiskCheckSummary', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeRiskItemTypeResponse().from_map(
            self.do_rpcrequest('DescribeRiskItemType', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_risk_item_type_with_options_async(
        self,
        request: sas_20181203_models.DescribeRiskItemTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskItemTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeRiskItemTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeRiskItemType', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeRiskListCheckResultResponse().from_map(
            self.do_rpcrequest('DescribeRiskListCheckResult', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_risk_list_check_result_with_options_async(
        self,
        request: sas_20181203_models.DescribeRiskListCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeRiskListCheckResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeRiskListCheckResultResponse().from_map(
            await self.do_rpcrequest_async('DescribeRiskListCheckResult', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_sas_asset_statistics_column_with_options(
        self,
        request: sas_20181203_models.DescribeSasAssetStatisticsColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSasAssetStatisticsColumnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSasAssetStatisticsColumnResponse().from_map(
            self.do_rpcrequest('DescribeSasAssetStatisticsColumn', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sas_asset_statistics_column_with_options_async(
        self,
        request: sas_20181203_models.DescribeSasAssetStatisticsColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSasAssetStatisticsColumnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSasAssetStatisticsColumnResponse().from_map(
            await self.do_rpcrequest_async('DescribeSasAssetStatisticsColumn', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sas_asset_statistics_column(
        self,
        request: sas_20181203_models.DescribeSasAssetStatisticsColumnRequest,
    ) -> sas_20181203_models.DescribeSasAssetStatisticsColumnResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sas_asset_statistics_column_with_options(request, runtime)

    async def describe_sas_asset_statistics_column_async(
        self,
        request: sas_20181203_models.DescribeSasAssetStatisticsColumnRequest,
    ) -> sas_20181203_models.DescribeSasAssetStatisticsColumnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sas_asset_statistics_column_with_options_async(request, runtime)

    def describe_search_condition_with_options(
        self,
        request: sas_20181203_models.DescribeSearchConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSearchConditionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSearchConditionResponse().from_map(
            self.do_rpcrequest('DescribeSearchCondition', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_search_condition_with_options_async(
        self,
        request: sas_20181203_models.DescribeSearchConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSearchConditionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSearchConditionResponse().from_map(
            await self.do_rpcrequest_async('DescribeSearchCondition', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSecureSuggestionResponse().from_map(
            self.do_rpcrequest('DescribeSecureSuggestion', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_secure_suggestion_with_options_async(
        self,
        request: sas_20181203_models.DescribeSecureSuggestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecureSuggestionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSecureSuggestionResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecureSuggestion', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSecurityCheckScheduleConfigResponse().from_map(
            self.do_rpcrequest('DescribeSecurityCheckScheduleConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_check_schedule_config_with_options_async(
        self,
        request: sas_20181203_models.DescribeSecurityCheckScheduleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityCheckScheduleConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSecurityCheckScheduleConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityCheckScheduleConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_security_event_operations_with_options(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityEventOperationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSecurityEventOperationsResponse().from_map(
            self.do_rpcrequest('DescribeSecurityEventOperations', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_event_operations_with_options_async(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityEventOperationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSecurityEventOperationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityEventOperations', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_security_event_operation_status_with_options(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityEventOperationStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSecurityEventOperationStatusResponse().from_map(
            self.do_rpcrequest('DescribeSecurityEventOperationStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_event_operation_status_with_options_async(
        self,
        request: sas_20181203_models.DescribeSecurityEventOperationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityEventOperationStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSecurityEventOperationStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityEventOperationStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_security_stat_info_with_options(
        self,
        request: sas_20181203_models.DescribeSecurityStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityStatInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSecurityStatInfoResponse().from_map(
            self.do_rpcrequest('DescribeSecurityStatInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_stat_info_with_options_async(
        self,
        request: sas_20181203_models.DescribeSecurityStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSecurityStatInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSecurityStatInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityStatInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_similar_event_scenarios_with_options(
        self,
        request: sas_20181203_models.DescribeSimilarEventScenariosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSimilarEventScenariosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSimilarEventScenariosResponse().from_map(
            self.do_rpcrequest('DescribeSimilarEventScenarios', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_similar_event_scenarios_with_options_async(
        self,
        request: sas_20181203_models.DescribeSimilarEventScenariosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSimilarEventScenariosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSimilarEventScenariosResponse().from_map(
            await self.do_rpcrequest_async('DescribeSimilarEventScenarios', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSimilarSecurityEventsResponse().from_map(
            self.do_rpcrequest('DescribeSimilarSecurityEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_similar_security_events_with_options_async(
        self,
        request: sas_20181203_models.DescribeSimilarSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSimilarSecurityEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSimilarSecurityEventsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSimilarSecurityEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_strategy_exec_detail_with_options(
        self,
        request: sas_20181203_models.DescribeStrategyExecDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeStrategyExecDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeStrategyExecDetailResponse().from_map(
            self.do_rpcrequest('DescribeStrategyExecDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_strategy_exec_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeStrategyExecDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeStrategyExecDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeStrategyExecDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeStrategyExecDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_stratety_with_options(
        self,
        request: sas_20181203_models.DescribeStratetyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeStratetyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeStratetyResponse().from_map(
            self.do_rpcrequest('DescribeStratety', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_stratety_with_options_async(
        self,
        request: sas_20181203_models.DescribeStratetyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeStratetyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeStratetyResponse().from_map(
            await self.do_rpcrequest_async('DescribeStratety', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_stratety(
        self,
        request: sas_20181203_models.DescribeStratetyRequest,
    ) -> sas_20181203_models.DescribeStratetyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_stratety_with_options(request, runtime)

    async def describe_stratety_async(
        self,
        request: sas_20181203_models.DescribeStratetyRequest,
    ) -> sas_20181203_models.DescribeStratetyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_stratety_with_options_async(request, runtime)

    def describe_summary_info_with_options(
        self,
        request: sas_20181203_models.DescribeSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSummaryInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSummaryInfoResponse().from_map(
            self.do_rpcrequest('DescribeSummaryInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_summary_info_with_options_async(
        self,
        request: sas_20181203_models.DescribeSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSummaryInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSummaryInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeSummaryInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_susp_event_detail_with_options(
        self,
        request: sas_20181203_models.DescribeSuspEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspEventDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSuspEventDetailResponse().from_map(
            self.do_rpcrequest('DescribeSuspEventDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_susp_event_detail_with_options_async(
        self,
        request: sas_20181203_models.DescribeSuspEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspEventDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSuspEventDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeSuspEventDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSuspEventQuaraFilesResponse().from_map(
            self.do_rpcrequest('DescribeSuspEventQuaraFiles', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_susp_event_quara_files_with_options_async(
        self,
        request: sas_20181203_models.DescribeSuspEventQuaraFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspEventQuaraFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSuspEventQuaraFilesResponse().from_map(
            await self.do_rpcrequest_async('DescribeSuspEventQuaraFiles', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSuspEventsResponse().from_map(
            self.do_rpcrequest('DescribeSuspEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_susp_events_with_options_async(
        self,
        request: sas_20181203_models.DescribeSuspEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeSuspEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeSuspEventsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSuspEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_user_baseline_authorization_with_options(
        self,
        request: sas_20181203_models.DescribeUserBaselineAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeUserBaselineAuthorizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeUserBaselineAuthorizationResponse().from_map(
            self.do_rpcrequest('DescribeUserBaselineAuthorization', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_baseline_authorization_with_options_async(
        self,
        request: sas_20181203_models.DescribeUserBaselineAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeUserBaselineAuthorizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeUserBaselineAuthorizationResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserBaselineAuthorization', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeUserLayoutAuthorizationResponse().from_map(
            self.do_rpcrequest('DescribeUserLayoutAuthorization', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_layout_authorization_with_options_async(
        self,
        request: sas_20181203_models.DescribeUserLayoutAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeUserLayoutAuthorizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeUserLayoutAuthorizationResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserLayoutAuthorization', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVersionConfigResponse().from_map(
            self.do_rpcrequest('DescribeVersionConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_version_config_with_options_async(
        self,
        request: sas_20181203_models.DescribeVersionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVersionConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVersionConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeVersionConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVolDingdingMessageResponse().from_map(
            self.do_rpcrequest('DescribeVolDingdingMessage', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vol_dingding_message_with_options_async(
        self,
        request: sas_20181203_models.DescribeVolDingdingMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVolDingdingMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVolDingdingMessageResponse().from_map(
            await self.do_rpcrequest_async('DescribeVolDingdingMessage', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: sas_20181203_models.DescribeVpcHoneyPotCriteriaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse().from_map(
            self.do_rpcrequest('DescribeVpcHoneyPotCriteria', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpc_honey_pot_criteria_with_options_async(
        self,
        request: sas_20181203_models.DescribeVpcHoneyPotCriteriaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpcHoneyPotCriteria', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpc_honey_pot_criteria(
        self,
        request: sas_20181203_models.DescribeVpcHoneyPotCriteriaRequest,
    ) -> sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_honey_pot_criteria_with_options(request, runtime)

    async def describe_vpc_honey_pot_criteria_async(
        self,
        request: sas_20181203_models.DescribeVpcHoneyPotCriteriaRequest,
    ) -> sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_honey_pot_criteria_with_options_async(request, runtime)

    def describe_vpc_honey_pot_list_with_options(
        self,
        request: sas_20181203_models.DescribeVpcHoneyPotListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcHoneyPotListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVpcHoneyPotListResponse().from_map(
            self.do_rpcrequest('DescribeVpcHoneyPotList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpc_honey_pot_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeVpcHoneyPotListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcHoneyPotListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVpcHoneyPotListResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpcHoneyPotList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: sas_20181203_models.DescribeVpcListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVpcListResponse().from_map(
            self.do_rpcrequest('DescribeVpcList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpc_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeVpcListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVpcListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVpcListResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpcList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpc_list(
        self,
        request: sas_20181203_models.DescribeVpcListRequest,
    ) -> sas_20181203_models.DescribeVpcListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_list_with_options(request, runtime)

    async def describe_vpc_list_async(
        self,
        request: sas_20181203_models.DescribeVpcListRequest,
    ) -> sas_20181203_models.DescribeVpcListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_list_with_options_async(request, runtime)

    def describe_vul_details_with_options(
        self,
        request: sas_20181203_models.DescribeVulDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVulDetailsResponse().from_map(
            self.do_rpcrequest('DescribeVulDetails', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vul_details_with_options_async(
        self,
        request: sas_20181203_models.DescribeVulDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVulDetailsResponse().from_map(
            await self.do_rpcrequest_async('DescribeVulDetails', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_vul_list_with_options(
        self,
        request: sas_20181203_models.DescribeVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVulListResponse().from_map(
            self.do_rpcrequest('DescribeVulList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vul_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVulListResponse().from_map(
            await self.do_rpcrequest_async('DescribeVulList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVulWhitelistResponse().from_map(
            self.do_rpcrequest('DescribeVulWhitelist', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vul_whitelist_with_options_async(
        self,
        request: sas_20181203_models.DescribeVulWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeVulWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeVulWhitelistResponse().from_map(
            await self.do_rpcrequest_async('DescribeVulWhitelist', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeWarningMachinesResponse().from_map(
            self.do_rpcrequest('DescribeWarningMachines', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_warning_machines_with_options_async(
        self,
        request: sas_20181203_models.DescribeWarningMachinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeWarningMachinesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeWarningMachinesResponse().from_map(
            await self.do_rpcrequest_async('DescribeWarningMachines', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeWebLockBindListResponse().from_map(
            self.do_rpcrequest('DescribeWebLockBindList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_lock_bind_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeWebLockBindListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeWebLockBindListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeWebLockBindListResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebLockBindList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeWebLockConfigListResponse().from_map(
            self.do_rpcrequest('DescribeWebLockConfigList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_lock_config_list_with_options_async(
        self,
        request: sas_20181203_models.DescribeWebLockConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.DescribeWebLockConfigListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.DescribeWebLockConfigListResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebLockConfigList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ExportRecordResponse().from_map(
            self.do_rpcrequest('ExportRecord', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_record_with_options_async(
        self,
        request: sas_20181203_models.ExportRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ExportRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ExportRecordResponse().from_map(
            await self.do_rpcrequest_async('ExportRecord', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def fix_check_warnings_with_options(
        self,
        request: sas_20181203_models.FixCheckWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.FixCheckWarningsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.FixCheckWarningsResponse().from_map(
            self.do_rpcrequest('FixCheckWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def fix_check_warnings_with_options_async(
        self,
        request: sas_20181203_models.FixCheckWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.FixCheckWarningsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.FixCheckWarningsResponse().from_map(
            await self.do_rpcrequest_async('FixCheckWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_inc_iocs_with_options(
        self,
        request: sas_20181203_models.GetIncIOCsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.GetIncIOCsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.GetIncIOCsResponse().from_map(
            self.do_rpcrequest('GetIncIOCs', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_inc_iocs_with_options_async(
        self,
        request: sas_20181203_models.GetIncIOCsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.GetIncIOCsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.GetIncIOCsResponse().from_map(
            await self.do_rpcrequest_async('GetIncIOCs', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_inc_iocs(
        self,
        request: sas_20181203_models.GetIncIOCsRequest,
    ) -> sas_20181203_models.GetIncIOCsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_inc_iocs_with_options(request, runtime)

    async def get_inc_iocs_async(
        self,
        request: sas_20181203_models.GetIncIOCsRequest,
    ) -> sas_20181203_models.GetIncIOCsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_inc_iocs_with_options_async(request, runtime)

    def get_iocs_with_options(
        self,
        request: sas_20181203_models.GetIOCsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.GetIOCsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.GetIOCsResponse().from_map(
            self.do_rpcrequest('GetIOCs', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_iocs_with_options_async(
        self,
        request: sas_20181203_models.GetIOCsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.GetIOCsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.GetIOCsResponse().from_map(
            await self.do_rpcrequest_async('GetIOCs', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_iocs(
        self,
        request: sas_20181203_models.GetIOCsRequest,
    ) -> sas_20181203_models.GetIOCsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_iocs_with_options(request, runtime)

    async def get_iocs_async(
        self,
        request: sas_20181203_models.GetIOCsRequest,
    ) -> sas_20181203_models.GetIOCsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_iocs_with_options_async(request, runtime)

    def handle_security_events_with_options(
        self,
        request: sas_20181203_models.HandleSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.HandleSecurityEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.HandleSecurityEventsResponse().from_map(
            self.do_rpcrequest('HandleSecurityEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def handle_security_events_with_options_async(
        self,
        request: sas_20181203_models.HandleSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.HandleSecurityEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.HandleSecurityEventsResponse().from_map(
            await self.do_rpcrequest_async('HandleSecurityEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.HandleSimilarSecurityEventsResponse().from_map(
            self.do_rpcrequest('HandleSimilarSecurityEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def handle_similar_security_events_with_options_async(
        self,
        request: sas_20181203_models.HandleSimilarSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.HandleSimilarSecurityEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.HandleSimilarSecurityEventsResponse().from_map(
            await self.do_rpcrequest_async('HandleSimilarSecurityEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.IgnoreHcCheckWarningsResponse().from_map(
            self.do_rpcrequest('IgnoreHcCheckWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ignore_hc_check_warnings_with_options_async(
        self,
        request: sas_20181203_models.IgnoreHcCheckWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.IgnoreHcCheckWarningsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.IgnoreHcCheckWarningsResponse().from_map(
            await self.do_rpcrequest_async('IgnoreHcCheckWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def modify_anti_brute_force_rule_with_options(
        self,
        request: sas_20181203_models.ModifyAntiBruteForceRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyAntiBruteForceRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyAntiBruteForceRuleResponse().from_map(
            self.do_rpcrequest('ModifyAntiBruteForceRule', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_anti_brute_force_rule_with_options_async(
        self,
        request: sas_20181203_models.ModifyAntiBruteForceRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyAntiBruteForceRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyAntiBruteForceRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyAntiBruteForceRule', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def modify_create_vul_whitelist_with_options(
        self,
        request: sas_20181203_models.ModifyCreateVulWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyCreateVulWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyCreateVulWhitelistResponse().from_map(
            self.do_rpcrequest('ModifyCreateVulWhitelist', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_create_vul_whitelist_with_options_async(
        self,
        request: sas_20181203_models.ModifyCreateVulWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyCreateVulWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyCreateVulWhitelistResponse().from_map(
            await self.do_rpcrequest_async('ModifyCreateVulWhitelist', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyEmgVulSubmitResponse().from_map(
            self.do_rpcrequest('ModifyEmgVulSubmit', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_emg_vul_submit_with_options_async(
        self,
        request: sas_20181203_models.ModifyEmgVulSubmitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyEmgVulSubmitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyEmgVulSubmitResponse().from_map(
            await self.do_rpcrequest_async('ModifyEmgVulSubmit', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyGroupPropertyResponse().from_map(
            self.do_rpcrequest('ModifyGroupProperty', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_group_property_with_options_async(
        self,
        request: sas_20181203_models.ModifyGroupPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyGroupPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyGroupPropertyResponse().from_map(
            await self.do_rpcrequest_async('ModifyGroupProperty', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyInstanceAntiBruteForceRuleResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAntiBruteForceRule', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_anti_brute_force_rule_with_options_async(
        self,
        request: sas_20181203_models.ModifyInstanceAntiBruteForceRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyInstanceAntiBruteForceRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyInstanceAntiBruteForceRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAntiBruteForceRule', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyLoginBaseConfigResponse().from_map(
            self.do_rpcrequest('ModifyLoginBaseConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_login_base_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyLoginBaseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyLoginBaseConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyLoginBaseConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyLoginBaseConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyLoginSwitchConfigResponse().from_map(
            self.do_rpcrequest('ModifyLoginSwitchConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_login_switch_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyLoginSwitchConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyLoginSwitchConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyLoginSwitchConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyLoginSwitchConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def modify_notice_config_with_options(
        self,
        request: sas_20181203_models.ModifyNoticeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyNoticeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyNoticeConfigResponse().from_map(
            self.do_rpcrequest('ModifyNoticeConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_notice_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyNoticeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyNoticeConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyNoticeConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyNoticeConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_notice_config(
        self,
        request: sas_20181203_models.ModifyNoticeConfigRequest,
    ) -> sas_20181203_models.ModifyNoticeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_notice_config_with_options(request, runtime)

    async def modify_notice_config_async(
        self,
        request: sas_20181203_models.ModifyNoticeConfigRequest,
    ) -> sas_20181203_models.ModifyNoticeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_notice_config_with_options_async(request, runtime)

    def modify_operate_vul_with_options(
        self,
        request: sas_20181203_models.ModifyOperateVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyOperateVulResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyOperateVulResponse().from_map(
            self.do_rpcrequest('ModifyOperateVul', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_operate_vul_with_options_async(
        self,
        request: sas_20181203_models.ModifyOperateVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyOperateVulResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyOperateVulResponse().from_map(
            await self.do_rpcrequest_async('ModifyOperateVul', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyPushAllTaskResponse().from_map(
            self.do_rpcrequest('ModifyPushAllTask', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_push_all_task_with_options_async(
        self,
        request: sas_20181203_models.ModifyPushAllTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyPushAllTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyPushAllTaskResponse().from_map(
            await self.do_rpcrequest_async('ModifyPushAllTask', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyRiskCheckStatusResponse().from_map(
            self.do_rpcrequest('ModifyRiskCheckStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_risk_check_status_with_options_async(
        self,
        request: sas_20181203_models.ModifyRiskCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyRiskCheckStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyRiskCheckStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyRiskCheckStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyRiskSingleResultStatusResponse().from_map(
            self.do_rpcrequest('ModifyRiskSingleResultStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_risk_single_result_status_with_options_async(
        self,
        request: sas_20181203_models.ModifyRiskSingleResultStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyRiskSingleResultStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyRiskSingleResultStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyRiskSingleResultStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifySecurityCheckScheduleConfigResponse().from_map(
            self.do_rpcrequest('ModifySecurityCheckScheduleConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_check_schedule_config_with_options_async(
        self,
        request: sas_20181203_models.ModifySecurityCheckScheduleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifySecurityCheckScheduleConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifySecurityCheckScheduleConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityCheckScheduleConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyStartVulScanResponse().from_map(
            self.do_rpcrequest('ModifyStartVulScan', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_start_vul_scan_with_options_async(
        self,
        request: sas_20181203_models.ModifyStartVulScanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyStartVulScanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyStartVulScanResponse().from_map(
            await self.do_rpcrequest_async('ModifyStartVulScan', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyTagWithUuidResponse().from_map(
            self.do_rpcrequest('ModifyTagWithUuid', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_tag_with_uuid_with_options_async(
        self,
        request: sas_20181203_models.ModifyTagWithUuidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyTagWithUuidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyTagWithUuidResponse().from_map(
            await self.do_rpcrequest_async('ModifyTagWithUuid', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyVpcHoneyPotResponse().from_map(
            self.do_rpcrequest('ModifyVpcHoneyPot', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vpc_honey_pot_with_options_async(
        self,
        request: sas_20181203_models.ModifyVpcHoneyPotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyVpcHoneyPotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyVpcHoneyPotResponse().from_map(
            await self.do_rpcrequest_async('ModifyVpcHoneyPot', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyVulTargetConfigResponse().from_map(
            self.do_rpcrequest('ModifyVulTargetConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vul_target_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyVulTargetConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyVulTargetConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyVulTargetConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyVulTargetConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyWebLockCreateConfigResponse().from_map(
            self.do_rpcrequest('ModifyWebLockCreateConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_lock_create_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyWebLockCreateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockCreateConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyWebLockCreateConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebLockCreateConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyWebLockDeleteConfigResponse().from_map(
            self.do_rpcrequest('ModifyWebLockDeleteConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_lock_delete_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyWebLockDeleteConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockDeleteConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyWebLockDeleteConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebLockDeleteConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyWebLockStartResponse().from_map(
            self.do_rpcrequest('ModifyWebLockStart', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_lock_start_with_options_async(
        self,
        request: sas_20181203_models.ModifyWebLockStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockStartResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyWebLockStartResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebLockStart', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def modify_web_lock_unbind_with_options(
        self,
        request: sas_20181203_models.ModifyWebLockUnbindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockUnbindResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyWebLockUnbindResponse().from_map(
            self.do_rpcrequest('ModifyWebLockUnbind', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_lock_unbind_with_options_async(
        self,
        request: sas_20181203_models.ModifyWebLockUnbindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockUnbindResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyWebLockUnbindResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebLockUnbind', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_lock_unbind(
        self,
        request: sas_20181203_models.ModifyWebLockUnbindRequest,
    ) -> sas_20181203_models.ModifyWebLockUnbindResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_unbind_with_options(request, runtime)

    async def modify_web_lock_unbind_async(
        self,
        request: sas_20181203_models.ModifyWebLockUnbindRequest,
    ) -> sas_20181203_models.ModifyWebLockUnbindResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_web_lock_unbind_with_options_async(request, runtime)

    def modify_web_lock_update_config_with_options(
        self,
        request: sas_20181203_models.ModifyWebLockUpdateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockUpdateConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyWebLockUpdateConfigResponse().from_map(
            self.do_rpcrequest('ModifyWebLockUpdateConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_web_lock_update_config_with_options_async(
        self,
        request: sas_20181203_models.ModifyWebLockUpdateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ModifyWebLockUpdateConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ModifyWebLockUpdateConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyWebLockUpdateConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def operate_suspicious_target_config_with_options(
        self,
        request: sas_20181203_models.OperateSuspiciousTargetConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperateSuspiciousTargetConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.OperateSuspiciousTargetConfigResponse().from_map(
            self.do_rpcrequest('OperateSuspiciousTargetConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def operate_suspicious_target_config_with_options_async(
        self,
        request: sas_20181203_models.OperateSuspiciousTargetConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperateSuspiciousTargetConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.OperateSuspiciousTargetConfigResponse().from_map(
            await self.do_rpcrequest_async('OperateSuspiciousTargetConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def operation_susp_events_with_options(
        self,
        request: sas_20181203_models.OperationSuspEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperationSuspEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.OperationSuspEventsResponse().from_map(
            self.do_rpcrequest('OperationSuspEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def operation_susp_events_with_options_async(
        self,
        request: sas_20181203_models.OperationSuspEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.OperationSuspEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.OperationSuspEventsResponse().from_map(
            await self.do_rpcrequest_async('OperationSuspEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.PauseClientResponse().from_map(
            self.do_rpcrequest('PauseClient', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pause_client_with_options_async(
        self,
        request: sas_20181203_models.PauseClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.PauseClientResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.PauseClientResponse().from_map(
            await self.do_rpcrequest_async('PauseClient', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def refresh_container_assets_with_options(
        self,
        request: sas_20181203_models.RefreshContainerAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.RefreshContainerAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.RefreshContainerAssetsResponse().from_map(
            self.do_rpcrequest('RefreshContainerAssets', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_container_assets_with_options_async(
        self,
        request: sas_20181203_models.RefreshContainerAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.RefreshContainerAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.RefreshContainerAssetsResponse().from_map(
            await self.do_rpcrequest_async('RefreshContainerAssets', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.RollbackSuspEventQuaraFileResponse().from_map(
            self.do_rpcrequest('RollbackSuspEventQuaraFile', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rollback_susp_event_quara_file_with_options_async(
        self,
        request: sas_20181203_models.RollbackSuspEventQuaraFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.RollbackSuspEventQuaraFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.RollbackSuspEventQuaraFileResponse().from_map(
            await self.do_rpcrequest_async('RollbackSuspEventQuaraFile', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.SasInstallCodeResponse().from_map(
            self.do_rpcrequest('SasInstallCode', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sas_install_code_with_options_async(
        self,
        request: sas_20181203_models.SasInstallCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.SasInstallCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.SasInstallCodeResponse().from_map(
            await self.do_rpcrequest_async('SasInstallCode', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.StartBaselineSecurityCheckResponse().from_map(
            self.do_rpcrequest('StartBaselineSecurityCheck', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_baseline_security_check_with_options_async(
        self,
        request: sas_20181203_models.StartBaselineSecurityCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.StartBaselineSecurityCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.StartBaselineSecurityCheckResponse().from_map(
            await self.do_rpcrequest_async('StartBaselineSecurityCheck', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.StartImageVulScanResponse().from_map(
            self.do_rpcrequest('StartImageVulScan', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_image_vul_scan_with_options_async(
        self,
        request: sas_20181203_models.StartImageVulScanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.StartImageVulScanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.StartImageVulScanResponse().from_map(
            await self.do_rpcrequest_async('StartImageVulScan', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def validate_hc_warnings_with_options(
        self,
        request: sas_20181203_models.ValidateHcWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ValidateHcWarningsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ValidateHcWarningsResponse().from_map(
            self.do_rpcrequest('ValidateHcWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def validate_hc_warnings_with_options_async(
        self,
        request: sas_20181203_models.ValidateHcWarningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20181203_models.ValidateHcWarningsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sas_20181203_models.ValidateHcWarningsResponse().from_map(
            await self.do_rpcrequest_async('ValidateHcWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
