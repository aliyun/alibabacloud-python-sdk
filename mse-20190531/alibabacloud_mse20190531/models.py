# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class GatewayOptionTraceDetails(TeaModel):
    def __init__(
        self,
        trace_enabled: bool = None,
        sample: int = None,
    ):
        # trace是否开启
        self.trace_enabled = trace_enabled
        # trace 采样率
        self.sample = sample

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trace_enabled is not None:
            result['TraceEnabled'] = self.trace_enabled
        if self.sample is not None:
            result['Sample'] = self.sample
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TraceEnabled') is not None:
            self.trace_enabled = m.get('TraceEnabled')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        return self


class GatewayOptionLogConfigDetails(TeaModel):
    def __init__(
        self,
        log_enabled: bool = None,
        project_name: str = None,
        log_store_name: str = None,
    ):
        # 是否开启日志投递
        self.log_enabled = log_enabled
        # 投递的目标project
        self.project_name = project_name
        # 投递的目标logstore
        self.log_store_name = log_store_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_enabled is not None:
            result['LogEnabled'] = self.log_enabled
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogEnabled') is not None:
            self.log_enabled = m.get('LogEnabled')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        return self


class GatewayOption(TeaModel):
    def __init__(
        self,
        trace_details: GatewayOptionTraceDetails = None,
        log_config_details: GatewayOptionLogConfigDetails = None,
    ):
        # xtrace config option
        self.trace_details = trace_details
        # 日志配置详情
        self.log_config_details = log_config_details

    def validate(self):
        if self.trace_details:
            self.trace_details.validate()
        if self.log_config_details:
            self.log_config_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trace_details is not None:
            result['TraceDetails'] = self.trace_details.to_map()
        if self.log_config_details is not None:
            result['LogConfigDetails'] = self.log_config_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TraceDetails') is not None:
            temp_model = GatewayOptionTraceDetails()
            self.trace_details = temp_model.from_map(m['TraceDetails'])
        if m.get('LogConfigDetails') is not None:
            temp_model = GatewayOptionLogConfigDetails()
            self.log_config_details = temp_model.from_map(m['LogConfigDetails'])
        return self


class ListAlarmHistoriesRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        page_num: int = None,
        page_size: int = None,
        alarm_mse_type: str = None,
        start_time: int = None,
        end_time: int = None,
        alarm_name: str = None,
    ):
        self.request_pars = request_pars
        self.page_num = page_num
        self.page_size = page_size
        self.alarm_mse_type = alarm_mse_type
        self.start_time = start_time
        self.end_time = end_time
        self.alarm_name = alarm_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.alarm_mse_type is not None:
            result['AlarmMseType'] = self.alarm_mse_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AlarmMseType') is not None:
            self.alarm_mse_type = m.get('AlarmMseType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        return self


class ListAlarmHistoriesResponseBodyData(TeaModel):
    def __init__(
        self,
        alarm_time: str = None,
        alarm_email: str = None,
        alarm_ding_ding: str = None,
        alarm_phone: str = None,
        alarm_name: str = None,
        alarm_content: str = None,
    ):
        self.alarm_time = alarm_time
        self.alarm_email = alarm_email
        self.alarm_ding_ding = alarm_ding_ding
        self.alarm_phone = alarm_phone
        self.alarm_name = alarm_name
        self.alarm_content = alarm_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.alarm_email is not None:
            result['AlarmEmail'] = self.alarm_email
        if self.alarm_ding_ding is not None:
            result['AlarmDingDing'] = self.alarm_ding_ding
        if self.alarm_phone is not None:
            result['AlarmPhone'] = self.alarm_phone
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.alarm_content is not None:
            result['AlarmContent'] = self.alarm_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('AlarmEmail') is not None:
            self.alarm_email = m.get('AlarmEmail')
        if m.get('AlarmDingDing') is not None:
            self.alarm_ding_ding = m.get('AlarmDingDing')
        if m.get('AlarmPhone') is not None:
            self.alarm_phone = m.get('AlarmPhone')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('AlarmContent') is not None:
            self.alarm_content = m.get('AlarmContent')
        return self


class ListAlarmHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListAlarmHistoriesResponseBodyData] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmHistoriesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAlarmHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGovernanceKubernetesClusterListRequest(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_name = cluster_name
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetGovernanceKubernetesClusterListResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        cluster_id: str = None,
        region: str = None,
        k_8s_version: str = None,
        namespace_infos: str = None,
        pilot_start_time: str = None,
    ):
        self.cluster_name = cluster_name
        self.cluster_id = cluster_id
        self.region = region
        self.k_8s_version = k_8s_version
        self.namespace_infos = namespace_infos
        self.pilot_start_time = pilot_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region is not None:
            result['Region'] = self.region
        if self.k_8s_version is not None:
            result['K8sVersion'] = self.k_8s_version
        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos
        if self.pilot_start_time is not None:
            result['PilotStartTime'] = self.pilot_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('K8sVersion') is not None:
            self.k_8s_version = m.get('K8sVersion')
        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')
        if m.get('PilotStartTime') is not None:
            self.pilot_start_time = m.get('PilotStartTime')
        return self


class GetGovernanceKubernetesClusterListResponseBodyData(TeaModel):
    def __init__(
        self,
        result: List[GetGovernanceKubernetesClusterListResponseBodyDataResult] = None,
        total_size: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.result = result
        self.total_size = total_size
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetGovernanceKubernetesClusterListResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetGovernanceKubernetesClusterListResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        data: GetGovernanceKubernetesClusterListResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetGovernanceKubernetesClusterListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGovernanceKubernetesClusterListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGovernanceKubernetesClusterListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGovernanceKubernetesClusterListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterConnectionTypesResponseBodyData(TeaModel):
    def __init__(
        self,
        show_name: str = None,
    ):
        self.show_name = show_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class ListClusterConnectionTypesResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        code: int = None,
        message: str = None,
        dynamic_message: str = None,
        data: List[ListClusterConnectionTypesResponseBodyData] = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.code = code
        self.message = message
        self.dynamic_message = dynamic_message
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClusterConnectionTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ListClusterConnectionTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClusterConnectionTypesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClusterConnectionTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEngineNamespaceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        name: str = None,
        desc: str = None,
        instance_id: str = None,
        service_count: int = None,
    ):
        self.cluster_id = cluster_id
        self.name = name
        self.desc = desc
        self.instance_id = instance_id
        self.service_count = service_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        return self


class CreateEngineNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        type: int = None,
        namespace_show_name: str = None,
        quota: int = None,
        namespace: str = None,
        namespace_desc: str = None,
        config_count: int = None,
        service_count: int = None,
    ):
        self.type = type
        self.namespace_show_name = namespace_show_name
        self.quota = quota
        self.namespace = namespace
        self.namespace_desc = namespace_desc
        self.config_count = config_count
        self.service_count = service_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        return self


class CreateEngineNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        cluster_id: str = None,
        data: CreateEngineNamespaceResponseBodyData = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.cluster_id = cluster_id
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Data') is not None:
            temp_model = CreateEngineNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEngineNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEngineNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterVersionsRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
    ):
        self.cluster_type = cluster_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class ListClusterVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        show_name: str = None,
        cluster_type: str = None,
    ):
        self.code = code
        self.show_name = show_name
        self.cluster_type = cluster_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class ListClusterVersionsResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        code: int = None,
        message: str = None,
        dynamic_message: str = None,
        data: List[ListClusterVersionsResponseBodyData] = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.code = code
        self.message = message
        self.dynamic_message = dynamic_message
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClusterVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ListClusterVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClusterVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClusterVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEngineNamespacesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListEngineNamespacesResponseBodyData(TeaModel):
    def __init__(
        self,
        type: int = None,
        namespace_show_name: str = None,
        quota: int = None,
        namespace: str = None,
        namespace_desc: str = None,
        config_count: int = None,
        service_count: str = None,
    ):
        self.type = type
        self.namespace_show_name = namespace_show_name
        self.quota = quota
        self.namespace = namespace
        self.namespace_desc = namespace_desc
        self.config_count = config_count
        self.service_count = service_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        return self


class ListEngineNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListEngineNamespacesResponseBodyData] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEngineNamespacesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEngineNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEngineNamespacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEngineNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        region: str = None,
        source: str = None,
        language: str = None,
        extra_info: str = None,
    ):
        self.app_name = app_name
        self.region = region
        self.source = source
        self.language = language
        self.extra_info = extra_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.region is not None:
            result['Region'] = self.region
        if self.source is not None:
            result['Source'] = self.source
        if self.language is not None:
            result['Language'] = self.language
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        return self


class CreateApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        status: int = None,
        extra_info: str = None,
        app_name: str = None,
        update_time: int = None,
        license_key: str = None,
        create_time: int = None,
        app_id: str = None,
        user_id: str = None,
        source: str = None,
        language: str = None,
        region_id: str = None,
    ):
        self.status = status
        self.extra_info = extra_info
        self.app_name = app_name
        self.update_time = update_time
        self.license_key = license_key
        self.create_time = create_time
        self.app_id = app_id
        self.user_id = user_id
        self.source = source
        self.language = language
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.source is not None:
            result['Source'] = self.source
        if self.language is not None:
            result['Language'] = self.language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateApplicationResponseBodyData = None,
        code: int = None,
        success: str = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOverviewRequest(TeaModel):
    def __init__(
        self,
        period: int = None,
        region: str = None,
    ):
        self.period = period
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetOverviewResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
        success: str = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOverviewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonitorRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        monitor_type: str = None,
        start_time: int = None,
        end_time: int = None,
        step: int = None,
        instance_id: str = None,
    ):
        self.request_pars = request_pars
        self.monitor_type = monitor_type
        self.start_time = start_time
        self.end_time = end_time
        self.step = step
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.step is not None:
            result['Step'] = self.step
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryMonitorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMonitorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScalingClusterRequest(TeaModel):
    def __init__(
        self,
        instance_count: int = None,
        cpu: int = None,
        memory_capacity: int = None,
        cluster_specification: str = None,
        instance_id: str = None,
    ):
        self.instance_count = instance_count
        self.cpu = cpu
        self.memory_capacity = memory_capacity
        self.cluster_specification = cluster_specification
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ScalingClusterResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScalingClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ScalingClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ScalingClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsServicesRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        page_num: int = None,
        page_size: int = None,
        cluster_id: str = None,
        service_name: str = None,
        group_name: str = None,
        has_ip_count: str = None,
        instance_id: str = None,
        namespace_id: str = None,
    ):
        self.request_pars = request_pars
        self.page_num = page_num
        self.page_size = page_size
        self.cluster_id = cluster_id
        self.service_name = service_name
        self.group_name = group_name
        self.has_ip_count = has_ip_count
        self.instance_id = instance_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.has_ip_count is not None:
            result['HasIpCount'] = self.has_ip_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HasIpCount') is not None:
            self.has_ip_count = m.get('HasIpCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListAnsServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        healthy_instance_count: int = None,
        group_name: str = None,
        ip_count: int = None,
        name: str = None,
        cluster_count: int = None,
    ):
        self.healthy_instance_count = healthy_instance_count
        self.group_name = group_name
        self.ip_count = ip_count
        self.name = name
        self.cluster_count = cluster_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.healthy_instance_count is not None:
            result['HealthyInstanceCount'] = self.healthy_instance_count
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_count is not None:
            result['IpCount'] = self.ip_count
        if self.name is not None:
            result['Name'] = self.name
        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthyInstanceCount') is not None:
            self.healthy_instance_count = m.get('HealthyInstanceCount')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')
        return self


class ListAnsServicesResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListAnsServicesResponseBodyData] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAnsServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAnsServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAnsServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAnsServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayOptionRequest(TeaModel):
    def __init__(
        self,
        gateway_id: int = None,
        gateway_option: GatewayOption = None,
    ):
        self.gateway_id = gateway_id
        self.gateway_option = gateway_option

    def validate(self):
        if self.gateway_option:
            self.gateway_option.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_option is not None:
            result['GatewayOption'] = self.gateway_option.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayOption') is not None:
            temp_model = GatewayOption()
            self.gateway_option = temp_model.from_map(m['GatewayOption'])
        return self


