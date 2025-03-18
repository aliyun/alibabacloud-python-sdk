# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sas20210114 import models as sas_20210114_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'tds.cn-shanghai.aliyuncs.com',
            'cn-beijing': 'tds.cn-shanghai.aliyuncs.com',
            'cn-zhangjiakou': 'tds.cn-shanghai.aliyuncs.com',
            'cn-huhehaote': 'tds.cn-shanghai.aliyuncs.com',
            'cn-wulanchabu': 'tds.cn-shanghai.aliyuncs.com',
            'cn-hangzhou': 'tds.cn-shanghai.aliyuncs.com',
            'cn-shanghai': 'tds.cn-shanghai.aliyuncs.com',
            'cn-nanjing': 'tds.cn-shanghai.aliyuncs.com',
            'cn-fuzhou': 'tds.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'tds.cn-shanghai.aliyuncs.com',
            'cn-heyuan': 'tds.cn-shanghai.aliyuncs.com',
            'cn-guangzhou': 'tds.cn-shanghai.aliyuncs.com',
            'ap-southeast-2': 'tds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-6': 'tds.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2': 'tds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'tds.ap-southeast-1.aliyuncs.com',
            'ap-northeast-1': 'tds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-7': 'tds.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'tds.cn-shanghai.aliyuncs.com',
            'ap-southeast-1': 'tds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'tds.ap-southeast-1.aliyuncs.com',
            'cn-hongkong': 'tds.cn-shanghai.aliyuncs.com',
            'eu-central-1': 'tds.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'tds.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'tds.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'tds.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'tds.ap-southeast-1.aliyuncs.com',
            'me-central-1': 'tds.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'tds.ap-southeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'tds.cn-shanghai.aliyuncs.com',
            'cn-hangzhou-finance': 'tds.cn-shanghai.aliyuncs.com',
            'cn-shanghai-finance-1': 'tds.cn-shanghai.aliyuncs.com',
            'cn-shenzhen-finance-1': 'tds.cn-shanghai.aliyuncs.com',
            'cn-heyuan-acdr-1': 'tds.cn-shanghai.aliyuncs.com',
            'cn-north-2-gov-1': 'tds.cn-shanghai.aliyuncs.com',
            'cn-qingdao-acdr-ut-1': 'tds.cn-shanghai.aliyuncs.com',
            'cn-shanghai-mybk': 'tds.cn-shanghai.aliyuncs.com',
            'cn-wuhan-lr': 'tds.cn-shanghai.aliyuncs.com',
            'cn-zhengzhou-jva': 'tds.cn-shanghai.aliyuncs.com'
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

    def create_screen_setting_with_options(
        self,
        request: sas_20210114_models.CreateScreenSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.CreateScreenSettingResponse:
        """
        @summary 新增或者修改用户大屏设置
        
        @param request: CreateScreenSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScreenSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.logo_power):
            query['LogoPower'] = request.logo_power
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.monitor_url):
            query['MonitorUrl'] = request.monitor_url
        if not UtilClient.is_unset(request.screen_data_map):
            query['ScreenDataMap'] = request.screen_data_map
        if not UtilClient.is_unset(request.screen_default):
            query['ScreenDefault'] = request.screen_default
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScreenSetting',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.CreateScreenSettingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.CreateScreenSettingResponse(),
                self.execute(params, req, runtime)
            )

    async def create_screen_setting_with_options_async(
        self,
        request: sas_20210114_models.CreateScreenSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.CreateScreenSettingResponse:
        """
        @summary 新增或者修改用户大屏设置
        
        @param request: CreateScreenSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScreenSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.logo_power):
            query['LogoPower'] = request.logo_power
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.monitor_url):
            query['MonitorUrl'] = request.monitor_url
        if not UtilClient.is_unset(request.screen_data_map):
            query['ScreenDataMap'] = request.screen_data_map
        if not UtilClient.is_unset(request.screen_default):
            query['ScreenDefault'] = request.screen_default
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScreenSetting',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.CreateScreenSettingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.CreateScreenSettingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_screen_setting(
        self,
        request: sas_20210114_models.CreateScreenSettingRequest,
    ) -> sas_20210114_models.CreateScreenSettingResponse:
        """
        @summary 新增或者修改用户大屏设置
        
        @param request: CreateScreenSettingRequest
        @return: CreateScreenSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_screen_setting_with_options(request, runtime)

    async def create_screen_setting_async(
        self,
        request: sas_20210114_models.CreateScreenSettingRequest,
    ) -> sas_20210114_models.CreateScreenSettingResponse:
        """
        @summary 新增或者修改用户大屏设置
        
        @param request: CreateScreenSettingRequest
        @return: CreateScreenSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_screen_setting_with_options_async(request, runtime)

    def delete_screen_setting_with_options(
        self,
        request: sas_20210114_models.DeleteScreenSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DeleteScreenSettingResponse:
        """
        @summary 删除大屏设置
        
        @param request: DeleteScreenSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScreenSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScreenSetting',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DeleteScreenSettingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DeleteScreenSettingResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_screen_setting_with_options_async(
        self,
        request: sas_20210114_models.DeleteScreenSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DeleteScreenSettingResponse:
        """
        @summary 删除大屏设置
        
        @param request: DeleteScreenSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScreenSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScreenSetting',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DeleteScreenSettingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DeleteScreenSettingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_screen_setting(
        self,
        request: sas_20210114_models.DeleteScreenSettingRequest,
    ) -> sas_20210114_models.DeleteScreenSettingResponse:
        """
        @summary 删除大屏设置
        
        @param request: DeleteScreenSettingRequest
        @return: DeleteScreenSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_screen_setting_with_options(request, runtime)

    async def delete_screen_setting_async(
        self,
        request: sas_20210114_models.DeleteScreenSettingRequest,
    ) -> sas_20210114_models.DeleteScreenSettingResponse:
        """
        @summary 删除大屏设置
        
        @param request: DeleteScreenSettingRequest
        @return: DeleteScreenSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_screen_setting_with_options_async(request, runtime)

    def describe_screen_alarm_event_list_with_options(
        self,
        request: sas_20210114_models.DescribeScreenAlarmEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenAlarmEventListResponse:
        """
        @summary 查询安全大屏告警事件
        
        @param request: DescribeScreenAlarmEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenAlarmEventListResponse
        """
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
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.time_end):
            query['TimeEnd'] = request.time_end
        if not UtilClient.is_unset(request.time_start):
            query['TimeStart'] = request.time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScreenAlarmEventList',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenAlarmEventListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenAlarmEventListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_alarm_event_list_with_options_async(
        self,
        request: sas_20210114_models.DescribeScreenAlarmEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenAlarmEventListResponse:
        """
        @summary 查询安全大屏告警事件
        
        @param request: DescribeScreenAlarmEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenAlarmEventListResponse
        """
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
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.time_end):
            query['TimeEnd'] = request.time_end
        if not UtilClient.is_unset(request.time_start):
            query['TimeStart'] = request.time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScreenAlarmEventList',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenAlarmEventListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenAlarmEventListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_alarm_event_list(
        self,
        request: sas_20210114_models.DescribeScreenAlarmEventListRequest,
    ) -> sas_20210114_models.DescribeScreenAlarmEventListResponse:
        """
        @summary 查询安全大屏告警事件
        
        @param request: DescribeScreenAlarmEventListRequest
        @return: DescribeScreenAlarmEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_alarm_event_list_with_options(request, runtime)

    async def describe_screen_alarm_event_list_async(
        self,
        request: sas_20210114_models.DescribeScreenAlarmEventListRequest,
    ) -> sas_20210114_models.DescribeScreenAlarmEventListResponse:
        """
        @summary 查询安全大屏告警事件
        
        @param request: DescribeScreenAlarmEventListRequest
        @return: DescribeScreenAlarmEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_alarm_event_list_with_options_async(request, runtime)

    def describe_screen_attack_analysis_data_with_options(
        self,
        request: sas_20210114_models.DescribeScreenAttackAnalysisDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenAttackAnalysisDataResponse:
        """
        @summary 查询大屏攻击防御事件
        
        @param request: DescribeScreenAttackAnalysisDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenAttackAnalysisDataResponse
        """
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
            action='DescribeScreenAttackAnalysisData',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenAttackAnalysisDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenAttackAnalysisDataResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_attack_analysis_data_with_options_async(
        self,
        request: sas_20210114_models.DescribeScreenAttackAnalysisDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenAttackAnalysisDataResponse:
        """
        @summary 查询大屏攻击防御事件
        
        @param request: DescribeScreenAttackAnalysisDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenAttackAnalysisDataResponse
        """
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
            action='DescribeScreenAttackAnalysisData',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenAttackAnalysisDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenAttackAnalysisDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_attack_analysis_data(
        self,
        request: sas_20210114_models.DescribeScreenAttackAnalysisDataRequest,
    ) -> sas_20210114_models.DescribeScreenAttackAnalysisDataResponse:
        """
        @summary 查询大屏攻击防御事件
        
        @param request: DescribeScreenAttackAnalysisDataRequest
        @return: DescribeScreenAttackAnalysisDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_attack_analysis_data_with_options(request, runtime)

    async def describe_screen_attack_analysis_data_async(
        self,
        request: sas_20210114_models.DescribeScreenAttackAnalysisDataRequest,
    ) -> sas_20210114_models.DescribeScreenAttackAnalysisDataResponse:
        """
        @summary 查询大屏攻击防御事件
        
        @param request: DescribeScreenAttackAnalysisDataRequest
        @return: DescribeScreenAttackAnalysisDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_attack_analysis_data_with_options_async(request, runtime)

    def describe_screen_cloud_hc_risk_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenCloudHcRiskResponse:
        """
        @summary 查询云产品基线问题
        
        @param request: DescribeScreenCloudHcRiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenCloudHcRiskResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenCloudHcRisk',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenCloudHcRiskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenCloudHcRiskResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_cloud_hc_risk_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenCloudHcRiskResponse:
        """
        @summary 查询云产品基线问题
        
        @param request: DescribeScreenCloudHcRiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenCloudHcRiskResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenCloudHcRisk',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenCloudHcRiskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenCloudHcRiskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_cloud_hc_risk(self) -> sas_20210114_models.DescribeScreenCloudHcRiskResponse:
        """
        @summary 查询云产品基线问题
        
        @return: DescribeScreenCloudHcRiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_cloud_hc_risk_with_options(runtime)

    async def describe_screen_cloud_hc_risk_async(self) -> sas_20210114_models.DescribeScreenCloudHcRiskResponse:
        """
        @summary 查询云产品基线问题
        
        @return: DescribeScreenCloudHcRiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_cloud_hc_risk_with_options_async(runtime)

    def describe_screen_data_map_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenDataMapResponse:
        """
        @summary 获取大屏可展示数据列表
        
        @param request: DescribeScreenDataMapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenDataMapResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenDataMap',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenDataMapResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenDataMapResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_data_map_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenDataMapResponse:
        """
        @summary 获取大屏可展示数据列表
        
        @param request: DescribeScreenDataMapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenDataMapResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenDataMap',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenDataMapResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenDataMapResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_data_map(self) -> sas_20210114_models.DescribeScreenDataMapResponse:
        """
        @summary 获取大屏可展示数据列表
        
        @return: DescribeScreenDataMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_data_map_with_options(runtime)

    async def describe_screen_data_map_async(self) -> sas_20210114_models.DescribeScreenDataMapResponse:
        """
        @summary 获取大屏可展示数据列表
        
        @return: DescribeScreenDataMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_data_map_with_options_async(runtime)

    def describe_screen_emer_risk_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenEmerRiskResponse:
        """
        @summary 查询云产品漏洞风险
        
        @param request: DescribeScreenEmerRiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenEmerRiskResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenEmerRisk',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenEmerRiskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenEmerRiskResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_emer_risk_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenEmerRiskResponse:
        """
        @summary 查询云产品漏洞风险
        
        @param request: DescribeScreenEmerRiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenEmerRiskResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenEmerRisk',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenEmerRiskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenEmerRiskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_emer_risk(self) -> sas_20210114_models.DescribeScreenEmerRiskResponse:
        """
        @summary 查询云产品漏洞风险
        
        @return: DescribeScreenEmerRiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_emer_risk_with_options(runtime)

    async def describe_screen_emer_risk_async(self) -> sas_20210114_models.DescribeScreenEmerRiskResponse:
        """
        @summary 查询云产品漏洞风险
        
        @return: DescribeScreenEmerRiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_emer_risk_with_options_async(runtime)

    def describe_screen_host_statistics_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenHostStatisticsResponse:
        """
        @summary 查询大屏主机统计数据
        
        @param request: DescribeScreenHostStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenHostStatisticsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenHostStatistics',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenHostStatisticsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenHostStatisticsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_host_statistics_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenHostStatisticsResponse:
        """
        @summary 查询大屏主机统计数据
        
        @param request: DescribeScreenHostStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenHostStatisticsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenHostStatistics',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenHostStatisticsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenHostStatisticsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_host_statistics(self) -> sas_20210114_models.DescribeScreenHostStatisticsResponse:
        """
        @summary 查询大屏主机统计数据
        
        @return: DescribeScreenHostStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_host_statistics_with_options(runtime)

    async def describe_screen_host_statistics_async(self) -> sas_20210114_models.DescribeScreenHostStatisticsResponse:
        """
        @summary 查询大屏主机统计数据
        
        @return: DescribeScreenHostStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_host_statistics_with_options_async(runtime)

    def describe_screen_operate_info_with_options(
        self,
        request: sas_20210114_models.DescribeScreenOperateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenOperateInfoResponse:
        """
        @summary 查看运营信息
        
        @param request: DescribeScreenOperateInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenOperateInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScreenOperateInfo',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenOperateInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenOperateInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_operate_info_with_options_async(
        self,
        request: sas_20210114_models.DescribeScreenOperateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenOperateInfoResponse:
        """
        @summary 查看运营信息
        
        @param request: DescribeScreenOperateInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenOperateInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScreenOperateInfo',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenOperateInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenOperateInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_operate_info(
        self,
        request: sas_20210114_models.DescribeScreenOperateInfoRequest,
    ) -> sas_20210114_models.DescribeScreenOperateInfoResponse:
        """
        @summary 查看运营信息
        
        @param request: DescribeScreenOperateInfoRequest
        @return: DescribeScreenOperateInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_operate_info_with_options(request, runtime)

    async def describe_screen_operate_info_async(
        self,
        request: sas_20210114_models.DescribeScreenOperateInfoRequest,
    ) -> sas_20210114_models.DescribeScreenOperateInfoResponse:
        """
        @summary 查看运营信息
        
        @param request: DescribeScreenOperateInfoRequest
        @return: DescribeScreenOperateInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_operate_info_with_options_async(request, runtime)

    def describe_screen_oss_upload_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenOssUploadInfoResponse:
        """
        @summary 查询大屏上传信息
        
        @param request: DescribeScreenOssUploadInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenOssUploadInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenOssUploadInfo',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenOssUploadInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenOssUploadInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_oss_upload_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenOssUploadInfoResponse:
        """
        @summary 查询大屏上传信息
        
        @param request: DescribeScreenOssUploadInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenOssUploadInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenOssUploadInfo',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenOssUploadInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenOssUploadInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_oss_upload_info(self) -> sas_20210114_models.DescribeScreenOssUploadInfoResponse:
        """
        @summary 查询大屏上传信息
        
        @return: DescribeScreenOssUploadInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_oss_upload_info_with_options(runtime)

    async def describe_screen_oss_upload_info_async(self) -> sas_20210114_models.DescribeScreenOssUploadInfoResponse:
        """
        @summary 查询大屏上传信息
        
        @return: DescribeScreenOssUploadInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_oss_upload_info_with_options_async(runtime)

    def describe_screen_score_thread_with_options(
        self,
        request: sas_20210114_models.DescribeScreenScoreThreadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenScoreThreadResponse:
        """
        @summary 查询安全大屏分数趋势
        
        @param request: DescribeScreenScoreThreadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenScoreThreadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScreenScoreThread',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenScoreThreadResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenScoreThreadResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_score_thread_with_options_async(
        self,
        request: sas_20210114_models.DescribeScreenScoreThreadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenScoreThreadResponse:
        """
        @summary 查询安全大屏分数趋势
        
        @param request: DescribeScreenScoreThreadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenScoreThreadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScreenScoreThread',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenScoreThreadResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenScoreThreadResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_score_thread(
        self,
        request: sas_20210114_models.DescribeScreenScoreThreadRequest,
    ) -> sas_20210114_models.DescribeScreenScoreThreadResponse:
        """
        @summary 查询安全大屏分数趋势
        
        @param request: DescribeScreenScoreThreadRequest
        @return: DescribeScreenScoreThreadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_score_thread_with_options(request, runtime)

    async def describe_screen_score_thread_async(
        self,
        request: sas_20210114_models.DescribeScreenScoreThreadRequest,
    ) -> sas_20210114_models.DescribeScreenScoreThreadResponse:
        """
        @summary 查询安全大屏分数趋势
        
        @param request: DescribeScreenScoreThreadRequest
        @return: DescribeScreenScoreThreadResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_score_thread_with_options_async(request, runtime)

    def describe_screen_security_stat_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenSecurityStatInfoResponse:
        """
        @summary 查询已处理的风险
        
        @param request: DescribeScreenSecurityStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenSecurityStatInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenSecurityStatInfo',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSecurityStatInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSecurityStatInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_security_stat_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenSecurityStatInfoResponse:
        """
        @summary 查询已处理的风险
        
        @param request: DescribeScreenSecurityStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenSecurityStatInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenSecurityStatInfo',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSecurityStatInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSecurityStatInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_security_stat_info(self) -> sas_20210114_models.DescribeScreenSecurityStatInfoResponse:
        """
        @summary 查询已处理的风险
        
        @return: DescribeScreenSecurityStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_security_stat_info_with_options(runtime)

    async def describe_screen_security_stat_info_async(self) -> sas_20210114_models.DescribeScreenSecurityStatInfoResponse:
        """
        @summary 查询已处理的风险
        
        @return: DescribeScreenSecurityStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_security_stat_info_with_options_async(runtime)

    def describe_screen_setting_with_options(
        self,
        request: sas_20210114_models.DescribeScreenSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenSettingResponse:
        """
        @summary 查询大屏配置
        
        @param request: DescribeScreenSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScreenSetting',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSettingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSettingResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_setting_with_options_async(
        self,
        request: sas_20210114_models.DescribeScreenSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenSettingResponse:
        """
        @summary 查询大屏配置
        
        @param request: DescribeScreenSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScreenSetting',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSettingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSettingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_setting(
        self,
        request: sas_20210114_models.DescribeScreenSettingRequest,
    ) -> sas_20210114_models.DescribeScreenSettingResponse:
        """
        @summary 查询大屏配置
        
        @param request: DescribeScreenSettingRequest
        @return: DescribeScreenSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_setting_with_options(request, runtime)

    async def describe_screen_setting_async(
        self,
        request: sas_20210114_models.DescribeScreenSettingRequest,
    ) -> sas_20210114_models.DescribeScreenSettingResponse:
        """
        @summary 查询大屏配置
        
        @param request: DescribeScreenSettingRequest
        @return: DescribeScreenSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_setting_with_options_async(request, runtime)

    def describe_screen_summary_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenSummaryInfoResponse:
        """
        @summary 查询大屏统计信息
        
        @param request: DescribeScreenSummaryInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenSummaryInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenSummaryInfo',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSummaryInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSummaryInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_summary_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenSummaryInfoResponse:
        """
        @summary 查询大屏统计信息
        
        @param request: DescribeScreenSummaryInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenSummaryInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenSummaryInfo',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSummaryInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenSummaryInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_summary_info(self) -> sas_20210114_models.DescribeScreenSummaryInfoResponse:
        """
        @summary 查询大屏统计信息
        
        @return: DescribeScreenSummaryInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_summary_info_with_options(runtime)

    async def describe_screen_summary_info_async(self) -> sas_20210114_models.DescribeScreenSummaryInfoResponse:
        """
        @summary 查询大屏统计信息
        
        @return: DescribeScreenSummaryInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_summary_info_with_options_async(runtime)

    def describe_screen_titles_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenTitlesResponse:
        """
        @summary 获取大屏幕设置全部列表
        
        @param request: DescribeScreenTitlesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenTitlesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenTitles',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenTitlesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenTitlesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_titles_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenTitlesResponse:
        """
        @summary 获取大屏幕设置全部列表
        
        @param request: DescribeScreenTitlesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenTitlesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenTitles',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenTitlesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenTitlesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_titles(self) -> sas_20210114_models.DescribeScreenTitlesResponse:
        """
        @summary 获取大屏幕设置全部列表
        
        @return: DescribeScreenTitlesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_titles_with_options(runtime)

    async def describe_screen_titles_async(self) -> sas_20210114_models.DescribeScreenTitlesResponse:
        """
        @summary 获取大屏幕设置全部列表
        
        @return: DescribeScreenTitlesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_titles_with_options_async(runtime)

    def describe_screen_upload_picture_with_options(
        self,
        request: sas_20210114_models.DescribeScreenUploadPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenUploadPictureResponse:
        """
        @summary 查询上传之后的图片显示地址
        
        @param request: DescribeScreenUploadPictureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenUploadPictureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScreenUploadPicture',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenUploadPictureResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenUploadPictureResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_upload_picture_with_options_async(
        self,
        request: sas_20210114_models.DescribeScreenUploadPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenUploadPictureResponse:
        """
        @summary 查询上传之后的图片显示地址
        
        @param request: DescribeScreenUploadPictureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenUploadPictureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScreenUploadPicture',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenUploadPictureResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenUploadPictureResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_upload_picture(
        self,
        request: sas_20210114_models.DescribeScreenUploadPictureRequest,
    ) -> sas_20210114_models.DescribeScreenUploadPictureResponse:
        """
        @summary 查询上传之后的图片显示地址
        
        @param request: DescribeScreenUploadPictureRequest
        @return: DescribeScreenUploadPictureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_upload_picture_with_options(request, runtime)

    async def describe_screen_upload_picture_async(
        self,
        request: sas_20210114_models.DescribeScreenUploadPictureRequest,
    ) -> sas_20210114_models.DescribeScreenUploadPictureResponse:
        """
        @summary 查询上传之后的图片显示地址
        
        @param request: DescribeScreenUploadPictureRequest
        @return: DescribeScreenUploadPictureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_upload_picture_with_options_async(request, runtime)

    def describe_screen_version_config_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenVersionConfigResponse:
        """
        @summary 查询安全大屏版本配置
        
        @param request: DescribeScreenVersionConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenVersionConfigResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenVersionConfig',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenVersionConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenVersionConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_screen_version_config_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.DescribeScreenVersionConfigResponse:
        """
        @summary 查询安全大屏版本配置
        
        @param request: DescribeScreenVersionConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScreenVersionConfigResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeScreenVersionConfig',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenVersionConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.DescribeScreenVersionConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_screen_version_config(self) -> sas_20210114_models.DescribeScreenVersionConfigResponse:
        """
        @summary 查询安全大屏版本配置
        
        @return: DescribeScreenVersionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_screen_version_config_with_options(runtime)

    async def describe_screen_version_config_async(self) -> sas_20210114_models.DescribeScreenVersionConfigResponse:
        """
        @summary 查询安全大屏版本配置
        
        @return: DescribeScreenVersionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_screen_version_config_with_options_async(runtime)

    def get_file_detect_result_inner_with_options(
        self,
        request: sas_20210114_models.GetFileDetectResultInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.GetFileDetectResultInnerResponse:
        """
        @summary 获取文件检测结果。
        
        @param request: GetFileDetectResultInnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileDetectResultInnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dna_hash_key_list):
            query['DnaHashKeyList'] = request.dna_hash_key_list
        if not UtilClient.is_unset(request.hash_key_list):
            query['HashKeyList'] = request.hash_key_list
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileDetectResultInner',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.GetFileDetectResultInnerResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.GetFileDetectResultInnerResponse(),
                self.execute(params, req, runtime)
            )

    async def get_file_detect_result_inner_with_options_async(
        self,
        request: sas_20210114_models.GetFileDetectResultInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.GetFileDetectResultInnerResponse:
        """
        @summary 获取文件检测结果。
        
        @param request: GetFileDetectResultInnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileDetectResultInnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dna_hash_key_list):
            query['DnaHashKeyList'] = request.dna_hash_key_list
        if not UtilClient.is_unset(request.hash_key_list):
            query['HashKeyList'] = request.hash_key_list
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileDetectResultInner',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.GetFileDetectResultInnerResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.GetFileDetectResultInnerResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_file_detect_result_inner(
        self,
        request: sas_20210114_models.GetFileDetectResultInnerRequest,
    ) -> sas_20210114_models.GetFileDetectResultInnerResponse:
        """
        @summary 获取文件检测结果。
        
        @param request: GetFileDetectResultInnerRequest
        @return: GetFileDetectResultInnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_file_detect_result_inner_with_options(request, runtime)

    async def get_file_detect_result_inner_async(
        self,
        request: sas_20210114_models.GetFileDetectResultInnerRequest,
    ) -> sas_20210114_models.GetFileDetectResultInnerResponse:
        """
        @summary 获取文件检测结果。
        
        @param request: GetFileDetectResultInnerRequest
        @return: GetFileDetectResultInnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_file_detect_result_inner_with_options_async(request, runtime)

    def list_global_user_config_with_options(
        self,
        tmp_req: sas_20210114_models.ListGlobalUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.ListGlobalUserConfigResponse:
        """
        @summary 首页配置情况汇总接口
        
        @param tmp_req: ListGlobalUserConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGlobalUserConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sas_20210114_models.ListGlobalUserConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.module_list):
            request.module_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.module_list, 'ModuleList', 'json')
        query = {}
        if not UtilClient.is_unset(request.module_list_shrink):
            query['ModuleList'] = request.module_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGlobalUserConfig',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.ListGlobalUserConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.ListGlobalUserConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def list_global_user_config_with_options_async(
        self,
        tmp_req: sas_20210114_models.ListGlobalUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_20210114_models.ListGlobalUserConfigResponse:
        """
        @summary 首页配置情况汇总接口
        
        @param tmp_req: ListGlobalUserConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGlobalUserConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sas_20210114_models.ListGlobalUserConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.module_list):
            request.module_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.module_list, 'ModuleList', 'json')
        query = {}
        if not UtilClient.is_unset(request.module_list_shrink):
            query['ModuleList'] = request.module_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGlobalUserConfig',
            version='2021-01-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                sas_20210114_models.ListGlobalUserConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sas_20210114_models.ListGlobalUserConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_global_user_config(
        self,
        request: sas_20210114_models.ListGlobalUserConfigRequest,
    ) -> sas_20210114_models.ListGlobalUserConfigResponse:
        """
        @summary 首页配置情况汇总接口
        
        @param request: ListGlobalUserConfigRequest
        @return: ListGlobalUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_global_user_config_with_options(request, runtime)

    async def list_global_user_config_async(
        self,
        request: sas_20210114_models.ListGlobalUserConfigRequest,
    ) -> sas_20210114_models.ListGlobalUserConfigResponse:
        """
        @summary 首页配置情况汇总接口
        
        @param request: ListGlobalUserConfigRequest
        @return: ListGlobalUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_global_user_config_with_options_async(request, runtime)