class UpdateGatewayOptionShrinkRequest(TeaModel):
    def __init__(
        self,
        gateway_id: int = None,
        gateway_option_shrink: str = None,
    ):
        self.gateway_id = gateway_id
        self.gateway_option_shrink = gateway_option_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_option_shrink is not None:
            result['GatewayOption'] = self.gateway_option_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayOption') is not None:
            self.gateway_option_shrink = m.get('GatewayOption')
        return self


class UpdateGatewayOptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        code: int = None,
        success: bool = None,
        data: GatewayOption = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GatewayOption()
            self.data = temp_model.from_map(m['Data'])
        return self


class UpdateGatewayOptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGatewayOptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateGatewayOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZnodeChildrenRequest(TeaModel):
    def __init__(
        self,
        path: str = None,
        cluster_id: str = None,
    ):
        self.path = path
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListZnodeChildrenResponseBodyData(TeaModel):
    def __init__(
        self,
        data: str = None,
        path: str = None,
        dir: bool = None,
        name: str = None,
    ):
        self.data = data
        self.path = path
        self.dir = dir
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListZnodeChildrenResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[ListZnodeChildrenResponseBodyData] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListZnodeChildrenResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListZnodeChildrenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListZnodeChildrenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListZnodeChildrenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEngineNamespaceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        instance_id: str = None,
        cluster_id: str = None,
    ):
        self.id = id
        self.instance_id = instance_id
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DeleteEngineNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEngineNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEngineNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteZnodeRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        cluster_id: str = None,
        path: str = None,
    ):
        self.request_pars = request_pars
        self.cluster_id = cluster_id
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DeleteZnodeResponseBodyData(TeaModel):
    def __init__(
        self,
        data: str = None,
        path: str = None,
        dir: bool = None,
        name: str = None,
    ):
        self.data = data
        self.path = path
        self.dir = dir
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteZnodeResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        data: DeleteZnodeResponseBodyData = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeleteZnodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteZnodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteZnodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportNacosConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_id: str = None,
        ids: str = None,
        data_id: str = None,
        group: str = None,
        app_name: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.ids = ids
        self.data_id = data_id
        self.group = group
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ExportNacosConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ExportNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        code: int = None,
        message: str = None,
        dynamic_message: str = None,
        data: ExportNacosConfigResponseBodyData = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.code = code
        self.message = message
        self.dynamic_message = dynamic_message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Data') is not None:
            temp_model = ExportNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ExportNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNacosHistoryConfigsRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        page_num: int = None,
        page_size: int = None,
        instance_id: str = None,
        region_id: str = None,
        data_id: str = None,
        group: str = None,
        namespace_id: str = None,
    ):
        self.request_pars = request_pars
        self.page_num = page_num
        self.page_size = page_size
        self.instance_id = instance_id
        self.region_id = region_id
        self.data_id = data_id
        self.group = group
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListNacosHistoryConfigsResponseBodyHistoryItems(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        data_id: str = None,
        group: str = None,
        last_modified_time: int = None,
        id: int = None,
        op_type: str = None,
    ):
        self.app_name = app_name
        self.data_id = data_id
        self.group = group
        self.last_modified_time = last_modified_time
        self.id = id
        self.op_type = op_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.id is not None:
            result['Id'] = self.id
        if self.op_type is not None:
            result['OpType'] = self.op_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        return self


class ListNacosHistoryConfigsResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        error_code: str = None,
        success: bool = None,
        history_items: List[ListNacosHistoryConfigsResponseBodyHistoryItems] = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.error_code = error_code
        self.success = success
        self.history_items = history_items

    def validate(self):
        if self.history_items:
            for k in self.history_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['HistoryItems'] = []
        if self.history_items is not None:
            for k in self.history_items:
                result['HistoryItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.history_items = []
        if m.get('HistoryItems') is not None:
            for k in m.get('HistoryItems'):
                temp_model = ListNacosHistoryConfigsResponseBodyHistoryItems()
                self.history_items.append(temp_model.from_map(k))
        return self


class ListNacosHistoryConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNacosHistoryConfigsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNacosHistoryConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMockRuleRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region: str = None,
        source: str = None,
        provider_app_id: str = None,
        provider_app_name: str = None,
        extra_json: str = None,
        sc_mock_items: str = None,
        dubbo_mock_items: str = None,
        consumer_app_ids: str = None,
        enable: bool = None,
        mock_type: int = None,
    ):
        self.name = name
        self.region = region
        self.source = source
        self.provider_app_id = provider_app_id
        self.provider_app_name = provider_app_name
        self.extra_json = extra_json
        self.sc_mock_items = sc_mock_items
        self.dubbo_mock_items = dubbo_mock_items
        self.consumer_app_ids = consumer_app_ids
        self.enable = enable
        self.mock_type = mock_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.source is not None:
            result['Source'] = self.source
        if self.provider_app_id is not None:
            result['ProviderAppId'] = self.provider_app_id
        if self.provider_app_name is not None:
            result['ProviderAppName'] = self.provider_app_name
        if self.extra_json is not None:
            result['ExtraJson'] = self.extra_json
        if self.sc_mock_items is not None:
            result['ScMockItems'] = self.sc_mock_items
        if self.dubbo_mock_items is not None:
            result['DubboMockItems'] = self.dubbo_mock_items
        if self.consumer_app_ids is not None:
            result['ConsumerAppIds'] = self.consumer_app_ids
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.mock_type is not None:
            result['MockType'] = self.mock_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ProviderAppId') is not None:
            self.provider_app_id = m.get('ProviderAppId')
        if m.get('ProviderAppName') is not None:
            self.provider_app_name = m.get('ProviderAppName')
        if m.get('ExtraJson') is not None:
            self.extra_json = m.get('ExtraJson')
        if m.get('ScMockItems') is not None:
            self.sc_mock_items = m.get('ScMockItems')
        if m.get('DubboMockItems') is not None:
            self.dubbo_mock_items = m.get('DubboMockItems')
        if m.get('ConsumerAppIds') is not None:
            self.consumer_app_ids = m.get('ConsumerAppIds')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('MockType') is not None:
            self.mock_type = m.get('MockType')
        return self


class AddMockRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
        sc_mock_item_json: str = None,
        consumer_app_name: str = None,
        consumer_app_id: str = None,
        account_id: str = None,
        extra_json: str = None,
        source: str = None,
        region: str = None,
        provider_app_id: str = None,
        provider_app_name: str = None,
        name: str = None,
        id: int = None,
        enable: bool = None,
        mock_type: int = None,
    ):
        self.namespace_id = namespace_id
        self.sc_mock_item_json = sc_mock_item_json
        self.consumer_app_name = consumer_app_name
        self.consumer_app_id = consumer_app_id
        self.account_id = account_id
        self.extra_json = extra_json
        self.source = source
        self.region = region
        self.provider_app_id = provider_app_id
        self.provider_app_name = provider_app_name
        self.name = name
        self.id = id
        self.enable = enable
        self.mock_type = mock_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.sc_mock_item_json is not None:
            result['ScMockItemJson'] = self.sc_mock_item_json
        if self.consumer_app_name is not None:
            result['ConsumerAppName'] = self.consumer_app_name
        if self.consumer_app_id is not None:
            result['ConsumerAppId'] = self.consumer_app_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.extra_json is not None:
            result['ExtraJson'] = self.extra_json
        if self.source is not None:
            result['Source'] = self.source
        if self.region is not None:
            result['Region'] = self.region
        if self.provider_app_id is not None:
            result['ProviderAppId'] = self.provider_app_id
        if self.provider_app_name is not None:
            result['ProviderAppName'] = self.provider_app_name
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.mock_type is not None:
            result['MockType'] = self.mock_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ScMockItemJson') is not None:
            self.sc_mock_item_json = m.get('ScMockItemJson')
        if m.get('ConsumerAppName') is not None:
            self.consumer_app_name = m.get('ConsumerAppName')
        if m.get('ConsumerAppId') is not None:
            self.consumer_app_id = m.get('ConsumerAppId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ExtraJson') is not None:
            self.extra_json = m.get('ExtraJson')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ProviderAppId') is not None:
            self.provider_app_id = m.get('ProviderAppId')
        if m.get('ProviderAppName') is not None:
            self.provider_app_name = m.get('ProviderAppName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('MockType') is not None:
            self.mock_type = m.get('MockType')
        return self


class AddMockRuleResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        data: AddMockRuleResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddMockRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddMockRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddMockRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddMockRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersByConfigRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        instance_id: str = None,
        data_id: str = None,
        group: str = None,
        namespace_id: str = None,
    ):
        self.request_pars = request_pars
        self.instance_id = instance_id
        self.data_id = data_id
        self.group = group
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListListenersByConfigResponseBodyListeners(TeaModel):
    def __init__(
        self,
        ip: str = None,
        md_5: str = None,
    ):
        self.ip = ip
        self.md_5 = md_5

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        return self


class ListListenersByConfigResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        listeners: List[ListListenersByConfigResponseBodyListeners] = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.listeners = listeners
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersByConfigResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListListenersByConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListListenersByConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListListenersByConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGovernanceKubernetesClusterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        cluster_id: str = None,
    ):
        self.region_id = region_id
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetGovernanceKubernetesClusterResponseBodyDataNamespaces(TeaModel):
    def __init__(
        self,
        name: str = None,
        tags: str = None,
    ):
        self.name = name
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GetGovernanceKubernetesClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        region: str = None,
        k_8s_version: str = None,
        namespace_infos: str = None,
        pilot_start_time: str = None,
        update_time: str = None,
        namespaces: List[GetGovernanceKubernetesClusterResponseBodyDataNamespaces] = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.region = region
        self.k_8s_version = k_8s_version
        self.namespace_infos = namespace_infos
        self.pilot_start_time = pilot_start_time
        self.update_time = update_time
        self.namespaces = namespaces

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.region is not None:
            result['Region'] = self.region
        if self.k_8s_version is not None:
            result['K8sVersion'] = self.k_8s_version
        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos
        if self.pilot_start_time is not None:
            result['PilotStartTime'] = self.pilot_start_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('K8sVersion') is not None:
            self.k_8s_version = m.get('K8sVersion')
        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')
        if m.get('PilotStartTime') is not None:
            self.pilot_start_time = m.get('PilotStartTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = GetGovernanceKubernetesClusterResponseBodyDataNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        return self


class GetGovernanceKubernetesClusterResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        data: GetGovernanceKubernetesClusterResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetGovernanceKubernetesClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGovernanceKubernetesClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGovernanceKubernetesClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGovernanceKubernetesClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGatewayTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        code: int = None,
        success: bool = None,
        data: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class QueryGatewayTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGatewayTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryGatewayTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGovernanceKubernetesClusterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        cluster_id: str = None,
        namespace_infos: str = None,
    ):
        self.region_id = region_id
        self.cluster_id = cluster_id
        self.namespace_infos = namespace_infos

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')
        return self


class ModifyGovernanceKubernetesClusterResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: int = None,
        success: bool = None,
    ):
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyGovernanceKubernetesClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyGovernanceKubernetesClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyGovernanceKubernetesClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterSpecificationResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_specification_name: str = None,
        disk_capacity: str = None,
        memory_capacity: str = None,
        instance_count: str = None,
        max_tps: str = None,
        max_con: str = None,
        cpu_capacity: str = None,
    ):
        self.cluster_specification_name = cluster_specification_name
        self.disk_capacity = disk_capacity
        self.memory_capacity = memory_capacity
        self.instance_count = instance_count
        self.max_tps = max_tps
        self.max_con = max_con
        self.cpu_capacity = cpu_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_specification_name is not None:
            result['ClusterSpecificationName'] = self.cluster_specification_name
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps
        if self.max_con is not None:
            result['MaxCon'] = self.max_con
        if self.cpu_capacity is not None:
            result['CpuCapacity'] = self.cpu_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterSpecificationName') is not None:
            self.cluster_specification_name = m.get('ClusterSpecificationName')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')
        if m.get('MaxCon') is not None:
            self.max_con = m.get('MaxCon')
        if m.get('CpuCapacity') is not None:
            self.cpu_capacity = m.get('CpuCapacity')
        return self


class QueryClusterSpecificationResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        code: int = None,
        message: str = None,
        data: List[QueryClusterSpecificationResponseBodyData] = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryClusterSpecificationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryClusterSpecificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryClusterSpecificationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryClusterSpecificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportNacosConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_id: str = None,
        policy: str = None,
        file_url: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.policy = policy
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class ImportNacosConfigResponseBodyDataSkipData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
    ):
        self.data_id = data_id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ImportNacosConfigResponseBodyDataFailData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
    ):
        self.data_id = data_id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ImportNacosConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        succ_count: int = None,
        skip_count: int = None,
        skip_data: List[ImportNacosConfigResponseBodyDataSkipData] = None,
        fail_data: List[ImportNacosConfigResponseBodyDataFailData] = None,
    ):
        self.succ_count = succ_count
        self.skip_count = skip_count
        self.skip_data = skip_data
        self.fail_data = fail_data

    def validate(self):
        if self.skip_data:
            for k in self.skip_data:
                if k:
                    k.validate()
        if self.fail_data:
            for k in self.fail_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.succ_count is not None:
            result['SuccCount'] = self.succ_count
        if self.skip_count is not None:
            result['SkipCount'] = self.skip_count
        result['SkipData'] = []
        if self.skip_data is not None:
            for k in self.skip_data:
                result['SkipData'].append(k.to_map() if k else None)
        result['FailData'] = []
        if self.fail_data is not None:
            for k in self.fail_data:
                result['FailData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuccCount') is not None:
            self.succ_count = m.get('SuccCount')
        if m.get('SkipCount') is not None:
            self.skip_count = m.get('SkipCount')
        self.skip_data = []
        if m.get('SkipData') is not None:
            for k in m.get('SkipData'):
                temp_model = ImportNacosConfigResponseBodyDataSkipData()
                self.skip_data.append(temp_model.from_map(k))
        self.fail_data = []
        if m.get('FailData') is not None:
            for k in m.get('FailData'):
                temp_model = ImportNacosConfigResponseBodyDataFailData()
                self.fail_data.append(temp_model.from_map(k))
        return self


class ImportNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        code: int = None,
        message: str = None,
        dynamic_message: str = None,
        data: ImportNacosConfigResponseBodyData = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.code = code
        self.message = message
        self.dynamic_message = dynamic_message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Data') is not None:
            temp_model = ImportNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ImportNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateZnodeRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        path: str = None,
        data: str = None,
    ):
        self.cluster_id = cluster_id
        self.path = path
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CreateZnodeResponseBodyData(TeaModel):
    def __init__(
        self,
        data: str = None,
        path: str = None,
        dir: bool = None,
        name: str = None,
    ):
        self.data = data
        self.path = path
        self.dir = dir
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateZnodeResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        data: CreateZnodeResponseBodyData = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateZnodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateZnodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateZnodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterDiskSpecificationRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
    ):
        self.cluster_type = cluster_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class QueryClusterDiskSpecificationResponseBodyData(TeaModel):
    def __init__(
        self,
        step: int = None,
        max: int = None,
        min: int = None,
    ):
        self.step = step
        self.max = max
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.step is not None:
            result['Step'] = self.step
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        return self


class QueryClusterDiskSpecificationResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        code: int = None,
        message: str = None,
        dynamic_message: str = None,
        data: QueryClusterDiskSpecificationResponseBodyData = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.code = code
        self.message = message
        self.dynamic_message = dynamic_message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Data') is not None:
            temp_model = QueryClusterDiskSpecificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryClusterDiskSpecificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryClusterDiskSpecificationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryClusterDiskSpecificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNacosConfigsRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        page_num: int = None,
        page_size: int = None,
        instance_id: str = None,
        region_id: str = None,
        data_id: str = None,
        group: str = None,
        app_name: str = None,
        tags: str = None,
        namespace_id: str = None,
    ):
        self.request_pars = request_pars
        self.page_num = page_num
        self.page_size = page_size
        self.instance_id = instance_id
        self.region_id = region_id
        self.data_id = data_id
        self.group = group
        self.app_name = app_name
        self.tags = tags
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListNacosConfigsResponseBodyConfigurations(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        data_id: str = None,
        id: str = None,
        group: str = None,
    ):
        self.app_name = app_name
        self.data_id = data_id
        self.id = id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.id is not None:
            result['Id'] = self.id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ListNacosConfigsResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        error_code: str = None,
        configurations: List[ListNacosConfigsResponseBodyConfigurations] = None,
        code: int = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.error_code = error_code
        self.configurations = configurations
        self.code = code
        self.success = success

    def validate(self):
        if self.configurations:
            for k in self.configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Configurations'] = []
        if self.configurations is not None:
            for k in self.configurations:
                result['Configurations'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.configurations = []
        if m.get('Configurations') is not None:
            for k in m.get('Configurations'):
                temp_model = ListNacosConfigsResponseBodyConfigurations()
                self.configurations.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListNacosConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNacosConfigsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNacosConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryConfigRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        cluster_id: str = None,
        config_type: str = None,
        instance_id: str = None,
    ):
        self.request_pars = request_pars
        self.cluster_id = cluster_id
        self.config_type = config_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        max_client_cnxns: str = None,
        config_auth_supported: bool = None,
        init_limit: str = None,
        mcpenabled: bool = None,
        open_super_acl: bool = None,
        restart_flag: bool = None,
        jvm_flags_custom: str = None,
        autopurge_purge_interval: str = None,
        autopurge_snap_retain_count: str = None,
        sync_limit: str = None,
        config_auth_enabled: bool = None,
        cluster_name: str = None,
        mcpsupported: bool = None,
        jute_maxbuffer: str = None,
        tick_time: str = None,
        pass_word: str = None,
        user_name: str = None,
        config_secret_supported: bool = None,
        config_secret_enabled: bool = None,
    ):
        self.max_client_cnxns = max_client_cnxns
        self.config_auth_supported = config_auth_supported
        self.init_limit = init_limit
        self.mcpenabled = mcpenabled
        self.open_super_acl = open_super_acl
        self.restart_flag = restart_flag
        self.jvm_flags_custom = jvm_flags_custom
        self.autopurge_purge_interval = autopurge_purge_interval
        self.autopurge_snap_retain_count = autopurge_snap_retain_count
        self.sync_limit = sync_limit
        self.config_auth_enabled = config_auth_enabled
        self.cluster_name = cluster_name
        self.mcpsupported = mcpsupported
        self.jute_maxbuffer = jute_maxbuffer
        self.tick_time = tick_time
        self.pass_word = pass_word
        self.user_name = user_name
        self.config_secret_supported = config_secret_supported
        self.config_secret_enabled = config_secret_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_client_cnxns is not None:
            result['MaxClientCnxns'] = self.max_client_cnxns
        if self.config_auth_supported is not None:
            result['ConfigAuthSupported'] = self.config_auth_supported
        if self.init_limit is not None:
            result['InitLimit'] = self.init_limit
        if self.mcpenabled is not None:
            result['MCPEnabled'] = self.mcpenabled
        if self.open_super_acl is not None:
            result['OpenSuperAcl'] = self.open_super_acl
        if self.restart_flag is not None:
            result['RestartFlag'] = self.restart_flag
        if self.jvm_flags_custom is not None:
            result['JvmFlagsCustom'] = self.jvm_flags_custom
        if self.autopurge_purge_interval is not None:
            result['AutopurgePurgeInterval'] = self.autopurge_purge_interval
        if self.autopurge_snap_retain_count is not None:
            result['AutopurgeSnapRetainCount'] = self.autopurge_snap_retain_count
        if self.sync_limit is not None:
            result['SyncLimit'] = self.sync_limit
        if self.config_auth_enabled is not None:
            result['ConfigAuthEnabled'] = self.config_auth_enabled
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.mcpsupported is not None:
            result['MCPSupported'] = self.mcpsupported
        if self.jute_maxbuffer is not None:
            result['JuteMaxbuffer'] = self.jute_maxbuffer
        if self.tick_time is not None:
            result['TickTime'] = self.tick_time
        if self.pass_word is not None:
            result['PassWord'] = self.pass_word
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.config_secret_supported is not None:
            result['ConfigSecretSupported'] = self.config_secret_supported
        if self.config_secret_enabled is not None:
            result['ConfigSecretEnabled'] = self.config_secret_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxClientCnxns') is not None:
            self.max_client_cnxns = m.get('MaxClientCnxns')
        if m.get('ConfigAuthSupported') is not None:
            self.config_auth_supported = m.get('ConfigAuthSupported')
        if m.get('InitLimit') is not None:
            self.init_limit = m.get('InitLimit')
        if m.get('MCPEnabled') is not None:
            self.mcpenabled = m.get('MCPEnabled')
        if m.get('OpenSuperAcl') is not None:
            self.open_super_acl = m.get('OpenSuperAcl')
        if m.get('RestartFlag') is not None:
            self.restart_flag = m.get('RestartFlag')
        if m.get('JvmFlagsCustom') is not None:
            self.jvm_flags_custom = m.get('JvmFlagsCustom')
        if m.get('AutopurgePurgeInterval') is not None:
            self.autopurge_purge_interval = m.get('AutopurgePurgeInterval')
        if m.get('AutopurgeSnapRetainCount') is not None:
            self.autopurge_snap_retain_count = m.get('AutopurgeSnapRetainCount')
        if m.get('SyncLimit') is not None:
            self.sync_limit = m.get('SyncLimit')
        if m.get('ConfigAuthEnabled') is not None:
            self.config_auth_enabled = m.get('ConfigAuthEnabled')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('MCPSupported') is not None:
            self.mcpsupported = m.get('MCPSupported')
        if m.get('JuteMaxbuffer') is not None:
            self.jute_maxbuffer = m.get('JuteMaxbuffer')
        if m.get('TickTime') is not None:
            self.tick_time = m.get('TickTime')
        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ConfigSecretSupported') is not None:
            self.config_secret_supported = m.get('ConfigSecretSupported')
        if m.get('ConfigSecretEnabled') is not None:
            self.config_secret_enabled = m.get('ConfigSecretEnabled')
        return self


class QueryConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: QueryConfigResponseBodyData = None,
        success: bool = None,
        code: int = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.success = success
        self.code = code
        self.http_status_code = http_status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class QueryConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayOptionRequest(TeaModel):
    def __init__(
        self,
        gateway_id: int = None,
    ):
        self.gateway_id = gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        return self


class GetGatewayOptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        code: int = None,
        success: bool = None,
        data: GatewayOption = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GatewayOption()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetGatewayOptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGatewayOptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGatewayOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterTypesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListClusterTypesResponseBodyData(TeaModel):
    def __init__(
        self,
        show_name: str = None,
    ):
        self.show_name = show_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class ListClusterTypesResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        code: int = None,
        message: str = None,
        dynamic_message: str = None,
        data: List[ListClusterTypesResponseBodyData] = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.code = code
        self.message = message
        self.dynamic_message = dynamic_message
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClusterTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ListClusterTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClusterTypesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClusterTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosConfigsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ids: str = None,
        namespace_id: str = None,
    ):
        self.instance_id = instance_id
        self.ids = ids
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNacosConfigsResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        request_id: str = None,
        message: str = None,
        error_code: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.request_id = request_id
        self.message = message
        self.error_code = error_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNacosConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNacosConfigsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNacosConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        data_id: str = None,
        group: str = None,
        app_name: str = None,
        tags: str = None,
        desc: str = None,
        type: str = None,
        content: str = None,
        namespace_id: str = None,
        md_5: str = None,
        beta_ips: str = None,
        encrypted_data_key: str = None,
    ):
        self.instance_id = instance_id
        self.data_id = data_id
        self.group = group
        self.app_name = app_name
        self.tags = tags
        self.desc = desc
        self.type = type
        self.content = content
        self.namespace_id = namespace_id
        self.md_5 = md_5
        self.beta_ips = beta_ips
        self.encrypted_data_key = encrypted_data_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.type is not None:
            result['Type'] = self.type
        if self.content is not None:
            result['Content'] = self.content
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips
        if self.encrypted_data_key is not None:
            result['EncryptedDataKey'] = self.encrypted_data_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')
        if m.get('EncryptedDataKey') is not None:
            self.encrypted_data_key = m.get('EncryptedDataKey')
        return self


class UpdateNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMseFeatureSwitchResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMseFeatureSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMseFeatureSwitchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMseFeatureSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        cluster_alias_name: str = None,
        instance_id: str = None,
    ):
        self.request_pars = request_pars
        self.cluster_alias_name = cluster_alias_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateClusterResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        pub_network_flow: str = None,
        pub_slb_specification: str = None,
        disk_type: str = None,
        vpc_id: str = None,
        net_type: str = None,
        v_switch_id: str = None,
        instance_count: int = None,
        cluster_specification: str = None,
        cluster_version: str = None,
        cluster_type: str = None,
        region: str = None,
        private_slb_specification: str = None,
        connection_type: str = None,
        request_pars: str = None,
        disk_capacity: int = None,
    ):
        self.pub_network_flow = pub_network_flow
        self.pub_slb_specification = pub_slb_specification
        self.disk_type = disk_type
        self.vpc_id = vpc_id
        self.net_type = net_type
        self.v_switch_id = v_switch_id
        self.instance_count = instance_count
        self.cluster_specification = cluster_specification
        self.cluster_version = cluster_version
        self.cluster_type = cluster_type
        self.region = region
        self.private_slb_specification = private_slb_specification
        self.connection_type = connection_type
        self.request_pars = request_pars
        self.disk_capacity = disk_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pub_network_flow is not None:
            result['PubNetworkFlow'] = self.pub_network_flow
        if self.pub_slb_specification is not None:
            result['PubSlbSpecification'] = self.pub_slb_specification
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.region is not None:
            result['Region'] = self.region
        if self.private_slb_specification is not None:
            result['PrivateSlbSpecification'] = self.private_slb_specification
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PubNetworkFlow') is not None:
            self.pub_network_flow = m.get('PubNetworkFlow')
        if m.get('PubSlbSpecification') is not None:
            self.pub_slb_specification = m.get('PubSlbSpecification')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PrivateSlbSpecification') is not None:
            self.private_slb_specification = m.get('PrivateSlbSpecification')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        instance_id: str = None,
        error_code: str = None,
        order_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.instance_id = instance_id
        self.error_code = error_code
        self.order_id = order_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEurekaServicesRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        page_num: int = None,
        page_size: int = None,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.request_pars = request_pars
        self.page_num = page_num
        self.page_size = page_size
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEurekaServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        instances_id: List[str] = None,
        name: str = None,
        up_status: str = None,
    ):
        self.instances_id = instances_id
        self.name = name
        self.up_status = up_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances_id is not None:
            result['InstancesId'] = self.instances_id
        if self.name is not None:
            result['Name'] = self.name
        if self.up_status is not None:
            result['UpStatus'] = self.up_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstancesId') is not None:
            self.instances_id = m.get('InstancesId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpStatus') is not None:
            self.up_status = m.get('UpStatus')
        return self


class ListEurekaServicesResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListEurekaServicesResponseBodyData] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEurekaServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEurekaServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEurekaServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEurekaServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEngineNamepaceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        instance_id: str = None,
        cluster_id: str = None,
    ):
        self.id = id
        self.instance_id = instance_id
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetEngineNamepaceResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        type: str = None,
        quota: str = None,
        request_id: str = None,
        message: str = None,
        config_count: str = None,
        namespace_show_name: str = None,
        error_code: str = None,
        success: bool = None,
        namespace_desc: str = None,
        namespace: str = None,
    ):
        self.http_code = http_code
        self.type = type
        self.quota = quota
        self.request_id = request_id
        self.message = message
        self.config_count = config_count
        self.namespace_show_name = namespace_show_name
        self.error_code = error_code
        self.success = success
        self.namespace_desc = namespace_desc
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.type is not None:
            result['Type'] = self.type
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class GetEngineNamepaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEngineNamepaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEngineNamepaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateZnodeRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        cluster_id: str = None,
        path: str = None,
        data: str = None,
    ):
        self.request_pars = request_pars
        self.cluster_id = cluster_id
        self.path = path
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class UpdateZnodeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateZnodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateZnodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterDetailRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: str = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class QueryClusterDetailResponseBodyDataInstanceModels(TeaModel):
    def __init__(
        self,
        pod_name: str = None,
        single_tunnel_vip: str = None,
        internet_ip: str = None,
        ip: str = None,
        role: str = None,
        health_status: str = None,
    ):
        self.pod_name = pod_name
        self.single_tunnel_vip = single_tunnel_vip
        self.internet_ip = internet_ip
        self.ip = ip
        self.role = role
        self.health_status = health_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.single_tunnel_vip is not None:
            result['SingleTunnelVip'] = self.single_tunnel_vip
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.role is not None:
            result['Role'] = self.role
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('SingleTunnelVip') is not None:
            self.single_tunnel_vip = m.get('SingleTunnelVip')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        return self


class QueryClusterDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        create_time: str = None,
        intranet_address: str = None,
        disk_type: str = None,
        pub_network_flow: str = None,
        disk_capacity: int = None,
        memory_capacity: int = None,
        cluster_alias_name: str = None,
        instance_count: int = None,
        intranet_port: str = None,
        instance_models: List[QueryClusterDetailResponseBodyDataInstanceModels] = None,
        intranet_domain: str = None,
        internet_domain: str = None,
        pay_info: str = None,
        internet_address: str = None,
        instance_id: str = None,
        acl_entry_list: str = None,
        health_status: str = None,
        init_cost_time: int = None,
        region_id: str = None,
        acl_id: str = None,
        cpu: int = None,
        cluster_type: str = None,
        cluster_name: str = None,
        init_status: str = None,
        internet_port: str = None,
        app_version: str = None,
        net_type: str = None,
        cluster_version: str = None,
        cluster_specification: str = None,
        v_switch_id: str = None,
        connection_type: str = None,
        mse_version: str = None,
        charge_type: str = None,
    ):
        self.vpc_id = vpc_id
        self.create_time = create_time
        self.intranet_address = intranet_address
        self.disk_type = disk_type
        self.pub_network_flow = pub_network_flow
        self.disk_capacity = disk_capacity
        self.memory_capacity = memory_capacity
        self.cluster_alias_name = cluster_alias_name
        self.instance_count = instance_count
        self.intranet_port = intranet_port
        self.instance_models = instance_models
        self.intranet_domain = intranet_domain
        self.internet_domain = internet_domain
        self.pay_info = pay_info
        self.internet_address = internet_address
        self.instance_id = instance_id
        self.acl_entry_list = acl_entry_list
        self.health_status = health_status
        self.init_cost_time = init_cost_time
        self.region_id = region_id
        self.acl_id = acl_id
        self.cpu = cpu
        self.cluster_type = cluster_type
        self.cluster_name = cluster_name
        self.init_status = init_status
        self.internet_port = internet_port
        self.app_version = app_version
        self.net_type = net_type
        self.cluster_version = cluster_version
        self.cluster_specification = cluster_specification
        self.v_switch_id = v_switch_id
        self.connection_type = connection_type
        self.mse_version = mse_version
        self.charge_type = charge_type

    def validate(self):
        if self.instance_models:
            for k in self.instance_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.pub_network_flow is not None:
            result['PubNetworkFlow'] = self.pub_network_flow
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.intranet_port is not None:
            result['IntranetPort'] = self.intranet_port
        result['InstanceModels'] = []
        if self.instance_models is not None:
            for k in self.instance_models:
                result['InstanceModels'].append(k.to_map() if k else None)
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.pay_info is not None:
            result['PayInfo'] = self.pay_info
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.acl_entry_list is not None:
            result['AclEntryList'] = self.acl_entry_list
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.init_cost_time is not None:
            result['InitCostTime'] = self.init_cost_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.init_status is not None:
            result['InitStatus'] = self.init_status
        if self.internet_port is not None:
            result['InternetPort'] = self.internet_port
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('PubNetworkFlow') is not None:
            self.pub_network_flow = m.get('PubNetworkFlow')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('IntranetPort') is not None:
            self.intranet_port = m.get('IntranetPort')
        self.instance_models = []
        if m.get('InstanceModels') is not None:
            for k in m.get('InstanceModels'):
                temp_model = QueryClusterDetailResponseBodyDataInstanceModels()
                self.instance_models.append(temp_model.from_map(k))
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('PayInfo') is not None:
            self.pay_info = m.get('PayInfo')
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AclEntryList') is not None:
            self.acl_entry_list = m.get('AclEntryList')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('InitCostTime') is not None:
            self.init_cost_time = m.get('InitCostTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('InitStatus') is not None:
            self.init_status = m.get('InitStatus')
        if m.get('InternetPort') is not None:
            self.internet_port = m.get('InternetPort')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        return self


class QueryClusterDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: QueryClusterDetailResponseBodyData = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryClusterDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryClusterDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryClusterDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosServiceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        service_name: str = None,
        group_name: str = None,
        namespace_id: str = None,
    ):
        self.instance_id = instance_id
        self.service_name = service_name
        self.group_name = group_name
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNacosServiceResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        message: str = None,
        code: int = None,
        success: bool = None,
        data: str = None,
    ):
        # http状态码
        self.http_status_code = http_status_code
        # 请求id
        self.request_id = request_id
        # 响应信息
        self.message = message
        # 响应码
        self.code = code
        # 成功标志
        self.success = success
        # 删除服务的结果
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DeleteNacosServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNacosServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNacosServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayRequestFilterParams(TeaModel):
    def __init__(
        self,
        gateway_type: str = None,
        name: str = None,
    ):
        self.gateway_type = gateway_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListGatewayRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        order_item: str = None,
        desc_sort: bool = None,
        filter_params: ListGatewayRequestFilterParams = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.order_item = order_item
        self.desc_sort = desc_sort
        self.filter_params = filter_params

    def validate(self):
        if self.filter_params:
            self.filter_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.order_item is not None:
            result['OrderItem'] = self.order_item
        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort
        if self.filter_params is not None:
            result['FilterParams'] = self.filter_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('DescSort') is not None:
            self.desc_sort = m.get('DescSort')
        if m.get('FilterParams') is not None:
            temp_model = ListGatewayRequestFilterParams()
            self.filter_params = temp_model.from_map(m['FilterParams'])
        return self


class ListGatewayShrinkRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        order_item: str = None,
        desc_sort: bool = None,
        filter_params_shrink: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.order_item = order_item
        self.desc_sort = desc_sort
        self.filter_params_shrink = filter_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.order_item is not None:
            result['OrderItem'] = self.order_item
        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort
        if self.filter_params_shrink is not None:
            result['FilterParams'] = self.filter_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('DescSort') is not None:
            self.desc_sort = m.get('DescSort')
        if m.get('FilterParams') is not None:
            self.filter_params_shrink = m.get('FilterParams')
        return self


class ListGatewayResponseBodyDataResultSlb(TeaModel):
    def __init__(
        self,
        slb_ip: str = None,
        slb_port: str = None,
        slb_spec: str = None,
        type: str = None,
        gateway_slb_status: str = None,
        status_desc: str = None,
        gateway_slb_mode: str = None,
        slb_id: str = None,
    ):
        self.slb_ip = slb_ip
        self.slb_port = slb_port
        self.slb_spec = slb_spec
        self.type = type
        self.gateway_slb_status = gateway_slb_status
        self.status_desc = status_desc
        self.gateway_slb_mode = gateway_slb_mode
        self.slb_id = slb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip
        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port
        if self.slb_spec is not None:
            result['SlbSpec'] = self.slb_spec
        if self.type is not None:
            result['Type'] = self.type
        if self.gateway_slb_status is not None:
            result['GatewaySlbStatus'] = self.gateway_slb_status
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.gateway_slb_mode is not None:
            result['GatewaySlbMode'] = self.gateway_slb_mode
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')
        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')
        if m.get('SlbSpec') is not None:
            self.slb_spec = m.get('SlbSpec')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('GatewaySlbStatus') is not None:
            self.gateway_slb_status = m.get('GatewaySlbStatus')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('GatewaySlbMode') is not None:
            self.gateway_slb_mode = m.get('GatewaySlbMode')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        return self


class ListGatewayResponseBodyDataResultInternetSlb(TeaModel):
    def __init__(
        self,
        slb_ip: str = None,
        slb_port: str = None,
        slb_spec: str = None,
        type: str = None,
        internet_network_flow: str = None,
        gateway_slb_status: str = None,
        status_desc: str = None,
        gateway_slb_mode: str = None,
        slb_id: str = None,
    ):
        self.slb_ip = slb_ip
        self.slb_port = slb_port
        self.slb_spec = slb_spec
        self.type = type
        self.internet_network_flow = internet_network_flow
        self.gateway_slb_status = gateway_slb_status
        self.status_desc = status_desc
        self.gateway_slb_mode = gateway_slb_mode
        self.slb_id = slb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip
        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port
        if self.slb_spec is not None:
            result['SlbSpec'] = self.slb_spec
        if self.type is not None:
            result['Type'] = self.type
        if self.internet_network_flow is not None:
            result['InternetNetworkFlow'] = self.internet_network_flow
        if self.gateway_slb_status is not None:
            result['GatewaySlbStatus'] = self.gateway_slb_status
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.gateway_slb_mode is not None:
            result['GatewaySlbMode'] = self.gateway_slb_mode
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')
        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')
        if m.get('SlbSpec') is not None:
            self.slb_spec = m.get('SlbSpec')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('InternetNetworkFlow') is not None:
            self.internet_network_flow = m.get('InternetNetworkFlow')
        if m.get('GatewaySlbStatus') is not None:
            self.gateway_slb_status = m.get('GatewaySlbStatus')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('GatewaySlbMode') is not None:
            self.gateway_slb_mode = m.get('GatewaySlbMode')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        return self


class ListGatewayResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        gateway_unique_id: str = None,
        gateway_type: str = None,
        region: str = None,
        primary_user: str = None,
        status: int = None,
        ahas_on: bool = None,
        arms_on: bool = None,
        spec: str = None,
        replica: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        status_desc: str = None,
        slb: List[ListGatewayResponseBodyDataResultSlb] = None,
        internet_slb: List[ListGatewayResponseBodyDataResultInternetSlb] = None,
        upgrade: bool = None,
        must_upgrade: bool = None,
        current_version: str = None,
        latest_version: str = None,
        vswitch_2: str = None,
        instance_id: str = None,
        charge_type: str = None,
        end_date: str = None,
        tag: str = None,
    ):
        self.id = id
        self.name = name
        self.gateway_unique_id = gateway_unique_id
        self.gateway_type = gateway_type
        self.region = region
        self.primary_user = primary_user
        self.status = status
        self.ahas_on = ahas_on
        self.arms_on = arms_on
        self.spec = spec
        self.replica = replica
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.status_desc = status_desc
        self.slb = slb
        self.internet_slb = internet_slb
        self.upgrade = upgrade
        self.must_upgrade = must_upgrade
        self.current_version = current_version
        self.latest_version = latest_version
        self.vswitch_2 = vswitch_2
        self.instance_id = instance_id
        self.charge_type = charge_type
        self.end_date = end_date
        self.tag = tag

    def validate(self):
        if self.slb:
            for k in self.slb:
                if k:
                    k.validate()
        if self.internet_slb:
            for k in self.internet_slb:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type
        if self.region is not None:
            result['Region'] = self.region
        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user
        if self.status is not None:
            result['Status'] = self.status
        if self.ahas_on is not None:
            result['AhasOn'] = self.ahas_on
        if self.arms_on is not None:
            result['ArmsOn'] = self.arms_on
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.replica is not None:
            result['Replica'] = self.replica
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        result['Slb'] = []
        if self.slb is not None:
            for k in self.slb:
                result['Slb'].append(k.to_map() if k else None)
        result['InternetSlb'] = []
        if self.internet_slb is not None:
            for k in self.internet_slb:
                result['InternetSlb'].append(k.to_map() if k else None)
        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade
        if self.must_upgrade is not None:
            result['MustUpgrade'] = self.must_upgrade
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.vswitch_2 is not None:
            result['Vswitch2'] = self.vswitch_2
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AhasOn') is not None:
            self.ahas_on = m.get('AhasOn')
        if m.get('ArmsOn') is not None:
            self.arms_on = m.get('ArmsOn')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Replica') is not None:
            self.replica = m.get('Replica')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        self.slb = []
        if m.get('Slb') is not None:
            for k in m.get('Slb'):
                temp_model = ListGatewayResponseBodyDataResultSlb()
                self.slb.append(temp_model.from_map(k))
        self.internet_slb = []
        if m.get('InternetSlb') is not None:
            for k in m.get('InternetSlb'):
                temp_model = ListGatewayResponseBodyDataResultInternetSlb()
                self.internet_slb.append(temp_model.from_map(k))
        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')
        if m.get('MustUpgrade') is not None:
            self.must_upgrade = m.get('MustUpgrade')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('Vswitch2') is not None:
            self.vswitch_2 = m.get('Vswitch2')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListGatewayResponseBodyData(TeaModel):
    def __init__(
        self,
        total_size: int = None,
        page_number: int = None,
        page_size: int = None,
        result: List[ListGatewayResponseBodyDataResult] = None,
    ):
        self.total_size = total_size
        self.page_number = page_number
        self.page_size = page_size
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGatewayResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListGatewayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        code: int = None,
        success: bool = None,
        data: ListGatewayResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = ListGatewayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGatewayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsServiceClustersRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        page_num: int = None,
        page_size: int = None,
        cluster_id: str = None,
        service_name: str = None,
        group_name: str = None,
        namespace_id: str = None,
        cluster_name: str = None,
    ):
        self.request_pars = request_pars
        self.page_num = page_num
        self.page_size = page_size
        self.cluster_id = cluster_id
        self.service_name = service_name
        self.group_name = group_name
        self.namespace_id = namespace_id
        self.cluster_name = cluster_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class ListAnsServiceClustersResponseBodyDataClusters(TeaModel):
    def __init__(
        self,
        default_check_port: int = None,
        health_checker_type: str = None,
        use_ipport_4check: bool = None,
        service_name: str = None,
        name: str = None,
        default_port: int = None,
        metadata: Dict[str, Any] = None,
    ):
        self.default_check_port = default_check_port
        self.health_checker_type = health_checker_type
        self.use_ipport_4check = use_ipport_4check
        self.service_name = service_name
        self.name = name
        self.default_port = default_port
        self.metadata = metadata

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_check_port is not None:
            result['DefaultCheckPort'] = self.default_check_port
        if self.health_checker_type is not None:
            result['HealthCheckerType'] = self.health_checker_type
        if self.use_ipport_4check is not None:
            result['UseIPPort4Check'] = self.use_ipport_4check
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.name is not None:
            result['Name'] = self.name
        if self.default_port is not None:
            result['DefaultPort'] = self.default_port
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCheckPort') is not None:
            self.default_check_port = m.get('DefaultCheckPort')
        if m.get('HealthCheckerType') is not None:
            self.health_checker_type = m.get('HealthCheckerType')
        if m.get('UseIPPort4Check') is not None:
            self.use_ipport_4check = m.get('UseIPPort4Check')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DefaultPort') is not None:
            self.default_port = m.get('DefaultPort')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class ListAnsServiceClustersResponseBodyData(TeaModel):
    def __init__(
        self,
        protect_threshold: float = None,
        group_name: str = None,
        clusters: List[ListAnsServiceClustersResponseBodyDataClusters] = None,
        name: str = None,
        selector_type: str = None,
        metadata: Dict[str, Any] = None,
    ):
        self.protect_threshold = protect_threshold
        self.group_name = group_name
        self.clusters = clusters
        self.name = name
        self.selector_type = selector_type
        self.metadata = metadata

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protect_threshold is not None:
            result['ProtectThreshold'] = self.protect_threshold
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.selector_type is not None:
            result['SelectorType'] = self.selector_type
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectThreshold') is not None:
            self.protect_threshold = m.get('ProtectThreshold')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = ListAnsServiceClustersResponseBodyDataClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SelectorType') is not None:
            self.selector_type = m.get('SelectorType')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class ListAnsServiceClustersResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListAnsServiceClustersResponseBodyData = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListAnsServiceClustersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAnsServiceClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAnsServiceClustersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAnsServiceClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNacosConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        data_id: str = None,
        group: str = None,
        namespace_id: str = None,
        beta: bool = None,
    ):
        self.instance_id = instance_id
        self.data_id = data_id
        self.group = group
        self.namespace_id = namespace_id
        self.beta = beta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.beta is not None:
            result['Beta'] = self.beta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Beta') is not None:
            self.beta = m.get('Beta')
        return self


class GetNacosConfigResponseBodyConfiguration(TeaModel):
    def __init__(
        self,
        type: str = None,
        app_name: str = None,
        tags: str = None,
        md_5: str = None,
        data_id: str = None,
        content: str = None,
        group: str = None,
        desc: str = None,
        encrypted_data_key: str = None,
        beta_ips: str = None,
    ):
        self.type = type
        self.app_name = app_name
        self.tags = tags
        self.md_5 = md_5
        self.data_id = data_id
        self.content = content
        self.group = group
        self.desc = desc
        self.encrypted_data_key = encrypted_data_key
        self.beta_ips = beta_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.content is not None:
            result['Content'] = self.content
        if self.group is not None:
            result['Group'] = self.group
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.encrypted_data_key is not None:
            result['EncryptedDataKey'] = self.encrypted_data_key
        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('EncryptedDataKey') is not None:
            self.encrypted_data_key = m.get('EncryptedDataKey')
        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')
        return self


class GetNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        configuration: GetNacosConfigResponseBodyConfiguration = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.configuration = configuration
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Configuration') is not None:
            temp_model = GetNacosConfigResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneNacosConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        origin_namespace_id: str = None,
        target_namespace_id: str = None,
        policy: str = None,
        ids: str = None,
    ):
        self.instance_id = instance_id
        self.origin_namespace_id = origin_namespace_id
        self.target_namespace_id = target_namespace_id
        self.policy = policy
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.origin_namespace_id is not None:
            result['OriginNamespaceId'] = self.origin_namespace_id
        if self.target_namespace_id is not None:
            result['TargetNamespaceId'] = self.target_namespace_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OriginNamespaceId') is not None:
            self.origin_namespace_id = m.get('OriginNamespaceId')
        if m.get('TargetNamespaceId') is not None:
            self.target_namespace_id = m.get('TargetNamespaceId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class CloneNacosConfigResponseBodyDataSkipData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
    ):
        self.data_id = data_id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class CloneNacosConfigResponseBodyDataFailData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        group: str = None,
    ):
        self.data_id = data_id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class CloneNacosConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        succ_count: int = None,
        skip_count: int = None,
        skip_data: List[CloneNacosConfigResponseBodyDataSkipData] = None,
        fail_data: List[CloneNacosConfigResponseBodyDataFailData] = None,
    ):
        self.succ_count = succ_count
        self.skip_count = skip_count
        self.skip_data = skip_data
        self.fail_data = fail_data

    def validate(self):
        if self.skip_data:
            for k in self.skip_data:
                if k:
                    k.validate()
        if self.fail_data:
            for k in self.fail_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.succ_count is not None:
            result['SuccCount'] = self.succ_count
        if self.skip_count is not None:
            result['SkipCount'] = self.skip_count
        result['SkipData'] = []
        if self.skip_data is not None:
            for k in self.skip_data:
                result['SkipData'].append(k.to_map() if k else None)
        result['FailData'] = []
        if self.fail_data is not None:
            for k in self.fail_data:
                result['FailData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuccCount') is not None:
            self.succ_count = m.get('SuccCount')
        if m.get('SkipCount') is not None:
            self.skip_count = m.get('SkipCount')
        self.skip_data = []
        if m.get('SkipData') is not None:
            for k in m.get('SkipData'):
                temp_model = CloneNacosConfigResponseBodyDataSkipData()
                self.skip_data.append(temp_model.from_map(k))
        self.fail_data = []
        if m.get('FailData') is not None:
            for k in m.get('FailData'):
                temp_model = CloneNacosConfigResponseBodyDataFailData()
                self.fail_data.append(temp_model.from_map(k))
        return self


class CloneNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        code: int = None,
        message: str = None,
        dynamic_message: str = None,
        data: CloneNacosConfigResponseBodyData = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.code = code
        self.message = message
        self.dynamic_message = dynamic_message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Data') is not None:
            temp_model = CloneNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CloneNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloneNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloneNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlarmRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        alarm_alias_name: str = None,
        alert_way: Dict[str, Any] = None,
        contact_group_ids: Dict[str, Any] = None,
        alarm_item: str = None,
        operator: str = None,
        aggregates: str = None,
        nvalue: int = None,
        value: float = None,
    ):
        self.instance_id = instance_id
        self.alarm_alias_name = alarm_alias_name
        self.alert_way = alert_way
        self.contact_group_ids = contact_group_ids
        self.alarm_item = alarm_item
        self.operator = operator
        self.aggregates = aggregates
        self.nvalue = nvalue
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.alarm_alias_name is not None:
            result['AlarmAliasName'] = self.alarm_alias_name
        if self.alert_way is not None:
            result['AlertWay'] = self.alert_way
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.alarm_item is not None:
            result['AlarmItem'] = self.alarm_item
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AlarmAliasName') is not None:
            self.alarm_alias_name = m.get('AlarmAliasName')
        if m.get('AlertWay') is not None:
            self.alert_way = m.get('AlertWay')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('AlarmItem') is not None:
            self.alarm_item = m.get('AlarmItem')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAlarmRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        alarm_alias_name: str = None,
        alert_way_shrink: str = None,
        contact_group_ids_shrink: str = None,
        alarm_item: str = None,
        operator: str = None,
        aggregates: str = None,
        nvalue: int = None,
        value: float = None,
    ):
        self.instance_id = instance_id
        self.alarm_alias_name = alarm_alias_name
        self.alert_way_shrink = alert_way_shrink
        self.contact_group_ids_shrink = contact_group_ids_shrink
        self.alarm_item = alarm_item
        self.operator = operator
        self.aggregates = aggregates
        self.nvalue = nvalue
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.alarm_alias_name is not None:
            result['AlarmAliasName'] = self.alarm_alias_name
        if self.alert_way_shrink is not None:
            result['AlertWay'] = self.alert_way_shrink
        if self.contact_group_ids_shrink is not None:
            result['ContactGroupIds'] = self.contact_group_ids_shrink
        if self.alarm_item is not None:
            result['AlarmItem'] = self.alarm_item
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AlarmAliasName') is not None:
            self.alarm_alias_name = m.get('AlarmAliasName')
        if m.get('AlertWay') is not None:
            self.alert_way_shrink = m.get('AlertWay')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids_shrink = m.get('ContactGroupIds')
        if m.get('AlarmItem') is not None:
            self.alarm_item = m.get('AlarmItem')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAlarmRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAlarmRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersByIpRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        instance_id: str = None,
        ip: str = None,
        namespace_id: str = None,
    ):
        self.request_pars = request_pars
        self.instance_id = instance_id
        self.ip = ip
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListListenersByIpResponseBodyListeners(TeaModel):
    def __init__(
        self,
        md_5: str = None,
        data_id: str = None,
        group: str = None,
    ):
        self.md_5 = md_5
        self.data_id = data_id
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ListListenersByIpResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        listeners: List[ListListenersByIpResponseBodyListeners] = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.listeners = listeners
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersByIpResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListListenersByIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListListenersByIpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListListenersByIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGovernanceKubernetesClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        cluster_id: str = None,
        region_id: str = None,
        k_8s_version: str = None,
        pilot_start_time: int = None,
        name_space_infos: str = None,
    ):
        self.cluster_name = cluster_name
        self.cluster_id = cluster_id
        self.region_id = region_id
        self.k_8s_version = k_8s_version
        self.pilot_start_time = pilot_start_time
        self.name_space_infos = name_space_infos

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.k_8s_version is not None:
            result['K8sVersion'] = self.k_8s_version
        if self.pilot_start_time is not None:
            result['PilotStartTime'] = self.pilot_start_time
        if self.name_space_infos is not None:
            result['NameSpaceInfos'] = self.name_space_infos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('K8sVersion') is not None:
            self.k_8s_version = m.get('K8sVersion')
        if m.get('PilotStartTime') is not None:
            self.pilot_start_time = m.get('PilotStartTime')
        if m.get('NameSpaceInfos') is not None:
            self.name_space_infos = m.get('NameSpaceInfos')
        return self


class CreateGovernanceKubernetesClusterResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: int = None,
        code: int = None,
        success: str = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class CreateGovernanceKubernetesClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGovernanceKubernetesClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateGovernanceKubernetesClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEurekaInstancesRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        page_num: int = None,
        page_size: int = None,
        cluster_id: str = None,
        service_name: str = None,
    ):
        self.request_pars = request_pars
        self.page_num = page_num
        self.page_size = page_size
        self.cluster_id = cluster_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListEurekaInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        last_dirty_timestamp: int = None,
        ip_addr: str = None,
        home_page_url: str = None,
        host_name: str = None,
        instance_id: str = None,
        port: int = None,
        secure_port: int = None,
        app: str = None,
        duration_in_secs: int = None,
        last_updated_timestamp: int = None,
        renewal_interval_in_secs: int = None,
        vip_address: str = None,
        metadata: Dict[str, Any] = None,
    ):
        self.status = status
        self.last_dirty_timestamp = last_dirty_timestamp
        self.ip_addr = ip_addr
        self.home_page_url = home_page_url
        self.host_name = host_name
        self.instance_id = instance_id
        self.port = port
        self.secure_port = secure_port
        self.app = app
        self.duration_in_secs = duration_in_secs
        self.last_updated_timestamp = last_updated_timestamp
        self.renewal_interval_in_secs = renewal_interval_in_secs
        self.vip_address = vip_address
        self.metadata = metadata

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.last_dirty_timestamp is not None:
            result['LastDirtyTimestamp'] = self.last_dirty_timestamp
        if self.ip_addr is not None:
            result['IpAddr'] = self.ip_addr
        if self.home_page_url is not None:
            result['HomePageUrl'] = self.home_page_url
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.secure_port is not None:
            result['SecurePort'] = self.secure_port
        if self.app is not None:
            result['App'] = self.app
        if self.duration_in_secs is not None:
            result['DurationInSecs'] = self.duration_in_secs
        if self.last_updated_timestamp is not None:
            result['LastUpdatedTimestamp'] = self.last_updated_timestamp
        if self.renewal_interval_in_secs is not None:
            result['RenewalIntervalInSecs'] = self.renewal_interval_in_secs
        if self.vip_address is not None:
            result['VipAddress'] = self.vip_address
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('LastDirtyTimestamp') is not None:
            self.last_dirty_timestamp = m.get('LastDirtyTimestamp')
        if m.get('IpAddr') is not None:
            self.ip_addr = m.get('IpAddr')
        if m.get('HomePageUrl') is not None:
            self.home_page_url = m.get('HomePageUrl')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SecurePort') is not None:
            self.secure_port = m.get('SecurePort')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('DurationInSecs') is not None:
            self.duration_in_secs = m.get('DurationInSecs')
        if m.get('LastUpdatedTimestamp') is not None:
            self.last_updated_timestamp = m.get('LastUpdatedTimestamp')
        if m.get('RenewalIntervalInSecs') is not None:
            self.renewal_interval_in_secs = m.get('RenewalIntervalInSecs')
        if m.get('VipAddress') is not None:
            self.vip_address = m.get('VipAddress')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class ListEurekaInstancesResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListEurekaInstancesResponseBodyData] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEurekaInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEurekaInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEurekaInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEurekaInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGatewayRegionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        code: int = None,
        success: bool = None,
        data: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class QueryGatewayRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGatewayRegionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryGatewayRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        data_id: str = None,
        group: str = None,
        namespace_id: str = None,
        beta: bool = None,
    ):
        self.instance_id = instance_id
        self.data_id = data_id
        self.group = group
        self.namespace_id = namespace_id
        self.beta = beta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.beta is not None:
            result['Beta'] = self.beta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Beta') is not None:
            self.beta = m.get('Beta')
        return self


class DeleteNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        request_id: str = None,
        message: str = None,
        error_code: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.request_id = request_id
        self.message = message
        self.error_code = error_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEngineNamespaceRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        desc: str = None,
        service_count: int = None,
        id: str = None,
        cluster_id: str = None,
        instance_id: str = None,
    ):
        self.name = name
        self.desc = desc
        self.service_count = service_count
        self.id = id
        self.cluster_id = cluster_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        if self.id is not None:
            result['Id'] = self.id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateEngineNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        type: int = None,
        namespace_show_name: str = None,
        quota: int = None,
        namespace: str = None,
        namespace_desc: str = None,
        config_count: int = None,
    ):
        self.type = type
        self.namespace_show_name = namespace_show_name
        self.quota = quota
        self.namespace = namespace
        self.namespace_desc = namespace_desc
        self.config_count = config_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        return self


class UpdateEngineNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: UpdateEngineNamespaceResponseBodyData = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = UpdateEngineNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEngineNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEngineNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        page_num: int = None,
        page_size: int = None,
        cluster_alias_name: str = None,
        region_id: str = None,
    ):
        self.request_pars = request_pars
        self.page_num = page_num
        self.page_size = page_size
        self.cluster_alias_name = cluster_alias_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListClustersResponseBodyData(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        intranet_domain: str = None,
        internet_domain: str = None,
        create_time: str = None,
        charge_type: str = None,
        intranet_address: str = None,
        instance_id: str = None,
        internet_address: str = None,
        cluster_alias_name: str = None,
        cluster_type: str = None,
        init_status: str = None,
        app_version: str = None,
        can_update: bool = None,
        version_code: str = None,
        instance_count: int = None,
    ):
        self.end_date = end_date
        self.intranet_domain = intranet_domain
        self.internet_domain = internet_domain
        self.create_time = create_time
        self.charge_type = charge_type
        self.intranet_address = intranet_address
        self.instance_id = instance_id
        self.internet_address = internet_address
        self.cluster_alias_name = cluster_alias_name
        self.cluster_type = cluster_type
        self.init_status = init_status
        self.app_version = app_version
        self.can_update = can_update
        self.version_code = version_code
        self.instance_count = instance_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.init_status is not None:
            result['InitStatus'] = self.init_status
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.can_update is not None:
            result['CanUpdate'] = self.can_update
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('InitStatus') is not None:
            self.init_status = m.get('InitStatus')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CanUpdate') is not None:
            self.can_update = m.get('CanUpdate')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListClustersResponseBodyData] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClustersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClustersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryZnodeDetailRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        cluster_id: str = None,
        path: str = None,
    ):
        self.request_pars = request_pars
        self.cluster_id = cluster_id
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class QueryZnodeDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        data: str = None,
        path: str = None,
        dir: bool = None,
        name: str = None,
    ):
        self.data = data
        self.path = path
        self.dir = dir
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryZnodeDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: QueryZnodeDetailResponseBodyData = None,
        error_code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryZnodeDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryZnodeDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryZnodeDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryZnodeDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        service_name: str = None,
        group_name: str = None,
        namespace_id: str = None,
        cluster_name: str = None,
        ip: str = None,
        port: int = None,
        ephemeral: bool = None,
        weight: str = None,
        enabled: bool = None,
        metadata: str = None,
    ):
        # 实例id
        self.instance_id = instance_id
        # 服务名
        self.service_name = service_name
        # 分组名
        self.group_name = group_name
        # 命名空间id
        self.namespace_id = namespace_id
        # Nacos集群名
        self.cluster_name = cluster_name
        # Nacos实例ip
        self.ip = ip
        # Nacos实例端口
        self.port = port
        # 临时节点标志
        self.ephemeral = ephemeral
        # 权重
        self.weight = weight
        # 服务禁用标志
        self.enabled = enabled
        # 节点元数据
        self.metadata = metadata

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class UpdateNacosInstanceResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        message: str = None,
        code: int = None,
        success: bool = None,
        data: str = None,
    ):
        # http状态码
        self.http_status_code = http_status_code
        # 请求id
        self.request_id = request_id
        # 响应信息
        self.message = message
        # 响应码
        self.code = code
        # 成功标志
        self.success = success
        # 修改结果
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class UpdateNacosInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNacosInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNacosInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlarmRuleRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        alarm_rule_id: str = None,
    ):
        self.request_pars = request_pars
        self.alarm_rule_id = alarm_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.alarm_rule_id is not None:
            result['AlarmRuleId'] = self.alarm_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('AlarmRuleId') is not None:
            self.alarm_rule_id = m.get('AlarmRuleId')
        return self


class DeleteAlarmRuleResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAlarmRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImportFileUrlRequest(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        instance_id: str = None,
        namespace_id: str = None,
    ):
        self.content_type = content_type
        self.instance_id = instance_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class GetImportFileUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetImportFileUrlResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        code: int = None,
        message: str = None,
        dynamic_message: str = None,
        data: GetImportFileUrlResponseBodyData = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.code = code
        self.message = message
        self.dynamic_message = dynamic_message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Data') is not None:
            temp_model = GetImportFileUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetImportFileUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImportFileUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImportFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_unique_id: str = None,
    ):
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class GetGatewayResponseBodyDataXtraceDetails(TeaModel):
    def __init__(
        self,
        sample: int = None,
        trace_on: bool = None,
    ):
        self.sample = sample
        self.trace_on = trace_on

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.trace_on is not None:
            result['TraceOn'] = self.trace_on
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('TraceOn') is not None:
            self.trace_on = m.get('TraceOn')
        return self


class GetGatewayResponseBodyDataLogConfigDetails(TeaModel):
    def __init__(
        self,
        log_enabled: bool = None,
        project_name: str = None,
        log_store_name: str = None,
    ):
        self.log_enabled = log_enabled
        self.project_name = project_name
        self.log_store_name = log_store_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_enabled is not None:
            result['LogEnabled'] = self.log_enabled
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogEnabled') is not None:
            self.log_enabled = m.get('LogEnabled')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        return self


class GetGatewayResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        gateway_unique_id: str = None,
        gateway_type: str = None,
        region: str = None,
        primary_user: str = None,
        status: int = None,
        arms_on: bool = None,
        vpc: str = None,
        vswitch: str = None,
        security_group: str = None,
        spec: str = None,
        replica: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        xtrace_details: GetGatewayResponseBodyDataXtraceDetails = None,
        vswitch_2: str = None,
        instance_id: str = None,
        charge_type: str = None,
        end_date: str = None,
        log_config_details: GetGatewayResponseBodyDataLogConfigDetails = None,
    ):
        self.id = id
        self.name = name
        self.gateway_unique_id = gateway_unique_id
        self.gateway_type = gateway_type
        self.region = region
        self.primary_user = primary_user
        self.status = status
        self.arms_on = arms_on
        self.vpc = vpc
        self.vswitch = vswitch
        self.security_group = security_group
        self.spec = spec
        self.replica = replica
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.xtrace_details = xtrace_details
        self.vswitch_2 = vswitch_2
        self.instance_id = instance_id
        self.charge_type = charge_type
        self.end_date = end_date
        self.log_config_details = log_config_details

    def validate(self):
        if self.xtrace_details:
            self.xtrace_details.validate()
        if self.log_config_details:
            self.log_config_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type
        if self.region is not None:
            result['Region'] = self.region
        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user
        if self.status is not None:
            result['Status'] = self.status
        if self.arms_on is not None:
            result['ArmsOn'] = self.arms_on
        if self.vpc is not None:
            result['Vpc'] = self.vpc
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.replica is not None:
            result['Replica'] = self.replica
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.xtrace_details is not None:
            result['XtraceDetails'] = self.xtrace_details.to_map()
        if self.vswitch_2 is not None:
            result['Vswitch2'] = self.vswitch_2
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.log_config_details is not None:
            result['LogConfigDetails'] = self.log_config_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ArmsOn') is not None:
            self.arms_on = m.get('ArmsOn')
        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Replica') is not None:
            self.replica = m.get('Replica')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('XtraceDetails') is not None:
            temp_model = GetGatewayResponseBodyDataXtraceDetails()
            self.xtrace_details = temp_model.from_map(m['XtraceDetails'])
        if m.get('Vswitch2') is not None:
            self.vswitch_2 = m.get('Vswitch2')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('LogConfigDetails') is not None:
            temp_model = GetGatewayResponseBodyDataLogConfigDetails()
            self.log_config_details = temp_model.from_map(m['LogConfigDetails'])
        return self


class GetGatewayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        code: int = None,
        success: bool = None,
        data: GetGatewayResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetGatewayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGatewayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmRulesRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        page_num: int = None,
        page_size: int = None,
        alarm_mse_type: str = None,
    ):
        self.request_pars = request_pars
        self.page_num = page_num
        self.page_size = page_size
        self.alarm_mse_type = alarm_mse_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.alarm_mse_type is not None:
            result['AlarmMseType'] = self.alarm_mse_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AlarmMseType') is not None:
            self.alarm_mse_type = m.get('AlarmMseType')
        return self


class ListAlarmRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        alarm_status: str = None,
        alarm_rule_id: str = None,
        create_time: str = None,
        alarm_rule_detail: str = None,
        alarm_name: str = None,
    ):
        self.alarm_status = alarm_status
        self.alarm_rule_id = alarm_rule_id
        self.create_time = create_time
        self.alarm_rule_detail = alarm_rule_detail
        self.alarm_name = alarm_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.alarm_rule_id is not None:
            result['AlarmRuleId'] = self.alarm_rule_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.alarm_rule_detail is not None:
            result['AlarmRuleDetail'] = self.alarm_rule_detail
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('AlarmRuleId') is not None:
            self.alarm_rule_id = m.get('AlarmRuleId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AlarmRuleDetail') is not None:
            self.alarm_rule_detail = m.get('AlarmRuleDetail')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        return self


class ListAlarmRulesResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListAlarmRulesResponseBodyData] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmRulesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAlarmRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBusinessLocationsResponseBodyData(TeaModel):
    def __init__(
        self,
        ordering: int = None,
        type: str = None,
        district_en_name: str = None,
        show_name: str = None,
        district_cn_name: str = None,
        en_name: str = None,
        district_id: str = None,
        district_show_name: str = None,
        description: str = None,
        en_description: str = None,
        cn_name: str = None,
        name: str = None,
        district_ordering: int = None,
    ):
        self.ordering = ordering
        self.type = type
        self.district_en_name = district_en_name
        self.show_name = show_name
        self.district_cn_name = district_cn_name
        self.en_name = en_name
        self.district_id = district_id
        self.district_show_name = district_show_name
        self.description = description
        self.en_description = en_description
        self.cn_name = cn_name
        self.name = name
        self.district_ordering = district_ordering

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ordering is not None:
            result['Ordering'] = self.ordering
        if self.type is not None:
            result['Type'] = self.type
        if self.district_en_name is not None:
            result['DistrictEnName'] = self.district_en_name
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.district_cn_name is not None:
            result['DistrictCnName'] = self.district_cn_name
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.district_show_name is not None:
            result['DistrictShowName'] = self.district_show_name
        if self.description is not None:
            result['Description'] = self.description
        if self.en_description is not None:
            result['EnDescription'] = self.en_description
        if self.cn_name is not None:
            result['CnName'] = self.cn_name
        if self.name is not None:
            result['Name'] = self.name
        if self.district_ordering is not None:
            result['DistrictOrdering'] = self.district_ordering
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ordering') is not None:
            self.ordering = m.get('Ordering')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DistrictEnName') is not None:
            self.district_en_name = m.get('DistrictEnName')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('DistrictCnName') is not None:
            self.district_cn_name = m.get('DistrictCnName')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('DistrictShowName') is not None:
            self.district_show_name = m.get('DistrictShowName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnDescription') is not None:
            self.en_description = m.get('EnDescription')
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DistrictOrdering') is not None:
            self.district_ordering = m.get('DistrictOrdering')
        return self


class QueryBusinessLocationsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[QueryBusinessLocationsResponseBodyData] = None,
        error_code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryBusinessLocationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBusinessLocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBusinessLocationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryBusinessLocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        cluster_id: str = None,
        config_type: str = None,
        tick_time: str = None,
        init_limit: str = None,
        sync_limit: str = None,
        max_client_cnxns: str = None,
        open_super_acl: str = None,
        user_name: str = None,
        pass_word: str = None,
        jute_maxbuffer: str = None,
        autopurge_purge_interval: str = None,
        autopurge_snap_retain_count: str = None,
        config_auth_enabled: bool = None,
        mcpenabled: bool = None,
        instance_id: str = None,
        config_secret_enabled: bool = None,
    ):
        self.request_pars = request_pars
        self.cluster_id = cluster_id
        self.config_type = config_type
        self.tick_time = tick_time
        self.init_limit = init_limit
        self.sync_limit = sync_limit
        self.max_client_cnxns = max_client_cnxns
        self.open_super_acl = open_super_acl
        self.user_name = user_name
        self.pass_word = pass_word
        self.jute_maxbuffer = jute_maxbuffer
        self.autopurge_purge_interval = autopurge_purge_interval
        self.autopurge_snap_retain_count = autopurge_snap_retain_count
        self.config_auth_enabled = config_auth_enabled
        self.mcpenabled = mcpenabled
        self.instance_id = instance_id
        self.config_secret_enabled = config_secret_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.tick_time is not None:
            result['TickTime'] = self.tick_time
        if self.init_limit is not None:
            result['InitLimit'] = self.init_limit
        if self.sync_limit is not None:
            result['SyncLimit'] = self.sync_limit
        if self.max_client_cnxns is not None:
            result['MaxClientCnxns'] = self.max_client_cnxns
        if self.open_super_acl is not None:
            result['OpenSuperAcl'] = self.open_super_acl
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.pass_word is not None:
            result['PassWord'] = self.pass_word
        if self.jute_maxbuffer is not None:
            result['JuteMaxbuffer'] = self.jute_maxbuffer
        if self.autopurge_purge_interval is not None:
            result['AutopurgePurgeInterval'] = self.autopurge_purge_interval
        if self.autopurge_snap_retain_count is not None:
            result['AutopurgeSnapRetainCount'] = self.autopurge_snap_retain_count
        if self.config_auth_enabled is not None:
            result['ConfigAuthEnabled'] = self.config_auth_enabled
        if self.mcpenabled is not None:
            result['MCPEnabled'] = self.mcpenabled
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.config_secret_enabled is not None:
            result['ConfigSecretEnabled'] = self.config_secret_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('TickTime') is not None:
            self.tick_time = m.get('TickTime')
        if m.get('InitLimit') is not None:
            self.init_limit = m.get('InitLimit')
        if m.get('SyncLimit') is not None:
            self.sync_limit = m.get('SyncLimit')
        if m.get('MaxClientCnxns') is not None:
            self.max_client_cnxns = m.get('MaxClientCnxns')
        if m.get('OpenSuperAcl') is not None:
            self.open_super_acl = m.get('OpenSuperAcl')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')
        if m.get('JuteMaxbuffer') is not None:
            self.jute_maxbuffer = m.get('JuteMaxbuffer')
        if m.get('AutopurgePurgeInterval') is not None:
            self.autopurge_purge_interval = m.get('AutopurgePurgeInterval')
        if m.get('AutopurgeSnapRetainCount') is not None:
            self.autopurge_snap_retain_count = m.get('AutopurgeSnapRetainCount')
        if m.get('ConfigAuthEnabled') is not None:
            self.config_auth_enabled = m.get('ConfigAuthEnabled')
        if m.get('MCPEnabled') is not None:
            self.mcpenabled = m.get('MCPEnabled')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConfigSecretEnabled') is not None:
            self.config_secret_enabled = m.get('ConfigSecretEnabled')
        return self


class UpdateConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        code: int = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success
        self.code = code
        self.http_status_code = http_status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class UpdateConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNacosHistoryConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        data_id: str = None,
        group: str = None,
        namespace_id: str = None,
        nid: str = None,
    ):
        self.instance_id = instance_id
        self.data_id = data_id
        self.group = group
        self.namespace_id = namespace_id
        self.nid = nid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nid is not None:
            result['Nid'] = self.nid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Nid') is not None:
            self.nid = m.get('Nid')
        return self


class GetNacosHistoryConfigResponseBodyConfiguration(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        md_5: str = None,
        data_id: str = None,
        content: str = None,
        group: str = None,
        op_type: str = None,
        encrypted_data_key: str = None,
    ):
        self.app_name = app_name
        self.md_5 = md_5
        self.data_id = data_id
        self.content = content
        self.group = group
        self.op_type = op_type
        self.encrypted_data_key = encrypted_data_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.content is not None:
            result['Content'] = self.content
        if self.group is not None:
            result['Group'] = self.group
        if self.op_type is not None:
            result['OpType'] = self.op_type
        if self.encrypted_data_key is not None:
            result['EncryptedDataKey'] = self.encrypted_data_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        if m.get('EncryptedDataKey') is not None:
            self.encrypted_data_key = m.get('EncryptedDataKey')
        return self


class GetNacosHistoryConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        configuration: GetNacosHistoryConfigResponseBodyConfiguration = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.configuration = configuration
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Configuration') is not None:
            temp_model = GetNacosHistoryConfigResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNacosHistoryConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNacosHistoryConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetNacosHistoryConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAclRequest(TeaModel):
    def __init__(
        self,
        acl_entry_list: str = None,
        instance_id: str = None,
    ):
        self.acl_entry_list = acl_entry_list
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_entry_list is not None:
            result['AclEntryList'] = self.acl_entry_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntryList') is not None:
            self.acl_entry_list = m.get('AclEntryList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateAclResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAclResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySlbSpecResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        spec: str = None,
        name: str = None,
        max_connection: str = None,
        new_connection_per_second: str = None,
        qps: str = None,
    ):
        self.id = id
        self.spec = spec
        self.name = name
        self.max_connection = max_connection
        self.new_connection_per_second = new_connection_per_second
        self.qps = qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.name is not None:
            result['Name'] = self.name
        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection
        if self.new_connection_per_second is not None:
            result['NewConnectionPerSecond'] = self.new_connection_per_second
        if self.qps is not None:
            result['Qps'] = self.qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')
        if m.get('NewConnectionPerSecond') is not None:
            self.new_connection_per_second = m.get('NewConnectionPerSecond')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        return self


class QuerySlbSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        code: int = None,
        success: bool = None,
        data: List[QuerySlbSpecResponseBodyData] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QuerySlbSpecResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class QuerySlbSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySlbSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySlbSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayRouteHTTPRewriteRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        gateway_id: int = None,
        http_rewrite_json: str = None,
    ):
        self.id = id
        self.gateway_id = gateway_id
        self.http_rewrite_json = http_rewrite_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.http_rewrite_json is not None:
            result['HttpRewriteJSON'] = self.http_rewrite_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('HttpRewriteJSON') is not None:
            self.http_rewrite_json = m.get('HttpRewriteJSON')
        return self


class UpdateGatewayRouteHTTPRewriteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        message: str = None,
        code: int = None,
        success: bool = None,
        data: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class UpdateGatewayRouteHTTPRewriteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGatewayRouteHTTPRewriteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateGatewayRouteHTTPRewriteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
    def __init__(
        self,
        version_code: str = None,
    ):
        # 集群版本
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        return self


class GetImageResponseBodyData(TeaModel):
    def __init__(
        self,
        current_version_full_show_name: str = None,
        max_version_code: str = None,
        max_version_full_show_name: str = None,
        max_version_changelog_url: str = None,
    ):
        # 当前集群镜像版本的4位全名
        self.current_version_full_show_name = current_version_full_show_name
        # 可升级的增量版本Code
        self.max_version_code = max_version_code
        # 可升级的增量版本全名
        self.max_version_full_show_name = max_version_full_show_name
        # 可升级的最大版本变更日志url
        self.max_version_changelog_url = max_version_changelog_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_version_full_show_name is not None:
            result['CurrentVersionFullShowName'] = self.current_version_full_show_name
        if self.max_version_code is not None:
            result['MaxVersionCode'] = self.max_version_code
        if self.max_version_full_show_name is not None:
            result['MaxVersionFullShowName'] = self.max_version_full_show_name
        if self.max_version_changelog_url is not None:
            result['MaxVersionChangelogUrl'] = self.max_version_changelog_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentVersionFullShowName') is not None:
            self.current_version_full_show_name = m.get('CurrentVersionFullShowName')
        if m.get('MaxVersionCode') is not None:
            self.max_version_code = m.get('MaxVersionCode')
        if m.get('MaxVersionFullShowName') is not None:
            self.max_version_full_show_name = m.get('MaxVersionFullShowName')
        if m.get('MaxVersionChangelogUrl') is not None:
            self.max_version_changelog_url = m.get('MaxVersionChangelogUrl')
        return self


class GetImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        error_code: str = None,
        success: bool = None,
        http_code: str = None,
        data: GetImageResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.error_code = error_code
        self.success = success
        self.http_code = http_code
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Data') is not None:
            temp_model = GetImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartClusterRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        instance_id: str = None,
        cluster_id: str = None,
    ):
        self.request_pars = request_pars
        self.instance_id = instance_id
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class RestartClusterResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNacosConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        data_id: str = None,
        group: str = None,
        app_name: str = None,
        tags: str = None,
        desc: str = None,
        type: str = None,
        content: str = None,
        namespace_id: str = None,
        beta_ips: str = None,
    ):
        self.instance_id = instance_id
        self.data_id = data_id
        self.group = group
        self.app_name = app_name
        self.tags = tags
        self.desc = desc
        self.type = type
        self.content = content
        self.namespace_id = namespace_id
        self.beta_ips = beta_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.type is not None:
            result['Type'] = self.type
        if self.content is not None:
            result['Content'] = self.content
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')
        return self


class CreateNacosConfigResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        request_id: str = None,
        message: str = None,
        error_code: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.request_id = request_id
        self.message = message
        self.error_code = error_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNacosConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNacosConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClusterRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        instance_id: str = None,
        upgrade_version: str = None,
    ):
        self.request_pars = request_pars
        self.instance_id = instance_id
        self.upgrade_version = upgrade_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.upgrade_version is not None:
            result['UpgradeVersion'] = self.upgrade_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UpgradeVersion') is not None:
            self.upgrade_version = m.get('UpgradeVersion')
        return self


class UpgradeClusterResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        http_code: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.http_code = http_code
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsInstancesRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        page_num: int = None,
        page_size: int = None,
        cluster_id: str = None,
        service_name: str = None,
        group_name: str = None,
        namespace_id: str = None,
        cluster_name: str = None,
    ):
        self.request_pars = request_pars
        self.page_num = page_num
        self.page_size = page_size
        self.cluster_id = cluster_id
        self.service_name = service_name
        self.group_name = group_name
        self.namespace_id = namespace_id
        self.cluster_name = cluster_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class ListAnsInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        default_key: str = None,
        ephemeral: bool = None,
        marked: bool = None,
        ip: str = None,
        instance_id: str = None,
        port: int = None,
        last_beat: int = None,
        ok_count: int = None,
        weight: int = None,
        instance_heart_beat_interval: int = None,
        ip_delete_timeout: int = None,
        app: str = None,
        fail_count: int = None,
        healthy: bool = None,
        enabled: bool = None,
        datum_key: str = None,
        cluster_name: str = None,
        instance_heart_beat_time_out: int = None,
        service_name: str = None,
        metadata: Dict[str, Any] = None,
    ):
        self.default_key = default_key
        self.ephemeral = ephemeral
        self.marked = marked
        self.ip = ip
        self.instance_id = instance_id
        self.port = port
        self.last_beat = last_beat
        self.ok_count = ok_count
        self.weight = weight
        self.instance_heart_beat_interval = instance_heart_beat_interval
        self.ip_delete_timeout = ip_delete_timeout
        self.app = app
        self.fail_count = fail_count
        self.healthy = healthy
        self.enabled = enabled
        self.datum_key = datum_key
        self.cluster_name = cluster_name
        self.instance_heart_beat_time_out = instance_heart_beat_time_out
        self.service_name = service_name
        self.metadata = metadata

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_key is not None:
            result['DefaultKey'] = self.default_key
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.marked is not None:
            result['Marked'] = self.marked
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.last_beat is not None:
            result['LastBeat'] = self.last_beat
        if self.ok_count is not None:
            result['OkCount'] = self.ok_count
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.instance_heart_beat_interval is not None:
            result['InstanceHeartBeatInterval'] = self.instance_heart_beat_interval
        if self.ip_delete_timeout is not None:
            result['IpDeleteTimeout'] = self.ip_delete_timeout
        if self.app is not None:
            result['App'] = self.app
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.healthy is not None:
            result['Healthy'] = self.healthy
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.datum_key is not None:
            result['DatumKey'] = self.datum_key
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.instance_heart_beat_time_out is not None:
            result['InstanceHeartBeatTimeOut'] = self.instance_heart_beat_time_out
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultKey') is not None:
            self.default_key = m.get('DefaultKey')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('Marked') is not None:
            self.marked = m.get('Marked')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('LastBeat') is not None:
            self.last_beat = m.get('LastBeat')
        if m.get('OkCount') is not None:
            self.ok_count = m.get('OkCount')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('InstanceHeartBeatInterval') is not None:
            self.instance_heart_beat_interval = m.get('InstanceHeartBeatInterval')
        if m.get('IpDeleteTimeout') is not None:
            self.ip_delete_timeout = m.get('IpDeleteTimeout')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('Healthy') is not None:
            self.healthy = m.get('Healthy')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('DatumKey') is not None:
            self.datum_key = m.get('DatumKey')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('InstanceHeartBeatTimeOut') is not None:
            self.instance_heart_beat_time_out = m.get('InstanceHeartBeatTimeOut')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class ListAnsInstancesResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListAnsInstancesResponseBodyData] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAnsInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAnsInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAnsInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAnsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmItemsRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
    ):
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListAlarmItemsResponseBodyData(TeaModel):
    def __init__(
        self,
        alarm_desc: str = None,
        cluster_type: str = None,
        alarm_code: str = None,
    ):
        self.alarm_desc = alarm_desc
        self.cluster_type = cluster_type
        self.alarm_code = alarm_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_desc is not None:
            result['AlarmDesc'] = self.alarm_desc
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.alarm_code is not None:
            result['AlarmCode'] = self.alarm_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmDesc') is not None:
            self.alarm_desc = m.get('AlarmDesc')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('AlarmCode') is not None:
            self.alarm_code = m.get('AlarmCode')
        return self


class ListAlarmItemsResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListAlarmItemsResponseBodyData] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmItemsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAlarmItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryClusterRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        instance_id: str = None,
    ):
        self.request_pars = request_pars
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RetryClusterResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RetryClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RetryClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RetryClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmContactGroupsRequest(TeaModel):
    def __init__(
        self,
        request_pars: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.request_pars = request_pars
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAlarmContactGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        contact_group_name: str = None,
        contact_group_id: str = None,
    ):
        self.contact_group_name = contact_group_name
        self.contact_group_id = contact_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        return self


class ListAlarmContactGroupsResponseBody(TeaModel):
    def __init__(
        self,
        http_code: str = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListAlarmContactGroupsResponseBodyData] = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.http_code = http_code
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmContactGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAlarmContactGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmContactGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmContactGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        version_code: str = None,
    ):
        # 目标集群的id
        self.cluster_id = cluster_id
        # 想修改的镜像版本code
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        return self


class UpdateImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


